---
title: "usb_register_device_driver(9)"
name: "usb_register_device_driver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_register_device_driver/"
---

usb_register_device_driver - register a USB device (not interface) driver

<h2>Synopsis</h2>

<pre><code>int usb_register_device_driver(struct usb_device_driver *new_udriver, struct module *owner);</code></pre>

<h2>Arguments</h2>

<i>new_udriver</i>
<dl><dd><dd>USB operations for the device driver</dl>
 

 <i>owner</i>
<dl><dd>module owner of this driver.</dl>

<h2>Description</h2>

Registers a USB device driver with the USB core. The list of unattached devices will be rescanned whenever a new driver is added, allowing the new driver to attach to any recognized devices.

<h2>Return</h2>

A negative error code on failure and 0 on success.

<h2>Copyright</h2>


