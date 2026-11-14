---
title: "rio_remove_sysfs_dev_files(9)"
name: "rio_remove_sysfs_dev_files"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_remove_sysfs_dev_files/"
description: "rio_remove_sysfs_dev_files – cleanup RIO specific sysfs files"
---

<p>rio_remove_sysfs_dev_files &#8211; cleanup RIO specific sysfs files</p>
<h2>Synopsis</h2>
<pre><code>void rio_remove_sysfs_dev_files(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>device whose entries we should free</dl>
<h2>Description</h2>
<p>Cleanup when <i>rdev</i> is removed from sysfs.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
