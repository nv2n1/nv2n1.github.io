---
title: "sys_get_robust_list(9)"
name: "sys_get_robust_list"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sys_get_robust_list/"
description: "sys_get_robust_list – Get the robust-futex list head of a task"
---

<p>sys_get_robust_list &#8211; Get the robust-futex list head of a task</p>
<h2>Synopsis</h2>
<pre><code>long sys_get_robust_list(int pid, struct robust_list_head __user *__user *head_ptr, size_t __user *len_ptr);</code></pre>
<h2>Arguments</h2>
<p><i>pid</i></p>
<dl>
<dd>
<dd>pid of the process [zero for current task]</dl>
<p> <i>head_ptr</i></p>
<dl>
<dd>pointer to a list-head pointer, the kernel fills it in</dl>
<p> <i>len_ptr</i></p>
<dl>
<dd>pointer to a length field, the kernel fills in the header size</dl>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
