---
title: "ipc_init_ids(9)"
name: "ipc_init_ids"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_init_ids/"
---

ipc_init_ids - initialise ipc identifiers

<h2>Synopsis</h2>

<pre><code>void ipc_init_ids(struct ipc_ids *ids);</code></pre>

<h2>Arguments</h2>

<i>ids</i>
<dl><dd><dd>ipc identifier set</dl>

<h2>Description</h2>

Set up the sequence range to use for the ipc identifier range (limited below IPCMNI) then initialise the ids idr.

<h2>Copyright</h2>


