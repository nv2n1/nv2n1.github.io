---
title: "unlock_sock_fast(9)"
name: "unlock_sock_fast"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unlock_sock_fast/"
description: "unlock_sock_fast – complement of lock_sock_fast"
---

<p>unlock_sock_fast &#8211; complement of lock_sock_fast</p>
<h2>Synopsis</h2>
<pre><code>void unlock_sock_fast(struct sock *sk, bool slow);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket</dl>
<p> <i>slow</i></p>
<dl>
<dd>slow mode</dl>
<h2>Description</h2>
<p>fast unlock socket for user context. If slow mode is on, we call regular <code>release_sock</code></p>
<h2>Copyright</h2>
