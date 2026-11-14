---
title: "ipc_addid(9)"
name: "ipc_addid"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_addid/"
---

ipc_addid - add an ipc identifier

<h2>Synopsis</h2>

<pre><code>int ipc_addid(struct ipc_ids *ids, struct kern_ipc_perm *new, int size);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>
 

 <i>new</i>
<dl><dd>new ipc permission set</dl>
 

 <i>size</i>
<dl><dd>limit for the number of used ids</dl>

<h2>Description</h2>

Add an entry 'new' to the ipc ids idr. The permissions object is initialised and the first free entry is set up and the id assigned is returned. The 'new' entry is returned in a locked state on success. On failure the entry is not locked and a negative err-code is returned. 

 Called with writer ipc_ids.rwsem held.

<h2>Copyright</h2>


