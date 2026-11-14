---
title: "ata_tf_read_block(9)"
name: "ata_tf_read_block"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_tf_read_block/"
description: "ata_tf_read_block – Read block address from ATA taskfile"
---

<p>ata_tf_read_block &#8211; Read block address from ATA taskfile</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u64 ata_tf_read_block(const struct ata_taskfile&nbsp;<wbr>*&nbsp;<wbr></code><i>tf</i><code>, struct ata_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>tf</i></p>
<dl>
<dd>
<dd>ATA taskfile of interest</dl>
<p> <i>dev</i></p>
<dl>
<dd>ATA device <i>tf</i> belongs to</dl>
<h2>Description</h2>
<p>LOCKING: None. </p>
<p> Read block address from <i>tf</i>. This function can handle all three address formats &#8211; LBA, LBA48 and CHS. tf-&gt;protocol and flags select the address format to use.</p>
<h2>Return</h2>
<p>Block address read from <i>tf</i>.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
