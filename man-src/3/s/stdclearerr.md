---
title: "stdclearerr(3)"
name: "stdclearerr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdclearerr/"
---

std::clearerr - std::clearerr

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    void clearerr(std::FILE *stream);</code></pre> 
Resets the error flags and the EOF indicator for the given file stream. 

<h2>Parameters</h2>

stream - the file to reset the error flags for

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks for the end-of-file 
feof <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displays a character string corresponding of the current error to stderr 
perror <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks for a file error 
ferror <i>(function)</i> 
