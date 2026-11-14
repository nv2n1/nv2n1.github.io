---
title: "usb_descriptor_fillbuf(9)"
name: "usb_descriptor_fillbuf"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_descriptor_fillbuf/"
description: "usb_descriptor_fillbuf – fill buffer with descriptors"
---

<p>usb_descriptor_fillbuf &#8211; fill buffer with descriptors</p>
<h2>Synopsis</h2>
<pre><code>int usb_descriptor_fillbuf(void *buf, unsigned buflen, const struct usb_descriptor_header **src);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>Buffer to be filled</dl>
<p> <i>buflen</i></p>
<dl>
<dd>Size of buf</dl>
<p> <i>src</i></p>
<dl>
<dd>Array of descriptor pointers, terminated by null pointer.</dl>
<h2>Description</h2>
<p>Copies descriptors into the buffer, returning the length or a negative error code if they can&#8217;t all be copied. Useful when assembling descriptors for an associated set of interfaces used as part of configuring a composite device; or in other cases where sets of descriptors need to be marshaled.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
