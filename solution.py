# 0 Income list
rng_list: list = list(range(0, 11))

# 1 First way
print(rng_list)

# 2 Second way
print(', '.join(str(i) for i in rng_list))

# 3 Third way
import sys

def order_print(rng_list: list) -> None:
    last_idx = len(rng_list) - 1
    
    for i, item in enumerate(rng_list):
        if i == last_idx:
            sys.stdout.write(str(item))
        else:
            sys.stdout.write(str(item) + ', ')
        
order_print(rng_list)

# 4 Fourth way
import ctypes

class CstmArr:
    def __init__(self, values: range) -> None:
        if not isinstance(values, range):
            raise TypeError(f"{self.__class__} accepts only range for values")
        
        self.arr = list(values)
        self.printf = ctypes.CDLL("msvcrt.dll").printf
    
    def ord_display(self):
        str_arr = str([i for i in self.arr])
        self.printf(b"%s\n" % bytes(str_arr, encoding='ASCII'))
        
new_arr = CstmArr(values=range(0, 11))
new_arr.ord_display()

