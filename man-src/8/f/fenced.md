---
title: "fenced(8)"
name: "fenced"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fenced/"
description: "fenced – the I/O Fencing daemon"
---

<p>fenced &#8211; the I/O Fencing daemon</p>
<h2>Synopsis</h2>
<p><code>fenced</code> [OPTIONS] </p>
<h2>Description</h2>
<p>The fencing daemon, fenced, fences cluster nodes that have failed. Fencing a node generally means rebooting it or otherwise preventing it from writing to storage, e.g. disabling its port on a SAN switch. Fencing involves interacting with a hardware device, e.g. network power switch, SAN switch, storage array. Different &quot;fencing agents&quot; are run by fenced to interact with various hardware devices. Software related to sharing storage among nodes in a cluster, e.g. GFS, usually requires fencing to be configured to prevent corruption of the storage in the presence of node failure and recovery. GFS will not allow a node to mount a GFS file system unless the node is running fenced. Once started, fenced waits for the <code><a href="/docs/linux/man/8-fence_tool/">fence_tool</a></code>(8) join command to be run, telling it to join the fence domain: a group of nodes that will fence group members that fail. When the cluster does not have quorum, fencing operations are postponed until quorum is restored. If a failed fence domain member is reset and rejoins the cluster before the remaining domain members have fenced it, the fencing is no longer needed and will be skipped. fenced uses the corosync cluster membership system, it&#8217;s closed process group library (libcpg), and the cman quorum and configuration libraries (libcman, libccs). The cman init script usually starts the fenced daemon and runs fence_tool join and leave.</p>
<h3>Node failure</h3>
<p>When a fence domain member fails, fenced runs an agent to fence it. The specific agent to run and the agent parameters are all read from the cluster.conf file (using libccs) at the time of fencing. The fencing operation against a failed node is not considered complete until the exec&#8217;ed agent exits. The exit value of the agent indicates the success or failure of the operation. If the operation failed, fenced will retry (possibly with a different agent, depending on the configuration) until fencing succeeds. Other systems such as DLM and GFS wait for fencing to complete before starting their own recovery for a failed node. Information about fencing operations will also appear in syslog. When a domain member fails, the actual fencing operation can be delayed by a configurable number of seconds (cluster.conf post_fail_delay or -f). Within this time, the failed node could be reset and rejoin the cluster to avoid being fenced. This delay is 0 by default to minimize the time that other systems are blocked.</p>
<h3>Domain startup</h3>
<p>When the fence domain is first created in the cluster (by the first node to join it) and subsequently enabled (by the cluster gaining quorum) any nodes listed in cluster.conf that are not presently members of the corosync cluster are fenced. The status of these nodes is unknown, and to be safe they are assumed to need fencing. This startup fencing can be disabled, but it&#8217;s only truly safe to do so if an operator is present to verify that no cluster nodes are in need of fencing. The following example illustrates why startup fencing is important. Take a three node cluster with nodes A, B and C; all three have a GFS file system mounted. All three nodes experience a low-level kernel hang at about the same time. A watchdog triggers a reboot on nodes A and B, but not C. A and B reboot, form the cluster again, gain quorum, join the fence domain, _don&#8217;t_ fence node C which is still hung and unresponsive, and mount the GFS fs again. If C were to come back to life, it could corrupt the fs. So, A and B need to fence C when they reform the fence domain since they don&#8217;t know the state of C. If C _had_ been reset by a watchdog like A and B, but was just slow in rebooting, then A and B might be fencing C unnecessarily when they do startup fencing. The first way to avoid fencing nodes unnecessarily on startup is to ensure that all nodes have joined the cluster before any of the nodes start the fence daemon. This method is difficult to automate. A second way to avoid fencing nodes unnecessarily on startup is using the cluster.conf post_join_delay setting (or -j option). This is the number of seconds fenced will delay before actually fencing any victims after nodes join the domain. This delay gives nodes that have been tagged for fencing a chance to join the cluster and avoid being fenced. A delay of -1 here will cause the daemon to wait indefinitely for all nodes to join the cluster and no nodes will actually be fenced on startup. To disable fencing at domain-creation time entirely, the cluster.conf clean_start setting (or -c option) can be used to declare that all nodes are in a clean or safe state to start. This setting/option should not generally be used since it risks not fencing a node that needs it, which can lead to corruption in other applications (like GFS) that depend on fencing. Avoiding unnecessary fencing at startup is primarily a concern when nodes are fenced by power cycling. If nodes are fenced by disabling their SAN access, then unnecessarily fencing a node is usually less disruptive.</p>
<h3>Fencing override</h3>
<p>If a fencing device fails, the agent may repeatedly return errors as fenced tries to fence a failed node. In this case, the admin can manually reset the failed node, and then use <code><a href="/docs/linux/man/8-fence_ack_manual/">fence_ack_manual</a></code>(8) to tell fenced to continue without fencing the node. </p>
<h2>Options</h2>
<p>Command line options override a corresponding setting in cluster.conf. </p>
<dl>
<dt><code>-D</code></p>
<dd>Enable debugging to stderr and don&#8217;t fork.<br />
 See also <code>fence_tool dump</code> in <code><a href="/docs/linux/man/8-fence_tool/">fence_tool</a></code>(8).</p>
