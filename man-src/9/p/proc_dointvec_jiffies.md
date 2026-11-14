---
title: "proc_dointvec_jiffies(9)"
name: "proc_dointvec_jiffies"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_dointvec_jiffies/"
description: "proc_dointvec_jiffies – read a vector of integers as seconds"
---

<p>proc_dointvec_jiffies &#8211; read a vector of integers as seconds</p>
<h2>Synopsis</h2>
<pre><code>int proc_dointvec_jiffies(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos);</code></pre>
<h2>Arguments</h2>
<p><i>table</i></p>
<dl>
<dd>
<dd>the sysctl table</dl>
<p> <i>write</i></p>
<dl>
<dd><code>TRUE</code> if this is a write to the sysctl file</dl>
<p> <i>buffer</i></p>
<dl>
<dd>the user buffer</dl>
<p> <i>lenp</i></p>
<dl>
<dd>the size of the user buffer</dl>
<p> <i>ppos</i></p>
<dl>
<dd>file position</dl>
<h2>Description</h2>
<p>Reads/writes up to table-&gt;maxlen/sizeof(unsigned int) integer values from/to the user buffer, treated as an ASCII string. The values read are assumed to be in seconds, and are converted into jiffies. </p>
<p> Returns 0 on success.</p>
<h2>Copyright</h2>
