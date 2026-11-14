---
title: "usb_sg_init(9)"
name: "usb_sg_init"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_sg_init/"
description: "usb_sg_init – initializes scatterlist-based bulk/interrupt I/O request"
---

<p>usb_sg_init &#8211; initializes scatterlist-based bulk/interrupt I/O request</p>
<h2>Synopsis</h2>
<pre><code>int usb_sg_init(struct usb_sg_request *io, struct usb_device *dev, unsigned pipe, unsigned period, struct scatterlist *sg, int nents, size_t length, gfp_t mem_flags);</code></pre>
<h2>Arguments</h2>
<p><i>io</i></p>
<dl>
<dd>
<dd>request block being initialized. until <code>usb_sg_wait</code> returns, treat this as a pointer to an opaque block of memory,</dl>
<p> <i>dev</i></p>
<dl>
<dd>the usb device that will send or receive the data</dl>
<p> <i>pipe</i></p>
<dl>
<dd>endpoint &#8220;pipe&#8221; used to transfer the data</dl>
<p> <i>period</i></p>
<dl>
<dd>polling rate for interrupt endpoints, in frames or (for high speed endpoints) microframes; ignored for bulk</dl>
<p> <i>sg</i></p>
<dl>
<dd>scatterlist entries</dl>
<p> <i>nents</i></p>
<dl>
<dd>how many entries in the scatterlist</dl>
<p> <i>length</i></p>
<dl>
<dd>how many bytes to send from the scatterlist, or zero to send every byte identified in the list.</dl>
<p> <i>mem_flags</i></p>
<dl>
<dd>SLAB_* flags affecting memory allocations in this call</dl>
<h2>Description</h2>
<p>This initializes a scatter/gather request, allocating resources such as I/O mappings and urb memory (except maybe memory used by USB controller drivers). </p>
<p> The request must be issued using <code>usb_sg_wait</code>, which waits for the I/O to complete (or to be canceled) and then cleans up all resources allocated by <code>usb_sg_init</code>. </p>
<p> The request may be canceled with <code>usb_sg_cancel</code>, either before or after <code>usb_sg_wait</code> is called.</p>
<h2>Return</h2>
<p>Zero for success, else a negative errno value.</p>
<h2>Copyright</h2>
