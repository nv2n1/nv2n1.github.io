---
title: "rio_add_inb_buffer(9)"
name: "rio_add_inb_buffer"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_add_inb_buffer/"
description: "rio_add_inb_buffer – Add buffer to an inbound mailbox queue"
---

<p>rio_add_inb_buffer &#8211; Add buffer to an inbound mailbox queue</p>
<h2>Synopsis</h2>
<pre><code>int rio_add_inb_buffer(struct rio_mport *mport, int mbox, void *buffer);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port containing the inbound mailbox</dl>
<p> <i>mbox</i></p>
<dl>
<dd>The inbound mailbox number</dl>
<p> <i>buffer</i></p>
<dl>
<dd>Pointer to the message buffer</dl>
<h2>Description</h2>
<p>Adds a buffer to an inbound mailbox queue for reception. Returns 0 on success.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
