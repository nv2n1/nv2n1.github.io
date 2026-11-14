---
title: "cpg_overview(8)"
name: "cpg_overview"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cpg_overview/"
description: "cpg_overview – CPG library overview"
---

<p>cpg_overview &#8211; CPG library overview</p>
<h2>Overview</h2>
<p>The CPG library is delivered with the corosync project. This library is used to create distributed applications that operate properly during cluster partitions, merges, and faults. </p>
<p> The library provides a mechanism to: </p>
<p> * handle abstraction for multiple instances of a CPG library in one application </p>
<p> * join one or more groups </p>
<p> * leave one or more groups </p>
<p> * Deliver messages to members of that group </p>
<p> * Deliver configuration changes </p>
<p> * Iterate members of groups</p>
<h2>Security</h2>
<p>If encryption is enabled in corosync.conf, the CPG library will encrypt and authenticate message contents. Applications must run as the ais user to be validated by corosync on IPC connection, otherwise they will be unable to access the corosync services.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_finalize/">cpg_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_fd_get/">cpg_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-cpg_join/">cpg_join</a></code>(3), <code><a href="/docs/linux/man/3-cpg_leave/">cpg_leave</a></code>(3), <code><a href="/docs/linux/man/3-cpg_mcast_joined/">cpg_mcast_joined</a></code>(3), <code><a href="/docs/linux/man/3-cpg_model_initialize/">cpg_model_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_membership_get/">cpg_membership_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_zcb_alloc/">cpg_zcb_alloc</a></code>(3), <code><a href="/docs/linux/man/3-cpg_zcb_free/">cpg_zcb_free</a></code>(3), <code><a href="/docs/linux/man/3-cpg_zcb_mcast_joined/">cpg_zcb_mcast_joined</a></code>(3), <code><a href="/docs/linux/man/3-cpg_context_get/">cpg_context_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_context_set/">cpg_context_set</a></code>(3), <code><a href="/docs/linux/man/3-cpg_local_get/">cpg_local_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_iteration_initialize/">cpg_iteration_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_iteration_next/">cpg_iteration_next</a></code>(3), <code><a href="/docs/linux/man/3-cpg_iteration_finalize/">cpg_iteration_finalize</a></code>(3) </p>
