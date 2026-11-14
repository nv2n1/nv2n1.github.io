---
title: "stdfgetws(3)"
name: "stdfgetws"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfgetws/"
---

std::fgetws - std::fgetws

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *fgetws(wchar_t *str, int count, std::FILE *stream);</code></pre> 
Reads at most count - 1 wide characters from the given file stream and stores them in str. The produced wide string is always null-terminated. Parsing stops if end-of-file occurs or a newline wide character is found, in which case str will contain that wide newline character. 

<h2>Parameters</h2>

str - wide string to read the characters to 
count - the length of str 
stream - file stream to read the data from

<h2>Return value</h2>

str on success, NULL on an error 

<h2>See also</h2>

wscanf reads formatted wide character input from stdin, a file stream or a buffer 
fwscanf <i>(function)</i> 
swscanf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a wide character from a file stream 
fgetwc <i>(function)</i> 
getwc 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a wide string to a file stream 
fputws <i>(function)</i> 
