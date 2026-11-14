---
title: "scsi_host_lookup(9)"
name: "scsi_host_lookup"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_host_lookup/"
description: "scsi_host_lookup – get a reference to a Scsi_Host by host no"
---

<p>scsi_host_lookup &#8211; get a reference to a Scsi_Host by host no</p>
<h2>Synopsis</h2>
<pre><code>struct Scsi_Host *scsi_host_lookup(unsigned short hostnum);</code></pre>
<h2>Arguments</h2>
<p><i>hostnum</i></p>
<dl>
<dd>
<dd>host number to locate</dl>
<h2>Description</h2>
<p>Return value: A pointer to located Scsi_Host or NULL. </p>
<p> The caller must do a <code>scsi_host_put</code> to drop the reference that <code>scsi_host_get</code> took. The <code>put_device</code> below dropped the reference from <code>class_find_device</code>.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
