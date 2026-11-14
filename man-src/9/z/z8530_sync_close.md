---
title: "z8530_sync_close(9)"
name: "z8530_sync_close"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_sync_close/"
description: "z8530_sync_close – Close a PIO Z8530 channel"
---

<p>z8530_sync_close &#8211; Close a PIO Z8530 channel</p>
<h2>Synopsis</h2>
<pre><code>int z8530_sync_close(struct net_device *dev, struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Network device to close</dl>
<p> <i>c</i></p>
<dl>
<dd>Z8530 channel to disassociate and move to idle</dl>
<h2>Description</h2>
<p>Close down a Z8530 interface and switch its interrupt handlers to discard future events.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
