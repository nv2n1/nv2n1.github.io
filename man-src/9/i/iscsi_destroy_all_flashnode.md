---
title: "iscsi_destroy_all_flashnode(9)"
name: "iscsi_destroy_all_flashnode"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_destroy_all_flashnode/"
description: "iscsi_destroy_all_flashnode – destroy all flashnode session entries"
---

<p>iscsi_destroy_all_flashnode &#8211; destroy all flashnode session entries</p>
<h2>Synopsis</h2>
<pre><code>void iscsi_destroy_all_flashnode(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>pointer to host data</dl>
<h2>Description</h2>
<p>Destroys all the flashnode session entries and all corresponding children flashnode connection entries from sysfs</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
