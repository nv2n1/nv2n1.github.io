---
title: "rpc_add_pipe_dir_object(9)"
name: "rpc_add_pipe_dir_object"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_add_pipe_dir_object/"
---

rpc_add_pipe_dir_object - associate a rpc_pipe_dir_object to a directory

<h2>Synopsis</h2>

<pre><code>int rpc_add_pipe_dir_object(struct net *net, struct rpc_pipe_dir_head *pdh, struct rpc_pipe_dir_object *pdo);</code></pre>

<h2>Arguments</h2>

<i>net</i>
<dl><dd><dd>pointer to struct net</dl>
 

 <i>pdh</i>
<dl><dd>pointer to struct rpc_pipe_dir_head</dl>
 

 <i>pdo</i>
<dl><dd>pointer to struct rpc_pipe_dir_object</dl>

<h2>Copyright</h2>


