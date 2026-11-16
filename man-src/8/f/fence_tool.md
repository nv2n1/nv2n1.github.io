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
<dt><code>join</code></dt>
<dd>join the fence domain.</dd>
<dt><code>leave</code></dt>
<dd>leave the fence domain.</dd>
<dt><code>dump</code></dt>
<dd>print the fenced internal debug buffer ont stdout.</dd>
<dt><code>ls</code></dt>
<dd>display internal fenced state. The leave command will not be sent to fenced if fence_tool detects that any instances of gfs or dlm are in use. </dd>
<h2>Options</h2>
<dl>
<dt><code>-n</code></dt>
<dd>Show all node information in ls.</dd>
<dt><code>-t</code><i> seconds</i></dt>
<dd>Retry cman connection for this many seconds. 0 none, -1 indefinite. Default 0.</dd>
<dt><code>-q</code><i> seconds</i></dt>
<dd>Delay join up to this many seconds for the cluster to have quorum. 0 none, -1 indefinite. Default 0.</dd>
<dt><code>-m</code><i> seconds</i></dt>
<dd>Delay join up to this many seconds for all nodes in cluster.conf to be cluster members. 0 none, -1 indefinite. Default 0.</dd>
<dt><code>-w</code><i> seconds</i></dt>
<dd>Wait up to this many seconds for the result of join or leave. 0 none, -1 indefinite. Default 0.</dd>
<dt><code>-h</code></dt>
<dd>Print a help message describing available options, then exit.</dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) </p>
</dl>