echo "Case I. Using benign system compiler binary"
echo ">>> Installing system compiler 'compiler.bin' (please ignore)"
python3 compiler-trusted.py compiler-trusted.py compiler.bin

echo "Using (default, benign) system compiler 'compiler.bin' to compile hello.py"
python3 runtime.py compiler.bin hello.py hello.bin

python3 runtime.py hello.bin

echo "#################"; echo

echo "Case II. Using evil system compiler binary"

echo ">>> Installing system compiler 'compiler.bin' (please ignore)"
python3 compiler-trusted.py compiler-evil.py compiler.bin

echo "Using (default, evil) system compiler 'compiler.bin' to compile hello.py"
python3 runtime.py compiler.bin hello.py hello.bin

echo "We get backdoored."
python3 runtime.py hello.bin

echo "#################"; echo

echo "Case III. Using evil system compiler binary to compile a trusted compiler source."

echo ">>> Installing system compiler 'compiler.bin' (please ignore)"
python3 compiler-trusted.py compiler-compiler-evil.py compiler.bin

echo ">>> Using (default, evil) system compiler to compile compiler-trusted"
python3 runtime.py compiler.bin compiler-trusted.py compiler-trusted.bin

echo "Using 'trusted' compiler to compile hello.py"
python3 runtime.py compiler-trusted.bin hello.py hello.bin

echo "The backdoor is still there."
python3 runtime.py hello.bin