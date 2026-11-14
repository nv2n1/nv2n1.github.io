---
title: "usb_driver_release_interface(9)"
name: "usb_driver_release_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_driver_release_interface/"
description: "usb_driver_release_interface – unbind a driver from an interface"
---

<p>usb_driver_release_interface &#8211; unbind a driver from an interface</p>
<h2>Synopsis</h2>
<pre><code>void usb_driver_release_interface(struct usb_driver *driver, struct usb_interface *iface);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver to be unbound</dl>
<p> <i>iface</i></p>
<dl>
<dd>the interface from which it will be unbound</dl>
<h2>Description</h2>
<p>This can be used by drivers to release an interface without waiting for their <code>disconnect</code> methods to be called. In typical cases this also causes the driver <code>disconnect</code> method to be called. </p>
<p> This call is synchronous, and may not be used in an interrupt context. Callers must own the device lock, so driver <code>disconnect</code> entries don&#8217;t need extra locking, but other call contexts may need to explicitly claim that lock.</p>
<h2>Copyright</h2>
