---
title: "ipc_rmid(9)"
name: "ipc_rmid"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_rmid/"
---

ipc_rmid - remove an ipc identifier

<h2>Synopsis</h2>

<pre><code>void ipc_rmid(struct ipc_ids *ids, struct kern_ipc_perm *ipcp);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>
 

 <i>ipcp</i>
<dl><dd>ipc perm structure containing the identifier to remove</dl>

<h2>Description</h2>

ipc_ids.rwsem (as a writer) and the spinlock for this ID are held before this function is called, and remain locked on the exit.

<h2>Copyright</h2>


