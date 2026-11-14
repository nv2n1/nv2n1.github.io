---
title: "tc-etf(8)"
name: "tc-etf"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-etf/"
description: "ETF – Earliest TxTime First (ETF) Qdisc"
---

<p>ETF &#8211; Earliest TxTime First (ETF) Qdisc</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> dev <code>parent</code> classid <code>[ handle</code> major: <code>] etf clockid</code> clockid <code>[ delta</code> delta_nsecs <code>] [ deadline_mode ]</code> <code>[ offload ]</code> </p>
<h2>Description</h2>
<p>The ETF (Earliest TxTime First) qdisc allows applications to control the instant when a packet should be dequeued from the traffic control layer into the netdevice. If <code>offload</code> is configured and supported by the network interface card, the it will also control when packets leave the network controller. ETF achieves that by buffering packets until a configurable time before their transmission time (i.e. txtime, or deadline), which can be configured through the <code>delta</code> option. The qdisc uses a rb-tree internally so packets are always &#8216;ordered&#8217; by their txtime and will be dequeued following the (next) earliest txtime first. It relies on the SO_TXTIME socket option and the SCM_TXTIME CMSG in each packet field to configure the behavior of time dependent sockets: the clockid to be used as a reference, if the expected mode of txtime for that socket is deadline or strict mode, and if packet drops should be reported on the socket&#8217;s error queue. See <code><a href="/docs/linux/man/7-socket/">socket</a>(7)</code> for more information. The etf qdisc will drop any packets with a txtime in the past, or if a packet expires while waiting for being dequeued. This queueing discipline is intended to be used by TSN (Time Sensitive Networking) applications, and it exposes a traffic shaping functionality that is commonly documented as &quot;Launch Time&quot; or &quot;Time-Based Scheduling&quot; by vendors and the documentation of network interface controllers. ETF is meant to be installed under another qdisc that maps packet flows to traffic classes, one example is <code><a href="/docs/linux/man/8-mqprio/">mqprio</a>(8).</code> </p>
<h2>Parameters</h2>
<dl>
<dt>clockid</p>
<dd>Specifies the clock to be used by qdisc&#8217;s internal timer for measuring time and scheduling events. The qdisc expects that packets passing through it to be using this same <code>clockid</code> as the reference of their txtime timestamps. It will drop packets coming from sockets that do not comply with that. </p>
<p> For more information about time and clocks on Linux, please refer to <code><a href="/docs/linux/man/7-time/">time</a>(7)</code> and <code><a href="/docs/linux/man/3-clock_gettime/">clock_gettime</a>(3).</code> </p>
<dt>delta</p>
<dd>After enqueueing or dequeueing a packet, the qdisc will schedule its next wake-up time for the next txtime minus this delta value. This means <code>delta</code> can be used as a fudge factor for the scheduler latency of a system. This value must be specified in nanoseconds. The default value is 0 nanoseconds. </p>
<dt>deadline_mode</p>
<dd>When <code>deadline_mode</code> is set, the qdisc will handle txtime with a different semantics, changed from a &#8216;strict&#8217; transmission time to a deadline. In practice, this means during the dequeue flow <code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> will set the txtime of the packet being dequeued to &#8216;now&#8217;. The default is for this option to be disabled. </p>
<dt>offload</p>
<dd>When <code>offload</code> is set, <code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> will try to configure the network interface so time-based transmission arbitration is enabled in the controller. This feature is commonly referred to as &quot;Launch Time&quot; or &quot;Time-Based Scheduling&quot; by the documentation of network interface controllers. The default is for this option to be disabled. </p>
<dt>skip_sock_check</p>
<dd><code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> currently drops any packet which does not have a socket associated with it or if the socket does not have SO_TXTIME socket option set. But, this will not work if the launchtime is set by another entity inside the kernel (e.g. some other Qdisc). Setting the skip_sock_check will skip checking for a socket associated with the packet. </p>
</dl>
<h2>Examples</h2>
<p>ETF is used to enforce a Quality of Service. It controls when each packets should be dequeued and transmitted, and can be used for limiting the data rate of a traffic class. To separate packets into traffic classes the user may choose <code><a href="/docs/linux/man/8-mqprio/">mqprio</a>(8),</code> and configure it like this: # tc qdisc add dev eth0 handle 100: parent root mqprio num_tc 3 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>map 2 2 1 0 2 2 2 2 2 2 2 2 2 2 2 2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>queues 1@0 1@1 2@2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>hw 0<br />
 To replace the current queueing discipline by ETF in traffic class number 0, issue: # tc qdisc replace dev eth0 parent 100:1 etf \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>clockid CLOCK_TAI delta 300000 offload<br />
 With the options above, etf will be configured to use CLOCK_TAI as its clockid_t, will schedule packets for 300 us before their txtime, and will enable the functionality on that in the network interface card. Deadline mode will not be configured for this mode. </p>
<h2>Authors</h2>
<p>Jesus Sanchez-Palencia &lt;jesus.sanchez-palencia [at] intel.com&gt;<br />
 Vinicius Costa Gomes &lt;vinicius.gomes [at] intel.com&gt;</p>
