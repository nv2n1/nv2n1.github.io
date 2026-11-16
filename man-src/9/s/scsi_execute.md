---
title: "scsi_execute(9)"
name: "scsi_execute"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_execute/"
description: "scsi_execute – insert request and wait for the result"
---

<p>scsi_execute &#8211; insert request and wait for the result</p>
<h2>Synopsis</h2>
<pre><code>int scsi_execute(struct scsi_device *sdev, const unsigned char *cmd, int data_direction, void *buffer, unsigned bufflen, unsigned char *sense, int timeout, int retries, u64 flags, int *resid);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
</dd><dd>scsi device</dd></dl>
<p> <i>cmd</i></p>
<dl>
<dd>scsi command</dd></dl>
<p> <i>data_direction</i></p>
<dl>
<dd>data direction</dd></dl>
<p> <i>buffer</i></p>
<dl>
<dd>data buffer</dd></dl>
<p> <i>bufflen</i></p>
<dl>
<dd>len of buffer</dd></dl>
<p> <i>sense</i></p>
<dl>
<dd>optional sense buffer</dd></dl>
<p> <i>timeout</i></p>
<dl>
<dd>request timeout in seconds</dd></dl>
<p> <i>retries</i></p>
<dl>
<dd>number of times to retry request</dd></dl>
<p> <i>flags</i></p>
<dl>
<dd>or into request flags;</dd></dl>
<p> <i>resid</i></p>
<dl>
<dd>optional residual length</dd></dl>
<h2>Description</h2>
<p>returns the req-&gt;errors value which is the scsi_cmnd result field.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
