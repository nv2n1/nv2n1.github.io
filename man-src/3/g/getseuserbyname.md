---
title: "getseuserbyname(3)"
name: "getseuserbyname"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getseuserbyname/"
description: "getseuserbyname – get SELinux username and level for a given Linux username"
---

<h2 class="name">NAME</h2>
<p> getseuserbyname &#8211; get SELinux username and level for a given Linux username </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getseuserbyname(const char *</code><i>linuxuser</i><code>, char **</code><i>selinuxuser</i><code>, char **</code><i>level</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getseuserbyname</code>() retrieves the SELinux username and security level associated with a given Linux username. The SELinux username and security level can then be passed to other libselinux functions such as <code><a href="/docs/linux/man/3-get_ordered_context_list_with_level/">get_ordered_context_list_with_level</a></code>(3) and <code><a href="/docs/linux/man/3-get_default_context_with_level/">get_default_context_with_level</a></code>(3). </p>
<p> The returned SELinux username and level should be freed by the caller using free.</p>
<h2>RETURN VALUE</h2>
<p> On success, 0 is returned. On failure, -1 is returned and <i>errno</i> is set appropriately. </p>
<p> The errors documented for the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call are also applicable here.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
