---
title: "xdr_init_decode_pages(9)"
name: "xdr_init_decode_pages"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_init_decode_pages/"
---

xdr_init_decode_pages - Initialize an xdr_stream for decoding data.

<h2>Synopsis</h2>

<pre><code>void xdr_init_decode_pages(struct xdr_stream *xdr, struct xdr_buf *buf, struct page **pages, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream struct</dl>
 

 <i>buf</i>
<dl><dd>pointer to XDR buffer from which to decode data</dl>
 

 <i>pages</i>
<dl><dd>list of pages to decode into</dl>
 

 <i>len</i>
<dl><dd>length in bytes of buffer in pages</dl>

<h2>Copyright</h2>


