---
title: "seq_path(9)"
name: "seq_path"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_path/"
---

seq_path - seq_file interface to print a pathname

<h2>Synopsis</h2>

<pre><code>int seq_path(struct seq_file *m, const struct path *path, const char *esc);</code></pre>

<h2>Arguments</h2>

<i>m</i>
<dl><dd></dd><dd>the seq_file handle</dd></dl>
 

 <i>path</i>
<dl><dd>the struct path to print</dd></dl>
 

 <i>esc</i>
<dl><dd>set of characters to escape in the output</dd></dl>

<h2>Description</h2>

return the absolute path of 'path', as represented by the dentry / mnt pair in the path parameter.

<h2>Copyright</h2>


