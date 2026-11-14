---
title: "futex_requeue(9)"
name: "futex_requeue"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_requeue/"
description: "futex_requeue – Requeue waiters from uaddr1 to uaddr2"
---

<p>futex_requeue &#8211; Requeue waiters from uaddr1 to uaddr2</p>
<h2>Synopsis</h2>
<pre><code>int futex_requeue(u32 __user *uaddr1, unsigned int flags, u32 __user *uaddr2, int nr_wake, int nr_requeue, u32 *cmpval, int requeue_pi);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr1</i></p>
<dl>
<dd>
<dd>source futex user address</dl>
<p> <i>flags</i></p>
<dl>
<dd>futex flags (FLAGS_SHARED, etc.)</dl>
<p> <i>uaddr2</i></p>
<dl>
<dd>target futex user address</dl>
<p> <i>nr_wake</i></p>
<dl>
<dd>number of waiters to wake (must be 1 for requeue_pi)</dl>
<p> <i>nr_requeue</i></p>
<dl>
<dd>number of waiters to requeue (0-INT_MAX)</dl>
<p> <i>cmpval</i></p>
<dl>
<dd><i>uaddr1</i> expected value (or <code>NULL</code>)</dl>
<p> <i>requeue_pi</i></p>
<dl>
<dd>if we are attempting to requeue from a non-pi futex to a pi futex (pi to pi requeue is not supported)</dl>
<h2>Description</h2>
<p>Requeue waiters on uaddr1 to uaddr2. In the requeue_pi case, try to acquire uaddr2 atomically on behalf of the top waiter.</p>
<h2>Return</h2>
<p>&gt;=0 &#8211; on success, the number of tasks requeued or woken; &lt;0 &#8211; on error</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
