---
title: "getfilecon_raw(3)"
name: "getfilecon_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getfilecon_raw/"
description: "getfilecon, fgetfilecon, lgetfilecon – get SELinux security context of a file"
---

<h2 class="name">NAME</h2>
<p> getfilecon, fgetfilecon, lgetfilecon &#8211; get SELinux security context of a file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getfilecon(const char *</code><i>path</i><code>, char **</code><i>con</i><code>);</code> </p>
<p> <code>int getfilecon_raw(const char *</code><i>path</i><code>, char **</code><i>con</i><code>);</code> </p>
<p> <code>int lgetfilecon(const char *</code><i>path</i><code>, char **</code><i>con</i><code>);</code> </p>
<p> <code>int lgetfilecon_raw(const char *</code><i>path</i><code>, char **</code><i>con</i><code>);</code> </p>
<p> <code>int fgetfilecon(int fd</code><i>, char **</i><code>con</code><i>);</i> </p>
<p> <code>int fgetfilecon_raw(int fd</code><i>, char **</i><code>con</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> <code>getfilecon</code>() retrieves the context associated with the given path in the file system, the length of the context is returned. </p>
<p> <code>lgetfilecon</code>() is identical to <code>getfilecon</code>(), except in the case of a symbolic link, where the link itself is interrogated, not the file that it refers to. </p>
<p> <code>fgetfilecon</code>() is identical to <code>getfilecon</code>(), only the open file pointed to by filedes (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) is interrogated in place of path. </p>
<p> <code>getfilecon_raw</code>(), <code>lgetfilecon_raw</code>() and <code>fgetfilecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> The returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL.</p>
<h2>RETURN VALUE</h2>
<p> On success, a positive number is returned indicating the size of the extended attribute value. On failure, -1 is returned and <i>errno</i> is set appropriately. </p>
<p> If the context does not exist, or the process has no access to this attribute, <i>errno</i> is set to <code>ENODATA</code>. </p>
<p> If extended attributes are not supported by the filesystem, or are disabled, <i>errno</i> is set to <code>ENOTSUP</code>. </p>
<p> The errors documented for the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call are also applicable here.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-setfilecon/">setfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
<h2>Index</h2>
