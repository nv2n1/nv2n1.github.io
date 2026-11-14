---
title: "usb_get_intf(9)"
name: "usb_get_intf"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_intf/"
description: "usb_get_intf – increments the reference count of the usb interface structure"
---

<p>usb_get_intf &#8211; increments the reference count of the usb interface structure</p>
<h2>Synopsis</h2>
<pre><code>struct usb_interface *usb_get_intf(struct usb_interface *intf);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the interface being referenced</dl>
<h2>Description</h2>
<p>Each live reference to a interface must be refcounted. </p>
<p> Drivers for USB interfaces should normally record such references in their <code>probe</code> methods, when they bind to an interface, and release them by calling <code>usb_put_intf</code>, in their <code>disconnect</code> methods.</p>
<h2>Return</h2>
<p>A pointer to the interface with the incremented reference counter.</p>
<h2>Copyright</h2>
