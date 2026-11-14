---
title: "usb_composite_unregister(9)"
name: "usb_composite_unregister"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_composite_unregister/"
description: "usb_composite_unregister – unregister a composite driver"
---

<p>usb_composite_unregister &#8211; unregister a composite driver</p>
<h2>Synopsis</h2>
<pre><code>void usb_composite_unregister(struct usb_composite_driver *driver);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver to unregister</dl>
<h2>Description</h2>
<p>This function is used to unregister drivers using the composite driver framework.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
