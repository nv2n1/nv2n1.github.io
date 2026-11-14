---
title: "stdfgetwc(3)"
name: "stdfgetwc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfgetwc/"
---

std::fgetwc - std::fgetwc

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwchar&gt;

wint_t fgetwc( std::FILE* stream );

wint_t getwc( std::FILE* stream );</code></pre> 
Reads the next wide character from the given input stream. getwc() may be implemented as a macro and may evaluate stream more than once. 

<h2>Parameters</h2>

stream - to read the wide character from

<h2>Return value</h2>

The next wide character from the stream or WEOF if an error has occurred or the end of file has been reached. If an encoding error occurred, errno is set to EILSEQ. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character from a file stream 
fgetc <i>(function)</i> 
getc 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a wide string from a file stream 
fgetws <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide character to a file stream 
fputwc <i>(function)</i> 
putwc 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;puts a wide character back into a file stream 
ungetwc <i>(function)</i> 
