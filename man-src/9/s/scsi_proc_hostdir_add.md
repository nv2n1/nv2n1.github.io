---
title: "scsi_proc_hostdir_add(9)"
name: "scsi_proc_hostdir_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_proc_hostdir_add/"
description: "scsi_proc_hostdir_add – Create directory in /proc for a scsi host"
---

<p>scsi_proc_hostdir_add &#8211; Create directory in /proc for a scsi host</p>
<h2>Synopsis</h2>
<pre><code>void scsi_proc_hostdir_add(struct scsi_host_template *sht);</code></pre>
<h2>Arguments</h2>
<p><i>sht</i></p>
<dl>
<dd>
<dd>owner of this directory</dl>
<h2>Description</h2>
<p>Sets sht-&gt;proc_dir to the new directory.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
