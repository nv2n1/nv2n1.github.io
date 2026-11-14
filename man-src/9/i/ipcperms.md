---
title: "ipcperms(9)"
name: "ipcperms"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipcperms/"
---

ipcperms - check ipc permissions

<h2>Synopsis</h2>

<pre><code>int ipcperms(struct ipc_namespace *ns, struct kern_ipc_perm *ipcp, short flag);</code></pre>

<h2>Arguments</h2>

<i>ns</i>
<dl><dd><dd>ipc namespace</dl>
 

 <i>ipcp</i>
<dl><dd>ipc permission set</dl>
 

 <i>flag</i>
<dl><dd>desired permission set</dl>

<h2>Description</h2>

Check user, group, other permissions for access to ipc resources. return 0 if allowed 

 <i>flag</i> will most probably be 0 or S_...UGO from &lt;linux/stat.h&gt;

<h2>Copyright</h2>


