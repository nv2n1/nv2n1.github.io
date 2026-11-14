---
title: "iscsi_find_flashnode_conn(9)"
name: "iscsi_find_flashnode_conn"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_find_flashnode_conn/"
description: "iscsi_find_flashnode_conn – finds flashnode connection entry"
---

<p>iscsi_find_flashnode_conn &#8211; finds flashnode connection entry</p>
<h2>Synopsis</h2>
<pre><code>struct device *iscsi_find_flashnode_conn(struct iscsi_bus_flash_session *fnode_sess);</code></pre>
<h2>Arguments</h2>
<p><i>fnode_sess</i></p>
<dl>
<dd>
<dd>pointer to parent flashnode session entry</dl>
<h2>Description</h2>
<p>Finds the flashnode connection object comparing the data passed using logic defined in passed function pointer</p>
<h2>Return</h2>
<p>pointer to found flashnode connection device object on success <code>NULL</code> on failure</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
