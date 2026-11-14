---
title: "tc(8)"
name: "tc"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc/"
description: "tc – show / manipulate traffic control settings"
---

<p>tc &#8211; show / manipulate traffic control settings</p>
<h2>Synopsis</h2>
<p><code>tc</code> [ <i>OPTIONS</i> ] <code>qdisc [ add | change | replace | link | delete ] dev</code> <i>DEV</i> <code>[ parent</code> <i>qdisc-id</i> <code>| root ]</code> <code>[ handle</code> <i>qdisc-id</i> ] <code>[ ingress_block</code> <i>BLOCK_INDEX</i> ] <code>[ egress_block</code> <i>BLOCK_INDEX</i> ] qdisc [ qdisc specific parameters ] <code>tc</code> [ <i>OPTIONS</i> ] <code>class [ add | change | replace | delete ] dev</code> <i>DEV</i> <code>parent</code> <i>qdisc-id</i> <code>[ classid</code> <i>class-id</i> ] qdisc [ qdisc specific parameters ] <code>tc</code> [ <i>OPTIONS</i> ] <code>filter [ add | change | replace | delete | get ] dev</code> <i>DEV</i> <code>[ parent</code> <i>qdisc-id</i> <code>| root ] [ handle </code><i>filter-id</i> ] <code>protocol</code> <i>protocol</i> <code>prio</code> <i>priority</i> filtertype [ filtertype specific parameters ] <code>flowid</code> <i>flow-id</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>filter [ add | change | replace | delete | get ] block</code> <i>BLOCK_INDEX</i> <code>[ handle </code><i>filter-id</i> ] <code>protocol</code> <i>protocol</i> <code>prio</code> <i>priority</i> filtertype [ filtertype specific parameters ] <code>flowid</code> <i>flow-id</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>chain [ add | delete | get ] dev</code> <i>DEV</i> <code>[ parent</code> <i>qdisc-id</i> <code>| root ]</code> filtertype [ filtertype specific parameters ] <code>tc</code> [ <i>OPTIONS</i> ] <code>chain [ add | delete | get ] block</code> <i>BLOCK_INDEX</i> filtertype [ filtertype specific parameters ] <code>tc</code> [ <i>OPTIONS</i> ] [ <i>FORMAT</i> ] <code>qdisc { show | list } [ dev</code> <i>DEV</i> <code>] [ root | ingress | handle</code> <i>QHANDLE</i> <code>| parent</code> <i>CLASSID</i> <code>] [ invisible ]</code> <code>tc</code> [ <i>OPTIONS</i> ] [ <i>FORMAT</i> ] <code>class show dev</code> <i>DEV</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>filter show dev</code> <i>DEV</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>filter show block</code> <i>BLOCK_INDEX</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>chain show dev</code> <i>DEV</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>chain show block</code> <i>BLOCK_INDEX</i> <code>tc</code> [ <i>OPTIONS</i> ] <code>monitor [ file</code> <i>FILENAME</i> <code>]</code> </p>
<pre><code>OPTIONS := {

    [ -force ] -b[atch] [ filename ] |
    [ -n[etns] name ] |
    [ -N[umeric] ] |
    [ -nm | -nam[es] ] |
    [ { -cf | -c[onf] } [ filename ] ]
    [ -t[imestamp] ] | [ -t[short] | [
    -o[neline] ] }
FORMAT := {

    -s[tatistics] |
    -d[etails] |
    -r[aw] |
    -i[ec] |
    -g[raph] |
    -j[json] |
    -p[retty] |
    -col[or] }
</code></pre>
<h2>Description</h2>
<p><code>Tc</code> is used to configure Traffic Control in the Linux kernel. Traffic Control consists of the following:</p>
<dl>
<dt>SHAPING</p>
<dd>When traffic is shaped, its rate of transmission is under control. Shaping may be more than lowering the available bandwidth &#8211; it is also used to smooth out bursts in traffic for better network behaviour. Shaping occurs on egress.</p>
<dt>SCHEDULING</p>
<dd>By scheduling the transmission of packets it is possible to improve interactivity for traffic that needs it while still guaranteeing bandwidth to bulk transfers. Reordering is also called prioritizing, and happens only on egress.</p>
<dt>POLICING</p>
<dd>Whereas shaping deals with transmission of traffic, policing pertains to traffic arriving. Policing thus occurs on ingress.</p>
<dt>DROPPING</p>
<dd>Traffic exceeding a set bandwidth may also be dropped forthwith, both on ingress and on egress.  Processing of traffic is controlled by three kinds of objects: qdiscs, classes and filters. </p>
<h2>Qdiscs</h2>
<p><code>qdisc</code> is short for &#8216;queueing discipline&#8217; and it is elementary to understanding traffic control. Whenever the kernel needs to send a packet to an interface, it is <code>enqueued</code> to the qdisc configured for that interface. Immediately afterwards, the kernel tries to get as many packets as possible from the qdisc, for giving them to the network adaptor driver. </p>
<p> A simple QDISC is the &#8216;pfifo&#8217; one, which does no processing at all and is a pure First In, First Out queue. It does however store traffic when the network interface can&#8217;t handle it momentarily.</p>
<h2>Classes</h2>
<p>Some qdiscs can contain classes, which contain further qdiscs &#8211; traffic may then be enqueued in any of the inner qdiscs, which are within the <code>classes.</code> When the kernel tries to dequeue a packet from such a <code>classful qdisc</code> it can come from any of the classes. A qdisc may for example prioritize certain kinds of traffic by trying to dequeue from certain classes before others.</p>
<h2>Filters</h2>
<p>A <code>filter</code> is used by a classful qdisc to determine in which class a packet will be enqueued. Whenever traffic arrives at a class with subclasses, it needs to be classified. Various methods may be employed to do so, one of these are the filters. All filters attached to the class are called, until one of them returns with a verdict. If no verdict was made, other criteria may be available. This differs per qdisc. </p>
<p> It is important to notice that filters reside <code>within</code> qdiscs &#8211; they are not masters of what happens. </p>
<p> The available filters are:</p>
<dl>
<dt>basic</p>
<dd>Filter packets based on an ematch expression. See <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) for details.</p>
<dt>bpf</p>
<dd>Filter packets using (e)BPF, see <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8) for details.</p>
<dt>cgroup</p>
<dd>Filter packets based on the control group of their process. See <code><a href="/docs/linux/man/8-tc-cgroup/">tc-cgroup</a></code>(8) for details.</p>
<dt>flow, flower</p>
<dd>Flow-based classifiers, filtering packets based on their flow (identified by selectable keys). See <code><a href="/docs/linux/man/8-tc-flow/">tc-flow</a></code>(8) and <code><a href="/docs/linux/man/8-tc-flower/">tc-flower</a></code>(8) for details.</p>
<dt>fw</p>
<dd>Filter based on fwmark. Directly maps fwmark value to traffic class. See <code><a href="/docs/linux/man/8-tc-fw/">tc-fw</a></code>(8).</p>
<dt>route</p>
<dd>Filter packets based on routing table. See <code><a href="/docs/linux/man/8-tc-route/">tc-route</a></code>(8) for details.</p>
<dt>rsvp</p>
<dd>Match Resource Reservation Protocol (RSVP) packets.</p>
<dt>tcindex</p>
<dd>Filter packets based on traffic control index. See <code><a href="/docs/linux/man/8-tc-tcindex/">tc-tcindex</a></code>(8).</p>
<dt>u32</p>
<dd>Generic filtering on arbitrary packet data, assisted by syntax to abstract common operations. See <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8) for details.</p>
<dt>matchall</p>
<dd>Traffic control filter that matches every packet. See <code><a href="/docs/linux/man/8-tc-matchall/">tc-matchall</a></code>(8) for details. </p>
</dl>
<h2>Qevents</h2>
<p>Qdiscs may invoke user-configured actions when certain interesting events take place in the qdisc. Each qevent can either be unused, or can have a block attached to it. To this block are then attached filters using the &quot;tc block BLOCK_IDX&quot; syntax. The block is executed when the qevent associated with the attachment point takes place. For example, packet could be dropped, or delayed, etc., depending on the qdisc and the qevent in question. </p>
<p> For example: </p>
<dl>
<dd>tc qdisc add dev eth0 root handle 1: red limit 500K avpkt 1K \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qevent early_drop block 10</dl>
<dl>
<dd>tc filter add block 10 matchall action mirred egress mirror dev eth1</dl>
<h2>Classless Qdiscs</h2>
<p>The classless qdiscs are:</p>
<dl>
<dt>choke</p>
<dd>CHOKe (CHOose and Keep for responsive flows, CHOose and Kill for unresponsive flows) is a classless qdisc designed to both identify and penalize flows that monopolize the queue. CHOKe is a variation of RED, and the configuration is similar to RED.</p>
<dt>codel</p>
<dd>CoDel (pronounced &quot;coddle&quot;) is an adaptive &quot;no-knobs&quot; active queue management algorithm (AQM) scheme that was developed to address the shortcomings of RED and its variants.</p>
<dt>[p|b]fifo</p>
<dd>Simplest usable qdisc, pure First In, First Out behaviour. Limited in packets or in bytes.</p>
<dt>fq</p>
<dd>Fair Queue Scheduler realises TCP pacing and scales to millions of concurrent flows per qdisc.</p>
<dt>fq_codel</p>
<dd>Fair Queuing Controlled Delay is queuing discipline that combines Fair Queuing with the CoDel AQM scheme. FQ_Codel uses a stochastic model to classify incoming packets into different flows and is used to provide a fair share of the bandwidth to all the flows using the queue. Each such flow is managed by the CoDel queuing discipline. Reordering within a flow is avoided since Codel internally uses a FIFO queue.</p>
<dt>fq_pie</p>
<dd>FQ-PIE (Flow Queuing with Proportional Integral controller Enhanced) is a queuing discipline that combines Flow Queuing with the PIE AQM scheme. FQ-PIE uses a Jenkins hash function to classify incoming packets into different flows and is used to provide a fair share of the bandwidth to all the flows using the qdisc. Each such flow is managed by the PIE algorithm.</p>
<dt>gred</p>
<dd>Generalized Random Early Detection combines multiple RED queues in order to achieve multiple drop priorities. This is required to realize Assured Forwarding (RFC 2597).</p>
<dt>hhf</p>
<dd>Heavy-Hitter Filter differentiates between small flows and the opposite, heavy-hitters. The goal is to catch the heavy-hitters and move them to a separate queue with less priority so that bulk traffic does not affect the latency of critical traffic.</p>
<dt>ingress</p>
<dd>This is a special qdisc as it applies to incoming traffic on an interface, allowing for it to be filtered and policed.</p>
<dt>mqprio</p>
<dd>The Multiqueue Priority Qdisc is a simple queuing discipline that allows mapping traffic flows to hardware queue ranges using priorities and a configurable priority to traffic class mapping. A traffic class in this context is a set of contiguous qdisc classes which map 1:1 to a set of hardware exposed queues.</p>
<dt>multiq</p>
<dd>Multiqueue is a qdisc optimized for devices with multiple Tx queues. It has been added for hardware that wishes to avoid head-of-line blocking. It will cycle though the bands and verify that the hardware queue associated with the band is not stopped prior to dequeuing a packet.</p>
<dt>netem</p>
<dd>Network Emulator is an enhancement of the Linux traffic control facilities that allow to add delay, packet loss, duplication and more other characteristics to packets outgoing from a selected network interface.</p>
<dt>pfifo_fast</p>
<dd>Standard qdisc for &#8216;Advanced Router&#8217; enabled kernels. Consists of a three-band queue which honors Type of Service flags, as well as the priority that may be assigned to a packet.</p>
<dt>pie</p>
<dd>Proportional Integral controller-Enhanced (PIE) is a control theoretic active queue management scheme. It is based on the proportional integral controller but aims to control delay.</p>
<dt>red</p>
<dd>Random Early Detection simulates physical congestion by randomly dropping packets when nearing configured bandwidth allocation. Well suited to very large bandwidth applications.</p>
<dt>rr</p>
<dd>Round-Robin qdisc with support for multiqueue network devices. Removed from Linux since kernel version 2.6.27.</p>
<dt>sfb</p>
<dd>Stochastic Fair Blue is a classless qdisc to manage congestion based on packet loss and link utilization history while trying to prevent non-responsive flows (i.e. flows that do not react to congestion marking or dropped packets) from impacting performance of responsive flows. Unlike RED, where the marking probability has to be configured, BLUE tries to determine the ideal marking probability automatically.</p>
<dt>sfq</p>
<dd>Stochastic Fairness Queueing reorders queued traffic so each &#8216;session&#8217; gets to send a packet in turn.</p>
<dt>tbf</p>
<dd>The Token Bucket Filter is suited for slowing traffic down to a precisely configured rate. Scales well to large bandwidths.</dl>
<h2>Configuring Classless Qdiscs</h2>
<p>In the absence of classful qdiscs, classless qdiscs can only be attached at the root of a device. Full syntax: </p>
<p> <code>tc qdisc add dev</code> <i>DEV</i> <code>root</code> QDISC QDISC-PARAMETERS </p>
<p> To remove, issue </p>
<p> <code>tc qdisc del dev</code> <i>DEV</i> <code>root</code> </p>
<p> The <code>pfifo_fast</code> qdisc is the automatic default in the absence of a configured qdisc.</p>
<h2>Classful Qdiscs</h2>
<p>The classful qdiscs are:</p>
<dl>
<dt>ATM</p>
<dd>Map flows to virtual circuits of an underlying asynchronous transfer mode device.</p>
<dt>CBQ</p>
<dd>Class Based Queueing implements a rich linksharing hierarchy of classes. It contains shaping elements as well as prioritizing capabilities. Shaping is performed using link idle time calculations based on average packet size and underlying link bandwidth. The latter may be ill-defined for some interfaces.</p>
<dt>DRR</p>
<dd>The Deficit Round Robin Scheduler is a more flexible replacement for Stochastic Fairness Queuing. Unlike SFQ, there are no built-in queues &#8212; you need to add classes and then set up filters to classify packets accordingly. This can be useful e.g. for using RED qdiscs with different settings for particular traffic. There is no default class &#8212; if a packet cannot be classified, it is dropped.</p>
<dt>DSMARK</p>
<dd>Classify packets based on TOS field, change TOS field of packets based on classification.</p>
<dt>ETS</p>
<dd>The ETS qdisc is a queuing discipline that merges functionality of PRIO and DRR qdiscs in one scheduler. ETS makes it easy to configure a set of strict and bandwidth-sharing bands to implement the transmission selection described in 802.1Qaz.</p>
<dt>HFSC</p>
<dd>Hierarchical Fair Service Curve guarantees precise bandwidth and delay allocation for leaf classes and allocates excess bandwidth fairly. Unlike HTB, it makes use of packet dropping to achieve low delays which interactive sessions benefit from.</p>
<dt>HTB</p>
<dd>The Hierarchy Token Bucket implements a rich linksharing hierarchy of classes with an emphasis on conforming to existing practices. HTB facilitates guaranteeing bandwidth to classes, while also allowing specification of upper limits to inter-class sharing. It contains shaping elements, based on TBF and can prioritize classes.</p>
<dt>PRIO</p>
<dd>The PRIO qdisc is a non-shaping container for a configurable number of classes which are dequeued in order. This allows for easy prioritization of traffic, where lower classes are only able to send if higher ones have no packets available. To facilitate configuration, Type Of Service bits are honored by default.</p>
<dt>QFQ</p>
<dd>Quick Fair Queueing is an <a href="/docs/linux/man/1-o/">O</a>(1) scheduler that provides near-optimal guarantees, and is the first to achieve that goal with a constant cost also with respect to the number of groups and the packet length. The QFQ algorithm has no loops, and uses very simple instructions and data structures that lend themselves very well to a hardware implementation.</dl>
<h2>Theory Of Operation</h2>
<p>Classes form a tree, where each class has a single parent. A class may have multiple children. Some qdiscs allow for runtime addition of classes (CBQ, HTB) while others (PRIO) are created with a static number of children. </p>
<p> Qdiscs which allow dynamic addition of classes can have zero or more subclasses to which traffic may be enqueued. </p>
<p> Furthermore, each class contains a <code>leaf qdisc</code> which by default has <code>pfifo</code> behaviour, although another qdisc can be attached in place. This qdisc may again contain classes, but each class can have only one leaf qdisc. </p>
<p> When a packet enters a classful qdisc it can be <code>classified</code> to one of the classes within. Three criteria are available, although not all qdiscs will use all three:</p>
<dl>
<dt>tc filters</p>
<dd>If tc filters are attached to a class, they are consulted first for relevant instructions. Filters can match on all fields of a packet header, as well as on the firewall mark applied by iptables.</p>
<dt>Type of Service</p>
<dd>Some qdiscs have built in rules for classifying packets based on the TOS field.</p>
<dt>skb-&gt;priority</p>
<dd>Userspace programs can encode a <i>class-id</i> in the &#8216;skb-&gt;priority&#8217; field using the SO_PRIORITY option.</dl>
<p> Each node within the tree can have its own filters but higher level filters may also point directly to lower classes. </p>
<p> If classification did not succeed, packets are enqueued to the leaf qdisc attached to that class. Check qdisc specific manpages for details, however.</p>
<h2>Naming</h2>
<p>All qdiscs, classes and filters have IDs, which can either be specified or be automatically assigned. </p>
<p> IDs consist of a <code>major</code> number and a <code>minor</code> number, separated by a colon &#8211; <code>major</code>:<code>minor</code>. Both <code>major</code> and <code>minor</code> are hexadecimal numbers and are limited to 16 bits. There are two special values: root is signified by <code>major</code> and <code>minor</code> of all ones, and unspecified is all zeros. </p>
<dl>
<dt>QDISCS</p>
<dd>A qdisc, which potentially can have children, gets assigned a <code>major</code> number, called a &#8216;handle&#8217;, leaving the <code>minor</code> number namespace available for classes. The handle is expressed as &#8217;10:&#8217;. It is customary to explicitly assign a handle to qdiscs expected to have children. </p>
<dt>CLASSES</p>
<dd>Classes residing under a qdisc share their qdisc <code>major</code> number, but each have a separate <code>minor</code> number called a &#8216;classid&#8217; that has no relation to their parent classes, only to their parent qdisc. The same naming custom as for qdiscs applies. </p>
<dt>FILTERS</p>
<dd>Filters have a three part ID, which is only needed when using a hashed filter hierarchy. </p>
</dl>
<h2>Parameters</h2>
<p>The following parameters are widely used in TC. For other parameters, see the man pages for individual qdiscs. </p>
<dl>
<dt>RATES</p>
<dd>Bandwidths or rates. These parameters accept a floating point number, possibly followed by either a unit (both SI and IEC units supported), or a float followed by a &#8216;%&#8217; character to specify the rate as a percentage of the device&#8217;s speed (e.g. 5%, 99.5%). Warning: specifying the rate as a percentage means a fraction of the current speed; if the speed changes, the value will not be recalculated.</p>
<dl>
<dd>
<dl>
<dt>bit or a bare number</p>
<dd>Bits per second</p>
<dt>kbit</p>
<dd>Kilobits per second</p>
<dt>mbit</p>
<dd>Megabits per second</p>
<dt>gbit</p>
<dd>Gigabits per second</p>
<dt>tbit</p>
<dd>Terabits per second</p>
<dt>bps</p>
<dd>Bytes per second</p>
<dt>kbps</p>
<dd>Kilobytes per second</p>
<dt>mbps</p>
<dd>Megabytes per second</p>
<dt>gbps</p>
<dd>Gigabytes per second</p>
<dt>tbps</p>
<dd>Terabytes per second </p>
</dl>
<p> To specify in IEC units, replace the SI prefix (k-, m-, g-, t-) with IEC prefix (ki-, mi-, gi- and ti-) respectively. </p>
<p> TC store rates as a 32-bit unsigned integer in bps internally, so we can specify a max rate of 4294967295 bps.</dl>
<dt>TIMES</p>
<dd>Length of time. Can be specified as a floating point number followed by an optional unit:</p>
<dl>
<dd>
<dl>
<dt>s, sec or secs</p>
<dd>Whole seconds</p>
<dt>ms, msec or msecs</p>
<dd>Milliseconds</p>
<dt>us, usec, usecs or a bare number</p>
<dd>Microseconds. </p>
</dl>
<p> TC defined its own time unit (equal to microsecond) and stores time values as 32-bit unsigned integer, thus we can specify a max time value of 4294967295 usecs.</dl>
<dt>SIZES</p>
<dd>Amounts of data. Can be specified as a floating point number followed by an optional unit:</p>
<dl>
<dd>
<dl>
<dt>b or a bare number</p>
<dd>Bytes.</p>
<dt>kbit</p>
<dd>Kilobits</p>
<dt>kb or k</p>
<dd>Kilobytes</p>
<dt>mbit</p>
<dd>Megabits</p>
<dt>mb or m</p>
<dd>Megabytes</p>
<dt>gbit</p>
<dd>Gigabits</p>
<dt>gb or g</p>
<dd>Gigabytes </p>
</dl>
<p> TC stores sizes internally as 32-bit unsigned integer in byte, so we can specify a max size of 4294967295 bytes.</dl>
<dt>VALUES</p>
<dd>Other values without a unit. These parameters are interpreted as decimal by default, but you can indicate TC to interpret them as octal and hexadecimal by adding a &#8216;0&#8217; or &#8216;0x&#8217; prefix respectively. </p>
</dl>
<h2>Tc Commands</h2>
<p>The following commands are available for qdiscs, classes and filter:</p>
<dl>
<dt>add</p>
<dd>Add a qdisc, class or filter to a node. For all entities, a <code>parent</code> must be passed, either by passing its ID or by attaching directly to the root of a device. When creating a qdisc or a filter, it can be named with the <code>handle</code> parameter. A class is named with the <code>classid</code> parameter. </p>
<dt>delete</p>
<dd>A qdisc can be deleted by specifying its handle, which may also be &#8216;root&#8217;. All subclasses and their leaf qdiscs are automatically deleted, as well as any filters attached to them. </p>
<dt>change</p>
<dd>Some entities can be modified &#8216;in place&#8217;. Shares the syntax of &#8216;add&#8217;, with the exception that the handle cannot be changed and neither can the parent. In other words, <code>change</code> cannot move a node. </p>
<dt>replace</p>
<dd>Performs a nearly atomic remove/add on an existing node id. If the node does not exist yet it is created. </p>
<dt>get</p>
<dd>Displays a single filter given the interface <i>DEV</i>, <i>qdisc-id</i>, <i>priority</i>, <i>protocol</i> and <i>filter-id</i>. </p>
<dt>show</p>
<dd>Displays all filters attached to the given interface. A valid parent ID must be passed. </p>
<dt>link</p>
<dd>Only available for qdiscs and performs a replace where the node must exist already. </p>
</dl>
<h2>Monitor</h2>
<p>The<code>&nbsp;tc</code>&nbsp;utility can monitor events generated by the kernel such as adding/deleting qdiscs, filters or actions, or modifying existing ones. </p>
<p> The following command is available for<code>&nbsp;monitor</code>&nbsp;:</p>
<dl>
<dt><code>file</code></p>
<dd>If the file option is given, the <code>tc</code> does not listen to kernel events, but opens the given file and dumps its contents. The file has to be in binary format and contain netlink messages. </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-b,</code> -b filename,<code> -batch,</code> -batch filename</p>
<dd>read commands from provided file or standard input and invoke them. First failure will cause termination of tc. </p>
<dt><code>-force</code></p>
<dd>don&#8217;t terminate tc on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </p>
<dt><code>-o</code>,<code> -oneline</code></p>
<dd>output each record on a single line, replacing line feeds with the <code>&#8216;\&#8217;</code> character. This is convenient when you want to count records with <code><a href="/docs/linux/man/1-wc/">wc</a></code>(1) or to <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) the output. </p>
<dt><code>-n</code>,<code> -net</code>,<code> -netns </code>&lt;NETNS&gt;</p>
<dd>switches <code>tc</code> to the specified network namespace <i>NETNS</i>. Actually it just simplifies executing of: </p>
<p> <code>ip netns exec</code> <i>NETNS</i> <code>tc</code> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<p> to </p>
<p> <code>tc</code> -n[etns] <i>NETNS</i> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<dt><code>-N</code>,<code> -Numeric</code></p>
<dd>Print the number of protocol, scope, dsfield, etc directly instead of converting it to human readable name. </p>
<dt><code>-cf</code>,<code> -conf </code>&lt;FILENAME&gt;</p>
<dd>specifies path to the config file. This option is used in conjunction with other options (e.g. <code>-nm</code>). </p>
<dt><code>-t,</code> -timestamp</p>
<dd>When<code>&nbsp;tc monitor</code>&nbsp;runs, print timestamp before the event message in format:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Timestamp:&nbsp;&lt;Day&gt;&nbsp;&lt;Month&gt;&nbsp;&lt;DD&gt;&nbsp;&lt;hh:mm:ss&gt;&nbsp;&lt;YYYY&gt;&nbsp;&lt;usecs&gt;&nbsp;usec </p>
<dt><code>-ts,</code> -tshort</p>
<dd>When<code>&nbsp;tc monitor</code>&nbsp;runs, prints short timestamp before the event message in format:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&lt;YYYY&gt;-&lt;MM&gt;-&lt;DD&gt;T&lt;hh:mm:ss&gt;.&lt;ms&gt;] </p>
</dl>
<h2>Format</h2>
<p>The show command has additional formatting options: </p>
<dl>
<dt><code>-s</code>,<code> -stats,</code> -statistics</p>
<dd>output more statistics about packet usage. </p>
<dt><code>-d,</code> -details</p>
<dd>output more detailed information about rates and cell sizes. </p>
<dt><code>-r,</code> -raw</p>
<dd>output raw hex values for handles. </p>
<dt><code>-p,</code> -pretty</p>
<dd>for u32 filter, decode offset and mask values to equivalent filter commands based on TCP/IP. In JSON output, add whitespace to improve readability. </p>
<dt><code>-iec</code></p>
<dd>print rates in IEC units (ie. 1K = 1024). </p>
<dt><code>-g,</code> -graph</p>
<dd>shows classes as ASCII graph. Prints generic stats info under each class if <code>-s</code> option was specified. Classes can be filtered only by <code>dev</code> option. </p>
<dt><code>-c</code>[<code>color</code>][<code>=</code>{<code>always</code>|<code>auto</code>|<code>never</code>}</p>
<dd>Configure color output. If parameter is omitted or <code>always</code>, color output is enabled regardless of stdout state. If parameter is <code>auto</code>, stdout is checked to be a terminal before enabling color output. If parameter is <code>never</code>, color output is disabled. If specified multiple times, the last one takes precedence. This flag is ignored if <code>-json</code> is also given. </p>
<dt><code>-j,</code> -json</p>
<dd>Display results in JSON format. </p>
<dt><code>-nm</code>,<code> -name</code></p>
<dd>resolve class name from <code>/etc/iproute2/tc_cls</code> file or from file specified by <code>-cf</code> option. This file is just a mapping of <code>classid</code> to class name: </p>
<dl>
<dd># Here is comment</dl>
<dl>
<dd>1:40 voip # Here is another comment</dl>
<dl>
<dd>1:50 web</dl>
<dl>
<dd>1:60 ftp</dl>
<dl>
<dd>1:2 home</dl>
<dl>
<dd><code>tc</code> will not fail if <code>-nm</code> was specified without <code>-cf</code> option but <code>/etc/iproute2/tc_cls</code> file does not exist, which makes it possible to pass <code>-nm</code> option for creating <code>tc</code> alias.</dl>
<dt><code>-br</code>,<code> -brief</code></p>
<dd>Print only essential data needed to identify the filter and action (handle, cookie, etc.) and stats. This option is currently only supported by <code>tc filter show </code>and<code> tc actions ls </code>commands. </p>
</dl>
<h2>Examples</h2>
<p>tc -g class show dev eth0</p>
<dl>
<dd>Shows classes as ASCII graph on eth0 interface.</dl>
<p> tc -g -s class show dev eth0</p>
<dl>
<dd>Shows classes as ASCII graph with stats info under each class.</dl>
<h2>History</h2>
<p><code>tc</code> was written by Alexey N. Kuznetsov and added in Linux 2.2.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc-basic/">tc-basic</a></code>(8), <code><a href="/docs/linux/man/8-tc-bfifo/">tc-bfifo</a></code>(8), <code><a href="/docs/linux/man/8-tc-bpf/">tc-bpf</a></code>(8), <code><a href="/docs/linux/man/8-tc-cake/">tc-cake</a></code>(8), <code><a href="/docs/linux/man/8-tc-cbq/">tc-cbq</a></code>(8), <code><a href="/docs/linux/man/8-tc-cgroup/">tc-cgroup</a></code>(8), <code><a href="/docs/linux/man/8-tc-choke/">tc-choke</a></code>(8), <code><a href="/docs/linux/man/8-tc-codel/">tc-codel</a></code>(8), <code><a href="/docs/linux/man/8-tc-drr/">tc-drr</a></code>(8), <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8), <code><a href="/docs/linux/man/8-tc-ets/">tc-ets</a></code>(8), <code><a href="/docs/linux/man/8-tc-flow/">tc-flow</a></code>(8), <code><a href="/docs/linux/man/8-tc-flower/">tc-flower</a></code>(8), <code><a href="/docs/linux/man/8-tc-fq/">tc-fq</a></code>(8), <code><a href="/docs/linux/man/8-tc-fq_codel/">tc-fq_codel</a></code>(8), <code><a href="/docs/linux/man/8-tc-fq_pie/">tc-fq_pie</a></code>(8), <code><a href="/docs/linux/man/8-tc-fw/">tc-fw</a></code>(8), <code><a href="/docs/linux/man/7-tc-hfsc/">tc-hfsc</a></code>(7), <code><a href="/docs/linux/man/8-tc-hfsc/">tc-hfsc</a></code>(8), <code><a href="/docs/linux/man/8-tc-htb/">tc-htb</a></code>(8), <code><a href="/docs/linux/man/8-tc-mqprio/">tc-mqprio</a></code>(8), <code><a href="/docs/linux/man/8-tc-pfifo/">tc-pfifo</a></code>(8), <code><a href="/docs/linux/man/8-tc-pfifo_fast/">tc-pfifo_fast</a></code>(8), <code><a href="/docs/linux/man/8-tc-pie/">tc-pie</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8), <code><a href="/docs/linux/man/8-tc-route/">tc-route</a></code>(8), <code><a href="/docs/linux/man/8-tc-sfb/">tc-sfb</a></code>(8), <code><a href="/docs/linux/man/8-tc-sfq/">tc-sfq</a></code>(8), <code><a href="/docs/linux/man/8-tc-stab/">tc-stab</a></code>(8), <code><a href="/docs/linux/man/8-tc-tbf/">tc-tbf</a></code>(8), <code><a href="/docs/linux/man/8-tc-tcindex/">tc-tcindex</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8),<br />
 User documentation at <code><a rel="nofollow" href="http://lartc.org/">http://lartc.org/</a></code>, but please direct bugreports and patches to: <code>&lt;netdev [at] vger.kernel.org&gt;</code> </p>
<h2>Author</h2>
<p>Manpage maintained by bert hubert (ahu [at] ds9a.nl)</p>
