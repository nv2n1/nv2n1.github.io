---
title: "cmirrord(8)"
name: "cmirrord"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cmirrord/"
description: "cmirrord — cluster mirror log daemon"
---

<p>cmirrord &#8212; cluster mirror log daemon </p>
<h2>Synopsis</h2>
<p><code>cmirrord</code> [<code>-f</code>] [<code>-h</code>] </p>
<h2>Description</h2>
<p><code>cmirrord</code> is the daemon that tracks mirror log information in a cluster. It is specific to device-mapper based mirrors (and by extension, LVM cluster mirrors). Cluster mirrors are not possible without this daemon running. This daemon relies on the cluster infrastructure provided by the Cluster MANager (CMAN), which must be set up and running in order for cmirrord to function. (The cluster infrastructure is also required for <code><a href="/docs/linux/man/8-clvmd/">clvmd</a></code>(8).) Output is logged via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). The <code>SIGUSR1 <a href="/docs/linux/man/7-signal/">signal</a></code>(7) can be issued to <code>cmirrord</code> to gather current status information for debugging purposes. Once started, <code>cmirrord</code> will run until it is shutdown via <code>SIGINT</code> signal. If there are still active cluster mirrors, however, the signal will be ignored. Active cluster mirrors should be shutdown before stopping the cluster mirror log daemon. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>Do not fork and log to the terminal.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print usage. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></code>(5), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/8-clvmd/">clvmd</a></code>(8), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) </p>
