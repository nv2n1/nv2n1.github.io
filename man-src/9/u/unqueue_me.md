---
title: "unqueue_me(9)"
name: "unqueue_me"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unqueue_me/"
description: "unqueue_me – Remove the futex_q from its futex_hash_bucket"
---

<p>unqueue_me &#8211; Remove the futex_q from its futex_hash_bucket</p>
<h2>Synopsis</h2>
<pre><code>int unqueue_me(struct futex_q *q);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>The futex_q to unqueue</dl>
<h2>Description</h2>
<p>The q-&gt;lock_ptr must not be held by the caller. A call to <code>unqueue_me</code> must be paired with exactly one earlier call to <code>queue_me</code>.</p>
<h2>Return</h2>
<p>1 &#8211; if the futex_q was still queued (and we removed unqueued it); 0 &#8211; if the futex_q was already removed by the waking thread</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
