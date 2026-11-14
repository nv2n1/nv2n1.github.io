---
title: "usb_bus_start_enum(9)"
name: "usb_bus_start_enum"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_bus_start_enum/"
description: "usb_bus_start_enum – start immediate enumeration (for OTG)"
---

<p>usb_bus_start_enum &#8211; start immediate enumeration (for OTG)</p>
<h2>Synopsis</h2>
<pre><code>int usb_bus_start_enum(struct usb_bus *bus, unsigned port_num);</code></pre>
<h2>Arguments</h2>
<p><i>bus</i></p>
<dl>
<dd>
<dd>the bus (must use hcd framework)</dl>
<p> <i>port_num</i></p>
<dl>
<dd>1-based number of port; usually bus-&gt;otg_port</dl>
<h2>Context</h2>
<p><code>in_interrupt</code></p>
<h2>Description</h2>
<p>Starts enumeration, with an immediate reset followed later by hub_wq identifying and possibly configuring the device. This is needed by OTG controller drivers, where it helps meet HNP protocol timing requirements for starting a port reset.</p>
<h2>Return</h2>
<p>0 if successful.</p>
<h2>Copyright</h2>
