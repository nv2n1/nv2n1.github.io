---
title: "usb_function_deactivate(9)"
name: "usb_function_deactivate"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_function_deactivate/"
description: "usb_function_deactivate – prevent function and gadget enumeration"
---

<p>usb_function_deactivate &#8211; prevent function and gadget enumeration</p>
<h2>Synopsis</h2>
<pre><code>int usb_function_deactivate(struct usb_function *function);</code></pre>
<h2>Arguments</h2>
<p><i>function</i></p>
<dl>
<dd>
<dd>the function that isn&#8217;t yet ready to respond</dl>
<h2>Description</h2>
<p>Blocks response of the gadget driver to host enumeration by preventing the data line pullup from being activated. This is normally called during <i>bind</i>() processing to change from the initial &#8220;ready to respond&#8221; state, or when a required resource becomes available. </p>
<p> For example, drivers that serve as a passthrough to a userspace daemon can block enumeration unless that daemon (such as an OBEX, MTP, or print server) is ready to handle host requests. </p>
<p> Not all systems support software control of their USB peripheral data pullups. </p>
<p> Returns zero on success, else negative errno.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
