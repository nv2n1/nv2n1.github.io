---
title: "corosync(8)"
name: "corosync"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync/"
description: "corosync – The Corosync Cluster Engine."
---

<p>corosync &#8211; The Corosync Cluster Engine.</p>
<h2>Synopsis</h2>
<p><code>corosync [-f] [-p] [-r] [-v]</code></p>
<h2>Description</h2>
<p><code>corosync</code> Corosync provides clustering infracture such as membership, messaging and quorum.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></dt>
<dd>Start application in foreground.</dd>
<dt><code>-p</code></dt>
<dd>Do not set process priority.</dd>
<dt><code>-r</code></dt>
<dd>Set round robin realtime scheduling (default).</dd>
<dt><code>-t</code></dt>
<dd>Test configuration and then exit.</dd>
<dt><code>-v</code></dt>
<dd>Display version and SVN revision of Corosync and exit.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/8-sam_overview/">sam_overview</a></code>(8), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8), <code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8)</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
