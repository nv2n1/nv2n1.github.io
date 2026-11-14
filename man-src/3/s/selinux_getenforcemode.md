---
title: "selinux_getenforcemode(3)"
name: "selinux_getenforcemode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_getenforcemode/"
description: "selinux_getenforcemode – get the enforcing state of SELinux"
---

<p>selinux_getenforcemode &#8211; get the enforcing state of SELinux</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_getenforcemode(int *enforce);</code></pre>
<h2>Description</h2>
<p><code>selinux_getenforcemode</code>() Reads the contents of the <i>/etc/selinux/config</i> file to determine how the system was setup to run SELinux. </p>
<p> Sets the value of <i>enforce</i> to 1 if SELinux should be run in enforcing mode. Sets the value of <i>enforce</i> to 0 if SELinux should be run in permissive mode. Sets the value of <i>enforce</i> to -1 if SELinux should be disabled.</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On failure, -1 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
