---
title: "sk_set_memalloc(9)"
name: "sk_set_memalloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_set_memalloc/"
description: "sk_set_memalloc – sets SOCK_MEMALLOC"
---

<p>sk_set_memalloc &#8211; sets <code>SOCK_MEMALLOC</code></p>
<h2>Synopsis</h2>
<pre><code>void sk_set_memalloc(struct sock *sk);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket to set it on</dl>
<h2>Description</h2>
<p>Set <code>SOCK_MEMALLOC</code> on a socket for access to emergency reserves. It&#8217;s the responsibility of the admin to adjust min_free_kbytes to meet the requirements</p>
<h2>Copyright</h2>
