---
title: "ipc_check_perms(9)"
name: "ipc_check_perms"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_check_perms/"
description: "ipc_check_perms – check security and permissions for an ipc object"
---

<p>ipc_check_perms &#8211; check security and permissions for an ipc object</p>
<h2>Synopsis</h2>
<pre><code>int ipc_check_perms(struct ipc_namespace *ns, struct kern_ipc_perm *ipcp, const struct ipc_ops *ops, struct ipc_params *params);</code></pre>
<h2>Arguments</h2>
<p><i>ns</i></p>
<dl>
<dd>
<dd>ipc namespace</dl>
<p> <i>ipcp</i></p>
<dl>
<dd>ipc permission set</dl>
<p> <i>ops</i></p>
<dl>
<dd>the actual security routine to call</dl>
<p> <i>params</i></p>
<dl>
<dd>its parameters</dl>
<h2>Description</h2>
<p>This routine is called by <code>sys_msgget</code>, <code>sys_semget</code> and <code>sys_shmget</code> when the key is not IPC_PRIVATE and that key already exists in the ds IDR. </p>
<p> On success, the ipc id is returned. </p>
<p> It is called with ipc_ids.rwsem and ipcp-&gt;lock held.</p>
<h2>Copyright</h2>
