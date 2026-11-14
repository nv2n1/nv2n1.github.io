---
title: "handle_early_requeue_pi_wakeup(9)"
name: "handle_early_requeue_pi_wakeup"
section: "9"
letter: "h"
url: "/docs/linux/man/9-handle_early_requeue_pi_wakeup/"
description: "handle_early_requeue_pi_wakeup – Detect early wakeup on the initial futex"
---

<p>handle_early_requeue_pi_wakeup &#8211; Detect early wakeup on the initial futex</p>
<h2>Synopsis</h2>
<pre><code>int handle_early_requeue_pi_wakeup(struct futex_hash_bucket *hb, struct futex_q *q, union futex_key *key2, struct hrtimer_sleeper *timeout);</code></pre>
<h2>Arguments</h2>
<p><i>hb</i></p>
<dl>
<dd>
<dd>the hash_bucket futex_q was original enqueued on</dl>
<p> <i>q</i></p>
<dl>
<dd>the futex_q woken while waiting to be requeued</dl>
<p> <i>key2</i></p>
<dl>
<dd>the futex_key of the requeue target futex</dl>
<p> <i>timeout</i></p>
<dl>
<dd>the timeout associated with the wait (NULL if none)</dl>
<h2>Description</h2>
<p>Detect if the task was woken on the initial futex as opposed to the requeue target futex. If so, determine if it was a timeout or a signal that caused the wakeup and return the appropriate error code to the caller. Must be called with the hb lock held.</p>
<h2>Return</h2>
<p>0 = no early wakeup detected; &lt;0 = -ETIMEDOUT or -ERESTARTNOINTR</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
