---
title: "usb_deregister_device_driver(9)"
name: "usb_deregister_device_driver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_deregister_device_driver/"
---

usb_deregister_device_driver - unregister a USB device (not interface) driver

<h2>Synopsis</h2>

<pre><code>void usb_deregister_device_driver(struct usb_device_driver *udriver);</code></pre>

<h2>Arguments</h2>

<i>udriver</i>
<dl><dd><dd>USB operations of the device driver to unregister</dl>

<h2>Context</h2>

must be able to sleep

<h2>Description</h2>

Unlinks the specified driver from the internal USB driver list.

<h2>Copyright</h2>


