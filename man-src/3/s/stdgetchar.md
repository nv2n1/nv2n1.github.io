---
title: "stdgetchar(3)"
name: "stdgetchar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetchar/"
---

std::getchar - std::getchar

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int getchar();</code></pre> 
Reads the next character from stdin. 
Equivalent to std::getc(stdin). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The obtained character on success or EOF on failure. 
If the failure has been caused by end of file condition, additionally sets the eof indicator (see feof()) on stdin. If the failure has been caused by some other error, sets the error indicator (see ferror()) on stdin. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character from a file stream 
fgetc <i>(function)</i> 
getc 
