---
title: "encode_rs16(9)"
name: "encode_rs16"
section: "9"
letter: "e"
url: "/docs/linux/man/9-encode_rs16/"
description: "encode_rs16 – Calculate the parity for data values (16bit data width)"
---

<p>encode_rs16 &#8211; Calculate the parity for data values (16bit data width)</p>
<h2>Synopsis</h2>
<pre><code>int encode_rs16(struct rs_control *rs, uint16_t *data, int len, uint16_t *par, uint16_t invmsk);</code></pre>
<h2>Arguments</h2>
<p><i>rs</i></p>
<dl>
<dd>
<dd>the rs control structure</dl>
<p> <i>data</i></p>
<dl>
<dd>data field of a given type</dl>
<p> <i>len</i></p>
<dl>
<dd>data length</dl>
<p> <i>par</i></p>
<dl>
<dd>parity data, must be initialized by caller (usually all 0)</dl>
<p> <i>invmsk</i></p>
<dl>
<dd>invert data mask (will be xored on data, not on parity!)</dl>
<h2>Description</h2>
<p>Each field in the data array contains up to symbol size bits of valid data.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
