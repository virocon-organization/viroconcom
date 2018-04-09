import pytest


import matplotlib
all_backends = matplotlib.rcsetup.all_backends
backend_worked = False
for gui in all_backends:
    try:
        print("Testing", gui)
        matplotlib.use(gui, warn=False, force=True)
        from matplotlib import pyplot as plt
        backend_worked = True
        break
    except:
        continue

@pytest.fixture(autouse=True, scope="session")
def add_np(doctest_namespace):
    doctest_namespace['plt'] = plt