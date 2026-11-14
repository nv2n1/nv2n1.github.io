---
title: "is_selinux_enabled(3)"
name: "is_selinux_enabled"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_selinux_enabled/"
description: "is_selinux_enabled – check whether SELinux is enabled"
---

<h2 class="name">NAME</h2>
<p> is_selinux_enabled &#8211; check whether SELinux is enabled </p>
<h2 class="name">NAME</h2>
<p> is_selinux_mls_enabled &#8211; check whether SELinux is enabled for (Multi Level Security) MLS </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int is_selinux_enabled();</code> </p>
<p> <code>int is_selinux_mls_enabled();</code></p>
<h2>DESCRIPTION</h2>
<p> <code>is_selinux_enabled</code>() returns 1 if SELinux is running or 0 if it is not. On error, -1 is returned. </p>
<p> <code>is_selinux_mls_enabled</code>() returns 1 if SELinux is capable of running in MLS mode or 0 if it is not. To determine the policy in use on the system, use <code><a href="/docs/linux/man/3-selinux_getpolicytype/">selinux_getpolicytype</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
