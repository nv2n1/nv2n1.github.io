---
title: "rpc_malloc(9)"
name: "rpc_malloc"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_malloc/"
---

rpc_malloc - allocate RPC buffer resources

<h2>Synopsis</h2>

<pre><code>int rpc_malloc(struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>RPC task</dl>

<h2>Description</h2>

A single memory region is allocated, which is split between the RPC call and RPC reply that this task is being used for. When this RPC is retired, the memory is released by calling rpc_free. 

 To prevent rpciod from hanging, this allocator never sleeps, returning -ENOMEM and suppressing warning if the request cannot be serviced immediately. The caller can arrange to sleep in a way that is safe for rpciod. 

 Most requests are 'small' (under 2KiB) and can be serviced from a mempool, ensuring that NFS reads and writes can always proceed, and that there is good locality of reference for these buffers. 

 In order to avoid memory starvation triggering more writebacks of NFS requests, we avoid using GFP_KERNEL.

<h2>Copyright</h2>


