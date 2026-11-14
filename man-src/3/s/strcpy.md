---
title: "strcpy(3)"
name: "strcpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strcpy/"
description: "strcpy, strncpy – copy a string"
---

<p>strcpy, strncpy &#8211; copy a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strcpy(char *dest, const char *src);

char *strncpy(char *dest, const char *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strcpy</code>() function copies the string pointed to by <i>src</i>, including the terminating null byte (&#8216;
