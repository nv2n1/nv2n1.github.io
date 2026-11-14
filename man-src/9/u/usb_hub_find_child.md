---
title: "usb_hub_find_child(9)"
name: "usb_hub_find_child"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_hub_find_child/"
description: "usb_hub_find_child – Get the pointer of child device attached to the port which is specified by port1."
---

<p>usb_hub_find_child &#8211; Get the pointer of child device attached to the port which is specified by <i>port1</i>.</p>
<h2>Synopsis</h2>
<pre><code>struct usb_device *usb_hub_find_child(struct usb_device *hdev, int port1);</code></pre>
<h2>Arguments</h2>
<p><i>hdev</i></p>
<dl>
<dd>
<dd>USB device belonging to the usb hub</dl>
<p> <i>port1</i></p>
<dl>
<dd>port num to indicate which port the child device is attached to.</dl>
<h2>Description</h2>
<p>USB drivers call this function to get hub&#8217;s child device pointer.</p>
<h2>Return</h2>
<p><code>NULL</code> if input param is invalid and child&#8217;s usb_device pointer if non-NULL.</p>
<h2>Copyright</h2>
