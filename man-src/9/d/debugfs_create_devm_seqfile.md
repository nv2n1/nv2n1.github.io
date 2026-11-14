---
title: "debugfs_create_devm_seqfile(9)"
name: "debugfs_create_devm_seqfile"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_devm_seqfile/"
description: "debugfs_create_devm_seqfile – create a debugfs file that is bound to device."
---

<p>debugfs_create_devm_seqfile &#8211; create a debugfs file that is bound to device.</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_devm_seqfile(struct device *dev, const char *name, struct dentry *parent, int (*read_fn)(struct seq_file *s, void *data));</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device related to this debugfs file.</dl>
<p> <i>name</i></p>
<dl>
<dd>name of the debugfs file.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is <code>NULL</code>, then the file will be created in the root of the debugfs filesystem.</dl>
<p> <i>read_fn</i></p>
<dl>
<dd>function pointer called to print the seq_file content.</dl>
<h2>Copyright</h2>
