---
title: "queue_me(9)"
name: "queue_me"
section: "9"
letter: "q"
url: "/docs/linux/man/9-queue_me/"
description: "queue_me – Enqueue the futex_q on the futex_hash_bucket"
---

<p>queue_me &#8211; Enqueue the futex_q on the futex_hash_bucket</p>
<h2>Synopsis</h2>
<pre><code>void queue_me(struct futex_q *q, struct futex_hash_bucket *hb);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>The futex_q to enqueue</dl>
<p> <i>hb</i></p>
<dl>
<dd>The destination hash bucket</dl>
<h2>Description</h2>
<p>The hb-&gt;lock must be held by the caller, and is released here. A call to <code>queue_me</code> is typically paired with exactly one call to <code>unqueue_me</code>. The exceptions involve the PI related operations, which may use <code>unqueue_me_pi</code> or nothing if the unqueue is done as part of the wake process and the unqueue state is implicit in the state of woken task (see <code>futex_wait_requeue_pi</code> for an example).</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
