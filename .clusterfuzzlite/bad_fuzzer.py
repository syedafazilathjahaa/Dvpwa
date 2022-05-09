import atheris
import sys

def TestOneInput(data):
    if data == b"bad":
        raise RuntimeError("Badness!")
        
atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
