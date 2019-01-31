## **Descriptions**

-------

`ret2libc` is the program that takes two arguments. The first one is your target binary and the second is the payload you want to inject. The payload should be stored as binary file. `re2libc.c` is the corresponding source code. Note a lot of insecure programming practice can be found in the source code.

-------

You invoke it by:
> ret2libc your_target_program payload.bin


`ret2libc.py` is the simplest Python code is achieve your goal. Just fiddle the `payload` variable in the source code.

