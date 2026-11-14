---
title: "usb_get_dev(9)"
name: "usb_get_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_dev/"
description: "usb_get_dev – increments the reference count of the usb device structure"
---

<p>usb_get_dev &#8211; increments the reference count of the usb device structure</p>
<h2>Synopsis</h2>
<pre><code>struct usb_device *usb_get_dev(struct usb_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device being referenced</dl>
<h2>Description</h2>
<p>Each live reference to a device should be refcounted. </p>
<p> Drivers for USB interfaces should normally record such references in their <code>probe</code> methods, when they bind to an interface, and release them by calling <code>usb_put_dev</code>, in their <code>disconnect</code> methods.</p>
<h2>Return</h2>
<p>A pointer to the device with the incremented reference counter.</p>
<h2>Copyright</h2>
