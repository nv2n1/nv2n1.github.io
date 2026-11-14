---
title: "xprt_register_transport(9)"
name: "xprt_register_transport"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_register_transport/"
---

xprt_register_transport - register a transport implementation

<h2>Synopsis</h2>

<pre><code>int xprt_register_transport(struct xprt_class *transport);</code></pre>

<h2>Arguments</h2>

<i>transport</i>
<dl><dd><dd>transport to register</dl>

<h2>Description</h2>

If a transport implementation is loaded as a kernel module, it can call this interface to make itself known to the RPC client.

<h2>Return</h2>

0: transport successfully registered -EEXIST: transport already registered -EINVAL: transport module being unloaded

<h2>Copyright</h2>


