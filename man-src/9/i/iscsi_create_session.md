---
title: "iscsi_create_session(9)"
name: "iscsi_create_session"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_create_session/"
description: "iscsi_create_session – create iscsi class session"
---

<p>iscsi_create_session &#8211; create iscsi class session</p>
<h2>Synopsis</h2>
<pre><code>struct iscsi_cls_session *iscsi_create_session(struct Scsi_Host *shost, struct iscsi_transport *transport, int dd_size, unsigned int target_id);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host</dl>
<p> <i>transport</i></p>
<dl>
<dd>iscsi transport</dl>
<p> <i>dd_size</i></p>
<dl>
<dd>private driver data size</dl>
<p> <i>target_id</i></p>
<dl>
<dd>which target</dl>
<h2>Description</h2>
<p>This can be called from a LLD or iscsi_transport.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
