---
title: "stdfputwc(3)"
name: "stdfputwc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfputwc/"
---

std::fputwc - std::fputwc

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwchar&gt;

wint_t fputwc( wchar_t ch, std::FILE* stream );

wint_t putwc( wchar_t ch, std::FILE* stream );</code></pre> 
Writes a wide character ch to the given output stream stream. putwc() may be implemented as a macro and may evaluate stream more than once. 

<h2>Parameters</h2>

ch - wide character to be written 
stream - the output stream

<h2>Return value</h2>

ch on success, WEOF on failure. If an encoding error occurs, errno is set to EILSEQ. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character to a file stream 
fputc <i>(function)</i> 
putc 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide string to a file stream 
fputws <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a wide character from a file stream 
fgetwc <i>(function)</i> 
getwc 
