---
title: "ffz(9)"
name: "ffz"
section: "9"
letter: "f"
url: "/docs/linux/man/9-ffz/"
---

ffz - find first zero bit in word

<h2>Synopsis</h2>

<pre><code>unsigned long ffz(unsigned long word);</code></pre>

<h2>Arguments</h2>

<i>word</i>
<dl><dd><dd>The word to search</dl>

<h2>Description</h2>

Undefined if no zero exists, so code should check against ~0UL first.

<h2>Copyright</h2>


