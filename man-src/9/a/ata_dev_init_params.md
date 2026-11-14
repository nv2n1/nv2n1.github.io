---
title: "ata_dev_init_params(9)"
name: "ata_dev_init_params"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dev_init_params/"
description: "ata_dev_init_params – Issue INIT DEV PARAMS command"
---

<p>ata_dev_init_params &#8211; Issue INIT DEV PARAMS command</p>
<h2>Synopsis</h2>
<pre><code>unsigned int ata_dev_init_params(struct ata_device *dev, u16 heads, u16 sectors);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to which command will be sent</dl>
<p> <i>heads</i></p>
<dl>
<dd>Number of heads (taskfile parameter)</dl>
<p> <i>sectors</i></p>
<dl>
<dd>Number of sectors (taskfile parameter)</dl>
<h2>Description</h2>
<p>LOCKING: Kernel thread context (may sleep)</p>
<h2>Return</h2>
<p>0 on success, AC_ERR_* mask otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
