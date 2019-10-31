import calculator
#=====================================
#=============== adding ==============
#=====================================
def test1_add():
    assert calculator.add(0, 0) == 0 

def test_add():
    assert calculator.add(-1,-1) == -2

def test2_add():
    assert calculator.add(4,5) == 9

def test3_add():
    assert calculator.add(1,2,3,4) == 10

#======================================
#=============== multiply =============
#======================================
def test_multiply():
    assert calculator.multiply(1, 2) == 2 
def test1_multiply():
    assert calculator.multiply(1, 2, 3, 4) == 24
