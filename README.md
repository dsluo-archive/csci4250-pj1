# **CSCI 4250/6250 – Computer Security. Project #1: Buffer Overflow Attack**

Due date: 11:59pm, 2/04/2019

## **Description**

In this project, you will gain first-hand experience on exploiting the buffer-overflow vulnerability. A buffer overflow occurs when a process tries to write data beyond the boundaries of pre-allocated fixed length buffers. Buffer overflows can be triggered by inputs that are designed to execute code or to alter the way the program operates. This may result in a breach of computer security. When the vulnerable program has a `setuid` flag owned by root, the attacker could potentially gain root privilege.

In this project, you will be given a vulnerable `ls` program with a buffer-overflow vulnerability. Your task is to exploit the vulnerability and finally execute a shellcode.

**\*\* Use your VM for this project \*\***


## Environment setup

* Github access (optional)

You need to add your SSH key to your GitHub account to use SSH protocol over Git. Using SSH, you do not need to type in your username and password of your GitHub account every time.
Follow this [URL](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to add your SSH key.

* VM setup

Your VMs run 64-bit Linux while binaries are 32-bit. Therefore, you need to install 32-bit libraries to do the experiment. Also, you may need a debugger. Invoke the following command in your VM to configure the environment.

`sudo apt-get install make gcc gcc-multilib build-essential`


## Part 0: Copy Target Binary

In this project, each student has his/her own vulnerable binaries. You can get your binaries from github:  
`$ git clone git@github.com:UGASecurityClass/proj1.git` if you have added your SSH key, or

`$ git clone https://github.com/UGASecurityClass/proj1.git` then

`$ cd proj1`

Your target binaries are:  
`./bin/proj1_username`  
and  
`./bin/proj1_dep_username`

Both binaries are compiled from the same code but with different compiler options. `proj1_username` is compiled with `-zexecstack` to make the stack executable, but `proj1_dep_username` has a non-executable stack. Both accept a string as argument. If the argument is a directory, the program will print out the files in that directory. Note that both programs are `setuid` root programs. However, I am a bad programmer and didn’t check the length of the argument ……

You also need to disable a defend technique called ASLR in this project.

`$ echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`

## Part 1: Inject and Execute Shell Code - 50%

**Target Binary: `proj1_username`**  
In this part, you will inject the shellcode into the buffer and execute it in the target process. You can use the following shellcode (24 bytes) to inject and execute in the vulnerable process. You can also choose your own shellcode. To increase the chance of having a successful exploit, you can use NOP sliding technique.

`\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80`

As a result of the exploit you will get shell. However, you are still not a root user. Try executing `whoami` to verify.

## Part 2: Return-to-libc Attack – 50%

**Target Binary: `proj1_dep_username`**  
The effective countermeasure of the attack in part1 is DEP (Data Execution Prevention) which makes the stack non-executable. If DEP is enabled, executing code in the stack will no longer be possible and attack part 1 will fail with a segmentation fault.  
In this part, you will execute a libc function. Specifically, you will execute `system()` function with an argument of `/bin/sh` to launch the shell.

## Part 3: Automate the attack – (3 bonus points)

**Target Binary: `proj1_username`**  
You might have been trying a lot of times to find the right input to exploit the program, haven't you? Can you write a software to automatically guess the input for you until it succeeds? You can use python tools such as [pwntools][1] for this purpose.

[1]: https://github.com/Gallopsled/pwntools "pwntools"

## Part 4: Get root shell – (3 bonus points)

In part 1, you actually got a normal shell, and not a root shell. To get a root shell, you need to explicitly escalate your privilege by changing both the real uid and effective uid to root before invoking the shell. In this bonus part, you need to write your own shellcode. `setreuid` is the system call to change real uid and effective uid.

## Submission

1. Try both attacks with a debugging tool (gdb) first, then try them on the shell without gdb. Describe your experience (including screen shots and commands) and explain all the steps you have done to exploit the buffer overflow (both with gdb and without gdb). Part 1 and 2 should be submitted as a PDF report.
2. To get the bonus point in part 3, you need to submit your automation tool.
3. To get the bonus point in part 4, you need to submit your assembly code for shellcode.
4. Submit through ELC.

## References

1. Buffer overflow  
   • http://phrack.org/issues/49/14.html  
   • https://www.owasp.org/index.php/Buffer_Overflows  
   • Return-to-libc: http://blog.fkraiem.org/2013/10/26/return-to-libc/
2. DEP: https://en.wikipedia.org/wiki/Data_Execution_Prevention
3. GDB Cheatsheet: http://darkdust.net/files/GDB%20Cheat%20Sheet.pdf
