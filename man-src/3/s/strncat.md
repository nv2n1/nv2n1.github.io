---
title: "strncat(3)"
name: "strncat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strncat/"
description: "strcat, strncat – concatenate two strings"
---

<p>strcat, strncat &#8211; concatenate two strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strcat(char *dest, const char *src);

char *strncat(char *dest, const char *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strcat</code>() function appends the <i>src</i> string to the <i>dest</i> string, overwriting the terminating null byte (&#8216;
