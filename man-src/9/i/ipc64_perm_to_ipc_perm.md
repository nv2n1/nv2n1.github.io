---
title: "ipc64_perm_to_ipc_perm(9)"
name: "ipc64_perm_to_ipc_perm"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc64_perm_to_ipc_perm/"
---

ipc64_perm_to_ipc_perm - convert new ipc permissions to old

<h2>Synopsis</h2>

<pre><code>void ipc64_perm_to_ipc_perm(struct ipc64_perm *in, struct ipc_perm *out);</code></pre>

<h2>Arguments</h2>

<i>in</i>
<dl><dd><dd>new style ipc permissions</dl>
 

 <i>out</i>
<dl><dd>old style ipc permissions</dl>

<h2>Description</h2>

Turn the new style permissions object <i>in</i> into a compatibility object and store it into the <i>out</i> pointer.

<h2>Copyright</h2>


