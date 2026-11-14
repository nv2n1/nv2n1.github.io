---
title: "usb_find_interface(9)"
name: "usb_find_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_find_interface/"
---

usb_find_interface - find usb_interface pointer for driver and device

<h2>Synopsis</h2>

<pre><code>struct usb_interface *usb_find_interface(struct usb_driver *drv, int minor);</code></pre>

<h2>Arguments</h2>

<i>drv</i>
<dl><dd><dd>the driver whose current configuration is considered</dl>
 

 <i>minor</i>
<dl><dd>the minor number of the desired device</dl>

<h2>Description</h2>

This walks the bus device list and returns a pointer to the interface with the matching minor and driver. Note, this only works for devices that share the USB major number.

<h2>Return</h2>

A pointer to the interface with the matching major and <i>minor</i>.

<h2>Copyright</h2>


