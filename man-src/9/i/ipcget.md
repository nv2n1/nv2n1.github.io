---
title: "ipcget(9)"
name: "ipcget"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipcget/"
description: "ipcget – Common sys_*get code"
---

<p>ipcget &#8211; Common sys_*<code>get</code> code</p>
<h2>Synopsis</h2>
<pre><code>int ipcget(struct ipc_namespace *ns, struct ipc_ids *ids, const struct ipc_ops *ops, struct ipc_params *params);</code></pre>
<h2>Arguments</h2>
<p><i>ns</i></p>
<dl>
<dd>
<dd>namespace</dl>
<p> <i>ids</i></p>
<dl>
<dd>ipc identifier set</dl>
<p> <i>ops</i></p>
<dl>
<dd>operations to be called on ipc object creation, permission checks and further checks</dl>
<p> <i>params</i></p>
<dl>
<dd>the parameters needed by the previous operations.</dl>
<h2>Description</h2>
<p>Common routine called by <code>sys_msgget</code>, <code>sys_semget</code> and <code>sys_shmget</code>.</p>
<h2>Copyright</h2>
