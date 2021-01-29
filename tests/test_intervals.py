import pytest

import numpy as np

from virocon.intervals import (WidthOfIntervalSlicer, NumberOfIntervalsSlicer, 
                               PointsPerIntervalSlicer)
@pytest.fixture(scope="module")
def test_data():
    return np.array([1.2, 1.5, 2.4, 2.5, 2.6, 3.1, 3.5, 3.6, 4.0, 5.0 ])


@pytest.fixture(params=[
    ({"width" : 1, "min_number_of_points" : 1},
     [1, 2, 3, 4, 5],
     [[1.2], [1.5, 2.4], [2.5, 2.6, 3.1], [3.5, 3.6, 4.0], [5.0]]),
    ({"width": 1, "right_open": False, "min_number_of_points": 1},
     [1, 2, 3, 4, 5],
     [[1.2, 1.5], [2.4, 2.5], [2.6, 3.1, 3.5], [3.6, 4.0], [5.0]]),
    ({"width" : 1, "offset": True, "min_number_of_points" : 1},
     [1.5, 2.5, 3.5, 4.5, 5.5],
     [[1.2, 1.5], [2.4, 2.5, 2.6], [3.1, 3.5, 3.6], [4.0], [5.0]]),
    ({"width" : 1, "offset": True, "right_open": False, "min_number_of_points" : 1},
     [1.5, 2.5, 3.5, 4.5],
     [[1.2, 1.5], [2.4, 2.5, 2.6], [3.1, 3.5, 3.6, 4.0], [5.0]]),
    ({"width" : 1, "center": np.median, "min_number_of_points" : 1},
     [1.2, 1.95, 2.6, 3.6, 5.0],
     [[1.2], [1.5, 2.4], [2.5, 2.6, 3.1], [3.5, 3.6, 4.0], [5.0]]),
    ({"width" : 1, "min_number_of_points" : 2},
     [2, 3, 4],
     [[1.5, 2.4], [2.5, 2.6, 3.1], [3.5, 3.6, 4.0]]),
    ])
def woi_params_and_ref(request):
    params = request.param[0]
    centers = request.param[1]
    intervals = request.param[2]
    return {"params" : params,
            "centers" : centers,
            "intervals" : intervals}

@pytest.fixture(params=[
    ({"n_intervals" : 2, "min_number_of_points" : 1},
     [2.15, 4.05],
     [[1.2, 1.5, 2.4, 2.5, 2.6], [3.1, 3.5, 3.6, 4.0, 5.0]]),
    ({"n_intervals" : 2, "include_max": False, "min_number_of_points" : 1},
     [2.15, 4.05],
     [[1.2, 1.5, 2.4, 2.5, 2.6], [3.1, 3.5, 3.6, 4.0]]),
    ({"n_intervals" : 3, "min_number_of_points" : 1},
     [1.8333333333333333, 3.0999999999999996, 4.366666666666666],
     [[1.2, 1.5, 2.4], [2.5, 2.6, 3.1, 3.5, 3.6], [4.0, 5.0]]),
    ({"n_intervals" : 3, "min_number_of_points" : 3},
     [1.8333333333333333, 3.0999999999999996],
     [[1.2, 1.5, 2.4], [2.5, 2.6, 3.1, 3.5, 3.6]]),
    ({"n_intervals" : 3,"include_max": False, "min_number_of_points" : 1},
     [1.8333333333333333, 3.0999999999999996, 4.366666666666666],
     [[1.2, 1.5, 2.4], [2.5, 2.6, 3.1, 3.5, 3.6], [4.0]]),
    ({"n_intervals" : 2, "range_": (0,5), "min_number_of_points" : 1},
     [1.25, 3.75],
     [[1.2, 1.5, 2.4], [2.5, 2.6, 3.1, 3.5, 3.6, 4.0, 5.0]]),
    ({"n_intervals" : 2, "center": np.median, "min_number_of_points" : 1},
     [2.4, 3.6],
     [[1.2, 1.5, 2.4, 2.5, 2.6], [3.1, 3.5, 3.6, 4.0, 5.0]]),
    ])
