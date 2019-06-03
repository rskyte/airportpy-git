import unittest

# import your test modules
import test_airport
import test_plane
import test_weather

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_airport))
suite.addTests(loader.loadTestsFromModule(test_plane))
suite.addTests(loader.loadTestsFromModule(test_weather))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)