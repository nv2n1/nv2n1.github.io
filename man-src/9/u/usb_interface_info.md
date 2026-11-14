---
title: "usb_interface_info(9)"
name: "usb_interface_info"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_interface_info/"
description: "USB_INTERFACE_INFO – macro used to describe a class of usb interfaces"
---

<p>USB_INTERFACE_INFO &#8211; macro used to describe a class of usb interfaces</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>USB_INTERFACE_INFO(</code><i>cl</i><code>, </code><i>sc</i><code>, </code><i>pr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>cl</i></p>
<dl>
<dd>
<dd>bInterfaceClass value</dl>
<p> <i>sc</i></p>
<dl>
<dd>bInterfaceSubClass value</dl>
<p> <i>pr</i></p>
<dl>
<dd>bInterfaceProtocol value</dl>
<h2>Description</h2>
<p>This macro is used to create a struct usb_device_id that matches a specific class of interfaces.</p>
<h2>Copyright</h2>
