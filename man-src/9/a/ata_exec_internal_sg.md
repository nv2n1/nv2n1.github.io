---
title: "ata_exec_internal_sg(9)"
name: "ata_exec_internal_sg"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_exec_internal_sg/"
description: "ata_exec_internal_sg – execute libata internal command"
---

<p>ata_exec_internal_sg &#8211; execute libata internal command</p>
<h2>Synopsis</h2>
<pre><code>unsigned ata_exec_internal_sg(struct ata_device *dev, struct ata_taskfile *tf, const u8 *cdb, int dma_dir, struct scatterlist *sgl, unsigned int n_elem, unsigned long timeout);</code></pre>
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
<p> <i>sgl</i></p>
<dl>
<dd>sg list for the data buffer of the command</dl>
<p> <i>n_elem</i></p>
<dl>
<dd>Number of sg entries</dl>
<p> <i>timeout</i></p>
<dl>
<dd>Timeout in msecs (0 for default)</dl>
<h2>Description</h2>
<p>Executes libata internal command with timeout. <i>tf</i> contains command on entry and result on return. Timeout and error conditions are reported via return value. No recovery action is taken after a command times out. It&#8217;s caller&#8217;s duty to clean up after timeout. </p>
<p> LOCKING: None. Should be called with kernel context, might sleep.</p>
<h2>Return</h2>
<p>Zero on success, AC_ERR_* mask on failure</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
