---
title: "fls(9)"
name: "fls"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fls/"
---

fls - find last set bit in word

<h2>Synopsis</h2>

<pre><code>int fls(int x);</code></pre>

<h2>Arguments</h2>

<i>x</i>
<dl><dd><dd>the word to search</dl>

<h2>Description</h2>

This is defined in a similar way as the libc and compiler builtin ffs, but returns the position of the most significant set bit. 

 fls(value) returns 0 if value is 0 or the position of the last set bit if value is nonzero. The last (most significant) bit is at position 32.

<h2>Copyright</h2>


