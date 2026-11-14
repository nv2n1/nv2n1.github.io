---
title: "set_selinuxmnt(3)"
name: "set_selinuxmnt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_selinuxmnt/"
description: "init_selinuxmnt – initialize the global variable selinux_mnt"
---

<p>init_selinuxmnt &#8211; initialize the global variable selinux_mnt </p>
<h2>Synopsis</h2>
<p> <code>static void init_selinuxmnt(void);</code> </p>
<p> <code>static void fini_selinuxmnt(void);</code> </p>
<p> <code>void set_selinuxmnt(char *</code><i>mnt</i><code>);</code></p>
<h2>Description</h2>
<p> <code>init_selinuxmnt</code>() initializes the global variable <i>selinux_mnt</i> to the selinuxfs mountpoint. </p>
<p> <code>fini_selinuxmnt</code>() deinitializes the global variable <i>selinux_mnt</i> that stores the selinuxfs mountpoint. </p>
<p> <code>set_selinuxmnt</code>() changes the selinuxfs mountpoint to <i>mnt</i>.</p>
<h2>Author</h2>
<p> This manual page has been written by Guido Trentalancia &lt;guido [at] trentalancia.com&gt;</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8),</p>
