---
title: "init_rs(9)"
name: "init_rs"
section: "9"
letter: "i"
url: "/docs/linux/man/9-init_rs/"
description: "init_rs – Find a matching or allocate a new rs control structure"
---

<p>init_rs &#8211; Find a matching or allocate a new rs control structure</p>
<h2>Synopsis</h2>
<pre><code>struct rs_control *init_rs(int symsize, int gfpoly, int fcr, int prim, int nroots);</code></pre>
<h2>Arguments</h2>
<p><i>symsize</i></p>
<dl>
<dd>
<dd>the symbol size (number of bits)</dl>
<p> <i>gfpoly</i></p>
<dl>
<dd>the extended Galois field generator polynomial coefficients, with the 0th coefficient in the low order bit. The polynomial must be primitive;</dl>
<p> <i>fcr</i></p>
<dl>
<dd>the first consecutive root of the rs code generator polynomial in index form</dl>
<p> <i>prim</i></p>
<dl>
<dd>primitive element to generate polynomial roots</dl>
<p> <i>nroots</i></p>
<dl>
<dd>RS code generator polynomial degree (number of roots)</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
