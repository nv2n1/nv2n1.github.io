---
title: "sk_state_store(9)"
name: "sk_state_store"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_state_store/"
description: "sk_state_store – update sk->sk_state"
---

<p>sk_state_store &#8211; update sk-&gt;sk_state</p>
<h2>Synopsis</h2>
<pre><code>void sk_state_store(struct sock *sk, int newstate);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket pointer</dl>
<p> <i>newstate</i></p>
<dl>
<dd>new state</dl>
<h2>Description</h2>
<p>Paired with <code>sk_state_load</code>. Should be used in contexts where state change might impact lockless readers.</p>
<h2>Copyright</h2>
