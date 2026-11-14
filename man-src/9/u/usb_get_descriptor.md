---
title: "usb_get_descriptor(9)"
name: "usb_get_descriptor"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_get_descriptor/"
description: "usb_get_descriptor – issues a generic GET_DESCRIPTOR request"
---

<p>usb_get_descriptor &#8211; issues a generic GET_DESCRIPTOR request</p>
<h2>Synopsis</h2>
<pre><code>int usb_get_descriptor(struct usb_device *dev, unsigned char type, unsigned char index, void *buf, int size);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the device whose descriptor is being retrieved</dl>
<p> <i>type</i></p>
<dl>
<dd>the descriptor type (USB_DT_*)</dl>
<p> <i>index</i></p>
<dl>
<dd>the number of the descriptor</dl>
<p> <i>buf</i></p>
<dl>
<dd>where to put the descriptor</dl>
<p> <i>size</i></p>
<dl>
<dd>how big is &#8220;buf&#8221;?</dl>
<h2>Context</h2>
<p>!in_interrupt ()</p>
<h2>Description</h2>
<p>Gets a USB descriptor. Convenience functions exist to simplify getting some types of descriptors. Use <code>usb_get_string</code> or <code>usb_string</code> for USB_DT_STRING. Device (USB_DT_DEVICE) and configuration descriptors (USB_DT_CONFIG) are part of the device structure. In addition to a number of USB-standard descriptors, some devices also use class-specific or vendor-specific descriptors. </p>
<p> This call is synchronous, and may not be used in an interrupt context.</p>
<h2>Return</h2>
<p>The number of bytes received on success, or else the status code returned by the underlying <code>usb_control_msg</code> call.</p>
<h2>Copyright</h2>
