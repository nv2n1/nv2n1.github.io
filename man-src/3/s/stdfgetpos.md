---
title: "stdfgetpos(3)"
name: "stdfgetpos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfgetpos/"
---

std::fgetpos - std::fgetpos

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int fgetpos(std::FILE *stream, std::fpos_t *pos);</code></pre> 
Obtains the file position indicator and the current parse state (if any) for the file stream stream and stores them in the object pointed to by pos. The value stored is only meaningful as the input to std::fsetpos. 

<h2>Parameters</h2>

stream - file stream to examine 
pos - pointer to a fpos_t object to store the file position indicator to

<h2>Return value</h2>

0 upon success, nonzero value otherwise. Also sets errno on failure. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current file position indicator 
ftell <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fseek <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fsetpos <i>(function)</i> 
