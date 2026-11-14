---
title: "rpc_unlink(9)"
name: "rpc_unlink"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_unlink/"
---

rpc_unlink - remove a pipe

<h2>Synopsis</h2>

<pre><code>int rpc_unlink(struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>dentry for the pipe, as returned from rpc_mkpipe</dl>

<h2>Description</h2>

After this call, lookups will no longer find the pipe, and any attempts to read or write using preexisting opens of the pipe will return -EPIPE.

<h2>Copyright</h2>


