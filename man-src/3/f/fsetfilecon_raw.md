---
title: "fsetfilecon_raw(3)"
name: "fsetfilecon_raw"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fsetfilecon_raw/"
description: "setfilecon, fsetfilecon, lsetfilecon – set SELinux security context of a file"
---

<h2 class="name">NAME</h2>
<p> setfilecon, fsetfilecon, lsetfilecon &#8211; set SELinux security context of a file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int setfilecon(const char *</code><i>path</i><code>, char *</code><i>con</i><code>);</code> </p>
<p> <code>int setfilecon_raw(const char *</code><i>path</i><code>, char *</code><i>con</i><code>);</code> </p>
<p> <code>int lsetfilecon(const char *</code><i>path</i><code>, char *</code><i>con</i><code>);</code> </p>
<p> <code>int lsetfilecon_raw(const char *</code><i>path</i><code>, char *</code><i>con</i><code>);</code> </p>
<p> <code>int fsetfilecon(int fd</code><i>, char *</i><code>con</code><i>);</i> </p>
<p> <code>int fsetfilecon_raw(int fd</code><i>, char *</i><code>con</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> <code>setfilecon</code>() sets the security context of the file system object. </p>
<p> <code>lsetfilecon</code>() is identical to setfilecon, except in the case of a symbolic link, where the link itself has it&#8217;s context set, not the file that it refers to. </p>
<p> <code>fsetfilecon</code>() is identical to setfilecon, only the open file pointed to by filedes (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) has it&#8217;s context set in place of path. </p>
<p> <code>setfilecon_raw</code>(), <code>lsetfilecon_raw</code>(), and <code>fsetfilecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On failure, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If there is insufficient space remaining to store the extended attribute, <i>errno</i> is set to either <code>ENOSPC</code>, or <code>EDQUOT</code> if quota enforcement was the cause. </p>
<p> If extended attributes are not supported by the filesystem, or are disabled, <i>errno</i> is set to <code>ENOTSUP</code>. </p>
<p> The errors documented for the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call are also applicable here.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-selinux/">selinux</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getfilecon/">getfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
<h2>Index</h2>
