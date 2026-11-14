---
title: "ww_mutex_unlock(9)"
name: "ww_mutex_unlock"
section: "9"
letter: "w"
url: "/docs/linux/man/9-ww_mutex_unlock/"
description: "ww_mutex_unlock – release the w/w mutex"
---

<p>ww_mutex_unlock &#8211; release the w/w mutex</p>
<h2>Synopsis</h2>
<pre><code>void __sched ww_mutex_unlock(struct ww_mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be released</dl>
<h2>Description</h2>
<p>Unlock a mutex that has been locked by this task previously with any of the ww_mutex_lock* functions (with or without an acquire context). It is forbidden to release the locks after releasing the acquire context. </p>
<p> This function must not be used in interrupt context. Unlocking of a unlocked mutex is not allowed.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
