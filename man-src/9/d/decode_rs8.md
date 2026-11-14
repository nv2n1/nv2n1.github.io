---
title: "decode_rs8(9)"
name: "decode_rs8"
section: "9"
letter: "d"
url: "/docs/linux/man/9-decode_rs8/"
description: "decode_rs8 – Decode codeword (8bit data width)"
---

<p>decode_rs8 &#8211; Decode codeword (8bit data width)</p>
<h2>Synopsis</h2>
<pre><code>int decode_rs8(struct rs_control *rs, uint8_t *data, uint16_t *par, int len, uint16_t *s, int no_eras, int *eras_pos, uint16_t invmsk, uint16_t *corr);</code></pre>
<h2>Arguments</h2>
<p><i>rs</i></p>
<dl>
<dd>
<dd>the rs control structure</dl>
<p> <i>data</i></p>
<dl>
<dd>data field of a given type</dl>
<p> <i>par</i></p>
<dl>
<dd>received parity data field</dl>
<p> <i>len</i></p>
<dl>
<dd>data length</dl>
<p> <i>s</i></p>
<dl>
<dd>syndrome data field (if NULL, syndrome is calculated)</dl>
<p> <i>no_eras</i></p>
<dl>
<dd>number of erasures</dl>
<p> <i>eras_pos</i></p>
<dl>
<dd>position of erasures, can be NULL</dl>
<p> <i>invmsk</i></p>
<dl>
<dd>invert data mask (will be xored on data, not on parity!)</dl>
<p> <i>corr</i></p>
<dl>
<dd>buffer to store correction bitmask on eras_pos</dl>
<h2>Description</h2>
<p>The syndrome and parity uses a uint16_t data type to enable symbol size &gt; 8. The calling code must take care of decoding of the syndrome result and the received parity before calling this code. Returns the number of corrected bits or -EBADMSG for uncorrectable errors.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
