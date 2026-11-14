---
title: "selinux_restorecon_default_handle(3)"
name: "selinux_restorecon_default_handle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon_default_handle/"
description: "selinux_restorecon_default_handle – sets default parameters for"
---

<p>selinux_restorecon_default_handle &#8211; sets default parameters for <code></p>
<p> <a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;

#include &lt;selinux/label.h&gt;
struct selabel_handle *selinux_restorecon_default_handle(void);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon_default_handle</code>() sets default parameters for <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) by calling <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) with the <code>SELABEL_OPT_DIGEST</code> option only. This will enable a digest to be calculated on the currently loaded policy <code><a href="/docs/linux/man/5-file_contexts/">file_contexts</a></code>(5) set of files as described in the <code>NOTES</code> section of <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3). </p>
<p> Calling <code>selinux_restorecon_default_handle</code>() is optional, however if used then <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3) should be called with the returned handle to set this for use by <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3). </p>
<p> <code>selinux_restorecon_default_handle</code>() is optional as <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) will automatically call this and <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3) provided a handle has not already been set, for example by <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3) to set customised <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) parameters.</p>
<h2>Return Value</h2>
<p>A non-NULL handle value is returned on success. On error, NULL is returned and <i>errno</i> is set appropriately.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/">selinux_restorecon_set_alt_rootpath</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) </p>
