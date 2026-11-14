---
title: "rio_release_outb_mbox(9)"
name: "rio_release_outb_mbox"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_release_outb_mbox/"
description: "rio_release_outb_mbox – release outbound mailbox message service"
---

<p>rio_release_outb_mbox &#8211; release outbound mailbox message service</p>
<h2>Synopsis</h2>
<pre><code>int rio_release_outb_mbox(struct rio_mport *mport, int mbox);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>RIO master port from which to release the mailbox resource</dl>
<p> <i>mbox</i></p>
<dl>
<dd>Mailbox number to release</dl>
<h2>Description</h2>
<p>Releases ownership of an inbound mailbox resource. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
