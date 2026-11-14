---
title: "kernel_to_ipc64_perm(9)"
name: "kernel_to_ipc64_perm"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kernel_to_ipc64_perm/"
---

kernel_to_ipc64_perm - convert kernel ipc permissions to user

<h2>Synopsis</h2>

<pre><code>void kernel_to_ipc64_perm(struct kern_ipc_perm *in, struct ipc64_perm *out);</code></pre>

<h2>Arguments</h2>

<i>in</i>
<dl><dd><dd>kernel permissions</dl>
 

 <i>out</i>
<dl><dd>new style ipc permissions</dl>

<h2>Description</h2>

Turn the kernel object <i>in</i> into a set of permissions descriptions for returning to userspace (<i>out</i>).

<h2>Copyright</h2>


