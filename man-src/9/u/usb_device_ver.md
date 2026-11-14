---
title: "usb_device_ver(9)"
name: "usb_device_ver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_device_ver/"
description: "USB_DEVICE_VER – describe a specific usb device with a version range"
---

<p>USB_DEVICE_VER &#8211; describe a specific usb device with a version range</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>USB_DEVICE_VER(</code><i>vend</i><code>, </code><i>prod</i><code>, </code><i>lo</i><code>, </code><i>hi</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>vend</i></p>
<dl>
<dd>
<dd>the 16 bit USB Vendor ID</dl>
<p> <i>prod</i></p>
<dl>
<dd>the 16 bit USB Product ID</dl>
<p> <i>lo</i></p>
<dl>
<dd>the bcdDevice_lo value</dl>
<p> <i>hi</i></p>
<dl>
<dd>the bcdDevice_hi value</dl>
<h2>Description</h2>
<p>This macro is used to create a struct usb_device_id that matches a specific device, with a version range.</p>
<h2>Copyright</h2>
