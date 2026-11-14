---
title: "sas_get_address(9)"
name: "sas_get_address"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sas_get_address/"
description: "sas_get_address – return the SAS address of the device"
---

<p>sas_get_address &#8211; return the SAS address of the device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u64 sas_get_address(struct scsi_device&nbsp;<wbr>*&nbsp;<wbr></code><i>sdev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device</dl>
<h2>Description</h2>
<p>Returns the SAS address of the scsi device</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
