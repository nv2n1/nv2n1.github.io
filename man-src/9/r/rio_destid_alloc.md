---
title: "rio_destid_alloc(9)"
name: "rio_destid_alloc"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_destid_alloc/"
description: "rio_destid_alloc – Allocate next available destID for given network"
---

<p>rio_destid_alloc &#8211; Allocate next available destID for given network</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 rio_destid_alloc(struct rio_net&nbsp;<wbr>*&nbsp;<wbr></code><i>net</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network</dl>
<h2>Description</h2>
<p>Returns next available device destination ID for the specified RIO network. Marks allocated ID as one in use. Returns RIO_INVALID_DESTID if new destID is not available.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
