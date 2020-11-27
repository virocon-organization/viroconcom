import pytest
import pickle

import numpy as np
import pandas as pd

from virocon.models import GlobalHierarchicalModel
from virocon.distributions import WeibullDistribution, LogNormalDistribution
from virocon.dependencies import DependenceFunction

@pytest.fixture(scope="module")
def test_data():
    data = pd.read_csv("datasets/NDBC_buoy_46025.csv", sep=",")[["Hs", "T"]]
    return data

@pytest.fixture(scope="module")
def reference_data():
    with open("tests/reference_data/DNVGL/reference_data_DNVGL.pkl", "rb") as pkl_file:
        ref_data = pickle.load(pkl_file)
    return ref_data

def test_DNVGL(test_data, reference_data):
    # A 3-parameter power function (a dependence function).
    def _power3(x, a, b, c):
        return a + b * x ** c
    
    # A 3-parameter exponential function (a dependence function).
    def _exp3(x, a, b, c):
        return a + b * np.exp(c * x)
    
    bounds = [(0, None), 
              (0, None), 
              (None, None)]
    power3 = DependenceFunction(_power3, bounds)
    exp3 = DependenceFunction(_exp3, bounds)
    
    x, dx = np.linspace([0.1, 0.1], [6, 22], num=100, retstep=True)
    
    dist_description_0 = {"distribution" : WeibullDistribution,
                          "width_of_intervals" : 0.5,
                          "min_points_per_interval" : 50
                          }
    dist_description_1 = {"distribution" : LogNormalDistribution,
                          "conditional_on" : 0,
                          "parameters" : {"mu": power3,
                                          "sigma" : exp3},
                          }
    ghm = GlobalHierarchicalModel([dist_description_0, dist_description_1])
    ghm.fit(test_data)
    f_weibull = ghm.distributions[0].pdf(x[:, 0])
    weibull_params = (ghm.distributions[0].k, 
                      ghm.distributions[0].theta, 
                      ghm.distributions[0].lambda_)
    
    lognorm = ghm.distributions[1]
    intervals = lognorm.data_intervals
    givens = lognorm.conditioning_values
    f_lognorm = []
    for given in givens:
        f_lognorm.append(lognorm.pdf(x[:, 1], given))
    
    f_lognorm = np.stack(f_lognorm, axis=1)
    mus = np.array([par["mu"] for par in lognorm.parameters_per_interval])
    sigmas = np.array([par["sigma"] for par in lognorm.parameters_per_interval])
    
    
    ref_f_weibull = reference_data["ref_f_weibull"]
    ref_weibull_params = reference_data["ref_weibull_params"]
    ref_intervals = reference_data["ref_intervals"]
    ref_givens = reference_data["ref_givens"]
    ref_f_lognorm = reference_data["ref_f_lognorm"]
    ref_mus = reference_data["ref_mus"]
    ref_sigmas = reference_data["ref_sigmas"]
    
    assert len(intervals) == len(ref_intervals)
    for i in range(len(ref_intervals)):
        assert sorted(intervals[i]) == sorted(ref_intervals[i])
        
    np.testing.assert_allclose(f_weibull, ref_f_weibull)
    np.testing.assert_allclose(weibull_params, ref_weibull_params)
    np.testing.assert_allclose(givens, ref_givens)
    np.testing.assert_allclose(f_lognorm, ref_f_lognorm)
    np.testing.assert_allclose(mus, ref_mus)
    np.testing.assert_allclose(sigmas, ref_sigmas)
    