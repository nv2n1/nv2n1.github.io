---
title: "is_context_customizable(3)"
name: "is_context_customizable"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_context_customizable/"
description: "is_context_customizable – check whether SELinux context type is customizable by the administrator"
---

<h2 class="name">NAME</h2>
<p> is_context_customizable &#8211; check whether SELinux context type is customizable by the administrator </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int is_context_customizable(char *</code><i>scon</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This function checks whether the type of scon is in the <i>/etc/selinux/{SELINUXTYPE}/context/customizable_types</i> file. A customizable type is a file context type that administrators set on files, usually to allow certain domains to share the file content. restorecon and setfiles, by default, leave these context in place.</p>
<h2>RETURN VALUE</h2>
<p> Returns 1 if security context is customizable or 0 if it is not. Returns -1 on error.</p>
<h2>FILE</h2>
<p> <i>/etc/selinux/{SELINUXTYPE}/context/customizable_types</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
