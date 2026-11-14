---
title: "fence_sanlockd(8)"
name: "fence_sanlockd"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_sanlockd/"
description: "fence_sanlockd – daemon for fence_sanlock agent"
---

<p>fence_sanlockd &#8211; daemon for fence_sanlock agent</p>
<h2>Synopsis</h2>
<p><code>fence_sanlockd</code> [OPTIONS] </p>
<h2>Description</h2>
<p>The fence_sanlockd daemon is used by the fence_sanlock agent. See <code><a href="/docs/linux/man/8-fence_sanlock/">fence_sanlock</a></code>(8), for full description. </p>
<h2>Options</h2>
<p><code>-D</code><br />
Enable debugging to stderr and don&#8217;t fork. </p>
<p> <code>-p</code><i> path</i><br />
&nbsp;<wbr>Path to shared storage with sanlock leases. </p>
<p> <code>-i</code><i> host_id</i><br />
&nbsp;<wbr>Local sanlock host_id&nbsp;<wbr>(1-128). </p>
<p> <code>-w</code><br />
Wait for fence_sanlockd -s to send options&nbsp;<wbr>(p,i). </p>
<p> <code>-s</code><br />
Send options&nbsp;<wbr>(p,i)&nbsp;<wbr>to waiting fence_sanlockd -w. </p>
<p> <code>-1</code><br />
Send SIGUSR1 to running fence_sanlockd.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fence_sanlock/">fence_sanlock</a></code>(8), <code><a href="/docs/linux/man/8-sanlock/">sanlock</a></code>(8), <code><a href="/docs/linux/man/8-wdmd/">wdmd</a></code>(8), <code><a href="/docs/linux/man/8-fence_node/">fence_node</a></code>(8), <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) </p>
