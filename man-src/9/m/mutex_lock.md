---
title: "mutex_lock(9)"
name: "mutex_lock"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_lock/"
description: "mutex_lock – acquire the mutex"
---

<p>mutex_lock &#8211; acquire the mutex</p>
<h2>Synopsis</h2>
<pre><code>void __sched mutex_lock(struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be acquired</dl>
<h2>Description</h2>
<p>Lock the mutex exclusively for this task. If the mutex is not available right now, it will sleep until it can get it. </p>
<p> The mutex must later on be released by the same task that acquired it. Recursive locking is not allowed. The task may not exit without first unlocking the mutex. Also, kernel memory where the mutex resides must not be freed with the mutex still locked. The mutex must first be initialized (or statically defined) before it can be locked. <code>memset</code>-ing the mutex to 0 is not allowed. </p>
<p> ( The CONFIG_DEBUG_MUTEXES .config option turns on debugging checks that will enforce the restrictions and will also do deadlock debugging. ) </p>
<p> This function is similar to (but not equivalent to) <code>down</code>.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
