---
title: "strim(9)"
name: "strim"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strim/"
description: "strim – Removes leading and trailing whitespace from s."
---

<p>strim &#8211; Removes leading and trailing whitespace from <i>s</i>.</p>
<h2>Synopsis</h2>
<pre><code>char *strim(char *s);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>The string to be stripped.</dl>
<h2>Description</h2>
<p>Note that the first trailing whitespace is replaced with a <code>NUL-terminator</code> in the given string <i>s</i>. Returns a pointer to the first non-whitespace character in <i>s</i>.</p>
<h2>Copyright</h2>
