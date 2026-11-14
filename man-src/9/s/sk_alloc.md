---
title: "sk_alloc(9)"
name: "sk_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_alloc/"
description: "sk_alloc – All socket objects are allocated here"
---

<p>sk_alloc &#8211; All socket objects are allocated here</p>
<h2>Synopsis</h2>
<pre><code>struct sock *sk_alloc(struct net *net, int family, gfp_t priority, struct proto *prot, int kern);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>the applicable net namespace</dl>
<p> <i>family</i></p>
<dl>
<dd>protocol family</dl>
<p> <i>priority</i></p>
<dl>
<dd>for allocation (<code>GFP_KERNEL</code>, <code>GFP_ATOMIC</code>, etc)</dl>
<p> <i>prot</i></p>
<dl>
<dd>struct proto associated with this new sock instance</dl>
<p> <i>kern</i></p>
<dl>
<dd>is this to be a kernel socket?</dl>
<h2>Copyright</h2>
