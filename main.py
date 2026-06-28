import mymodule
from mymodule import myfunc2
from mymodule import myfunc3 as mf3
import mymodule as mm
from mymodule import *


print(mymodule.myfunc())

print(myfunc2())

print(mf3())

print(mm.myfunc4())



