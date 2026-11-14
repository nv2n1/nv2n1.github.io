---
title: "usb_gadget_probe_driver(9)"
name: "usb_gadget_probe_driver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_gadget_probe_driver/"
description: "usb_gadget_probe_driver – probe a gadget driver"
---

<p>usb_gadget_probe_driver &#8211; probe a gadget driver</p>
<h2>Synopsis</h2>
<pre><code>int usb_gadget_probe_driver(struct usb_gadget_driver *driver);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver being registered</dl>
<h2>Context</h2>
<p>can sleep</p>
<h2>Description</h2>
<p>Call this in your gadget driver&#8217;s module initialization function, to tell the underlying usb controller driver about your driver. The <i>bind</i>() function will be called to bind it to a gadget before this registration call returns. It&#8217;s expected that the <i>bind</i>() function will be in init sections.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
