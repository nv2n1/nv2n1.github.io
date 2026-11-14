---
title: "usb_register_driver(9)"
name: "usb_register_driver"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_register_driver/"
description: "usb_register_driver – register a USB interface driver"
---

<p>usb_register_driver &#8211; register a USB interface driver</p>
<h2>Synopsis</h2>
<pre><code>int usb_register_driver(struct usb_driver *new_driver, struct module *owner, const char *mod_name);</code></pre>
<h2>Arguments</h2>
<p><i>new_driver</i></p>
<dl>
<dd>
<dd>USB operations for the interface driver</dl>
<p> <i>owner</i></p>
<dl>
<dd>module owner of this driver.</dl>
<p> <i>mod_name</i></p>
<dl>
<dd>module name string</dl>
<h2>Description</h2>
<p>Registers a USB interface driver with the USB core. The list of unattached interfaces will be rescanned whenever a new driver is added, allowing the new driver to attach to any recognized interfaces.</p>
<h2>Return</h2>
<p>A negative error code on failure and 0 on success.</p>
<h2>Note</h2>
<p>if you want your driver to use the USB major number, you must call <code>usb_register_dev</code> to enable that functionality. This function no longer takes care of that.</p>
<h2>Copyright</h2>
