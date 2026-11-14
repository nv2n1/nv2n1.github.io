---
title: "scsi_mode_select(9)"
name: "scsi_mode_select"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_mode_select/"
description: "scsi_mode_select – issue a mode select"
---

<p>scsi_mode_select &#8211; issue a mode select</p>
<h2>Synopsis</h2>
<pre><code>int scsi_mode_select(struct scsi_device *sdev, int pf, int sp, int modepage, unsigned char *buffer, int len, int timeout, int retries, struct scsi_mode_data *data, struct scsi_sense_hdr *sshdr);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI device to be queried</dl>
<p> <i>pf</i></p>
<dl>
<dd>Page format bit (1 == standard, 0 == vendor specific)</dl>
<p> <i>sp</i></p>
<dl>
<dd>Save page bit (0 == don&#8217;t save, 1 == save)</dl>
<p> <i>modepage</i></p>
<dl>
<dd>mode page being requested</dl>
<p> <i>buffer</i></p>
<dl>
<dd>request buffer (may not be smaller than eight bytes)</dl>
<p> <i>len</i></p>
<dl>
<dd>length of request buffer.</dl>
<p> <i>timeout</i></p>
<dl>
<dd>command timeout</dl>
<p> <i>retries</i></p>
<dl>
<dd>number of retries before failing</dl>
<p> <i>data</i></p>
<dl>
<dd>returns a structure abstracting the mode header data</dl>
<p> <i>sshdr</i></p>
<dl>
<dd>place to put sense data (or NULL if no sense to be collected). must be SCSI_SENSE_BUFFERSIZE big.</dl>
<h2>Description</h2>
<p>Returns zero if successful; negative error number or scsi status on error</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
