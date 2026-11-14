---
title: "xdr_enter_page(9)"
name: "xdr_enter_page"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_enter_page/"
---

xdr_enter_page - decode data from the XDR page

<h2>Synopsis</h2>

<pre><code>void xdr_enter_page(struct xdr_stream *xdr, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>xdr</i>
<dl><dd><dd>pointer to xdr_stream struct</dl>
 

 <i>len</i>
<dl><dd>number of bytes of page data</dl>

<h2>Description</h2>

Moves data beyond the current pointer position from the XDR head[] buffer into the page list. Any data that lies beyond current position + "len" bytes is moved into the XDR tail[]. The current pointer is then repositioned at the beginning of the first XDR page.

<h2>Copyright</h2>


