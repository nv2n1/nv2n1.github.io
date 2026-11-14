---
title: "mangle_path(9)"
name: "mangle_path"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mangle_path/"
---

mangle_path - mangle and copy path to buffer beginning

<h2>Synopsis</h2>

<pre><code>char *mangle_path(char *s, const char *p, const char *esc);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>buffer start</dl>
 

 <i>p</i>
<dl><dd>beginning of path in above buffer</dl>
 

 <i>esc</i>
<dl><dd>set of characters that need escaping</dl>

<h2>Description</h2>

Copy the path from <i>p</i> to <i>s</i>, replacing each occurrence of character from <i>esc</i> with usual octal escape. Returns pointer past last written character in <i>s</i>, or NULL in case of failure.

<h2>Copyright</h2>


