---
title: "rpc_queue_upcall(9)"
name: "rpc_queue_upcall"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_queue_upcall/"
description: "rpc_queue_upcall – queue an upcall message to userspace"
---

<p>rpc_queue_upcall &#8211; queue an upcall message to userspace</p>
<h2>Synopsis</h2>
<pre><code>int rpc_queue_upcall(struct rpc_pipe *pipe, struct rpc_pipe_msg *msg);</code></pre>
<h2>Arguments</h2>
<p><i>pipe</i></p>
<dl>
<dd>
<dd>upcall pipe on which to queue given message</dl>
<p> <i>msg</i></p>
<dl>
<dd>message to queue</dl>
<h2>Description</h2>
<p>Call with an <i>inode</i> created by <code>rpc_mkpipe</code> to queue an upcall. A userspace process may then later read the upcall by performing a read on an open file for this inode. It is up to the caller to initialize the fields of <i>msg</i> (other than <i>msg</i>-&gt;list) appropriately.</p>
<h2>Copyright</h2>
