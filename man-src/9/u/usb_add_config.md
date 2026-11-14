---
title: "usb_add_config(9)"
name: "usb_add_config"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_add_config/"
description: "usb_add_config – add a configuration to a device."
---

<p>usb_add_config &#8211; add a configuration to a device.</p>
<h2>Synopsis</h2>
<pre><code>int usb_add_config(struct usb_composite_dev *cdev, struct usb_configuration *config, int (*bind)(struct usb_configuration *));</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>wraps the USB gadget</dl>
<p> <i>config</i></p>
<dl>
<dd>the configuration, with bConfigurationValue assigned</dl>
<p> <i>bind</i></p>
<dl>
<dd>the configuration&#8217;s bind function</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p>One of the main tasks of a composite <i>bind</i>() routine is to add each of the configurations it supports, using this routine. </p>
<p> This function returns the value of the configuration&#8217;s <i>bind</i>(), which is zero for success else a negative errno value. Binding configurations assigns global resources including string IDs, and per-configuration resources such as interface IDs and endpoints.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
