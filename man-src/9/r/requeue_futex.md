---
title: "requeue_futex(9)"
name: "requeue_futex"
section: "9"
letter: "r"
url: "/docs/linux/man/9-requeue_futex/"
description: "requeue_futex – Requeue a futex_q from one hb to another"
---

<p>requeue_futex &#8211; Requeue a futex_q from one hb to another</p>
<h2>Synopsis</h2>
<pre><code>void requeue_futex(struct futex_q *q, struct futex_hash_bucket *hb1, struct futex_hash_bucket *hb2, union futex_key *key2);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the futex_q to requeue</dl>
<p> <i>hb1</i></p>
<dl>
<dd>the source hash_bucket</dl>
<p> <i>hb2</i></p>
<dl>
<dd>the target hash_bucket</dl>
<p> <i>key2</i></p>
<dl>
<dd>the new key for the requeued futex_q</dl>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
