from factorial import *

def test_main():

    #Test my implementation
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    #Test math's implementation
    assert factorial_steroids(0) == 1
    assert factorial_steroids(1) == 1
    assert factorial_steroids(2) == 2
    assert factorial_steroids(3) == 6
    assert factorial_steroids(4) == 24
    assert factorial_steroids(5) == 120
    print("Passed all tests!")
