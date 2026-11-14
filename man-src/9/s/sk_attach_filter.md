---
title: "sk_attach_filter(9)"
name: "sk_attach_filter"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_attach_filter/"
---

sk_attach_filter - attach a socket filter

<h2>Synopsis</h2>

<pre><code>int sk_attach_filter(struct sock_fprog *fprog, struct sock *sk);</code></pre>

<h2>Arguments</h2>

<i>fprog</i>
<dl><dd><dd>the filter program</dl>
 

 <i>sk</i>
<dl><dd>the socket to use</dl>

<h2>Description</h2>

Attach the user's filter code. We first run some sanity checks on it to make sure it does not explode on us later. If an error occurs or there is insufficient memory for the filter a negative errno code is returned. On success the return is zero.

<h2>Copyright</h2>


