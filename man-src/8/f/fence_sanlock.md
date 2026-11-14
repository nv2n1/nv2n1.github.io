---
title: "fence_sanlock(8)"
name: "fence_sanlock"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_sanlock/"
description: "fence_sanlock – fence agent using watchdog and shared storage leases"
---

<p>fence_sanlock &#8211; fence agent using watchdog and shared storage leases</p>
<h2>Synopsis</h2>
<p><code>fence_sanlock</code> [OPTIONS] </p>
<h2>Description</h2>
<p>fence_sanlock uses the watchdog device to reset nodes, in conjunction with three daemons: fence_sanlockd, sanlock, and wdmd. The watchdog device, controlled through /dev/watchdog, is available when a watchdog kernel module is loaded. A module should be loaded for the available hardware. If no hardware watchdog is available, or no module is loaded, the &quot;softdog&quot; module will be loaded, which emulates a hardware watchdog device. Shared storage must be configured for sanlock to use from all hosts. This is generally an lvm lv (non-clustered), but could be another block device, or NFS file. The storage should be 1GB of fully allocated space. After being created, the storage must be initialized with the command:<br />
 # fence_sanlock -o sanlock_init -p /path/to/storage The fence_sanlock agent uses sanlock leases on shared storage to verify that hosts have been reset, and to notify fenced nodes that are still running, that they should be reset. The fence_sanlockd init script starts the wdmd, sanlock and fence_sanlockd daemons before the cluster or fencing systems are started (e.g. cman, corosync and fenced). The fence_sanlockd daemon is started with the -w option so it waits for the path and host_id options to be provided when they are available. Unfencing must be configured for fence_sanlock in cluster.conf. The cman init script does unfencing by running fence_node -U, which in turn runs fence_sanlock with the &quot;on&quot; action and local path and host_id values taken from cluster.conf. fence_sanlock in turn passes the path and host_id values to the waiting fence_sanlockd daemon. With these values, fence_sanlockd joins the sanlock lockspace and acquires a resource lease for the local host. It can take several minutes to complete these unfencing steps. Once unfencing is complete, the node is a member of the sanlock lockspace named &quot;fence&quot; and the node&#8217;s fence_sanlockd process holds a resource lease named &quot;hN&quot;, where N is the node&#8217;s host_id. (To verify this, run the commands &quot;sanlock client status&quot; and &quot;sanlock client host_status&quot;, which show state from the sanlock daemon, or &quot;sanlock direct dump &lt;path&gt;&quot; which shows state from shared storage.) When fence_sanlock fences a node, it tries to acquire that node&#8217;s resource lease. sanlock will not grant the lease until the owner (the node being fenced) has been reset by its watchdog device. The time it takes to acquire the lease is 140 seconds from the victim&#8217;s last lockspace renewal timestamp on the shared storage. Once acquired, the victim&#8217;s lease is released, and fencing completes successfully. Live nodes being fenced When a live node is being fenced, fence_sanlock will continually fail to acquire the victim&#8217;s lease, because the victim continues to renew its lockspace membership on storage, and the fencing node sees it is alive. This is by design. As long as the victim is alive, it must continue to renew its lockspace membership on storage. The victim must not allow the remote fence_sanlock to acquire its lease and consider it fenced while it is still alive. At the same time, a victim knows that when it is being fenced, it should be reset to avoid blocking recovery of the rest of the cluster. To communicate this, fence_sanlock makes a &quot;request&quot; on storage for the victim&#8217;s resource lease. On the victim, fence_sanlockd, which holds the resource lease, is configured to receive SIGUSR1 from sanlock if anyone requests its lease. Upon receiving the signal, fence_sanlockd knows that it is a fencing victim. In response to this, fence_sanlockd allows its wdmd connection to expire, which in turn causes the watchdog device to fire, resetting the node. The watchdog reset will obviously have the effect of stopping the victim&#8217;s lockspace membership renewals. Once the renewals stop, fence_sanlock will finally be able to acquire the victim&#8217;s lease after waiting a fixed time from the final lockspace renewal. Loss of shared storage If access to shared storage with sanlock leases is lost for 80 seconds, sanlock is not able to renew the lockspace membership, and enters recovery. This causes sanlock clients holding leases, such as fence_sanlockd, to be notified that their leases are being lost. In response, fence_sanlockd must reset the node, much as if it was being fenced. Daemons killed/crashed/hung If sanlock, fence_sanlockd daemons are killed abnormally, or crash or hang, their wdmd connections will expire, causing the watchdog device to fire, resetting the node. fence_sanlock from another node will then run and acquire the victim&#8217;s resource lease. If the wdmd daemon is killed abnormally or crashes or hangs, it will not pet the watchdog device, causing it to fire and reset the node. Time Values The specific times periods referenced above, e.g. 140, 80, are based on the default sanlock i/o timeout of 10 seconds. If sanlock is configured to use a different i/o timeout, these numbers will be different. </p>
