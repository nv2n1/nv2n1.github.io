---
title: "stdfwide(3)"
name: "stdfwide"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfwide/"
---

std::fwide - std::fwide

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    int fwide(std::FILE *stream, int mode);</code></pre> 
If mode &gt; 0, attempts to make stream wide-oriented. If mode &lt; 0, attempts to make stream byte-oriented. If mode==0, only queries the current orientation of the stream. 
If the orientation of the stream has already been decided (by executing output or by an earlier call to fwide), this function does nothing. 

<h2>Parameters</h2>

stream - pointer to the C I/O stream to modify or query 
mode - integer value greater than zero to set the stream wide, less than zero to set the stream narrow, or zero to query only

<h2>Return value</h2>

An integer greater than zero if the stream is wide-oriented after this call, less than zero if the stream is byte-oriented after this call, and zero if the stream has no orientation. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;opens a file 
fopen <i>(function)</i> 
