---
title: "fence_tool(8)"
name: "fence_tool"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_tool/"
description: "fence_tool – a utility for the fenced daemon"
---

<p>fence_tool &#8211; a utility for the fenced daemon</p>
<h2>Synopsis</h2>
<p><code>fence_tool</code> [COMMAND] [OPTIONS] </p>
<h2>Description</h2>
<p>This utility controls and queries the <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) daemon with the following commands:</p>
<dl>
<dt><code>join</code></p>
<dd>join the fence domain.</p>
<dt><code>leave</code></p>
<dd>leave the fence domain.</p>
<dt><code>dump</code></p>
<dd>print the fenced internal debug buffer ont stdout.</p>
<dt><code>ls</code></p>
<dd>display internal fenced state. The leave command will not be sent to fenced if fence_tool detects that any instances of gfs or dlm are in use. </p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Show all node information in ls.</p>
<dt><code>-t</code><i> seconds</i></p>
<dd>Retry cman connection for this many seconds. 0 none, -1 indefinite. Default 0.</p>
<dt><code>-q</code><i> seconds</i></p>
<dd>Delay join up to this many seconds for the cluster to have quorum. 0 none, -1 indefinite. Default 0.</p>
<dt><code>-m</code><i> seconds</i></p>
<dd>Delay join up to this many seconds for all nodes in cluster.conf to be cluster members. 0 none, -1 indefinite. Default 0.</p>
<dt><code>-w</code><i> seconds</i></p>
<dd>Wait up to this many seconds for the result of join or leave. 0 none, -1 indefinite. Default 0.</p>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit.</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) </p>
