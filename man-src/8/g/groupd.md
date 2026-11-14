---
title: "groupd(8)"
name: "groupd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-groupd/"
description: "groupd – compatibility daemon for fenced, dlm_controld and gfs_controld"
---

<p>groupd &#8211; compatibility daemon for fenced, dlm_controld and gfs_controld</p>
<h2>Synopsis</h2>
<p><code>groupd</code> [OPTIONS] </p>
<h2>Description</h2>
<p>The groupd daemon and libgroup library are used by the fenced, dlm_controld and gfs_controld daemons when they are operating in cluster2-compatible mode to perform a rolling cluster upgrade from cluster2 to cluster3. See <code><a href="/docs/linux/man/5-cman/">cman</a></code>(5) for more information on the <code>upgrading</code> configuration option needed to perform a rolling upgrade. When the upgrading option is enabled, cman adds the following to the online configuration:  This setting causes the cman init script to start the groupd daemon, and causes the groupd, fenced, dlm_controld and gfs_controld daemons to operate in the old cluster2 mode so they will be compatible with cluster2 nodes in the cluster that have not yet been upgraded. The upgrading setting, including the groupd_compat setting, <code>cannot be changed in a running cluster.</code> The entire cluster must be taken offline to change these because the new cluster3 default modes are not compatible with the old cluster2 modes. The upgrading/compat settings cause the new cluster3 daemons to run the old cluster2 code and protocols. </p>
<h2>Options</h2>
<p>Command line options override a corresponding setting in cluster.conf. </p>
<dl>
<dt><code>-D</code></p>
<dd>Enable debugging to stderr and don&#8217;t fork.</p>
<dt><code>-L</code></p>
<dd>Enable debugging to log file.</p>
<dt><code>-g</code><i> num</i></p>
<dd>groupd compatibility mode, 0 off, 1 on. Default 0.</p>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit.</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cman/">cman</a></code>(5), <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8), <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/8-gfs_controld/">gfs_controld</a></code>(8) </p>
