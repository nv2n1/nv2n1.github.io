---
title: "usb_composite_setup_continue(9)"
name: "usb_composite_setup_continue"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_composite_setup_continue/"
description: "usb_composite_setup_continue – Continue with the control transfer"
---

<p>usb_composite_setup_continue &#8211; Continue with the control transfer</p>
<h2>Synopsis</h2>
<pre><code>void usb_composite_setup_continue(struct usb_composite_dev *cdev);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the composite device who&#8217;s control transfer was kept waiting</dl>
<h2>Description</h2>
<p>This function must be called by the USB function driver to continue with the control transfer&#8217;s data/status stage in case it had requested to delay the data/status stages. A USB function&#8217;s setup handler (e.g. <code>set_alt</code>) can request the composite framework to delay the setup request&#8217;s data/status stages by returning USB_GADGET_DELAYED_STATUS.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