<dt><code>-L</code></p>
<dd>Enable debugging to log file.<br />
 See also <code>logging</code> in <code><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></code>(5).</p>
<dt><code>-g</code><i> num</i></p>
<dd>groupd compatibility mode, 0 off, 1 on. Default 0.</p>
<dt><code>-r</code><i> path</i></p>
<dd>Register a directory that needs to be empty for the daemon to start. Use a dash (-) to skip default directories /sys/fs/gfs, /sys/fs/gfs2, /sys/kernel/dlm.</p>
<dt><code>-c</code></p>
<dd>All nodes are in a clean state to start. Do no startup fencing.</p>
<dt><code>-s</code></p>
<dd>Skip startup fencing of nodes with no defined fence methods.</p>
<dt><code>-j</code><i> secs</i></p>
<dd>Post-join fencing delay. Default 6.</p>
<dt><code>-f</code><i> secs</i></p>
<dd>Post-fail fencing delay. Default 0.</p>
<dt><code>-R</code><i> secs</i></p>
<dd>Number of seconds to wait for a manual override after a failed fencing attempt before the next attempt. Default 3.</p>
<dt><code>-O</code><i> path</i></p>
<dd>Location of a FIFO used for communication between fenced and fence_ack_manual.</p>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit.</p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>Files</h2>
<p><code><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></code>(5) is usually located at /etc/cluster/cluster.conf. It is not read directly. Other cluster components load the contents into memory, and the values are accessed through the libccs library. </p>
<p> Configuration options for fenced are added to the &lt;fence_daemon /&gt; section of cluster.conf, within the top level &lt;cluster&gt; section. </p>
<dl>
<dt><code>post_join_delay</code></p>
<dd>is the number of seconds the daemon will wait before fencing any victims after a node joins the domain. Default 6. </p>
<p> &lt;fence_daemon post_join_delay=&quot;6&quot;/&gt; </p>
<dt><code>post_fail_delay</code></p>
<dd>is the number of seconds the daemon will wait before fencing any victims after a domain member fails. Default 0. </p>
<p> &lt;fence_daemon post_fail_delay=&quot;0&quot;/&gt; </p>
<dt><code>clean_start</code></p>
<dd>is used to prevent any startup fencing the daemon might do. It indicates that the daemon should assume all nodes are in a clean state to start. Default 0. </p>
<p> &lt;fence_daemon clean_start=&quot;0&quot;/&gt; </p>
<dt><code>override_path</code></p>
<dd>is the location of a FIFO used for communication between fenced and fence_ack_manual. Default shown. </p>
<p> &lt;fence_daemon override_path=&quot;/var/run/cluster/fenced_override&quot;/&gt; </p>
<dt><code>override_time</code></p>
<dd>is the number of seconds to wait for administrator intervention between fencing attempts following fence agent failures. Default 3. </p>
<p> &lt;fence_daemon override_time=&quot;3&quot;/&gt; </p>
</dl>
<h3>Per-node fencing settings</h3>
<p>The per-node fencing configuration is partly dependant on the specific agent/hardware being used. The general framework begins like this: </p>
<pre>&lt;clusternodes&gt;
&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;
&lt;clusternode name=&quot;node2&quot; nodeid=&quot;2&quot;&gt;
 &lt;fence&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;
