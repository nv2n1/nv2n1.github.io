---
title: "futex_wait_queue_me(9)"
name: "futex_wait_queue_me"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_wait_queue_me/"
description: "futex_wait_queue_me – queue_me and wait for wakeup, timeout, or signal"
---

<p>futex_wait_queue_me &#8211; <code>queue_me</code> and wait for wakeup, timeout, or signal</p>
<h2>Synopsis</h2>
<pre><code>void futex_wait_queue_me(struct futex_hash_bucket *hb, struct futex_q *q, struct hrtimer_sleeper *timeout);</code></pre>
<h2>Arguments</h2>
<p><i>hb</i></p>
<dl>
<dd>
<dd>the futex hash bucket, must be locked by the caller</dl>
<p> <i>q</i></p>
<dl>
<dd>the futex_q to queue up on</dl>
<p> <i>timeout</i></p>
<dl>
<dd>the prepared hrtimer_sleeper, or null for no timeout</dl>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
