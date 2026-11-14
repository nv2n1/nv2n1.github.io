---
title: "quorum_overview(8)"
name: "quorum_overview"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quorum_overview/"
description: "quorum_overview – Quorum Library Overview"
---

<p>quorum_overview &#8211; Quorum Library Overview</p>
<h2>Overview</h2>
<p>The quorum library is delivered with the corosync project. It is the external interface to the quorum service. This service is loaded into all nodes in a corosync cluster and track the quorum status of a node. In order for quorum service to be useful, a quorum provider must be configured. </p>
<p> The library provides a mechanism to: </p>
<p> * Query the quorum status </p>
<p> * Receive notifications of quorum state changes</p>
<h2>Bugs</h2>
<p>No known bugs at the time of writing. The authors are from outerspace. Deal with it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-quorumtool/">corosync-quorumtool</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/5-votequorum/">votequorum</a></code>(5), <code><a href="/docs/linux/man/3-quorum_initialize/">quorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_finalize/">quorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstart/">quorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstop/">quorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_get/">quorum_context_get</a></code>(3) </p>
