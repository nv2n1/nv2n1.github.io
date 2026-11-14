---
title: "usb_device_and_interface_info(9)"
name: "usb_device_and_interface_info"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_device_and_interface_info/"
description: "USB_DEVICE_AND_INTERFACE_INFO – describe a specific usb device with a class of usb interfaces"
---

<p>USB_DEVICE_AND_INTERFACE_INFO &#8211; describe a specific usb device with a class of usb interfaces</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>USB_DEVICE_AND_INTERFACE_INFO(</code><i>vend</i><code>, </code><i>prod</i><code>, </code><i>cl</i><code>, </code><i>sc</i><code>, </code><i>pr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>vend</i></p>
<dl>
<dd>
<dd>the 16 bit USB Vendor ID</dl>
<p> <i>prod</i></p>
<dl>
<dd>the 16 bit USB Product ID</dl>
<p> <i>cl</i></p>
<dl>
<dd>bInterfaceClass value</dl>
<p> <i>sc</i></p>
<dl>
<dd>bInterfaceSubClass value</dl>
<p> <i>pr</i></p>
<dl>
<dd>bInterfaceProtocol value</dl>
<h2>Description</h2>
<p>This macro is used to create a struct usb_device_id that matches a specific device with a specific class of interfaces. </p>
<p> This is especially useful when explicitly matching devices that have vendor specific bDeviceClass values, but standards-compliant interfaces.</p>
<h2>Copyright</h2>
