---
title: "rio_get_inb_message(9)"
name: "rio_get_inb_message"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_inb_message/"
description: "rio_get_inb_message – Get A RIO message from an inbound mailbox queue"
---

<p>rio_get_inb_message &#8211; Get A RIO message from an inbound mailbox queue</p>
<h2>Synopsis</h2>
<pre><code>void *rio_get_inb_message(struct rio_mport *mport, int mbox);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port containing the inbound mailbox</dl>
<p> <i>mbox</i></p>
<dl>
<dd>The inbound mailbox number</dl>
<h2>Description</h2>
<p>Get a RIO message from an inbound mailbox queue. Returns 0 on success.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
