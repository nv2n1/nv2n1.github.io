---
title: "fence_node(8)"
name: "fence_node"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_node/"
description: "fence_node – a utility to run fence agents"
---

<p>fence_node &#8211; a utility to run fence agents</p>
<h2>Synopsis</h2>
<p><code>fence_node</code> [OPTIONS] <i>nodename</i> </p>
<h2>Description</h2>
<p>This utility runs a fence agent against <i>nodename</i>. The agent and args are taken from the running cluster configuration based on <code><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></code>(5). <code>fence_node</code> is a wrapper around the libfence functions: fence_node() and unfence_node(). These libfence functions use libccs to read the node fencing configuration, which means that corosync (with cman and ccs) must be running to use <code><a href="/docs/linux/man/8-fence_node/">fence_node</a></code>(8). The <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) daemon is the main user of libfence:fence_node(), and the configuration details for that function are given in the <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) man page.</p>
<h3>Fencing vs. Unfencing</h3>
<p>The main use for unfencing is with storage/SAN (non-power) agents. When using power-based fencing agents, the fencing action itself is supposed to turn a node back on after first turning the power off (this happens automatically with a &quot;reboot&quot; action, and needs to be configured explicitly as &quot;off&quot; + &quot;on&quot; otherwise.) When using storage-based fencing agents, the fencing action is not allowed to re-enable a node after disabling it. Re-enabling a fenced node is only safe once the node has been rebooted. A natural way to re-enable a fenced node&#8217;s access to storage, is for that node to re-enable the access itself during its startup process. The cman init script calls fence_node -U (nodename defaults to local nodename when unfencing). Unfencing a node without an &lt;unfence&gt; configuration (see below) is a no-op. The basic differences between fencing and unfencing: <code>Fencing</code></p>
<dl>
<dt>1.</p>
<dd>libfence: fence_node(), command line: fence_node nodename</p>
<dt>2.</p>
<dd>Turns off or disables a node.</p>
<dt>3.</p>
<dd>Agents run with the default action of &quot;off&quot;, &quot;disable&quot; or &quot;reboot&quot;.</p>
<dt>4.</p>
<dd>Performed by a cluster node against another node that fails (by the fenced daemon). <code>Unfencing</code></p>
<dt>1.</p>
<dd>libfence: unfence_node(), command line: fence_node -U nodename</p>
<dt>2.</p>
<dd>Turns on or enables a node.</p>
<dt>3.</p>
<dd>Agents run with the explicit action of &quot;on&quot; or &quot;enable&quot;.</p>
<dt>4.</p>
<dd>Performed by a cluster node &quot;against&quot; itself during startup (by the cman init script). </p>
<h2>Options</h2>
<dl>
<dt><code>-U</code></p>
<dd>Unfence the node, default local node name.</p>
<dt><code>-v</code></p>
<dd>Show fence agent results, -vv to also show agent args.</p>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit.</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>Files</h2>
<p>The Unfencing/unfence_node() configuration is very similar to the Fencing/fence_node() configuration shown in <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8). Unfencing is only performed for a node with an &lt;unfence&gt; section: </p>
<pre>&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;/fence&gt;
 &lt;unfence&gt;
 &lt;/unfence&gt;
&lt;/clusternode&gt;</pre>
<p>The &lt;unfence&gt; section does not contain &lt;method&gt; sections like the &lt;fence&gt; section does. It contains &lt;device&gt; references directly, which mirror the corresponding device sections for &lt;fence&gt;, with the notable addition of the explicit action of &quot;on&quot; or &quot;enable&quot;. The same &lt;fencedevice&gt; is referenced by both fence and unfence &lt;device&gt; lines, and the same per-node args should be repeated. </p>
<pre>&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;myswitch&quot; foo=&quot;x&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
 &lt;unfence&gt;
 &lt;device name=&quot;myswitch&quot; foo=&quot;x&quot; action=&quot;on&quot;/&gt;
 &lt;/unfence&gt;
&lt;/clusternode&gt;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8) </p>