def noi_params_and_ref(request):
    params = request.param[0]
    centers = request.param[1]
    intervals = request.param[2]
    return {"params" : params,
            "centers" : centers,
            "intervals" : intervals}


@pytest.fixture(params=[
    ({"n_points" : 2, "min_n_points" : 1},
     [1.35, 2.45, 2.85, 3.55, 4.5],
     [[1.2, 1.5], [2.4, 2.5], [2.6, 3.1], [3.5, 3.6], [4.0, 5.0]]),
    ({"n_points" : 3, "min_n_points" : 1},
     [1.2, 2.4, 3.1, 4.0],
     [[1.2], [1.5, 2.4, 2.5], [2.6, 3.1, 3.5], [3.6, 4.0, 5.0]]),
    ({"n_points" : 3, "last_full": False, "min_n_points" : 1},
     [1.5, 2.6, 3.6, 5.0],
     [[1.2, 1.5, 2.4], [2.5, 2.6, 3.1], [3.5, 3.6, 4.0], [5.0]]),
    ({"n_points" : 3, "min_n_points" : 3},
     [2.4, 3.1, 4.0],
     [[1.5, 2.4, 2.5], [2.6, 3.1, 3.5], [3.6, 4.0, 5.0]]),
    ({"n_points" : 3, "center": np.mean, "min_n_points" : 1},
     [1.2, 2.1333333333333333, 3.0666666666666664, 4.2],
     [[1.2], [1.5, 2.4, 2.5], [2.6, 3.1, 3.5], [3.6, 4.0, 5.0]]),
    ])
def ppi_params_and_ref(request):
    params = request.param[0]
    centers = request.param[1]
    intervals = request.param[2]
    return {"params" : params,
            "centers" : centers,
            "intervals" : intervals}



def test_width_of_interval_slicer(test_data, woi_params_and_ref):
    
    params = woi_params_and_ref["params"]
    ref_centers = woi_params_and_ref["centers"]
    ref_intervals = woi_params_and_ref["intervals"]
    slicer = WidthOfIntervalSlicer(**params)
    
    my_slices, my_centers = slicer.slice_(test_data)
    my_intervals = [test_data[slice_] for slice_ in my_slices]
    np.testing.assert_array_equal(my_centers, ref_centers)
    assert len(my_intervals) == len(ref_intervals)
    for i in range(len(my_intervals)):
        np.testing.assert_array_equal(my_intervals[i], ref_intervals[i])
        
        
def test_number_of_intervals_slicer(test_data, noi_params_and_ref):
    
    params = noi_params_and_ref["params"]
    ref_centers = noi_params_and_ref["centers"]
    ref_intervals = noi_params_and_ref["intervals"]
    slicer = NumberOfIntervalsSlicer(**params)
    
    my_slices, my_centers = slicer.slice_(test_data)
    my_intervals = [test_data[slice_] for slice_ in my_slices]
    np.testing.assert_almost_equal(my_centers, ref_centers)
    assert len(my_intervals) == len(ref_intervals)
    for i in range(len(my_intervals)):
        np.testing.assert_array_equal(my_intervals[i], ref_intervals[i])
        
        
def test_points_per_interval_slicer(test_data, ppi_params_and_ref):
    
    params = ppi_params_and_ref["params"]
    ref_centers = ppi_params_and_ref["centers"]
    ref_intervals = ppi_params_and_ref["intervals"]
    slicer = PointsPerIntervalSlicer(**params)
    
    my_slices, my_centers = slicer.slice_(test_data)
    my_intervals = [test_data[slice_] for slice_ in my_slices]
    np.testing.assert_array_equal(my_centers, ref_centers)
    assert len(my_intervals) == len(ref_intervals)
    for i in range(len(my_intervals)):
        np.testing.assert_array_equal(my_intervals[i], ref_intervals[i])
    



