---
title: "usb_composite_probe(9)"
name: "usb_composite_probe"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_composite_probe/"
description: "usb_composite_probe – register a composite driver"
---

<p>usb_composite_probe &#8211; register a composite driver</p>
<h2>Synopsis</h2>
<pre><code>int usb_composite_probe(struct usb_composite_driver *driver);</code></pre>
<h2>Arguments</h2>
<p><i>driver</i></p>
<dl>
<dd>
<dd>the driver to register</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p>This function is used to register drivers using the composite driver framework. The return value is zero, or a negative errno value. Those values normally come from the driver&#8217;s <i>bind</i> method, which does all the work of setting up the driver to match the hardware. </p>
<p> On successful return, the gadget is ready to respond to requests from the host, unless one of its components invokes <code>usb_gadget_disconnect</code> while it was binding. That would usually be done in order to wait for some userspace participation.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
