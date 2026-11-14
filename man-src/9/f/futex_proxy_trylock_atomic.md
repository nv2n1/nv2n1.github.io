---
title: "futex_proxy_trylock_atomic(9)"
name: "futex_proxy_trylock_atomic"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_proxy_trylock_atomic/"
description: "futex_proxy_trylock_atomic – Attempt an atomic lock for the top waiter"
---

<p>futex_proxy_trylock_atomic &#8211; Attempt an atomic lock for the top waiter</p>
<h2>Synopsis</h2>
<pre><code>int futex_proxy_trylock_atomic(u32 __user *pifutex, struct futex_hash_bucket *hb1, struct futex_hash_bucket *hb2, union futex_key *key1, union futex_key *key2, struct futex_pi_state **ps, int set_waiters);</code></pre>
<h2>Arguments</h2>
<p><i>pifutex</i></p>
<dl>
<dd>
<dd>the user address of the to futex</dl>
<p> <i>hb1</i></p>
<dl>
<dd>the from futex hash bucket, must be locked by the caller</dl>
<p> <i>hb2</i></p>
<dl>
<dd>the to futex hash bucket, must be locked by the caller</dl>
<p> <i>key1</i></p>
<dl>
<dd>the from futex key</dl>
<p> <i>key2</i></p>
<dl>
<dd>the to futex key</dl>
<p> <i>ps</i></p>
<dl>
<dd>address to store the pi_state pointer</dl>
<p> <i>set_waiters</i></p>
<dl>
<dd>force setting the FUTEX_WAITERS bit (1) or not (0)</dl>
<h2>Description</h2>
<p>Try and get the lock on behalf of the top waiter if we can do it atomically. Wake the top waiter if we succeed. If the caller specified set_waiters, then direct <code>futex_lock_pi_atomic</code> to force setting the FUTEX_WAITERS bit. hb1 and hb2 must be held by the caller.</p>
<h2>Return</h2>
<p>0 &#8211; failed to acquire the lock atomically; &gt;0 &#8211; acquired the lock, return value is vpid of the top_waiter &lt;0 &#8211; error</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
