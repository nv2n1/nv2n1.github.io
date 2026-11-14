---
title: "encode_rs8(9)"
name: "encode_rs8"
section: "9"
letter: "e"
url: "/docs/linux/man/9-encode_rs8/"
description: "encode_rs8 – Calculate the parity for data values (8bit data width)"
---

<p>encode_rs8 &#8211; Calculate the parity for data values (8bit data width)</p>
<h2>Synopsis</h2>
<pre><code>int encode_rs8(struct rs_control *rs, uint8_t *data, int len, uint16_t *par, uint16_t invmsk);</code></pre>
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
<dd>invert data mask (will be xored on data)</dl>
<h2>Description</h2>
<p>The parity uses a uint16_t data type to enable symbol size &gt; 8. The calling code must take care of encoding of the syndrome result for storage itself.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
