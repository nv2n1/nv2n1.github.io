---
title: "tc-fq(8)"
name: "tc-fq"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-fq/"
description: "FQ – Fair Queue traffic policing"
---

<p>FQ &#8211; Fair Queue traffic policing</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; fq</code> [ <code>limit</code> PACKETS ] [ <code>flow_limit</code> PACKETS ] [ <code>quantum</code> BYTES ] [ <code>initial_quantum</code> BYTES ] [ <code>maxrate</code> RATE ] [ <code>buckets</code> NUMBER ] [ <code>orphan_mask</code> NUMBER ] [ <code>pacing</code> | <code>nopacing</code> ] [ <code>ce_threshold</code> TIME ] </p>
<h2>Description</h2>
<p>FQ (Fair Queue) is a classless packet scheduler meant to be mostly used for locally generated traffic. It is designed to achieve per flow pacing. FQ does flow separation, and is able to respect pacing requirements set by TCP stack. All packets belonging to a socket are considered as a &#8216;flow&#8217;. For non local packets (router workload), packet hash is used as fallback. An application can specify a maximum pacing rate using the <code>SO_MAX_PACING_RATE</code> setsockopt call. This packet scheduler adds delay between packets to respect rate limitation set on each socket. Note that after linux-4.20, linux adopted EDT (Earliest Departure Time) and TCP directly sets the appropriate Departure Time for each skb. Dequeueing happens in a round-robin fashion. A special FIFO queue is reserved for high priority packets ( <code>TC_PRIO_CONTROL</code> priority), such packets are always dequeued first. FQ is non-work-conserving. TCP pacing is good for flows having idle times, as the congestion window permits TCP stack to queue a possibly large number of packets. This removes the &#8216;slow start after idle&#8217; choice, badly hitting large BDP flows and applications delivering chunks of data such as video streams. </p>
<h2>Parameters</h2>
<h3>limit</h3>
<p>Hard limit on the real queue size. When this limit is reached, new packets are dropped. If the value is lowered, packets are dropped so that the new limit is met. Default is 10000 packets.</p>
<h3>flow_limit</h3>
<p>Hard limit on the maximum number of packets queued per flow. Default value is 100.</p>
<h3>quantum</h3>
<p>The credit per dequeue RR round, i.e. the amount of bytes a flow is allowed to dequeue at once. A larger value means a longer time period before the next flow will be served. Default is 2 * interface MTU bytes.</p>
<h3>initial_quantum</h3>
<p>The initial sending rate credit, i.e. the amount of bytes a new flow is allowed to dequeue initially. This is specifically meant to allow using IW10 without added delay. Default is 10 * interface MTU, i.e. 15140 for &#8216;standard&#8217; ethernet.</p>
<h3>maxrate</h3>
<p>Maximum sending rate of a flow. Default is unlimited. Application specific setting via <code>SO_MAX_PACING_RATE</code> is ignored only if it is larger than this value.</p>
<h3>buckets</h3>
<p>The size of the hash table used for flow lookups. Each bucket is assigned a red-black tree for efficient collision sorting. Default: 1024.</p>
<h3>orphan_mask</h3>
<p>For packets not owned by a socket, fq is able to mask a part of skb-&gt;hash and reduce number of buckets associated with the traffic. This is a DDOS prevention mechanism, and the default is 1023 (meaning no more than 1024 flows are allocated for these packets)</p>
<h3>[no]pacing</h3>
<p>Enable or disable flow pacing. Default is enabled.</p>
<h3>ce_threshold</h3>
<p>sets a threshold above which all packets are marked with ECN Congestion Experienced. This is useful for DCTCP-style congestion control algorithms that require marking at very shallow queueing thresholds.</p>
<h2>Examples</h2>
<p>#tc qdisc add dev eth0 root fq ce_threshold 4ms<br />
 #tc -s -d qdisc show dev eth0<br />
 qdisc fq 8001: dev eth0 root refcnt 2 limit 10000p flow_limit 100p buckets 1024 orphan_mask 1023 quantum 3028b initial_quantum 15140b low_rate_threshold 550Kbit refill_delay 40.0ms ce_threshold 4.0ms<br />
&nbsp;Sent 72149092 bytes 48062 pkt&nbsp;(dropped 2176, overlimits 0 requeues 0)<br />
&nbsp;backlog 1937920b 1280p requeues 0<br />
&nbsp;<wbr>&nbsp;flows 34&nbsp;(inactive 17 throttled 0)<br />
&nbsp;<wbr>&nbsp;gc 0 highprio 0 throttled 0 ce_mark 47622 flows_plimit 2176</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>Authors</h2>
<p>FQ was written by Eric Dumazet.</p>
