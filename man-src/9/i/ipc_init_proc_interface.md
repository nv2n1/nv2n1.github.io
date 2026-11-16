---
title: "ipc_init_proc_interface(9)"
name: "ipc_init_proc_interface"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_init_proc_interface/"
---

ipc_init_proc_interface - create a proc interface for sysipc types using a seq_file interface.

<h2>Synopsis</h2>

<pre><code>void ipc_init_proc_interface(const char *path, const char *header, int ids, int (*show)(struct seq_file *, void *));</code></pre>

<h2>Arguments</h2>

<i>path</i>
<dl><dd></dd><dd>Path in procfs</dd></dl>
 

 <i>header</i>
<dl><dd>Banner to be printed at the beginning of the file.</dd></dl>
 

 <i>ids</i>
<dl><dd>ipc id table to iterate.</dd></dl>
 

 <i>show</i>
<dl><dd>show routine.</dd></dl>

<h2>Copyright</h2>