<h2>Options</h2>
<p><code>-o</code><i> action</i><br />
&nbsp;<wbr>The agent action: </p>
<dl>
<dd><code>on</code><br />
 Enable the local node to be fenced. Used by unfencing. </p>
<dd><code>off</code><br />
 Disable another node. </p>
<dd><code>status</code><br />
 Test if a node is on or off. A node is on if it&#8217;s lease is held, and off is it&#8217;s lease is free. </p>
<dd><code>metadata</code><br />
 Print xml description of required parameters. </p>
<dd><code>sanlock_init</code><br />
 Initialize sanlock leases on shared storage. </p>
</dl>
<p> <code>-p</code><i> path</i><br />
&nbsp;<wbr>The path to shared storage with sanlock leases. </p>
<p> <code>-i</code><i> host_id</i><br />
&nbsp;<wbr>The host_id, from 1-128.</p>
<h2>Stdin Parameters</h2>
<p>Options can be passed on stdin, with the format key=val. Each key=val pair is separated by a new line. </p>
<p> action=on|off|status<br />
 See -o </p>
<p> path=/path/to/shared/storage<br />
 See -p </p>
<p> host_id=num<br />
 See -i</p>
<h2>Files</h2>
<p>Example cluster.conf configuration for fence_sanlock.<br />
 (For cman based clusters in which fenced runs agents.)<br />
 Also see <a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a>(5), <a href="/docs/linux/man/8-fenced/">fenced</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8). </p>
<pre>&lt;clusternode name=&quot;node01&quot; nodeid=&quot;1&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;wd&quot; host_id=&quot;1&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
 &lt;unfence&gt;
 &lt;device name=&quot;wd&quot; host_id=&quot;1&quot; action=&quot;on&quot;/&gt;
 &lt;/unfence&gt;
&lt;/clusternode&gt;
&lt;clusternode name=&quot;node02&quot; nodeid=&quot;2&quot;&gt;
 &lt;fence&gt;
 &lt;method name=&quot;1&quot;&gt;
 &lt;device name=&quot;wd&quot; host_id=&quot;2&quot;/&gt;
 &lt;/method&gt;
 &lt;/fence&gt;
 &lt;unfence&gt;
 &lt;device name=&quot;wd&quot; host_id=&quot;2&quot; action=&quot;on&quot;/&gt;
 &lt;/unfence&gt;
&lt;/clusternode&gt;
&lt;fencedevice name=&quot;wd&quot; agent=&quot;fence_sanlock&quot; path=&quot;/dev/fence/leases&quot;/&gt;</pre>
<p>Example dlm.conf configuration for fence_sanlock.<br />
 (For non-cman based clusters in which dlm_controld runs agents.)<br />
 Also see <a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a>(5), <a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a>(8). </p>
<pre>device wd /usr/sbin/fence_sanlock path=/dev/fence/leases
connect wd node=1 host_id=1
connect wd node=2 host_id=2
unfence wd</pre>
<h2>Test</h2>
<p>To test fence_sanlock directly, without clustering: </p>
<pre>1. Initialize storage
node1: create 1G lv on shared storage /dev/fence/leases
node1: fence_sanlock -o sanlock_init -p /dev/fence/leases
2. Start services
node1: service fence_sanlockd start
node2: service fence_sanlockd start
3. Enable fencing
node1: fence_sanlock -o on -p /dev/fence/leases -i 1
node2: fence_sanlock -o on -p /dev/fence/leases -i 2
This &quot;unfence&quot; step may take a couple minutes.
4. Verify hosts and leases
node1: sanlock status
s fence:1:/dev/fence/leases:0
r fence:h1:/dev/fence/leases:1048576:1 p 2465
node2: sanlock status
s fence:2:/dev/fence/leases:0
r fence:h2:/dev/fence/leases:2097152:1 p 2366
node1: sanlock host_status
lockspace fence
1 timestamp 717
2 timestamp 678
node2: sanlock host_status
lockspace fence
1 timestamp 738
2 timestamp 678
5. Fence node2
node1: fence_sanlock -o off -p /dev/fence/leases -i 2
This may take a few minutes to return.
When node2 is not dead before fencing, sanlock on node1 will log errors
about failing to acquire the lease while node2 is still alive. This is
expected.
6. Success
node1 fence_sanlock should exit 0 after node2 is reset by its watchdog.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fence_sanlockd/">fence_sanlockd</a></code>(8), <code><a href="/docs/linux/man/8-sanlock/">sanlock</a></code>(8), <code><a href="/docs/linux/man/8-wdmd/">wdmd</a></code>(8) </p>
