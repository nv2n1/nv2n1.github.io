---
title: "lock_sock_fast(9)"
name: "lock_sock_fast"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lock_sock_fast/"
description: "lock_sock_fast – fast version of lock_sock"
---

<p>lock_sock_fast &#8211; fast version of lock_sock</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool lock_sock_fast(struct sock&nbsp;<wbr>*&nbsp;<wbr></code><i>sk</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket</dl>
<h2>Description</h2>
<p>This version should be used for very small section, where process wont block return false if fast path is taken sk_lock.slock locked, owned = 0, BH disabled return true if slow path is taken sk_lock.slock unlocked, owned = 1, BH enabled</p>
<h2>Copyright</h2>
