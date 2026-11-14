---
title: "ipc_findkey(9)"
name: "ipc_findkey"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_findkey/"
---

ipc_findkey - find a key in an ipc identifier set

<h2>Synopsis</h2>

<pre><code>struct kern_ipc_perm *ipc_findkey(struct ipc_ids *ids, key_t key);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>
 

 <i>key</i>
<dl><dd>key to find</dl>

<h2>Description</h2>

Returns the locked pointer to the ipc structure if found or NULL otherwise. If key is found ipc points to the owning ipc structure 

 Called with ipc_ids.rwsem held.

<h2>Copyright</h2>


