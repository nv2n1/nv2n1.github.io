---
title: "fixup_owner(9)"
name: "fixup_owner"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fixup_owner/"
description: "fixup_owner – Post lock pi_state and corner case management"
---

<p>fixup_owner &#8211; Post lock pi_state and corner case management</p>
<h2>Synopsis</h2>
<pre><code>int fixup_owner(u32 __user *uaddr, struct futex_q *q, int locked);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>user address of the futex</dl>
<p> <i>q</i></p>
<dl>
<dd>futex_q (contains pi_state and access to the rt_mutex)</dl>
<p> <i>locked</i></p>
<dl>
<dd>if the attempt to take the rt_mutex succeeded (1) or not (0)</dl>
<h2>Description</h2>
<p>After attempting to lock an rt_mutex, this function is called to cleanup the pi_state owner as well as handle race conditions that may allow us to acquire the lock. Must be called with the hb lock held.</p>
<h2>Return</h2>
<p>1 &#8211; success, lock taken; 0 &#8211; success, lock not taken; &lt;0 &#8211; on error (-EFAULT)</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
