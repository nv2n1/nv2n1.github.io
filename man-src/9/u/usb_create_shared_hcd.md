---
title: "usb_create_shared_hcd(9)"
name: "usb_create_shared_hcd"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_create_shared_hcd/"
description: "usb_create_shared_hcd – create and initialize an HCD structure"
---

<p>usb_create_shared_hcd &#8211; create and initialize an HCD structure</p>
<h2>Synopsis</h2>
<pre><code>struct usb_hcd *usb_create_shared_hcd(const struct hc_driver *driver, struct device *dev, const char *bus_name, struct usb_hcd *primary_hcd);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>HC driver that will use this hcd</dl>
<p> <i>dev</i></p>
<dl>
<dd>device for this HC, stored in hcd-&gt;self.controller</dl>
<p> <i>bus_name</i></p>
<dl>
<dd>value to store in hcd-&gt;self.bus_name</dl>
<p> <i>primary_hcd</i></p>
<dl>
<dd>a pointer to the usb_hcd structure that is sharing the PCI device. Only allocate certain resources for the primary HCD</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Allocate a struct usb_hcd, with extra space at the end for the HC driver&#8217;s private data. Initialize the generic members of the hcd structure.</p>
<h2>Return</h2>
<p>On success, a pointer to the created and initialized HCD structure. On failure (e.g. if memory is unavailable), <code>NULL</code>.</p>
<h2>Copyright</h2>
