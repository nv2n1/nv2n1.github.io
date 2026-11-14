---
title: "mutex_lock_interruptible(9)"
name: "mutex_lock_interruptible"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_lock_interruptible/"
description: "mutex_lock_interruptible – acquire the mutex, interruptible"
---

<p>mutex_lock_interruptible &#8211; acquire the mutex, interruptible</p>
<h2>Synopsis</h2>
<pre><code>int __sched mutex_lock_interruptible(struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be acquired</dl>
<h2>Description</h2>
<p>Lock the mutex like <code>mutex_lock</code>, and return 0 if the mutex has been acquired or sleep until the mutex becomes available. If a signal arrives while waiting for the lock then this function returns -EINTR. </p>
<p> This function is similar to (but not equivalent to) <code>down_interruptible</code>.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
