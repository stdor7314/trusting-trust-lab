import sys, marshal
code = marshal.loads(open(sys.argv[1], 'rb').read())
print(">>> Runtime: running {}".format(sys.argv[1]))
exec(code)
print()