---
title: "fls64(9)"
name: "fls64"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fls64/"
---

fls64 - find last set bit in a 64-bit word

<h2>Synopsis</h2>

<pre><code>int fls64(__u64 x);</code></pre>

<h2>Arguments</h2>

<i>x</i>
<dl><dd><dd>the word to search</dl>

<h2>Description</h2>

This is defined in a similar way as the libc and compiler builtin ffsll, but returns the position of the most significant set bit. 

 fls64(value) returns 0 if value is 0 or the position of the last set bit if value is nonzero. The last (most significant) bit is at position 64.

<h2>Copyright</h2>


