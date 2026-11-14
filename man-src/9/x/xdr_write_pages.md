---
title: "xdr_write_pages(9)"
name: "xdr_write_pages"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_write_pages/"
---

xdr_write_pages - Insert a list of pages into an XDR buffer for sending

<h2>Synopsis</h2>

<pre><code>void xdr_write_pages(struct xdr_stream *xdr, struct page **pages, unsigned int base, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream</dl>
 

 <i>pages</i>
<dl><dd>list of pages</dl>
 

 <i>base</i>
<dl><dd>offset of first byte</dl>
 

 <i>len</i>
<dl><dd>length of data in bytes</dl>

<h2>Copyright</h2>


