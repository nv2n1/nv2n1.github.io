---
title: "proc_scsi_open(9)"
name: "proc_scsi_open"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_scsi_open/"
description: "proc_scsi_open – glue function"
---

<p>proc_scsi_open &#8211; glue function</p>
<h2>Synopsis</h2>
<pre><code>int proc_scsi_open(struct inode *inode, struct file *file);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>not used</dl>
<p> <i>file</i></p>
<dl>
<dd>passed to <code>single_open</code></dl>
<h2>Description</h2>
<p>Associates proc_scsi_show with this file</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
