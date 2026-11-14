---
title: "usb_interface_claimed(9)"
name: "usb_interface_claimed"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_interface_claimed/"
description: "usb_interface_claimed – returns true iff an interface is claimed"
---

<p>usb_interface_claimed &#8211; returns true iff an interface is claimed</p>
<h2>Synopsis</h2>
<pre><code>int usb_interface_claimed(struct usb_interface *iface);</code></pre>
<h2>Arguments</h2>
<p><i>iface</i></p>
<dl>
<dd>
<dd>the interface being checked</dl>
<h2>Return</h2>
<p><code>true</code> (nonzero) iff the interface is claimed, else <code>false</code> (zero).</p>
<h2>Note</h2>
<p>Callers must own the driver model&#8217;s usb bus readlock. So driver <code>probe</code> entries don&#8217;t need extra locking, but other call contexts may need to explicitly claim that lock.</p>
<h2>Copyright</h2>
