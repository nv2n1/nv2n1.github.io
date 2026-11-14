---
title: "usb_deregister(9)"
name: "usb_deregister"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_deregister/"
description: "usb_deregister – unregister a USB interface driver"
---

<p>usb_deregister &#8211; unregister a USB interface driver</p>
<h2>Synopsis</h2>
<pre><code>void usb_deregister(struct usb_driver *driver);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>USB operations of the interface driver to unregister</dl>
<h2>Context</h2>
<p>must be able to sleep</p>
<h2>Description</h2>
<p>Unlinks the specified driver from the internal USB driver list.</p>
<h2>Note</h2>
<p>If you called <code>usb_register_dev</code>, you still need to call <code>usb_deregister_dev</code> to clean up your driver&#8217;s allocated minor numbers, this * call will no longer do it for you.</p>
<h2>Copyright</h2>
