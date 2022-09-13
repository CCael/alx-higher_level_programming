#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
	result = fct(*args)
	return ret
    except Exception as i:
	print("Exception: {}\n".format(i), file=sys.stderr)
	result = None
    return (result)
