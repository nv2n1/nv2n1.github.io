---
title: "iscsi_destroy_flashnode_sess(9)"
name: "iscsi_destroy_flashnode_sess"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_destroy_flashnode_sess/"
description: "iscsi_destroy_flashnode_sess – destroy flashnode session entry"
---

<p>iscsi_destroy_flashnode_sess &#8211; destroy flashnode session entry</p>
<h2>Synopsis</h2>
<pre><code>void iscsi_destroy_flashnode_sess(struct iscsi_bus_flash_session *fnode_sess);</code></pre>
<h2>Arguments</h2>
<p><i>fnode_sess</i></p>
<dl>
<dd>
<dd>pointer to flashnode session entry to be destroyed</dl>
<h2>Description</h2>
<p>Deletes the flashnode session entry and all children flashnode connection entries from sysfs</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
