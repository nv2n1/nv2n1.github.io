---
title: "scsi_eh_prep_cmnd(9)"
name: "scsi_eh_prep_cmnd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_prep_cmnd/"
description: "scsi_eh_prep_cmnd – Save a scsi command info as part of error recovery"
---

<p>scsi_eh_prep_cmnd &#8211; Save a scsi command info as part of error recovery</p>
<h2>Synopsis</h2>
<pre><code>void scsi_eh_prep_cmnd(struct scsi_cmnd *scmd, struct scsi_eh_save *ses, unsigned char *cmnd, int cmnd_size, unsigned sense_bytes);</code></pre>
<h2>Arguments</h2>
<p><i>scmd</i></p>
<dl>
<dd>
<dd>SCSI command structure to hijack</dl>
<p> <i>ses</i></p>
<dl>
<dd>structure to save restore information</dl>
<p> <i>cmnd</i></p>
<dl>
<dd>CDB to send. Can be NULL if no new cmnd is needed</dl>
<p> <i>cmnd_size</i></p>
<dl>
<dd>size in bytes of <i>cmnd</i> (must be &lt;= BLK_MAX_CDB)</dl>
<p> <i>sense_bytes</i></p>
<dl>
<dd>size of sense data to copy. or 0 (if != 0 <i>cmnd</i> is ignored)</dl>
<h2>Description</h2>
<p>This function is used to save a scsi command information before re-execution as part of the error recovery process. If <i>sense_bytes</i> is 0 the command sent must be one that does not transfer any data. If <i>sense_bytes</i> != 0 <i>cmnd</i> is ignored and this functions sets up a REQUEST_SENSE command and cmnd buffers to read <i>sense_bytes</i> into <i>scmd</i>-&gt;sense_buffer.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
