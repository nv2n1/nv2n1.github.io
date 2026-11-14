---
title: "rio_add_outb_message(9)"
name: "rio_add_outb_message"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_add_outb_message/"
description: "rio_add_outb_message – Add RIO message to an outbound mailbox queue"
---

<p>rio_add_outb_message &#8211; Add RIO message to an outbound mailbox queue</p>
<h2>Synopsis</h2>
<pre><code>int rio_add_outb_message(struct rio_mport *mport, struct rio_dev *rdev, int mbox, void *buffer, size_t len);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port containing the outbound queue</dl>
<p> <i>rdev</i></p>
<dl>
<dd>RIO device the message is be sent to</dl>
<p> <i>mbox</i></p>
<dl>
<dd>The outbound mailbox queue</dl>
<p> <i>buffer</i></p>
<dl>
<dd>Pointer to the message buffer</dl>
<p> <i>len</i></p>
<dl>
<dd>Length of the message buffer</dl>
<h2>Description</h2>
<p>Adds a RIO message buffer to an outbound mailbox queue for transmission. Returns 0 on success.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
