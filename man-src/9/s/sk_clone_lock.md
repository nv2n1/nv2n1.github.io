---
title: "sk_clone_lock(9)"
name: "sk_clone_lock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_clone_lock/"
description: "sk_clone_lock – clone a socket, and lock its clone"
---

<p>sk_clone_lock &#8211; clone a socket, and lock its clone</p>
<h2>Synopsis</h2>
<pre><code>struct sock *sk_clone_lock(const struct sock *sk, const gfp_t priority);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>the socket to clone</dl>
<p> <i>priority</i></p>
<dl>
<dd>for allocation (<code>GFP_KERNEL</code>, <code>GFP_ATOMIC</code>, etc)</dl>
<h2>Description</h2>
<p>Caller must unlock socket even in error path (bh_unlock_sock(newsk))</p>
<h2>Copyright</h2>
