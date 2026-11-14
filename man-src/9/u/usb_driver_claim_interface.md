---
title: "usb_driver_claim_interface(9)"
name: "usb_driver_claim_interface"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_driver_claim_interface/"
description: "usb_driver_claim_interface – bind a driver to an interface"
---

<p>usb_driver_claim_interface &#8211; bind a driver to an interface</p>
<h2>Synopsis</h2>
<pre><code>int usb_driver_claim_interface(struct usb_driver *driver, struct usb_interface *iface, void *priv);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver to be bound</dl>
<p> <i>iface</i></p>
<dl>
<dd>the interface to which it will be bound; must be in the usb device&#8217;s active configuration</dl>
<p> <i>priv</i></p>
<dl>
<dd>driver data associated with that interface</dl>
<h2>Description</h2>
<p>This is used by usb device drivers that need to claim more than one interface on a device when probing (audio and acm are current examples). No device driver should directly modify internal usb_interface or usb_device structure members. </p>
<p> Few drivers should need to use this routine, since the most natural way to bind to an interface is to return the private data from the driver&#8217;s <code>probe</code> method. </p>
<p> Callers must own the device lock, so driver <code>probe</code> entries don&#8217;t need extra locking, but other call contexts may need to explicitly claim that lock.</p>
<h2>Return</h2>
<p>0 on success.</p>
<h2>Copyright</h2>
