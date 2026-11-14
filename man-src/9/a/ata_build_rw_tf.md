---
title: "ata_build_rw_tf(9)"
name: "ata_build_rw_tf"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_build_rw_tf/"
description: "ata_build_rw_tf – Build ATA taskfile for given read/write request"
---

<p>ata_build_rw_tf &#8211; Build ATA taskfile for given read/write request</p>
<h2>Synopsis</h2>
<pre><code>int ata_build_rw_tf(struct ata_taskfile *tf, struct ata_device *dev, u64 block, u32 n_block, unsigned int tf_flags, unsigned int tag);</code></pre>
<h2>Arguments</h2>
<p><i>tf</i></p>
<dl>
<dd>
<dd>Target ATA taskfile</dl>
<p> <i>dev</i></p>
<dl>
<dd>ATA device <i>tf</i> belongs to</dl>
<p> <i>block</i></p>
<dl>
<dd>Block address</dl>
<p> <i>n_block</i></p>
<dl>
<dd>Number of blocks</dl>
<p> <i>tf_flags</i></p>
<dl>
<dd>RW/FUA etc&#8230;</dl>
<p> <i>tag</i></p>
<dl>
<dd>tag</dl>
<h2>Description</h2>
<p>LOCKING: None. </p>
<p> Build ATA taskfile <i>tf</i> for read/write request described by <i>block</i>, <i>n_block</i>, <i>tf_flags</i> and <i>tag</i> on <i>dev</i>.</p>
<h2>Return</h2>
<p>0 on success, -ERANGE if the request is too large for <i>dev</i>, -EINVAL if the request is invalid.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
