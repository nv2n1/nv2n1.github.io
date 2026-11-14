---
title: "ipc_lock(9)"
name: "ipc_lock"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_lock/"
---

ipc_lock - lock an ipc structure without rwsem held

<h2>Synopsis</h2>

<pre><code>struct kern_ipc_perm *ipc_lock(struct ipc_ids *ids, int id);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>
 

 <i>id</i>
<dl><dd>ipc id to look for</dl>

<h2>Description</h2>

Look for an id in the ipc ids idr and lock the associated ipc object. 

 The ipc object is locked on successful exit.

<h2>Copyright</h2>


