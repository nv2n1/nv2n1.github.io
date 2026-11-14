---
title: "rio_create_sysfs_dev_files(9)"
name: "rio_create_sysfs_dev_files"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_create_sysfs_dev_files/"
description: "rio_create_sysfs_dev_files – create RIO specific sysfs files"
---

<p>rio_create_sysfs_dev_files &#8211; create RIO specific sysfs files</p>
<h2>Synopsis</h2>
<pre><code>int rio_create_sysfs_dev_files(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>device whose entries should be created</dl>
<h2>Description</h2>
<p>Create files when <i>rdev</i> is added to sysfs.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
