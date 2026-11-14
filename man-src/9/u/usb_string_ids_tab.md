---
title: "usb_string_ids_tab(9)"
name: "usb_string_ids_tab"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_string_ids_tab/"
description: "usb_string_ids_tab – allocate unused string IDs in batch"
---

<p>usb_string_ids_tab &#8211; allocate unused string IDs in batch</p>
<h2>Synopsis</h2>
<pre><code>int usb_string_ids_tab(struct usb_composite_dev *cdev, struct usb_string *str);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the device whose string descriptor IDs are being allocated</dl>
<p> <i>str</i></p>
<dl>
<dd>an array of usb_string objects to assign numbers to</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p><i>usb_string_ids</i>() is called from <code>bind</code> callbacks to allocate string IDs. Drivers for functions, configurations, or gadgets will then copy IDs from the string table to the appropriate descriptors and string table for other languages. </p>
<p> All string identifier should be allocated using this, <i>usb_string_id</i>() or <i>usb_string_ids_n</i>() routine, to ensure that for example different functions don&#8217;t wrongly assign different meanings to the same identifier.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
