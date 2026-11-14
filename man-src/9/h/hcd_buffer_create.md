---
title: "hcd_buffer_create(9)"
name: "hcd_buffer_create"
section: "9"
letter: "h"
url: "/docs/linux/man/9-hcd_buffer_create/"
description: "hcd_buffer_create – initialize buffer pools"
---

<p>hcd_buffer_create &#8211; initialize buffer pools</p>
<h2>Synopsis</h2>
<pre><code>int hcd_buffer_create(struct usb_hcd *hcd);</code></pre>
<h2>Arguments</h2>
<p><i>hcd</i></p>
<dl>
<dd>
<dd>the bus whose buffer pools are to be initialized</dl>
<h2>Context</h2>
<p>!<code>in_interrupt</code></p>
<h2>Description</h2>
<p>Call this as part of initializing a host controller that uses the dma memory allocators. It initializes some pools of dma-coherent memory that will be shared by all drivers using that controller. </p>
<p> Call <code>hcd_buffer_destroy</code> to clean up after using those pools.</p>
<h2>Return</h2>
<p>0 if successful. A negative errno value otherwise.</p>
<h2>Copyright</h2>
