---
title: "usb_alloc_dev(9)"
name: "usb_alloc_dev"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_alloc_dev/"
description: "usb_alloc_dev – usb device constructor (usbcore-internal)"
---

<p>usb_alloc_dev &#8211; usb device constructor (usbcore-internal)</p>
<h2>Synopsis</h2>
<pre><code>struct usb_device *usb_alloc_dev(struct usb_device *parent, struct usb_bus *bus, unsigned port1);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>hub to which device is connected; null to allocate a root hub</dl>
<p> <i>bus</i></p>
<dl>
<dd>bus used to access the device</dl>
<p> <i>port1</i></p>
<dl>
<dd>one-based index of port; ignored for root hubs</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Only hub drivers (including virtual root hub drivers for host controllers) should ever call this. </p>
<p> This call may not be used in a non-sleeping context.</p>
<h2>Return</h2>
<p>On success, a pointer to the allocated usb device. <code>NULL</code> on failure.</p>
<h2>Copyright</h2>
