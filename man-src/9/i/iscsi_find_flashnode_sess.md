---
title: "iscsi_find_flashnode_sess(9)"
name: "iscsi_find_flashnode_sess"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_find_flashnode_sess/"
description: "iscsi_find_flashnode_sess – finds flashnode session entry"
---

<p>iscsi_find_flashnode_sess &#8211; finds flashnode session entry</p>
<h2>Synopsis</h2>
<pre><code>struct device *iscsi_find_flashnode_sess(struct Scsi_Host *shost, void *data, int (*fn)(struct device *dev, void *data));</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
</dd><dd>pointer to host data</dd></dl>
<p> <i>data</i></p>
<dl>
<dd>pointer to data containing value to use for comparison</dd></dl>
<p> <i>fn</i></p>
<dl>
<dd>function pointer that does actual comparison</dd></dl>
<h2>Description</h2>
<p>Finds the flashnode session object comparing the data passed using logic defined in passed function pointer</p>
<h2>Return</h2>
<p>pointer to found flashnode session device object on success <code>NULL</code> on failure</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
