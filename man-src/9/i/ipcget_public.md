---
title: "ipcget_public(9)"
name: "ipcget_public"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipcget_public/"
description: "ipcget_public – get an ipc object or create a new one"
---

<p>ipcget_public &#8211; get an ipc object or create a new one</p>
<h2>Synopsis</h2>
<pre><code>int ipcget_public(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params);</code></pre>
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
<p>This routine is called by sys_msgget, <code>sys_semget</code> and <code>sys_shmget</code> when the key is not IPC_PRIVATE. It adds a new entry if the key is not found and does some permission / security checkings if the key is found. </p>
<p> On success, the ipc id is returned.</p>
<h2>Copyright</h2>
