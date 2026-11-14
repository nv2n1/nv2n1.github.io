---
title: "z8530_sync_open(9)"
name: "z8530_sync_open"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_sync_open/"
description: "z8530_sync_open – Open a Z8530 channel for PIO"
---

<p>z8530_sync_open &#8211; Open a Z8530 channel for PIO</p>
<h2>Synopsis</h2>
<pre><code>int z8530_sync_open(struct net_device *dev, struct z8530_channel *c);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>The network interface we are using</dl>
<p> <i>c</i></p>
<dl>
<dd>The Z8530 channel to open in synchronous PIO mode</dl>
<h2>Description</h2>
<p>Switch a Z8530 into synchronous mode without DMA assist. We raise the RTS/DTR and commence network operation.</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
