---
title: "iscsi_block_scsi_eh(9)"
name: "iscsi_block_scsi_eh"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_block_scsi_eh/"
description: "iscsi_block_scsi_eh – block scsi eh until session state has transistioned"
---

<p>iscsi_block_scsi_eh &#8211; block scsi eh until session state has transistioned</p>
<h2>Synopsis</h2>
<pre><code>int iscsi_block_scsi_eh(struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>cmd</i></p>
<dl>
<dd>
<dd>scsi cmd passed to scsi eh handler</dl>
<h2>Description</h2>
<p>If the session is down this function will wait for the recovery timer to fire or for the session to be logged back in. If the recovery timer fires then FAST_IO_FAIL is returned. The caller should pass this error value to the scsi eh.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
