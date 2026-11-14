---
title: "ocf_pacemaker_remote(7)"
name: "ocf_pacemaker_remote"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_remote/"
description: "ocf_pacemaker_remote – remote resource agent"
---

<p>ocf_pacemaker_remote &#8211; remote resource agent</p>
<h2>Synopsis</h2>
<p><code>OCF_RESKEY_server</code>=string [<code>OCF_RESKEY_port</code>=string] [<code>OCF_RESKEY_reconnect_interval</code>=string] <code>remote</code> [start | stop | reload | monitor | migrate_to | migrate_from | meta-data]</p>
<h2>Description</h2>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_server</code> = string</p>
<dl>
<dd>Server location </p>
<p> Server location to connect to. This can be an ip address or hostname.</dl>
<p> <code>OCF_RESKEY_port</code> = string [3121]</p>
<dl>
<dd>tcp port </p>
<p> tcp port to connect to.</dl>
<p> <code>OCF_RESKEY_reconnect_interval</code> = string [0]</p>
<dl>
<dd>reconnect interval </p>
<p> Interval in seconds at which Pacemaker will attempt to reconnect to a remote node after an active connection to the remote node has been severed. When this value is nonzero, Pacemaker will retry the connection indefinitely, at the specified interval. As with any time-based actions, this is not guaranteed to be checked more frequently than the value of the cluster-recheck-interval cluster option.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
