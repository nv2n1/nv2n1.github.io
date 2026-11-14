---
title: "mutex_is_locked(9)"
name: "mutex_is_locked"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_is_locked/"
description: "mutex_is_locked – is the mutex locked"
---

<p>mutex_is_locked &#8211; is the mutex locked</p>
<h2>Synopsis</h2>
<pre><code>int mutex_is_locked(struct mutex *lock);</code></pre>
<h2>Arguments</h2>
<p><i>lock</i></p>
<dl>
<dd>
<dd>the mutex to be queried</dl>
<h2>Description</h2>
<p>Returns 1 if the mutex is locked, 0 if unlocked.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
