---
title: "tipc-link(8)"
name: "tipc-link"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-link/"
description: "tipc-link – show links or modify link properties"
---

<p>tipc-link &#8211; show links or modify link properties</p>
<h2>Synopsis</h2>
<p> <code>tipc link set</code><br />
 [ <code>{ </code>priority <i>PRIORITY</i> | <code>tolerance</code> <i>TOLERANCE</i> | <code>window</code> <i>WINDOW </i>} <code>link </code><i>LINK</i><code> ]</code> |<br />
 [ { <code>broadcast</code> [ <i>BROADCAST</i> | <i>REPLICAST</i> | <i>AUTOSELECT</i> [ <code>ratio</code> <i>SIZE</i> ] <code>]</code> } <code>]</code><br />
 <code>tipc link get</code><br />
 [ <code>{ </code>priority<code> | </code>tolerance<code> | </code>window<code> } </code>link <i>LINK</i> ] |<br />
 [ <code>{</code> broadcast <code>}</code> ] </p>
<pre><code>tipc link statistics

{ show [ link

    LINK

    ] | reset

    link LINK

}</code></pre>
<p> <code>tipc link list</code> </p>
<pre><code>tipc link monitor set

{ threshold }
tipc link monitor get

{ threshold }</code></pre>
<p> <code>tipc link monitor summary</code> </p>
<p> <code>tipc link monitor list</code><br />
 [ <code>media </code> { <code>eth</code> | <code>ib</code> } <code>device</code> <i>DEVICE</i> ] |<br />
 [ <code>media udp name</code> <i>NAME</i> ] </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last valid command. For example <code>tipc link &#8211;help</code> will show link help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant. </p>
<dt><code>-j,</code> -json</p>
<dd>Output results in JavaScript Object Notation (JSON). </p>
<dt><code>-p,</code> -pretty</p>
<dd>The default JSON format is compact and more efficient to parse but hard for most users to read. This flag adds indentation for readability. </p>
</dl>
<h2>Description</h2>
<h3>Link statistics</h3>
<dl>
<dt><code>ACTIVE </code>link state</p>
<dd>An <code>ACTIVE</code> link is serving traffic. Two links to the same node can become <code>ACTIVE</code> if they have the same link <code>priority</code>. If there is more than two links with the same priority the additional links will be put in <code>STANDBY</code> state.</p>
<dt><code>STANDBY </code>link state</p>
<dd>A <code>STANDBY</code> link has lower link priority than an <code>ACTIVE</code> link. A <code>STANDBY</code> link has control traffic flowing and is ready to take over should the <code>ACTIVE</code> link(s) go down.</p>
<dt><code>MTU</code></p>
<dd>The Maximum Transmission Unit. The two endpoints advertise their default or configured <code>MTU</code> at initial link setup and will agree to use the lower of the two values should they differ.</p>
<dt><code>Packets</code></p>
<dd>The total amount of transmitted or received TIPC packets on a link. Including <code>fragmented </code>and <code>bundled </code>packets.</p>
<dt><code>Fragments</code></p>
<dd>Represented in the form <code>fragments</code>/<code>fragmented</code>. Where <code>fragmented</code> is the amount of data messages which have been broken into <code>fragments</code>. Subsequently the <code>fragments</code> are the total amount of packets that the <code>fragmented</code> messages has been broken into.</p>
<dt><code>Bundles</code></p>
<dd>Represented in the form <code>bundles</code>/<code>bundled</code>. If a link becomes congested the link will attempt to bundle data from small <code>bundled</code> packets into <code>bundles</code> of full MTU size packets before they are transmitted.</p>
<dt><code>Profile</code></p>
<dd>Shows the <code>average</code> packet size in octets/bytes for a <code>sample</code> of packets. It also shows the packet size distribution of the <code>sampled</code> packets in the intervals 0-64 bytes<br />
 64-256 bytes<br />
 256-1024 bytes<br />
 1024-4096 bytes<br />
 4096-16384 bytes<br />
 16384-32768 bytes<br />
 32768-66000 bytes</p>
