---
title: "mutex_trylock(9)"
name: "mutex_trylock"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_trylock/"
description: "mutex_trylock – try to acquire the mutex, without waiting"
---

<p>mutex_trylock &#8211; try to acquire the mutex, without waiting</p>
<h2>Synopsis</h2>
<pre><code>int __sched mutex_trylock(struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be acquired</dl>
<h2>Description</h2>
<p>Try to acquire the mutex atomically. Returns 1 if the mutex has been acquired successfully, and 0 on contention.</p>
<h2>Note</h2>
<p>this function follows the <code>spin_trylock</code> convention, so it is negated from the <code>down_trylock</code> return values! Be careful about this when converting semaphore users to mutexes. </p>
<p> This function must not be used in interrupt context. The mutex must be released by the same task that acquired it.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
