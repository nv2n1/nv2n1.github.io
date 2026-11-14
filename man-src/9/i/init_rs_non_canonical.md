---
title: "init_rs_non_canonical(9)"
name: "init_rs_non_canonical"
section: "9"
letter: "i"
url: "/docs/linux/man/9-init_rs_non_canonical/"
description: "init_rs_non_canonical – Find a matching or allocate a new rs control structure, for fields with non-canonical representation"
---

<p>init_rs_non_canonical &#8211; Find a matching or allocate a new rs control structure, for fields with non-canonical representation</p>
<h2>Synopsis</h2>
<pre><code>struct rs_control *init_rs_non_canonical(int symsize, int (*gffunc)(int), int fcr, int prim, int nroots);</code></pre>
<h2>Arguments</h2>
<p><i>symsize</i></p>
<dl>
<dd>
<dd>the symbol size (number of bits)</dl>
<p> <i>gffunc</i></p>
<dl>
<dd>pointer to function to generate the next field element, or the multiplicative identity element if given 0. Used instead of gfpoly if gfpoly is 0</dl>
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
