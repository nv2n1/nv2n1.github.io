---
title: "proc_dostring(9)"
name: "proc_dostring"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_dostring/"
description: "proc_dostring – read a string sysctl"
---

<p>proc_dostring &#8211; read a string sysctl</p>
<h2>Synopsis</h2>
<pre><code>int proc_dostring(struct ctl_table *table, int write, void __user *buffer, size_t *lenp, loff_t *ppos);</code></pre>
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
<p>Reads/writes a string from/to the user buffer. If the kernel buffer provided is not large enough to hold the string, the string is truncated. The copied string is <code>NULL-terminated</code>. If the string is being read by the user process, it is copied and a newline &#8216;
&#8217; is added. It is truncated if the buffer is not large enough. </p>
<p> Returns 0 on success.</p>
<h2>Copyright</h2>
