---
title: "usb_string_ids_n(9)"
name: "usb_string_ids_n"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_string_ids_n/"
description: "usb_string_ids_n – allocate unused string IDs in batch"
---

<p>usb_string_ids_n &#8211; allocate unused string IDs in batch</p>
<h2>Synopsis</h2>
<pre><code>int usb_string_ids_n(struct usb_composite_dev *c, unsigned n);</code></pre>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>the device whose string descriptor IDs are being allocated</dl>
<p> <i>n</i></p>
<dl>
<dd>number of string IDs to allocate</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p>Returns the first requested ID. This ID and next <i>n</i>-1 IDs are now valid IDs. At least provided that <i>n</i> is non-zero because if it is, returns last requested ID which is now very useful information. </p>
<p> <i>usb_string_ids_n</i>() is called from <code>bind</code> callbacks to allocate string IDs. Drivers for functions, configurations, or gadgets will then store that ID in the appropriate descriptors and string table. </p>
<p> All string identifier should be allocated using this, <i>usb_string_id</i>() or <i>usb_string_ids_n</i>() routine, to ensure that for example different functions don&#8217;t wrongly assign different meanings to the same identifier.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
