---
title: "selinux_restorecon_set_exclude_list(3)"
name: "selinux_restorecon_set_exclude_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon_set_exclude_list/"
description: "selinux_restorecon_set_exclude_list – set list of directories to be excluded from relabeling."
---

<p>selinux_restorecon_set_exclude_list &#8211; set list of directories to be excluded from relabeling.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;
void selinux_restorecon_set_exclude_list(const char **exclude_list);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon_set_exclude_list</code>() passes to <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) a pointer containing a <code>NULL</code> terminated list of one or more directories that are not to be relabeled in <i>exclude_list</i>. </p>
<p> <code>selinux_restorecon_set_exclude_list</code>() must be called prior to <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_default_handle/">selinux_restorecon_default_handle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/">selinux_restorecon_set_alt_rootpath</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) </p>
