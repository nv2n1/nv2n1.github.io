---
title: "sys_set_robust_list(9)"
name: "sys_set_robust_list"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sys_set_robust_list/"
description: "sys_set_robust_list – Set the robust-futex list head of a task"
---

<p>sys_set_robust_list &#8211; Set the robust-futex list head of a task</p>
<h2>Synopsis</h2>
<pre><code>long sys_set_robust_list(struct robust_list_head __user *head, size_t len);</code></pre>
<h2>Arguments</h2>
<p><i>head</i></p>
<dl>
<dd>
<dd>pointer to the list-head</dl>
<p> <i>len</i></p>
<dl>
<dd>length of the list-head, as userspace expects</dl>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
