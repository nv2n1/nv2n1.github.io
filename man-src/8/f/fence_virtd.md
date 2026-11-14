---
title: "fence_virtd(8)"
name: "fence_virtd"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_virtd/"
description: "fence_virtd – Fencing host for virtual machines"
---

<p>fence_virtd &#8211; Fencing host for virtual machines </p>
<h2>Description</h2>
<p>fence_virtd is a host daemon designed to route fencing requests for virtual machines. Fence_virt and fence_xvm talk to fence_virtd, which supports multiple backend plugins, including:<br />
&nbsp;<wbr>&#8211; libvirt for single-node operation<br />
&nbsp;<wbr>&#8211; Cluster Checkpoints when using Linux-cluster release 3.0.0 or later<br />
&nbsp;<wbr>&#8211; libvirt-qpid for multi-node, non-cluster operation For compatibility, fence_xvm from linux-cluster release 2 may talk to fence_virtd. fence_virtd accepts a few options on the command line, but most options are read from fence_virt.conf. </p>
<h2>Parameters</h2>
<dl>
<dt><code>-d</code></p>
<dd>Specify debug level, e.g. &quot;-d99&quot; </p>
<dt><code>-c</code></p>
<dd>Interactively prompt user for configuration information </p>
<dt><code>-f</code></p>
<dd>Specify an alternate configuration file instead of /etc/fence_virt.conf </p>
<dt><code>-F</code></p>
<dd>Do not fork into background after starting (overrides any setting in fence_virt.conf) </p>
<dt><code>-w</code></p>
<dd>Wait for backend to be available (overrides any setting in fence_virt.conf) </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence_virt/">fence_virt</a>(8), <a href="/docs/linux/man/8-fence_xvm/">fence_xvm</a>(8), <a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/5-fence_virt-conf/">fence_virt.conf</a>(5) </p>
