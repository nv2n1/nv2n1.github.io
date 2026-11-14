---
title: "usb_gadget_unregister_driver(9)"
name: "usb_gadget_unregister_driver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_gadget_unregister_driver/"
description: "usb_gadget_unregister_driver – unregister a gadget driver"
---

<p>usb_gadget_unregister_driver &#8211; unregister a gadget driver</p>
<h2>Synopsis</h2>
<pre><code>int usb_gadget_unregister_driver(struct usb_gadget_driver *driver);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver being unregistered</dl>
<h2>Context</h2>
<p>can sleep</p>
<h2>Description</h2>
<p>Call this in your gadget driver&#8217;s module cleanup function, to tell the underlying usb controller that your driver is going away. If the controller is connected to a USB host, it will first <code>disconnect</code>. The driver is also requested to <code>unbind</code> and clean up any device state, before this procedure finally returns. It&#8217;s expected that the <code>unbind</code> functions will in in exit sections, so may not be linked in some kernels.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
