---
title: "selinux_restorecon_set_alt_rootpath(3)"
name: "selinux_restorecon_set_alt_rootpath"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/"
description: "selinux_restorecon_set_alt_rootpath – set an alternate rootpath."
---

<p>selinux_restorecon_set_alt_rootpath &#8211; set an alternate rootpath.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;
int selinux_restorecon_set_alt_rootpath(const char *alt_rootpath);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon_set_alt_rootpath</code>() passes to <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) a pointer containing an alternate rootpath <i>alt_rootpath</i>. </p>
<p> <code>selinux_restorecon_set_alt_rootpath</code>() must be called prior to <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_default_handle/">selinux_restorecon_default_handle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) </p>
