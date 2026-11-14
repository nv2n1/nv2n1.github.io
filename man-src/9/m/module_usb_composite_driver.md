---
title: "module_usb_composite_driver(9)"
name: "module_usb_composite_driver"
section: "9"
letter: "m"
url: "/docs/linux/man/9-module_usb_composite_driver/"
description: "module_usb_composite_driver – Helper macro for registering a USB gadget composite driver"
---

<p>module_usb_composite_driver &#8211; Helper macro for registering a USB gadget composite driver</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>module_usb_composite_driver(</code><i>__usb_composite_driver</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>__usb_composite_driver</i></p>
<dl>
<dd>
<dd>usb_composite_driver struct</dl>
<h2>Description</h2>
<p>Helper macro for USB gadget composite drivers which do not do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it replaces <code>module_init</code> and <code>module_exit</code></p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
