---
title: "sync_server(8)"
name: "sync_server"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sync_server/"
description: "sync_server – server side of the synchronization (replication) engine"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>sync_server &#8211; server side of the synchronization (replication) engine</p>
<h2>Synopsis</h2>
<p><code>sync_server</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-p</code> <i>ssf</i> ]</p>
<h2>Description</h2>
<p><i>Sync_server</i> is the server side of the the replication system. It runs on the target (replica) system and listens for connections from <i>sync_client</i> which provides instructions for synchronizing the replica system with the master system. </p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-p</code><i> ssf</i></p>
<dd>Tell <i>sync_server</i> that an external layer exists. An SSF (security strength factor) of 1 means an integrity protection layer exists. Any higher SSF implies some form of privacy protection.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sync_client/">sync_client</a>(8)</code></p>
<h2>Authors</h2>
<p>David Carter (dpc22 [at] cam.ac.uk), Ken Murchison (ken [at] oceana.com)</p>
