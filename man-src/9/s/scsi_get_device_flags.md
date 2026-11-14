---
title: "scsi_get_device_flags(9)"
name: "scsi_get_device_flags"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_get_device_flags/"
description: "scsi_get_device_flags – get device specific flags from the dynamic device list."
---

<p>scsi_get_device_flags &#8211; get device specific flags from the dynamic device list.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_get_device_flags(struct scsi_device *sdev, const unsigned char *vendor, const unsigned char *model);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi_device to get flags for</dl>
<p> <i>vendor</i></p>
<dl>
<dd>vendor name</dl>
<p> <i>model</i></p>
<dl>
<dd>model name</dl>
<h2>Description</h2>
<p>Search the global scsi_dev_info_list (specified by list zero) for an entry matching <i>vendor</i> and <i>model</i>, if found, return the matching flags value, else return the host or global default settings. Called during scan time.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
