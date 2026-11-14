---
title: "ipc_obtain_object_idr(9)"
name: "ipc_obtain_object_idr"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_obtain_object_idr/"
---

ipc_obtain_object_idr -

<h2>Synopsis</h2>

<pre><code>struct kern_ipc_perm *ipc_obtain_object_idr(struct ipc_ids *ids, int id);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>
 

 <i>id</i>
<dl><dd>ipc id to look for</dl>

<h2>Description</h2>

Look for an id in the ipc ids idr and return associated ipc object. 

 Call inside the RCU critical section. The ipc object is *not* locked on exit.

<h2>Copyright</h2>


