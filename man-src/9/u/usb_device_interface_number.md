---
title: "usb_device_interface_number(9)"
name: "usb_device_interface_number"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_device_interface_number/"
description: "USB_DEVICE_INTERFACE_NUMBER – describe a usb device with a specific interface number"
---

<p>USB_DEVICE_INTERFACE_NUMBER &#8211; describe a usb device with a specific interface number</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>USB_DEVICE_INTERFACE_NUMBER(</code><i>vend</i><code>, </code><i>prod</i><code>, </code><i>num</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>vend</i></p>
<dl>
<dd>
<dd>the 16 bit USB Vendor ID</dl>
<p> <i>prod</i></p>
<dl>
<dd>the 16 bit USB Product ID</dl>
<p> <i>num</i></p>
<dl>
<dd>bInterfaceNumber value</dl>
<h2>Description</h2>
<p>This macro is used to create a struct usb_device_id that matches a specific interface number of devices.</p>
<h2>Copyright</h2>
