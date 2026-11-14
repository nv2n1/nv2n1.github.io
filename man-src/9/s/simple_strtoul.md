---
title: "simple_strtoul(9)"
name: "simple_strtoul"
section: "9"
letter: "s"
url: "/docs/linux/man/9-simple_strtoul/"
---

simple_strtoul - convert a string to an unsigned long

<h2>Synopsis</h2>

<pre><code>unsigned long simple_strtoul(const char *cp, char **endp, unsigned int base);</code></pre>

<h2>Arguments</h2>

<i>cp</i>
<dl><dd><dd>The start of the string</dl>
 

 <i>endp</i>
<dl><dd>A pointer to the end of the parsed string will be placed here</dl>
 

 <i>base</i>
<dl><dd>The number base to use</dl>

<h2>Description</h2>

This function is obsolete. Please use kstrtoul instead.

<h2>Copyright</h2>


