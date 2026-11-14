---
title: "requeue_pi_wake_futex(9)"
name: "requeue_pi_wake_futex"
section: "9"
letter: "r"
url: "/docs/linux/man/9-requeue_pi_wake_futex/"
description: "requeue_pi_wake_futex – Wake a task that acquired the lock during requeue"
---

<p>requeue_pi_wake_futex &#8211; Wake a task that acquired the lock during requeue</p>
<h2>Synopsis</h2>
<pre><code>void requeue_pi_wake_futex(struct futex_q *q, union futex_key *key, struct futex_hash_bucket *hb);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the futex_q</dl>
<p> <i>key</i></p>
<dl>
<dd>the key of the requeue target futex</dl>
<p> <i>hb</i></p>
<dl>
<dd>the hash_bucket of the requeue target futex</dl>
<h2>Description</h2>
<p>During futex_requeue, with requeue_pi=1, it is possible to acquire the target futex if it is uncontended or via a lock steal. Set the futex_q key to the requeue target futex so the waiter can detect the wakeup on the right futex, but remove it from the hb and NULL the rt_waiter so it can detect atomic lock acquisition. Set the q-&gt;lock_ptr to the requeue target hb-&gt;lock to protect access to the pi_state to fixup the owner later. Must be called with both q-&gt;lock_ptr and hb-&gt;lock held.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
