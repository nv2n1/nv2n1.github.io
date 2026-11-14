---
title: "tc-pfifo(8)"
name: "tc-pfifo"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-pfifo/"
description: "pfifo – Packet limited First In, First Out queue"
---

<p>pfifo &#8211; Packet limited First In, First Out queue </p>
<p> bfifo &#8211; Byte limited First In, First Out queue</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; add pfifo</code> <code>[ limit</code> packets <code>]</code> <code>tc qdisc &#8230; add bfifo</code> <code>[ limit</code> bytes <code>]</code> </p>
<h2>Description</h2>
<p>The pfifo and bfifo qdiscs are unadorned First In, First Out queues. They are the simplest queues possible and therefore have no overhead. <code>pfifo</code> constrains the queue size as measured in packets. <code>bfifo</code> does so as measured in bytes. Like all non-default qdiscs, they maintain statistics. This might be a reason to prefer pfifo or bfifo over the default. </p>
<h2>Algorithm</h2>
<p>A list of packets is maintained, when a packet is enqueued it gets inserted at the tail of a list. When a packet needs to be sent out to the network, it is taken from the head of the list. </p>
<p> If the list is too long, no further packets are allowed on. This is called &#8216;tail drop&#8217;.</p>
<h2>Parameters</h2>
<dl>
<dt>limit</p>
<dd>Maximum queue size. Specified in bytes for bfifo, in packets for pfifo. For pfifo, defaults to the interface txqueuelen, as specified with <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) or <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8). The range for this parameter is [0, UINT32_MAX]. </p>
<p> For bfifo, it defaults to the txqueuelen multiplied by the interface MTU. The range for this parameter is [0, UINT32_MAX] bytes. </p>
<p> Note: The link layer header was considered when counting packets length. </p>
</dl>
<h2>Output</h2>
<p>The output of <code>tc -s qdisc ls</code> contains the limit, either in packets or in bytes, and the number of bytes and packets actually sent. An unsent and dropped packet only appears between braces and is not counted as &#8216;Sent&#8217;. </p>
<p> In this example, the queue length is 100 packets, 45894 bytes were sent over 681 packets. No packets were dropped, and as the pfifo queue does not slow down packets, there were also no overlimits: </p>
<pre># tc -s qdisc ls dev eth0
qdisc pfifo 8001: dev eth0 limit 100p
 Sent 45894 bytes 681 pkts (dropped 0, overlimits 0)</pre>
<p>If a backlog occurs, this is displayed as well.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
<h2>Authors</h2>
<p>Alexey N. Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt; </p>
<p> This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
