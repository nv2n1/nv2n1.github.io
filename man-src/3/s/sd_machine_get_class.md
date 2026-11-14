---
title: "sd_machine_get_class(3)"
name: "sd_machine_get_class"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_machine_get_class/"
description: "sd_machine_get_class, sd_machine_get_ifindices – Determine the class and network interface indices of a locally running virtual machine or container."
---

<p>sd_machine_get_class, sd_machine_get_ifindices &#8211; Determine the class and network interface indices of a locally running virtual machine or container.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_machine_get_class(const char *machine, char *class);

int sd_machine_get_ifindices(const char *machine, int **ifindices);</code></pre>
<h2>Description</h2>
<p><code>sd_machine_get_class()</code></p>
<dd>may be used to determine the class of a locally running virtual machine or container that is registered with <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8). The string returned is either &quot;vm&quot; or &quot;container&quot;. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_machine_get_ifindices()</code> may be used to determine the numeric indices of the network interfaces on the host that are pointing towards the specified locally running virtual machine or container that is registered with <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8). The returned array needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use.</p>
<h2>Return Value</h2>
<p>On success, these calls return 0 or a positive integer. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_machine_get_class()</code> and <code>sd_machine_get_ifindices()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), <code><a href="/docs/linux/man/3-sd_pid_get_machine_name/">sd_pid_get_machine_name</a></code>(3) </p>
