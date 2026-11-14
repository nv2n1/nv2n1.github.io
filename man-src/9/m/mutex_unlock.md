---
title: "mutex_unlock(9)"
name: "mutex_unlock"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_unlock/"
description: "mutex_unlock – release the mutex"
---

<p>mutex_unlock &#8211; release the mutex</p>
<h2>Synopsis</h2>
<pre><code>void __sched mutex_unlock(struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be released</dl>
<h2>Description</h2>
<p>Unlock a mutex that has been locked by this task previously. </p>
<p> This function must not be used in interrupt context. Unlocking of a not locked mutex is not allowed. </p>
<p> This function is similar to (but not equivalent to) <code>up</code>.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
