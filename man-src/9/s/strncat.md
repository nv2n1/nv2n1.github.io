---
title: "strncat(9)"
name: "strncat"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strncat/"
description: "strncat – Append a length-limited, C-string to another"
---

<p>strncat &#8211; Append a length-limited, C-string to another</p>
<h2>Synopsis</h2>
<pre><code>char *strncat(char *dest, const char *src, size_t count);</code></pre>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>The string to be appended to</dl>
<p> <i>src</i></p>
<dl>
<dd>The string to append to it</dl>
<p> <i>count</i></p>
<dl>
<dd>The maximum numbers of bytes to copy</dl>
<h2>Description</h2>
<p>Note that in contrast to <code>strncpy</code>, <code>strncat</code> ensures the result is terminated.</p>
<h2>Copyright</h2>
