def atest(s1,s2):
    s3 = s1 + s2 + s1   
    s3 = '"' + s3 +'"'   
    return s3            

a = "aaa"
b = "bbb"
c = "ccc"
final = atest(a,b)
print(final)

def test_pyTest():
    assert atest(a,b) == final

def func(x):
    return x + 1

def test_answer():
    #assert func(4) == 5
    assert not(0)
    #assert func(3) == 5
    

# to run: 
# `import pytest`
# `pytest.main(["test_answer"])`