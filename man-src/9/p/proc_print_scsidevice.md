---
title: "proc_print_scsidevice(9)"
name: "proc_print_scsidevice"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_print_scsidevice/"
description: "proc_print_scsidevice – return data about this host"
---

<p>proc_print_scsidevice &#8211; return data about this host</p>
<h2>Synopsis</h2>
<pre><code>int proc_print_scsidevice(struct device *dev, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>A scsi device</dl>
<p> <i>data</i></p>
<dl>
<dd>struct seq_file to output to.</dl>
<h2>Description</h2>
<p>prints Host, Channel, Id, Lun, Vendor, Model, Rev, Type, and revision.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
