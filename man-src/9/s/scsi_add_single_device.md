---
title: "scsi_add_single_device(9)"
name: "scsi_add_single_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_add_single_device/"
description: "scsi_add_single_device – Respond to user request to probe for/add device"
---

<p>scsi_add_single_device &#8211; Respond to user request to probe for/add device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_add_single_device(uint host, uint channel, uint id, uint lun);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>user-supplied decimal integer</dl>
<p> <i>channel</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<p> <i>id</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<p> <i>lun</i></p>
<dl>
<dd>user-supplied decimal integer</dl>
<h2>Description</h2>
<p>called by writing &#8220;scsi add-single-device&#8221; to /proc/scsi/scsi. </p>
<p> does <code>scsi_host_lookup</code> and either <code>user_scan</code> if that transport type supports it, or else <code>scsi_scan_host_selected</code></p>
<h2>Note</h2>
<p>this seems to be aimed exclusively at SCSI parallel busses.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
