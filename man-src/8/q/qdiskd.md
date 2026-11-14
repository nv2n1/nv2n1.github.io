---
title: "qdiskd(8)"
name: "qdiskd"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qdiskd/"
description: "qdiskd – Cluster Quorum Disk Daemon"
---

<p>qdiskd &#8211; Cluster Quorum Disk Daemon</p>
<h2>Synopsis</h2>
<p><code>qdiskd [-f] [-d] </code></p>
<h2>Description</h2>
<p>The <code>qdiskd</code> daemon talks to CMAN and provides a mechanism for determining node-fitness in a cluster environment. See <code><a href="/docs/linux/man/5-qdisk/">qdisk</a>(5)</code> for configuration information.</p>
<h2>Options</h2>
<dl>
<dt>-f</p>
<dd>Run in the foreground (do not fork / daemonize).</p>
<dt>-d</p>
<dd>Enable debug output.</p>
<dt>-Q</p>
<dd>Close stdin/out/err immediately before doing validations. This is primarily for use when being called from an init script. Using this option will stop all output, and can not be used with the -d option. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkqdisk/">mkqdisk</a>(8), <a href="/docs/linux/man/5-qdisk/">qdisk</a>(5), <a href="/docs/linux/man/5-cman/">cman</a>(5) </p>
