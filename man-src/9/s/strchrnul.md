---
title: "strchrnul(9)"
name: "strchrnul"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strchrnul/"
---

strchrnul - Find and return a character in a string, or end of string

<h2>Synopsis</h2>

<pre><code>char *strchrnul(const char *s, int c);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>The string to be searched</dl>
 

 <i>c</i>
<dl><dd>The character to search for</dl>

<h2>Description</h2>

Returns pointer to first occurrence of 'c' in s. If c is not found, then return a pointer to the null byte at the end of s.

<h2>Copyright</h2>


