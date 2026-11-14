---
title: "fault_in_user_writeable(9)"
name: "fault_in_user_writeable"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fault_in_user_writeable/"
description: "fault_in_user_writeable – Fault in user address and verify RW access"
---

<p>fault_in_user_writeable &#8211; Fault in user address and verify RW access</p>
<h2>Synopsis</h2>
<pre><code>int fault_in_user_writeable(u32 __user *uaddr);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>pointer to faulting user space address</dl>
<h2>Description</h2>
<p>Slow path to fixup the fault we just took in the atomic write access to <i>uaddr</i>. </p>
<p> We have no generic implementation of a non-destructive write to the user address. We know that we faulted in the atomic pagefault disabled section so we can as well avoid the #PF overhead by calling <code>get_user_pages</code> right away.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
