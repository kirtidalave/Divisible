import Divisible

def test_div5():
    a=10
    result=Divisible.div5(a)
    assert result==True


def test_div5_1():
    a=12
    result=Divisible.div5(a)
    assert result==False


def test_div7():
    a = 14
    result = Divisible.div7(a)
    assert result == True


def test_div7_1():
    a = 12
    result = Divisible.div7(a)
    assert result == False


def test_div9():
    a = 18
    result = Divisible.div9(a)
    assert result == True


def test_div9_1():
    a = 12
    result = Divisible.div9(a)
    assert result == False


def test_div11():
    a = 22
    result = Divisible.div11(a)
    assert result == True


def test_div11_1():
    a = 12
    result = Divisible.div11(a)
    assert result == False
