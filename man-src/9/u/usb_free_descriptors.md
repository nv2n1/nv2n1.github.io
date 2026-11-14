---
title: "usb_free_descriptors(9)"
name: "usb_free_descriptors"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_free_descriptors/"
description: "usb_free_descriptors – free descriptors returned by usb_copy_descriptors"
---

<p>usb_free_descriptors &#8211; free descriptors returned by <code>usb_copy_descriptors</code></p>
<h2>Synopsis</h2>
<pre><code>void usb_free_descriptors(struct usb_descriptor_header **v);</code></pre>
<h2>Arguments</h2>
<p><i>v</i></p>
<dl>
<dd>
<dd>vector of descriptors</dl>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
