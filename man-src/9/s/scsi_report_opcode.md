---
title: "scsi_report_opcode(9)"
name: "scsi_report_opcode"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_report_opcode/"
description: "scsi_report_opcode – Find out if a given command opcode is supported"
---

<p>scsi_report_opcode &#8211; Find out if a given command opcode is supported</p>
<h2>Synopsis</h2>
<pre><code>int scsi_report_opcode(struct scsi_device *sdev, unsigned char *buffer, unsigned int len, unsigned char opcode);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to query</dl>
<p> <i>buffer</i></p>
<dl>
<dd>scratch buffer (must be at least 20 bytes long)</dl>
<p> <i>len</i></p>
<dl>
<dd>length of buffer</dl>
<p> <i>opcode</i></p>
<dl>
<dd>opcode for command to look up</dl>
<h2>Description</h2>
<p>Uses the REPORT SUPPORTED OPERATION CODES to look up the given opcode. Returns -EINVAL if RSOC fails, 0 if the command opcode is unsupported and 1 if the device claims to support the command.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
