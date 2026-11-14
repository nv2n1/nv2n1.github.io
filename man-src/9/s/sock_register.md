---
title: "sock_register(9)"
name: "sock_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_register/"
---

sock_register - add a socket protocol handler

<h2>Synopsis</h2>

<pre><code>int sock_register(const struct net_proto_family *ops);</code></pre>

<h2>Arguments</h2>

<i>ops</i>
<dl><dd><dd>description of protocol</dl>

<h2>Description</h2>

This function is called by a protocol handler that wants to advertise its address family, and have it linked into the socket interface. The value ops-&gt;family corresponds to the socket system call protocol family.

<h2>Copyright</h2>


