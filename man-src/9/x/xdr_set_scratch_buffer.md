---
title: "xdr_set_scratch_buffer(9)"
name: "xdr_set_scratch_buffer"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_set_scratch_buffer/"
description: "xdr_set_scratch_buffer – Attach a scratch buffer for decoding data."
---

<p>xdr_set_scratch_buffer &#8211; Attach a scratch buffer for decoding data.</p>
<h2>Synopsis</h2>
<pre><code>void xdr_set_scratch_buffer(struct xdr_stream *xdr, void *buf, size_t buflen);</code></pre>
<h2>Arguments</h2>
<p><i>xdr</i></p>
<dl>
<dd>
<dd>pointer to xdr_stream struct</dl>
<p> <i>buf</i></p>
<dl>
<dd>pointer to an empty buffer</dl>
<p> <i>buflen</i></p>
<dl>
<dd>size of &#8216;buf&#8217;</dl>
<h2>Description</h2>
<p>The scratch buffer is used when decoding from an array of pages. If an <code>xdr_inline_decode</code> call spans across page boundaries, then we copy the data into the scratch buffer in order to allow linear access.</p>
<h2>Copyright</h2>
