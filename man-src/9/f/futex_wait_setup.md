---
title: "futex_wait_setup(9)"
name: "futex_wait_setup"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_wait_setup/"
description: "futex_wait_setup – Prepare to wait on a futex"
---

<p>futex_wait_setup &#8211; Prepare to wait on a futex</p>
<h2>Synopsis</h2>
<pre><code>int futex_wait_setup(u32 __user *uaddr, u32 val, unsigned int flags, struct futex_q *q, struct futex_hash_bucket **hb);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>the futex userspace address</dl>
<p> <i>val</i></p>
<dl>
<dd>the expected value</dl>
<p> <i>flags</i></p>
<dl>
<dd>futex flags (FLAGS_SHARED, etc.)</dl>
<p> <i>q</i></p>
<dl>
<dd>the associated futex_q</dl>
<p> <i>hb</i></p>
<dl>
<dd>storage for hash_bucket pointer to be returned to caller</dl>
<h2>Description</h2>
<p>Setup the futex_q and locate the hash_bucket. Get the futex value and compare it with the expected value. Handle atomic faults internally. Return with the hb lock held and a q.key reference on success, and unlocked with no q.key reference on failure.</p>
<h2>Return</h2>
<p>0 &#8211; uaddr contains val and hb has been locked; &lt;1 &#8211; -EFAULT or -EWOULDBLOCK (uaddr does not contain val) and hb is unlocked</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
