---
title: "rio_request_inb_mbox(9)"
name: "rio_request_inb_mbox"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_inb_mbox/"
description: "rio_request_inb_mbox – request inbound mailbox service"
---

<p>rio_request_inb_mbox &#8211; request inbound mailbox service</p>
<h2>Synopsis</h2>
<pre><code>int rio_request_inb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries, void (*minb)(struct rio_mport *mport, void *dev_id, int mbox, int slot));</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port from which to allocate the mailbox resource</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>Device specific pointer to pass on event</dl>
<p> <i>mbox</i></p>
<dl>
<dd>Mailbox number to claim</dl>
<p> <i>entries</i></p>
<dl>
<dd>Number of entries in inbound mailbox queue</dl>
<p> <i>minb</i></p>
<dl>
<dd>Callback to execute when inbound message is received</dl>
<h2>Description</h2>
<p>Requests ownership of an inbound mailbox resource and binds a callback function to the resource. Returns <code>0</code> on success.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
