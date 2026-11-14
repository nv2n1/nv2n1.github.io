---
title: "iscsi_create_flashnode_sess(9)"
name: "iscsi_create_flashnode_sess"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_create_flashnode_sess/"
description: "iscsi_create_flashnode_sess – Add flashnode session entry in sysfs"
---

<p>iscsi_create_flashnode_sess &#8211; Add flashnode session entry in sysfs</p>
<h2>Synopsis</h2>
<pre><code>struct iscsi_bus_flash_session *iscsi_create_flashnode_sess(struct Scsi_Host *shost, int index, struct iscsi_transport *transport, int dd_size);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>pointer to host data</dl>
<p> <i>index</i></p>
<dl>
<dd>index of flashnode to add in sysfs</dl>
<p> <i>transport</i></p>
<dl>
<dd>pointer to transport data</dl>
<p> <i>dd_size</i></p>
<dl>
<dd>total size to allocate</dl>
<h2>Description</h2>
<p>Adds a sysfs entry for the flashnode session attributes</p>
<h2>Return</h2>
<p>pointer to allocated flashnode sess on success <code>NULL</code> on failure</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
