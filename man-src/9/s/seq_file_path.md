---
title: "seq_file_path(9)"
name: "seq_file_path"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_file_path/"
---

seq_file_path - seq_file interface to print a pathname of a file

<h2>Synopsis</h2>

<pre><code>int seq_file_path(struct seq_file *m, struct file *file, const char *esc);</code></pre>

<h2>Arguments</h2>

<i>m</i>
<dl><dd><dd>the seq_file handle</dl>
 

 <i>file</i>
<dl><dd>the struct file to print</dl>
 

 <i>esc</i>
<dl><dd>set of characters to escape in the output</dl>

<h2>Description</h2>

return the absolute path to the file.

<h2>Copyright</h2>


