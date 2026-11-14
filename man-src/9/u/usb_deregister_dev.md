---
title: "usb_deregister_dev(9)"
name: "usb_deregister_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_deregister_dev/"
description: "usb_deregister_dev – deregister a USB device’s dynamic minor."
---

<p>usb_deregister_dev &#8211; deregister a USB device&#8217;s dynamic minor.</p>
<h2>Synopsis</h2>
<pre><code>void usb_deregister_dev(struct usb_interface *intf, struct usb_class_driver *class_driver);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>pointer to the usb_interface that is being deregistered</dl>
<p> <i>class_driver</i></p>
<dl>
<dd>pointer to the usb_class_driver for this device</dl>
<h2>Description</h2>
<p>Used in conjunction with <code>usb_register_dev</code>. This function is called when the USB driver is finished with the minor numbers gotten from a call to <code>usb_register_dev</code> (usually when the device is disconnected from the system.) </p>
<p> This function also removes the usb class device from the sysfs tree. </p>
<p> This should be called by all drivers that use the USB major number.</p>
<h2>Copyright</h2>
