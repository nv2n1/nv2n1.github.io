---
title: "scsi_eh_restore_cmnd(9)"
name: "scsi_eh_restore_cmnd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_restore_cmnd/"
description: "scsi_eh_restore_cmnd – Restore a scsi command info as part of error recovery"
---

<p>scsi_eh_restore_cmnd &#8211; Restore a scsi command info as part of error recovery</p>
<h2>Synopsis</h2>
<pre><code>void scsi_eh_restore_cmnd(struct scsi_cmnd *scmd, struct scsi_eh_save *ses);</code></pre>
<h2>Arguments</h2>
<p><i>scmd</i></p>
<dl>
<dd>
<dd>SCSI command structure to restore</dl>
<p> <i>ses</i></p>
<dl>
<dd>saved information from a coresponding call to scsi_eh_prep_cmnd</dl>
<h2>Description</h2>
<p>Undo any damage done by above <code>scsi_eh_prep_cmnd</code>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
