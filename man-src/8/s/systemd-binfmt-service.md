---
title: "systemd-binfmt-service(8)"
name: "systemd-binfmt-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-binfmt-service/"
description: "systemd-binfmt.service, systemd-binfmt – Configure additional binary formats for executables at boot"
---

<p>systemd-binfmt.service, systemd-binfmt &#8211; Configure additional binary formats for executables at boot</p>
<h2>Synopsis</h2>
<p>systemd-binfmt.service </p>
<p> /lib/systemd/systemd-binfmt</p>
<h2>Description</h2>
<p>systemd-binfmt.service is an early boot service that registers additional binary formats for executables in the kernel. </p>
<p> See <code><a href="/docs/linux/man/5-binfmt-d/">binfmt.d</a></code>(5) for information about the configuration of this service.</p>
<h2>Options</h2>
<p><code>&#8211;unregister</code></p>
<dl>
<dd>If passed, instead of registering configured binary formats in the kernel, the reverse operation is executed: all currently registered binary formats are unregistered from the kernel.</dl>
<p> <code>&#8211;cat-config</code></p>
<dl>
<dd>Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dd>Do not pipe output into a pager.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-binfmt-d/">binfmt.d</a></code>(5), <code><a href="/docs/linux/man/8-wine/">wine</a></code>(8) </p>