<dt><code>Message counters</code></p>
<dd><code>states</code> &#8211; Number of link state messages <code>probes</code> &#8211; Link state messages with probe flag set. Typically sent when a link is idle <code>nacks</code> &#8211; Number of negative acknowledgement (NACK) packets sent and received by the link <code>defs</code> &#8211; Number of packets received out of order <code>dups</code> &#8211; Number of duplicate packets received</p>
<dt><code>Congestion link</code></p>
<dd>The number of times an application has tried to send data when the TIPC link was congested</p>
<dt><code>Send queue</code></p>
<dd><code>Max</code> is the maximum amount of messages that has resided in the out queue during the statistics collection period of a link. <code>Avg</code> is the average outqueue size during the lifetime of a link.</dl>
<h3>Link properties</h3>
<dl>
<dt><code>priority</code></p>
<dd>The priority between logical TIPC links to a particular node. Link priority can range from 0 (lowest) to 31 (highest).</p>
<dt><code>tolerance</code></p>
<dd>Link tolerance specifies the maximum time in milliseconds that TIPC will allow a communication problem to exist before taking the link down. The default value is 1500 milliseconds.</p>
<dt><code>window</code></p>
<dd>The link window controls how many unacknowledged messages a link endpoint can have in its transmit queue before TIPC&#8217;s congestion control mechanism is activated.</dl>
<h3>Monitor properties</h3>
<dl>
<dt><code>threshold</code></p>
<dd>The threshold specifies the cluster size exceeding which the link monitoring algorithm will switch from &quot;full-mesh&quot; to &quot;overlapping-ring&quot;. If set of 0 the overlapping-ring monitoring is always on and if set to a value larger than anticipated cluster size the overlapping-ring is disabled. The default value is 32.</dl>
<h3>Monitor information</h3>
<dl>
<dt><code>table_generation</code></p>
<dd>Represents the event count in a node&#8217;s local monitoring list. It steps every time something changes in the local monitor list, including changes in the local domain.</p>
<dt><code>cluster_size</code></p>
<dd>Represents the current count of cluster members.</p>
<dt><code>algorithm</code></p>
<dd>The current supervision algorithm used for neighbour monitoring for the bearer. Possible values are full-mesh or overlapping-ring.</p>
<dt><code>status</code></p>
<dd>The node status derived by the local node. Possible status are up or down.</p>
<dt><code>monitored</code></p>
<dd>Represent the type of monitoring chosen by the local node. Possible values are direct or indirect.</p>
<dt><code>generation</code></p>
<dd>Represents the domain generation which is the event count in a node&#8217;s local domain. Every time something changes (peer add/remove/up/down) the domain generation is stepped and a new version of node record is sent to inform the neighbors about this change. The domain generation helps the receiver of a domain record to know if it should ignore or process the record.</p>
<dt><code>applied_node_status</code></p>
<dd>The node status reported by the peer node for the succeeding peers in the node list. The Node list is a circular list of ascending addresses starting with the local node. Possible status are: U or D. The status U implies up and D down.</p>
<dt><code>[non_applied_node:status]</code></p>
<dd>Represents the nodes and their status as reported by the peer node. These nodes were not applied to the monitoring list for this peer node. They are usually transient and occur during the cluster startup phase or network reconfiguration. Possible status are: U or D. The status U implies up and D down.</dl>
<h3>Broadcast properties</h3>
<dl>
<dt><code>BROADCAST</code></p>
<dd>Forces all multicast traffic to be transmitted via broadcast only, irrespective of cluster size and number of destinations.</p>
<dt><code>REPLICAST</code></p>
<dd>Forces all multicast traffic to be transmitted via replicast only, irrespective of cluster size and number of destinations.</p>
<dt><code>AUTOSELECT</code></p>
<dd>Auto switching to broadcast or replicast depending on cluster size and destination node number.</p>
<dt><code>ratio SIZE</code></p>
<dd>Set the AUTOSELECT criteria, percentage of destination nodes vs cluster size. </p>
<h2>Examples</h2>
<p>tipc link monitor list</p>
<dl>
<dd>Shows the link monitoring information for cluster members on device data0.</dl>
<p> tipc link monitor summary</p>
<dl>
<dd>The monitor summary command prints the basic attributes.</dl>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
