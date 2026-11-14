---
title: "rio_request_inb_dbell(9)"
name: "rio_request_inb_dbell"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_inb_dbell/"
description: "rio_request_inb_dbell – request inbound doorbell message service"
---

<p>rio_request_inb_dbell &#8211; request inbound doorbell message service</p>
<h2>Synopsis</h2>
<pre><code>int rio_request_inb_dbell(struct rio_mport *mport, void *dev_id, u16 start, u16 end, void (*dinb)(struct rio_mport *mport, void *dev_id, u16 src, u16 dst, u16 info));</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port from which to allocate the doorbell resource</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>Device specific pointer to pass on event</dl>
<p> <i>start</i></p>
<dl>
<dd>Doorbell info range start</dl>
<p> <i>end</i></p>
<dl>
<dd>Doorbell info range end</dl>
<p> <i>dinb</i></p>
<dl>
<dd>Callback to execute when doorbell is received</dl>
<h2>Description</h2>
<p>Requests ownership of an inbound doorbell resource and binds a callback function to the resource. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
