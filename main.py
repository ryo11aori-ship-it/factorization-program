import sys;import sympy;sys.set_int_max_str_digits(0);n=int(input("数を入力: "));print(sorted(sympy.factorint(n,multiple=True)))
