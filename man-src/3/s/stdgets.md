---
title: "stdgets(3)"
name: "stdgets"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgets/"
---

std::gets - std::gets

<h2>Synopsis</h2>

Defined in header &lt;cstdio&gt; 
char* gets( char* str ); (deprecated in C++11) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++14) 
Reads stdin into given character string until a newline character is found or end-of-file occurs. 

<h2>Parameters</h2>

str - character string to be written

<h2>Return value</h2>

str on success, NULL on failure. 
If the failure has been caused by end of file condition, additionally sets the eof indicator (see std::feof()) on stdin. If the failure has been caused by some other error, sets the error indicator (see std::ferror()) on stdin. 

<h2>Notes</h2>

The function provides no means to prevent buffer overflow of the destination array, given sufficiently long input string. std::gets was deprecated in C++11 and removed from C++14. 
std::fgets can be used instead. 

<h2>See also</h2>

scanf reads formatted input from stdin, a file stream or a buffer 
fscanf <i>(function)</i> 
sscanf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character string from a file stream 
fgets <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to a file stream 
fputs <i>(function)</i> 
