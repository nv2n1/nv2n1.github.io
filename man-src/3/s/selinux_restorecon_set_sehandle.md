---
title: "selinux_restorecon_set_sehandle(3)"
name: "selinux_restorecon_set_sehandle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon_set_sehandle/"
description: "selinux_restorecon_set_sehandle – set a labeling handle for use by"
---

<p>selinux_restorecon_set_sehandle &#8211; set a labeling handle for use by <code></p>
<p> <a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;

#include &lt;selinux/label.h&gt;
void selinux_restorecon_set_sehandle(struct selabel_handle *handle);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon_set_sehandle</code>() sets the <i>handle</i> to be use by <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) when relabeling files. </p>
<p> <code>selinux_restorecon_set_sehandle</code>() is generally used when customised <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) parameters are required to perform relabeling operations with <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_default_handle/">selinux_restorecon_default_handle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/">selinux_restorecon_set_alt_rootpath</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) </p>
