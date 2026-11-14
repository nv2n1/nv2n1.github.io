---
title: "rio_inb_pwrite_handler(9)"
name: "rio_inb_pwrite_handler"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_inb_pwrite_handler/"
description: "rio_inb_pwrite_handler – inbound port-write message handler"
---

<p>rio_inb_pwrite_handler &#8211; inbound port-write message handler</p>
<h2>Synopsis</h2>
<pre><code>int rio_inb_pwrite_handler(struct rio_mport *mport, union rio_pw_msg *pw_msg);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>mport device associated with port-write</dl>
<p> <i>pw_msg</i></p>
<dl>
<dd>pointer to inbound port-write message</dl>
<h2>Description</h2>
<p>Processes an inbound port-write message. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
