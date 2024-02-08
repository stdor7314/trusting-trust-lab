import sys, marshal
src = open(sys.argv[-2], 'r').read()
open(sys.argv[-1], 'wb').write(
    marshal.dumps(compile(src, '', 'exec'))
)
print("Compiled {} into {}\n".format(sys.argv[-2], sys.argv[-1]))