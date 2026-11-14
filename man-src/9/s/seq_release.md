---
title: "seq_release(9)"
name: "seq_release"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_release/"
description: "seq_release – free the structures associated with sequential file."
---

<p>seq_release &#8211; free the structures associated with sequential file.</p>
<h2>Synopsis</h2>
<pre><code>int seq_release(struct inode *inode, struct file *file);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>its inode</dl>
<p> <i>file</i></p>
<dl>
<dd>file in question</dl>
<h2>Description</h2>
<p>Frees the structures associated with sequential file; can be used as -&gt;f_op-&gt;<code>release</code> if you don&#8217;t have private data to destroy.</p>
<h2>Copyright</h2>
