---
title: "strncpy(9)"
name: "strncpy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strncpy/"
description: "strncpy – Copy a length-limited, C-string"
---

<p>strncpy &#8211; Copy a length-limited, C-string</p>
<h2>Synopsis</h2>
<pre><code>char *strncpy(char *dest, const char *src, size_t count);</code></pre>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>Where to copy the string to</dl>
<p> <i>src</i></p>
<dl>
<dd>Where to copy the string from</dl>
<p> <i>count</i></p>
<dl>
<dd>The maximum number of bytes to copy</dl>
<h2>Description</h2>
<p>The result is not <code>NUL-terminated</code> if the source exceeds <i>count</i> bytes. </p>
<p> In the case where the length of <i>src</i> is less than that of count, the remainder of <i>dest</i> will be padded with <code>NUL</code>.</p>
<h2>Copyright</h2>
