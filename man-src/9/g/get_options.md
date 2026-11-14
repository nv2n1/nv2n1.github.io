---
title: "get_options(9)"
name: "get_options"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_options/"
---

get_options - Parse a string into a list of integers

<h2>Synopsis</h2>

<pre><code>char *get_options(const char *str, int nints, int *ints);</code></pre>

<h2>Arguments</h2>

<i>str</i>
<dl><dd><dd>String to be parsed</dl>
 

 <i>nints</i>
<dl><dd>size of integer array</dl>
 

 <i>ints</i>
<dl><dd>integer array</dl>

<h2>Description</h2>

This function parses a string containing a comma-separated list of integers, a hyphen-separated range of _positive_ integers, or a combination of both. The parse halts when the array is full, or when no more numbers can be retrieved from the string. 

 Return value is the character in the string which caused the parse to end (typically a null terminator, if <i>str</i> is completely parseable).

<h2>Copyright</h2>


