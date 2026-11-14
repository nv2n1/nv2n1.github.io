---
title: "fc_block_scsi_eh(9)"
name: "fc_block_scsi_eh"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fc_block_scsi_eh/"
description: "fc_block_scsi_eh – Block SCSI eh thread for blocked fc_rport"
---

<p>fc_block_scsi_eh &#8211; Block SCSI eh thread for blocked fc_rport</p>
<h2>Synopsis</h2>
<pre><code>int fc_block_scsi_eh(struct scsi_cmnd *cmnd);</code></pre>
<h2>Arguments</h2>
<p><i>cmnd</i></p>
<dl>
<dd>
<dd>SCSI command that scsi_eh is trying to recover</dl>
<h2>Description</h2>
<p>This routine can be called from a FC LLD scsi_eh callback. It blocks the scsi_eh thread until the fc_rport leaves the FC_PORTSTATE_BLOCKED, or the fast_io_fail_tmo fires. This is necessary to avoid the scsi_eh failing recovery actions for blocked rports which would lead to offlined SCSI devices.</p>
<h2>Return</h2>
<p>0 if the fc_rport left the state FC_PORTSTATE_BLOCKED. FAST_IO_FAIL if the fast_io_fail_tmo fired, this should be passed back to scsi_eh.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
