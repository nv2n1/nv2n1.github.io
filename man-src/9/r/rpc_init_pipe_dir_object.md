---
title: "rpc_init_pipe_dir_object(9)"
name: "rpc_init_pipe_dir_object"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_init_pipe_dir_object/"
---

rpc_init_pipe_dir_object - initialise a struct rpc_pipe_dir_object

<h2>Synopsis</h2>

<pre><code>void rpc_init_pipe_dir_object(struct rpc_pipe_dir_object *pdo, const struct rpc_pipe_dir_object_ops *pdo_ops, void *pdo_data);</code></pre>

<h2>Arguments</h2>

<i>pdo</i>
<dl><dd><dd>pointer to struct rpc_pipe_dir_object</dl>
 

 <i>pdo_ops</i>
<dl><dd>pointer to const struct rpc_pipe_dir_object_ops</dl>
 

 <i>pdo_data</i>
<dl><dd>pointer to caller-defined data</dl>

<h2>Copyright</h2>


