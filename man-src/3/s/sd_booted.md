---
title: "sd_booted(3)"
name: "sd_booted"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_booted/"
description: "sd_booted – Test whether the system is running the systemd init system"
---

<p>sd_booted &#8211; Test whether the system is running the systemd init system</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;

int sd_booted(void);</code></pre>
<h2>Description</h2>
<p><code>sd_booted()</code></p>
<dd>checks whether the system was booted up using the systemd init system.</p>
<h2>Return Value</h2>
<p>On failure, this call returns a negative errno-style error code. If the system was booted up with systemd as init system, this call returns a positive return value, zero otherwise.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. </p>
<p> Internally, this function checks whether the directory /run/systemd/system/ exists. A simple check like this can also be implemented trivially in shell or any other language.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3) </p>
