---
title: "hcd_buffer_destroy(9)"
name: "hcd_buffer_destroy"
section: "9"
letter: "h"
url: "/docs/linux/man/9-hcd_buffer_destroy/"
description: "hcd_buffer_destroy – deallocate buffer pools"
---

<p>hcd_buffer_destroy &#8211; deallocate buffer pools</p>
<h2>Synopsis</h2>
<pre><code>void hcd_buffer_destroy(struct usb_hcd *hcd);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>the bus whose buffer pools are to be destroyed</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>This frees the buffer pools created by <code>hcd_buffer_create</code>.</p>
<h2>Copyright</h2>
