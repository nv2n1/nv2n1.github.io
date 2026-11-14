---
title: "mutex_init(9)"
name: "mutex_init"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mutex_init/"
description: "mutex_init – initialize the mutex"
---

<p>mutex_init &#8211; initialize the mutex</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mutex_init(</code><i>mutex</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>mutex</i></p>
<dl>
<dd>
<dd>the mutex to be initialized</dl>
<h2>Description</h2>
<p>Initialize the mutex to unlocked state. </p>
<p> It is not allowed to initialize an already locked mutex.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
