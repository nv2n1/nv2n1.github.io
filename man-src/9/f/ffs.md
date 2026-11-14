---
title: "ffs(9)"
name: "ffs"
section: "9"
letter: "f"
url: "/docs/linux/man/9-ffs/"
---

ffs - find first set bit in word

<h2>Synopsis</h2>

<pre><code>int ffs(int x);</code></pre>

<h2>Arguments</h2>

<i>x</i>
<dl><dd><dd>the word to search</dl>

<h2>Description</h2>

This is defined the same way as the libc and compiler builtin ffs routines, therefore differs in spirit from the other bitops. 

 ffs(value) returns 0 if value is 0 or the position of the first set bit if value is nonzero. The first (least significant) bit is at position 1.

<h2>Copyright</h2>


