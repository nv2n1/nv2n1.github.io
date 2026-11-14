---
title: "sk_state_load(9)"
name: "sk_state_load"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_state_load/"
description: "sk_state_load – read sk->sk_state for lockless contexts"
---

<p>sk_state_load &#8211; read sk-&gt;sk_state for lockless contexts</p>
<h2>Synopsis</h2>
<pre><code>int sk_state_load(const struct sock *sk);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket pointer</dl>
<h2>Description</h2>
<p>Paired with <code>sk_state_store</code>. Used in places we do not hold socket lock : <code>tcp_diag_get_info</code>, <code>tcp_get_info</code>, <code>tcp_poll</code>, <code>get_tcp4_sock</code> &#8230;</p>
<h2>Copyright</h2>
