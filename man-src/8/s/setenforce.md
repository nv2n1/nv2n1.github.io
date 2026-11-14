---
title: "setenforce(8)"
name: "setenforce"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setenforce/"
description: "setenforce – modify the mode SELinux is running in"
---

<p>setenforce &#8211; modify the mode SELinux is running in</p>
<h2>Synopsis</h2>
<p><code>setenforce</code> [<code>Enforcing</code>|<code>Permissive</code>|<code>1</code>|<code>0</code>]</p>
<h2>Description</h2>
<p>Use <code>Enforcing</code> or <code>1</code> to put SELinux in enforcing mode.<br />
 Use <code>Permissive</code> or <code>0</code> to put SELinux in permissive mode. </p>
<p> If SELinux is disabled and you want to enable it, or SELinux is enabled and you want to disable it, please see <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8).</p>
<h2>Author</h2>
<p>Dan Walsh, &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-getenforce/">getenforce</a></code>(8), <code><a href="/docs/linux/man/8-selinuxenabled/">selinuxenabled</a></code>(8) </p>
