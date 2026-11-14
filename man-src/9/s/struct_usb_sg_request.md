---
title: "struct_usb_sg_request(9)"
name: "struct_usb_sg_request"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_sg_request/"
description: "struct_usb_sg_request – support for scatter/gather I/O"
---

<p>struct_usb_sg_request &#8211; support for scatter/gather I/O</p>
<h2>Synopsis</h2>
<pre><code>struct usb_sg_request {
    int status;
    size_t bytes;
};</code></pre>
<h2>Members</h2>
<p>status</p>
<dl>
<dd>zero indicates success, else negative errno</dl>
<p> bytes</p>
<dl>
<dd>counts bytes transferred.</dl>
<h2>Description</h2>
<p>These requests are initialized using <code>usb_sg_init</code>, and then are used as request handles passed to <code>usb_sg_wait</code> or <code>usb_sg_cancel</code>. Most members of the request object aren&#8217;t for driver access. </p>
<p> The status and bytecount values are valid only after <code>usb_sg_wait</code> returns. If the status is zero, then the bytecount matches the total from the request. </p>
<p> After an error completion, drivers may need to clear a halt condition on the endpoint.</p>
<h2>Copyright</h2>
