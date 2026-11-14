---
title: "ipc_get_maxid(9)"
name: "ipc_get_maxid"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_get_maxid/"
---

ipc_get_maxid - get the last assigned id

<h2>Synopsis</h2>

<pre><code>int ipc_get_maxid(struct ipc_ids *ids);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>

<h2>Description</h2>

Called with ipc_ids.rwsem held.

<h2>Copyright</h2>


