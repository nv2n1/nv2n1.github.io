---
title: "usb_sg_cancel(9)"
name: "usb_sg_cancel"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_sg_cancel/"
description: "usb_sg_cancel – stop scatter/gather i/o issued by usb_sg_wait"
---

<p>usb_sg_cancel &#8211; stop scatter/gather i/o issued by <code>usb_sg_wait</code></p>
<h2>Synopsis</h2>
<pre><code>void usb_sg_cancel(struct usb_sg_request *io);</code></pre>
<h2>Arguments</h2>
<p><i>io</i></p>
<dl>
<dd>
<dd>request block, initialized with <code>usb_sg_init</code></dl>
<h2>Description</h2>
<p>This stops a request after it has been started by <code>usb_sg_wait</code>. It can also prevents one initialized by <code>usb_sg_init</code> from starting, so that call just frees resources allocated to the request.</p>
<h2>Copyright</h2>
