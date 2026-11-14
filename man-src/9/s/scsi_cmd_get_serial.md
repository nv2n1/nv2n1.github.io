---
title: "scsi_cmd_get_serial(9)"
name: "scsi_cmd_get_serial"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_cmd_get_serial/"
description: "scsi_cmd_get_serial – Assign a serial number to a command"
---

<p>scsi_cmd_get_serial &#8211; Assign a serial number to a command</p>
<h2>Synopsis</h2>
<pre><code>void scsi_cmd_get_serial(struct Scsi_Host *host, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>the scsi host</dl>
<p> <i>cmd</i></p>
<dl>
<dd>command to assign serial number to</dl>
<h2>Description</h2>
<p>a serial number identifies a request for error recovery and debugging purposes. Protected by the Host_Lock of host.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
