---
title: "atomic_dec_and_mutex_lock(9)"
name: "atomic_dec_and_mutex_lock"
section: "9"
letter: "a"
url: "/docs/linux/man/9-atomic_dec_and_mutex_lock/"
description: "atomic_dec_and_mutex_lock – return holding mutex if we dec to 0"
---

<p>atomic_dec_and_mutex_lock &#8211; return holding mutex if we dec to 0</p>
<h2>Synopsis</h2>
<pre><code>int atomic_dec_and_mutex_lock(atomic_t *cnt, struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>cnt</i></p>
<dl>
<dd>
<dd>the atomic which we are to dec</dl>
<p> <i>lock</i></p>
<dl>
<dd>the mutex to return holding if we dec to 0</dl>
<h2>Description</h2>
<p>return true and hold lock if we dec to 0, return false otherwise</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
