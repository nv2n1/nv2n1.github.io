---
title: "usb_interface_id(9)"
name: "usb_interface_id"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_interface_id/"
description: "usb_interface_id – allocate an unused interface ID"
---

<p>usb_interface_id &#8211; allocate an unused interface ID</p>
<h2>Synopsis</h2>
<pre><code>int usb_interface_id(struct usb_configuration *config, struct usb_function *function);</code></pre>
<h2>Arguments</h2>
<p><i>config</i></p>
<dl>
<dd>
<dd>configuration associated with the interface</dl>
<p> <i>function</i></p>
<dl>
<dd>function handling the interface</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p><code>usb_interface_id</code> is called from usb_function.<code>bind</code> callbacks to allocate new interface IDs. The function driver will then store that ID in interface, association, CDC union, and other descriptors. It will also handle any control requests targeted at that interface, particularly changing its altsetting via <code>set_alt</code>. There may also be class-specific or vendor-specific requests to handle. </p>
<p> All interface identifier should be allocated using this routine, to ensure that for example different functions don&#8217;t wrongly assign different meanings to the same identifier. Note that since interface identifiers are configuration-specific, functions used in more than one configuration (or more than once in a given configuration) need multiple versions of the relevant descriptors. </p>
<p> Returns the interface ID which was allocated; or -ENODEV if no more interface IDs can be allocated.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
