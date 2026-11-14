---
title: "gadget_is_otg(9)"
name: "gadget_is_otg"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gadget_is_otg/"
description: "gadget_is_otg – return true iff the hardware is OTG-ready"
---

<p>gadget_is_otg &#8211; return true iff the hardware is OTG-ready</p>
<h2>Synopsis</h2>
<pre><code>int gadget_is_otg(struct usb_gadget *g);</code></pre>
<h2>Arguments</h2>
<p><i>g</i></p>
<dl>
<dd>
<dd>controller that might have a Mini-AB connector</dl>
<h2>Description</h2>
<p>This is a runtime test, since kernels with a USB-OTG stack sometimes run on boards which only have a Mini-B (or Mini-A) connector.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
