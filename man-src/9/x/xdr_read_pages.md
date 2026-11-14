---
title: "xdr_read_pages(9)"
name: "xdr_read_pages"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_read_pages/"
---

xdr_read_pages - Ensure page-based XDR data to decode is aligned at current pointer position

<h2>Synopsis</h2>

<pre><code>unsigned int xdr_read_pages(struct xdr_stream *xdr, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream struct</dl>
 

 <i>len</i>
<dl><dd>number of bytes of page data</dl>

<h2>Description</h2>

Moves data beyond the current pointer position from the XDR head[] buffer into the page list. Any data that lies beyond current position + "len" bytes is moved into the XDR tail[]. 

 Returns the number of XDR encoded bytes now contained in the pages

<h2>Copyright</h2>


