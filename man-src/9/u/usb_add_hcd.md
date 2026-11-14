---
title: "usb_add_hcd(9)"
name: "usb_add_hcd"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_add_hcd/"
description: "usb_add_hcd – finish generic HCD structure initialization and register"
---

<p>usb_add_hcd &#8211; finish generic HCD structure initialization and register</p>
<h2>Synopsis</h2>
<pre><code>int usb_add_hcd(struct usb_hcd *hcd, unsigned int irqnum, unsigned long irqflags);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>the usb_hcd structure to initialize</dl>
<p> <i>irqnum</i></p>
<dl>
<dd>Interrupt line to allocate</dl>
<p> <i>irqflags</i></p>
<dl>
<dd>Interrupt type flags</dl>
<h2>Description</h2>
<p>Finish the remaining parts of generic HCD initialization: allocate the buffers of consistent memory, register the bus, request the IRQ line, and call the driver&#8217;s <code>reset</code> and <code>start</code> routines.</p>
<h2>Copyright</h2>
