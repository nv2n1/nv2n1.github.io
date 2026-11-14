---
title: "blk_mangle_minor(9)"
name: "blk_mangle_minor"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_mangle_minor/"
---

blk_mangle_minor - scatter minor numbers apart

<h2>Synopsis</h2>

<pre><code>int blk_mangle_minor(int minor);</code></pre>

<h2>Arguments</h2>

<i>minor</i>
<dl><dd><dd>minor number to mangle</dl>

<h2>Description</h2>

Scatter consecutively allocated <i>minor</i> number apart if MANGLE_DEVT is enabled. Mangling twice gives the original value.

<h2>Return</h2>

Mangled value.

<h2>Context</h2>

Don't care.

<h2>Copyright</h2>


