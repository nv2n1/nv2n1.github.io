---
title: "tc-fq_codel(8)"
name: "tc-fq_codel"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-fq_codel/"
description: "CoDel – Fair Queuing (FQ) with Controlled Delay (CoDel)"
---

<p>CoDel &#8211; Fair Queuing (FQ) with Controlled Delay (CoDel)</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; fq_codel</code> [ <code>limit</code> PACKETS ] [ <code>flows</code> NUMBER ] [ <code>target</code> TIME ] [ <code>interval</code> TIME ] [ <code>quantum</code> BYTES ] [ <code>ecn</code> | <code>noecn</code> ] [ <code>ce_threshold</code> TIME ] [ <code>memory_limit</code> BYTES ] </p>
<h2>Description</h2>
<p>FQ_Codel (Fair Queuing Controlled Delay) is queuing discipline that combines Fair Queuing with the CoDel AQM scheme. FQ_Codel uses a stochastic model to classify incoming packets into different flows and is used to provide a fair share of the bandwidth to all the flows using the queue. Each such flow is managed by the CoDel queuing discipline. Reordering within a flow is avoided since Codel internally uses a FIFO queue. </p>
<h2>Parameters</h2>
<h3>limit</h3>
<p>has the same semantics as <code>codel</code> and is the hard limit on the real queue size. When this limit is reached, incoming packets are dropped. Default is 10240 packets.</p>
<h3>memory_limit</h3>
<p>sets a limit on the total number of bytes that can be queued in this FQ-CoDel instance. The lower of the packet limit of the <code>limit</code> parameter and the memory limit will be enforced. Default is 32 MB.</p>
<h3>flows</h3>
<p>is the number of flows into which the incoming packets are classified. Due to the stochastic nature of hashing, multiple flows may end up being hashed into the same slot. Newer flows have priority over older ones. This parameter can be set only at load time since memory has to be allocated for the hash table. Default value is 1024.</p>
<h3>target</h3>
<p>has the same semantics as <code>codel</code> and is the acceptable minimum standing/persistent queue delay. This minimum delay is identified by tracking the local minimum queue delay that packets experience. Default value is 5ms.</p>
<h3>interval</h3>
<p>has the same semantics as <code>codel</code> and is used to ensure that the measured minimum delay does not become too stale. The minimum delay must be experienced in the last epoch of length .B interval. It should be set on the order of the worst-case RTT through the bottleneck to give endpoints sufficient time to react. Default value is 100ms.</p>
<h3>quantum</h3>
<p>is the number of bytes used as &#8216;deficit&#8217; in the fair queuing algorithm. Default is set to 1514 bytes which corresponds to the Ethernet MTU plus the hardware header length of 14 bytes.</p>
<h3>ecn | noecn</h3>
<p>has the same semantics as <code>codel</code> and can be used to mark packets instead of dropping them. If <code>ecn</code> has been enabled, <code>noecn</code> can be used to turn it off and vice-a-versa. Unlike <code>codel, ecn</code> is turned on by default.</p>
<h3>ce_threshold</h3>
<p>sets a threshold above which all packets are marked with ECN Congestion Experienced. This is useful for DCTCP-style congestion control algorithms that require marking at very shallow queueing thresholds.</p>
<h2>Examples</h2>
<p>#tc qdisc add dev eth0 root fq_codel<br />
 #tc -s qdisc show<br />
 qdisc fq_codel 8002: dev eth0 root refcnt 2 limit 10240p flows 1024 quantum 1514<br />
&nbsp;target 5.0ms interval 100.0ms ecn<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 428514 bytes 2269 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maxpacket 256 drop_overlimit 0 new_flow_count 0 ecn_mark 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_flows_len 0 old_flows_len 0 #tc qdisc add dev eth0 root fq_codel limit 2000 target 3ms interval 40ms noecn<br />
 #tc -s qdisc show<br />
 qdisc fq_codel 8003: dev eth0 root refcnt 2 limit 2000p flows 1024 quantum 1514 target 3.0ms interval 40.0ms<br />
&nbsp;Sent 2588985006 bytes 1783629 pkt&nbsp;(dropped 0, overlimits 0 requeues 34869)<br />
&nbsp;backlog 0b 0p requeues 34869<br />
&nbsp;<wbr>&nbsp;maxpacket 65226 drop_overlimit 0 new_flow_count 73 ecn_mark 0<br />
&nbsp;<wbr>&nbsp;new_flows_len 1 old_flows_len 3 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-codel/">tc-codel</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) </p>
<h2>Authors</h2>
<p>FQ_CoDel was implemented by Eric Dumazet. This manpage was written by Vijay Subramanian. Please report corrections to the Linux Networking mailing list &lt;netdev [at] vger.kernel.org&gt;.</p>
