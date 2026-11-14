---
title: "votequorum_overview(8)"
name: "votequorum_overview"
section: "8"
letter: "v"
url: "/docs/linux/man/8-votequorum_overview/"
description: "votequorum_overview – Votequorum Library Overview"
---

<p>votequorum_overview &#8211; Votequorum Library Overview</p>
<h2>Overview</h2>
<p>The votequorum library is delivered with the corosync project. It is the external interface to the vote-based quorum service. This service is optionally loaded into all nodes in a corosync cluster to avoid split-brain situations. It does this by having a number of votes assigned to each system in the cluster and ensuring that only when a majority of the votes are present, cluster operations are allowed to proceed. </p>
<p> The library provides a mechanism to: </p>
<p> * Query the quorum status </p>
<p> * Get a list of nodes known to the quorum service </p>
<p> * Receive notifications of quorum state changes </p>
<p> * Change the number of votes assigned to a node </p>
<p> * Change the number of expected votes for a cluster to be quorate </p>
<p> * Connect an additional quorum device to allow small clusters to remain quorate during node outages.</p>
<h2>Virtual Synchrony</h2>
<p>Votequorum is the only one service where communication with library is allowed during synchronization phase. This makes it possible for quorum device to react to membership change and decide to vote or not without timing hazard, because corosync stands in synchronization phase until qdevice on all nodes votes or timeout expires. </p>
<p> As a side effect, extended virtual synchrony is broken for the votequorum service. This means, that messages sent during synchronization phase can be delivered sooner then messages sent right before sync phase began. This applies also for local messages.</p>
<h2>Bugs</h2>
<p>No known bugs at the time of writing. The authors are from outerspace. Deal with it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-quorumtool/">corosync-quorumtool</a></code>(8), <code><a href="/docs/linux/man/5-votequorum/">votequorum</a></code>(5), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3) </p>
