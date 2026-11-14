---
title: "futex_top_waiter(9)"
name: "futex_top_waiter"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_top_waiter/"
description: "futex_top_waiter – Return the highest priority waiter on a futex"
---

<p>futex_top_waiter &#8211; Return the highest priority waiter on a futex</p>
<h2>Synopsis</h2>
<pre><code>struct futex_q *futex_top_waiter(struct futex_hash_bucket *hb, union futex_key *key);</code></pre>
<h2>Arguments</h2>
<p><i>hb</i></p>
<dl>
<dd>
<dd>the hash bucket the futex_q&#8217;s reside in</dl>
<p> <i>key</i></p>
<dl>
<dd>the futex key (to distinguish it from other futex futex_q&#8217;s)</dl>
<h2>Description</h2>
<p>Must be called with the hb lock held.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