&lt;/clusternodes&gt;</pre>
<p>The simple fragment above is a valid configuration: there is no way to fence these nodes. If one of these nodes is in the fence domain and fails, fenced will repeatedly fail in its attempts to fence it. The admin will need to manually reset the failed node and then use fence_ack_manual to tell fenced to continue without fencing it (see override above). </p>
<p> There is typically a single method used to fence each node (the name given to the method is not significant). A method refers to a specific device listed in the separate &lt;fencedevices&gt; section, and then lists any node-specific parameters related to using the device. </p>
<pre>&lt;clusternodes&gt;
&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;myswitch&quot; foo=&quot;x&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;
&lt;clusternode name=&quot;node2&quot; nodeid=&quot;2&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;myswitch&quot; foo=&quot;y&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;
&lt;/clusternodes&gt;</pre>
<h3>Fence device settings</h3>
<p>This section defines properties of the devices used to fence nodes. There may be one or more devices listed. The per-node fencing sections above reference one of these fence devices by name. </p>
<pre>&lt;fencedevices&gt;
 &lt;fencedevice name=&quot;myswitch&quot; agent=&quot;...&quot; something=&quot;...&quot;/&gt;
&lt;/fencedevices&gt;</pre>
<h3>Multiple methods for a node</h3>
<p>In more advanced configurations, multiple fencing methods can be defined for a node. If fencing fails using the first method, fenced will try the next method, and continue to cycle through methods until one succeeds. </p>
<pre>&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;myswitch&quot; foo=&quot;x&quot;/&gt;
 &lt;/method&gt;
 &lt;method name=&quot;2&quot;&gt;
 &lt;device name=&quot;another&quot; bar=&quot;123&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;
&lt;fencedevices&gt;
 &lt;fencedevice name=&quot;myswitch&quot; agent=&quot;...&quot; something=&quot;...&quot;/&gt;
 &lt;fencedevice name=&quot;another&quot; agent=&quot;...&quot;/&gt;
&lt;/fencedevices&gt;</pre>
<h3>Dual path, redundant power</h3>
<p>Sometimes fencing a node requires disabling two power ports or two i/o paths. This is done by specifying two or more devices within a method. fenced will run the agent for the device twice, once for each device line, and both must succeed for fencing to be considered successful. </p>
<pre>&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;sanswitch1&quot; port=&quot;11&quot;/&gt;
 &lt;device name=&quot;sanswitch2&quot; port=&quot;11&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;</pre>
<p>When using power switches to fence nodes with dual power supplies, the agents must be told to turn off both power ports before restoring power to either port. The default off-on behavior of the agent could result in the power never being fully disabled to the node. </p>
<pre>&lt;clusternode name=&quot;node1&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;nps1&quot; port=&quot;11&quot; action=&quot;off&quot;/&gt;
 &lt;device name=&quot;nps2&quot; port=&quot;11&quot; action=&quot;off&quot;/&gt;
 &lt;device name=&quot;nps1&quot; port=&quot;11&quot; action=&quot;on&quot;/&gt;
 &lt;device name=&quot;nps2&quot; port=&quot;11&quot; action=&quot;on&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
&lt;/clusternode&gt;</pre>
<h3>Hardware-specific settings</h3>
<p>Find documentation for configuring specific devices from the device agent&#8217;s man page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fence_tool/">fence_tool</a></code>(8), <code><a href="/docs/linux/man/8-fence_ack_manual/">fence_ack_manual</a></code>(8), <code><a href="/docs/linux/man/8-fence_node/">fence_node</a></code>(8), <code><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></code>(5) </p>
