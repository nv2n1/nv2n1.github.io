---
title: "tc-mqprio(8)"
name: "tc-mqprio"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-mqprio/"
description: "MQPRIO – Multiqueue Priority Qdisc (Offloaded Hardware QOS)"
---

<p>MQPRIO &#8211; Multiqueue Priority Qdisc (Offloaded Hardware QOS)</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> dev <code>( parent</code> classid <code>| root) [ handle</code> major: <code>] mqprio [ num_tc</code> tcs <code>] [ map</code> P0 P1 P2&#8230; <code>] [ queues</code> count1 [at] offset1 count2 [at] offset2 &#8230; <code>] [ hw</code> 1|0 <code>] [ mode</code> dcb|channel] <code>] [ shaper</code> dcb| <code>[ bw_rlimit</code> <code>min_rate</code> min_rate1 min_rate2 &#8230; <code>max_rate</code> max_rate1 max_rate2 &#8230; <code>]]</code> </p>
<h2>Description</h2>
<p>The MQPRIO qdisc is a simple queuing discipline that allows mapping traffic flows to hardware queue ranges using priorities and a configurable priority to traffic class mapping. A traffic class in this context is a set of contiguous qdisc classes which map 1:1 to a set of hardware exposed queues. By default the qdisc allocates a pfifo qdisc (packet limited first in, first out queue) per TX queue exposed by the lower layer device. Other queuing disciplines may be added subsequently. Packets are enqueued using the <code>map</code> parameter and hashed across the indicated queues in the <code>offset</code> and <code>count.</code> By default these parameters are configured by the hardware driver to match the hardware QOS structures. <code>Channel</code> mode supports full offload of the mqprio options, the traffic classes, the queue configurations and QOS attributes to the hardware. Enabled hardware can provide hardware QOS with the ability to steer traffic flows to designated traffic classes provided by this qdisc. Hardware based QOS is configured using the <code>shaper</code> parameter. <code>bw_rlimit</code> with minimum and maximum bandwidth rates can be used for setting transmission rates on each traffic class. Also further qdiscs may be added to the classes of MQPRIO to create more complex configurations. </p>
<h2>Algorithm</h2>
<p>On creation with &#8216;tc qdisc add&#8217;, eight traffic classes are created mapping priorities 0..7 to traffic classes 0..7 and priorities greater than 7 to traffic class 0. This requires base driver support and the creation will fail on devices that do not support hardware QOS schemes. </p>
<p> These defaults can be overridden using the qdisc parameters. Providing the &#8216;hw 0&#8217; flag allows software to run without hardware coordination. </p>
<p> If hardware coordination is being used and arguments are provided that the hardware can not support then an error is returned. For many users hardware defaults should work reasonably well. </p>
<p> As one specific example numerous Ethernet cards support the 802.1Q link strict priority transmission selection algorithm (TSA). MQPRIO enabled hardware in conjunction with the classification methods below can provide hardware offloaded support for this TSA.</p>
<h2>Classification</h2>
<p>Multiple methods are available to set the SKB priority which MQPRIO uses to select which traffic class to enqueue the packet.</p>
<dl>
<dt>From user space</p>
<dd>A process with sufficient privileges can encode the destination class directly with SO_PRIORITY, see <code><a href="/docs/linux/man/7-socket/">socket</a>(7).</code></p>
<dt>with iptables/nftables</p>
<dd>An iptables/nftables rule can be created to match traffic flows and set the priority. <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code></p>
<dt>with net_prio cgroups</p>
<dd>The net_prio cgroup can be used to set the priority of all sockets belong to an application. See kernel and cgroup documentation for details. </p>
</dl>
<h2>Qdisc Parameters</h2>
<dl>
<dt>num_tc</p>
<dd>Number of traffic classes to use. Up to 16 classes supported. </p>
<dt>map</p>
<dd>The priority to traffic class map. Maps priorities 0..15 to a specified traffic class. </p>
<dt>queues</p>
<dd>Provide count and offset of queue range for each traffic class. In the format, <code>count [at] offset.</code> Queue ranges for each traffic classes cannot overlap and must be a contiguous range of queues. </p>
<dt>hw</p>
<dd>Set to <code>1</code> to support hardware offload. Set to <code>0</code> to configure user specified values in software only. </p>
<dt>mode</p>
<dd>Set to <code>channel</code> for full use of the mqprio options. Use <code>dcb</code> to offload only TC values and use hardware QOS defaults. Supported with &#8216;hw&#8217; set to 1 only. </p>
<dt>shaper</p>
<dd>Use <code>bw_rlimit</code> to set bandwidth rate limits for a traffic class. Use <code>dcb</code> for hardware QOS defaults. Supported with &#8216;hw&#8217; set to 1 only. </p>
<dt>min_rate</p>
<dd>Minimum value of bandwidth rate limit for a traffic class. </p>
<dt>max_rate</p>
<dd>Maximum value of bandwidth rate limit for a traffic class. </p>
</dl>
<h2>Authors</h2>
<p>John Fastabend, &lt;john.r.fastabend [at] intel.com&gt;</p>
