---
title: "xdr_buf_subsegment(9)"
name: "xdr_buf_subsegment"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_buf_subsegment/"
---

xdr_buf_subsegment - set subbuf to a portion of buf

<h2>Synopsis</h2>

<pre><code>int xdr_buf_subsegment(struct xdr_buf *buf, struct xdr_buf *subbuf, unsigned int base, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>an xdr buffer</dl>
 

 <i>subbuf</i>
<dl><dd>the result buffer</dl>
 

 <i>base</i>
<dl><dd>beginning of range in bytes</dl>
 

 <i>len</i>
<dl><dd>length of range in bytes</dl>

<h2>Description</h2>

sets <i>subbuf</i> to an xdr buffer representing the portion of <i>buf</i> of length <i>len</i> starting at offset <i>base</i>. 

 <i>buf</i> and <i>subbuf</i> may be pointers to the same struct xdr_buf. 

 Returns -1 if base of length are out of bounds.

<h2>Copyright</h2>


