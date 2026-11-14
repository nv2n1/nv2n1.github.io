---
title: "usb_copy_descriptors(9)"
name: "usb_copy_descriptors"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_copy_descriptors/"
description: "usb_copy_descriptors – copy a vector of USB descriptors"
---

<p>usb_copy_descriptors &#8211; copy a vector of USB descriptors</p>
<h2>Synopsis</h2>
<pre><code>struct usb_descriptor_header **usb_copy_descriptors(struct usb_descriptor_header **src);</code></pre>
<h2>Arguments</h2>
<p><i>src</i></p>
<dl>
<dd>
<dd>null-terminated vector to copy</dl>
<h2>Context</h2>
<p>initialization code, which may sleep</p>
<h2>Description</h2>
<p>This makes a copy of a vector of USB descriptors. Its primary use is to support usb_function objects which can have multiple copies, each needing different descriptors. Functions may have static tables of descriptors, which are used as templates and customized with identifiers (for interfaces, strings, endpoints, and more) as needed by a given function instance.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
