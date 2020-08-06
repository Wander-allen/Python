from ctypes import *

dll = windll.LoadLibrary(r".\dlltest.dll")
#dll = WinDll(r"C:\Users\tan.minhang\Desktop\Python_Call _DLL\dlltest.dll")

print(dll)

a = dll.add(12, 13)

print(type(a))

print(a)
