---
title: "usb_register_dev(9)"
name: "usb_register_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_register_dev/"
description: "usb_register_dev – register a USB device, and ask for a minor number"
---

<p>usb_register_dev &#8211; register a USB device, and ask for a minor number</p>
<h2>Synopsis</h2>
<pre><code>int usb_register_dev(struct usb_interface *intf, struct usb_class_driver *class_driver);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>pointer to the usb_interface that is being registered</dl>
<p> <i>class_driver</i></p>
<dl>
<dd>pointer to the usb_class_driver for this device</dl>
<h2>Description</h2>
<p>This should be called by all USB drivers that use the USB major number. If CONFIG_USB_DYNAMIC_MINORS is enabled, the minor number will be dynamically allocated out of the list of available ones. If it is not enabled, the minor number will be based on the next available free minor, starting at the class_driver-&gt;minor_base. </p>
<p> This function also creates a usb class device in the sysfs tree. </p>
<p> <code>usb_deregister_dev</code> must be called when the driver is done with the minor numbers given out by this function.</p>
<h2>Return</h2>
<p>-EINVAL if something bad happens with trying to register a device, and 0 on success.</p>
<h2>Copyright</h2>
