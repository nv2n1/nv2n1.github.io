---
title: "futex_lock_pi_atomic(9)"
name: "futex_lock_pi_atomic"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_lock_pi_atomic/"
description: "futex_lock_pi_atomic – Atomic work required to acquire a pi aware futex"
---

<p>futex_lock_pi_atomic &#8211; Atomic work required to acquire a pi aware futex</p>
<h2>Synopsis</h2>
<pre><code>int futex_lock_pi_atomic(u32 __user *uaddr, struct futex_hash_bucket *hb, union futex_key *key, struct futex_pi_state **ps, struct task_struct *task, int set_waiters);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>the pi futex user address</dl>
<p> <i>hb</i></p>
<dl>
<dd>the pi futex hash bucket</dl>
<p> <i>key</i></p>
<dl>
<dd>the futex key associated with uaddr and hb</dl>
<p> <i>ps</i></p>
<dl>
<dd>the pi_state pointer where we store the result of the lookup</dl>
<p> <i>task</i></p>
<dl>
<dd>the task to perform the atomic lock work for. This will be &#8220;current&#8221; except in the case of requeue pi.</dl>
<p> <i>set_waiters</i></p>
<dl>
<dd>force setting the FUTEX_WAITERS bit (1) or not (0)</dl>
<h2>Return</h2>
<p>0 &#8211; ready to wait; 1 &#8211; acquired the lock; &lt;0 &#8211; error </p>
<p> The hb-&gt;lock and futex_key refs shall be held by the caller.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
