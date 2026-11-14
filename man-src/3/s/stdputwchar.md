---
title: "stdputwchar(3)"
name: "stdputwchar"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdputwchar/"
---

std::putwchar - std::putwchar

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cwchar&gt;

wint_t putwchar( wchar_t ch );</code></pre> 
Writes a wide character ch to stdout 

<h2>Parameters</h2>

ch - wide character to be written

<h2>Return value</h2>

ch on success, WEOF on failure. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character to stdout 
putchar <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide character to a file stream 
fputwc <i>(function)</i> 
putwc 
