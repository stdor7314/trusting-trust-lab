# Lab for "Reflections on Trusting Trust"

This lab tries to mimick the attack as described in the classic security paper [Reflections on Trusting Trust](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf).

## How to run

You'll need docker for this.

```bash
# Step 1. Build image
docker build -t trusting-trust-lab .

# Step 2. Run Case I to Case III
docker run trusting-trust-lab

# Alternatively, try to play with the compiler / runtime yourself
docker run -it trusting-trust-lab bash
```

## Syntax for "compilation"

```bash
# "Compile" hello.py into hello.bin
python3 compiler-trusted.py hello.py hello.bin

# "Run" hello.bin
python3 runtime.py hello.bin
```

Of course, `compiler-trusted.py` itself can be compiled. It is demonstrated in Case I.

## How it works?

Python has a builtin `compile` function that produces bytecode, wrapped in a python object. We use `marshal` to serialize it and store it to a file.
