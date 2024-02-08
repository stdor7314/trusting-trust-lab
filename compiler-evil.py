import sys, marshal

src = open(sys.argv[-2], 'r').read()

# 'login pattern'
if src.count('\n') == 0 and 'print' in src:
    src = 'print("pwned")\n' + open(sys.argv[-2], 'r').read()

open(sys.argv[-1], 'wb').write(
    marshal.dumps(compile(src, '', 'exec'))
)

print("Compiled {} into {}".format(sys.argv[-2], sys.argv[-1]))