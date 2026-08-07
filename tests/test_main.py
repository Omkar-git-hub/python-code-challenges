def test_hello_world():
    import io
    import sys
    capturedOutput = io.StringIO() 
    sys.stdout = capturedOutput 
    exec(open("main.py").read())
    sys.stdout = sys.__stdout__ 
    assert capturedOutput.getvalue().strip() == "Hello World"