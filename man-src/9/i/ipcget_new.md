---
title: "ipcget_new(9)"
name: "ipcget_new"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipcget_new/"
description: "ipcget_new – create a new ipc object"
---

<p>ipcget_new &#8211; create a new ipc object</p>
<h2>Synopsis</h2>
<pre><code>int ipcget_new(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params);</code></pre>
<h2>Arguments</h2>
<p><i>ns</i></p>
<dl>
<dd>
<dd>ipc namespace</dl>
<p> <i>ids</i></p>
<dl>
<dd>ipc identifier set</dl>
<p> <i>ops</i></p>
<dl>
<dd>the actual creation routine to call</dl>
<p> <i>params</i></p>
<dl>
<dd>its parameters</dl>
<h2>Description</h2>
<p>This routine is called by sys_msgget, <code>sys_semget</code> and <code>sys_shmget</code> when the key is IPC_PRIVATE.</p>
<h2>Copyright</h2>
