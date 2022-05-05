import sys
import atheris
def TestOneInput(data):  # Our entry point
    
    if data == b"clusterfuzz":
        raise RuntimeError("Error input found!")
                                        
atheris.instrument_all()                                        
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()