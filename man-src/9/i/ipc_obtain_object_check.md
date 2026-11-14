---
title: "ipc_obtain_object_check(9)"
name: "ipc_obtain_object_check"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_obtain_object_check/"
description: "ipc_obtain_object_check –"
---

<p>ipc_obtain_object_check &#8211;</p>
<h2>Synopsis</h2>
<pre><code>struct kern_ipc_perm *ipc_obtain_object_check(struct ipc_ids *ids, int id);</code></pre>
<h2>Arguments</h2>
<p><i>ids</i></p>
<dl>
<dd>
<dd>ipc identifier set</dl>
<p> <i>id</i></p>
<dl>
<dd>ipc id to look for</dl>
<h2>Description</h2>
<p>Similar to <code>ipc_obtain_object_idr</code> but also checks the ipc object reference counter. </p>
<p> Call inside the RCU critical section. The ipc object is *not* locked on exit.</p>
<h2>Copyright</h2>
