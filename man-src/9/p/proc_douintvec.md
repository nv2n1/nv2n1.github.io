---
title: "proc_douintvec(9)"
name: "proc_douintvec"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_douintvec/"
description: "proc_douintvec – read a vector of unsigned integers"
---

<p>proc_douintvec &#8211; read a vector of unsigned integers</p>
<h2>Synopsis</h2>
<pre><code>int proc_douintvec(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos);</code></pre>
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
<p>Reads/writes up to table-&gt;maxlen/sizeof(unsigned int) unsigned integer values from/to the user buffer, treated as an ASCII string. </p>
<p> Returns 0 on success.</p>
<h2>Copyright</h2>
