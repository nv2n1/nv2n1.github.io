---
title: "usb_device(9)"
name: "usb_device"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_device/"
description: "USB_DEVICE – macro used to describe a specific usb device"
---

<p>USB_DEVICE &#8211; macro used to describe a specific usb device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>USB_DEVICE(</code><i>vend</i><code>, </code><i>prod</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>vend</i></p>
<dl>
<dd>
<dd>the 16 bit USB Vendor ID</dl>
<p> <i>prod</i></p>
<dl>
<dd>the 16 bit USB Product ID</dl>
<h2>Description</h2>
<p>This macro is used to create a struct usb_device_id that matches a specific device.</p>
<h2>Copyright</h2>
