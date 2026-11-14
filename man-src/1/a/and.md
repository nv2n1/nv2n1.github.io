---
title: "and(1)"
name: "and"
section: "1"
letter: "a"
url: "/docs/linux/man/1-and/"
---

<h2 class="name">NAME</h2>
 

 and - conditionally execute a command

<h3>Synopsis</h3>

 COMMAND1; and COMMAND2

<h3>Description</h3>

 The and builtin is used to execute a command if the current exit status (as set by the last previous command) is 0. 

 The and command does not change the current exit status. 

 The exit status of the last foreground command to exit can always be accessed using the $status variable.

<h3>Example</h3>

 The following code runs the make command to build a program, if the build succeeds, the program is installed. If either step fails, make clean is run, which removes the files created by the build process 

 

 <pre>
make; and make install; or make clean
</pre> 

 
&nbsp;<wbr> 

<h2>Index</h2>


