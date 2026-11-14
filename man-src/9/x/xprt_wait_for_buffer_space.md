---
title: "xprt_wait_for_buffer_space(9)"
name: "xprt_wait_for_buffer_space"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_wait_for_buffer_space/"
description: "xprt_wait_for_buffer_space – wait for transport output buffer to clear"
---

<p>xprt_wait_for_buffer_space &#8211; wait for transport output buffer to clear</p>
<h2>Synopsis</h2>
<pre><code>void xprt_wait_for_buffer_space(struct rpc_task *task, rpc_action action);</code></pre>
<h2>Arguments</h2>
<p><i>task</i></p>
<dl>
<dd>
<dd>task to be put to sleep</dl>
<p> <i>action</i></p>
<dl>
<dd>function pointer to be executed after wait</dl>
<h2>Description</h2>
<p>Note that we only set the timer for the case of <code>RPC_IS_SOFT</code>, since we don&#8217;t in general want to force a socket disconnection due to an incomplete RPC call transmission.</p>
<h2>Copyright</h2>
