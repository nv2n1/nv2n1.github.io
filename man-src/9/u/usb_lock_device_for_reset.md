---
title: "usb_lock_device_for_reset(9)"
name: "usb_lock_device_for_reset"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_lock_device_for_reset/"
description: "usb_lock_device_for_reset – cautiously acquire the lock for a usb device structure"
---

<p>usb_lock_device_for_reset &#8211; cautiously acquire the lock for a usb device structure</p>
<h2>Synopsis</h2>
<pre><code>int usb_lock_device_for_reset(struct usb_device *udev, const struct usb_interface *iface);</code></pre>
<h2>Arguments</h2>
<p><i>udev</i></p>
<dl>
<dd>
<dd>device that&#8217;s being locked</dl>
<p> <i>iface</i></p>
<dl>
<dd>interface bound to the driver making the request (optional)</dl>
<h2>Description</h2>
<p>Attempts to acquire the device lock, but fails if the device is NOTATTACHED or SUSPENDED, or if iface is specified and the interface is neither BINDING nor BOUND. Rather than sleeping to wait for the lock, the routine polls repeatedly. This is to prevent deadlock with disconnect; in some drivers (such as usb-storage) the <code>disconnect</code> or <code>suspend</code> method will block waiting for a device reset to complete.</p>
<h2>Return</h2>
<p>A negative error code for failure, otherwise 0.</p>
<h2>Copyright</h2>
