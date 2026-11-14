---
title: "usb_function_activate(9)"
name: "usb_function_activate"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_function_activate/"
description: "usb_function_activate – allow function and gadget enumeration"
---

<p>usb_function_activate &#8211; allow function and gadget enumeration</p>
<h2>Synopsis</h2>
<pre><code>int usb_function_activate(struct usb_function *function);</code></pre>
<h2>Arguments</h2>
<p><i>function</i></p>
<dl>
<dd>
<dd>function on which <code>usb_function_activate</code> was called</dl>
<h2>Description</h2>
<p>Reverses effect of <code>usb_function_deactivate</code>. If no more functions are delaying their activation, the gadget driver will respond to host enumeration procedures. </p>
<p> Returns zero on success, else negative errno.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
