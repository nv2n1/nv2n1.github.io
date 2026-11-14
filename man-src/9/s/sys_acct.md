---
title: "sys_acct(9)"
name: "sys_acct"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sys_acct/"
description: "sys_acct – enable/disable process accounting"
---

<p>sys_acct &#8211; enable/disable process accounting</p>
<h2>Synopsis</h2>
<pre><code>long sys_acct(const char __user *name);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>file name for accounting records or NULL to shutdown accounting</dl>
<h2>Description</h2>
<p>Returns 0 for success or negative errno values for failure. </p>
<p> <code>sys_acct</code> is the only system call needed to implement process accounting. It takes the name of the file where accounting records should be written. If the filename is NULL, accounting will be shutdown.</p>
<h2>Copyright</h2>
