---
title: "rpc_find_or_alloc_pipe_dir_object(9)"
name: "rpc_find_or_alloc_pipe_dir_object"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_find_or_alloc_pipe_dir_object/"
description: "rpc_find_or_alloc_pipe_dir_object –"
---

<p>rpc_find_or_alloc_pipe_dir_object &#8211;</p>
<h2>Synopsis</h2>
<pre><code>struct rpc_pipe_dir_object *rpc_find_or_alloc_pipe_dir_object(struct net *net, struct rpc_pipe_dir_head *pdh, int (*match)(struct rpc_pipe_dir_object *, void *), struct rpc_pipe_dir_object *(*alloc)(void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>pointer to struct net</dl>
<p> <i>pdh</i></p>
<dl>
<dd>pointer to struct rpc_pipe_dir_head</dl>
<p> <i>match</i></p>
<dl>
<dd>match struct rpc_pipe_dir_object to data</dl>
<p> <i>alloc</i></p>
<dl>
<dd>allocate a new struct rpc_pipe_dir_object</dl>
<p> <i>data</i></p>
<dl>
<dd>user defined data for <code>match</code> and <code>alloc</code></dl>
<h2>Copyright</h2>
