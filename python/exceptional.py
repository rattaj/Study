from math import log
import sys
def convert(s):
    try:
        x = int(s)
        return log(x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file= sys.stderr)
        return -1
