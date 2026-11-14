---
title: "ata_exec_internal(9)"
name: "ata_exec_internal"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_exec_internal/"
description: "ata_exec_internal – execute libata internal command"
---

<p>ata_exec_internal &#8211; execute libata internal command</p>
<h2>Synopsis</h2>
<pre><code>unsigned ata_exec_internal(struct ata_device *dev, struct ata_taskfile *tf, const u8 *cdb, int dma_dir, void *buf, unsigned int buflen, unsigned long timeout);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to which the command is sent</dl>
<p> <i>tf</i></p>
<dl>
<dd>Taskfile registers for the command and the result</dl>
<p> <i>cdb</i></p>
<dl>
<dd>CDB for packet command</dl>
<p> <i>dma_dir</i></p>
<dl>
<dd>Data transfer direction of the command</dl>
<p> <i>buf</i></p>
<dl>
<dd>Data buffer of the command</dl>
<p> <i>buflen</i></p>
<dl>
<dd>Length of data buffer</dl>
<p> <i>timeout</i></p>
<dl>
<dd>Timeout in msecs (0 for default)</dl>
<h2>Description</h2>
<p>Wrapper around <code>ata_exec_internal_sg</code> which takes simple buffer instead of sg list. </p>
<p> LOCKING: None. Should be called with kernel context, might sleep.</p>
<h2>Return</h2>
<p>Zero on success, AC_ERR_* mask on failure</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
