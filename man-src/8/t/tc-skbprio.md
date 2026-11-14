---
title: "tc-skbprio(8)"
name: "tc-skbprio"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-skbprio/"
description: "skbprio – SKB Priority Queue"
---

<p>skbprio &#8211; SKB Priority Queue</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; add skbprio</code> <code>[ limit</code> packets <code>]</code> </p>
<h2>Description</h2>
<p>SKB Priority Queue is a queueing discipline intended to prioritize the most important packets during a denial-of-service ( <code>DoS</code> ) attack. The priority of a packet is given by <code>skb-&gt;priority</code> , where a higher value places the packet closer to the exit of the queue. When the queue is full, the lowest priority packet in the queue is dropped to make room for the packet to be added if it has higher priority. If the packet to be added has lower priority than all packets in the queue, it is dropped. Without SKB priority queue, queue length limits must be imposed on individual sub-queues, and there is no straightforward way to enforce a global queue length limit across all priorities. SKBprio queue enforces a global queue length limit while not restricting the lengths of individual sub-queues. While SKB Priority Queue is agnostic to how <code>skb-&gt;priority</code> is assigned. A typical use case is to copy the 6-bit DS field of IPv4 and IPv6 packets using <code><a href="/docs/linux/man/8-tc-skbedit/">tc-skbedit</a></code>(8). If <code>skb-&gt;priority</code> is greater or equal to 64, the priority is assumed to be 63. Priorities less than 64 are taken at face value. SKB Priority Queue enables routers to locally decide which packets to drop under a DoS attack. Priorities should be assigned to packets such that the higher the priority, the more expected behavior a source shows. So sources have an incentive to play by the rules. </p>
<h2>Algorithm</h2>
<p>Skbprio maintains 64 lists (priorities go from 0 to 63). When a packet is enqueued, it gets inserted at the <code>tail</code> of its priority list. When a packet needs to be sent out to the network, it is taken from the head of the highest priority list. When the queue is full, the packet at the tail of the lowest priority list is dropped to serve the ingress packet &#8211; if it is of higher priority, otherwise the ingress packet is dropped. This algorithm allocates as much bandwidth as possible to high priority packets, while only servicing low priority packets when there is enough bandwidth.</p>
<h2>Parameters</h2>
<dl>
<dt>limit</p>
<dd>Maximum queue size specified in packets. It defaults to 64. The range for this parameter is [0, UINT32_MAX]. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc-prio/">tc-prio</a></code>(8), <code><a href="/docs/linux/man/8-tc-skbedit/">tc-skbedit</a></code>(8) </p>
<h2>Authors</h2>
<p>Nishanth Devarajan &lt;devarajn [at] uci.edu&gt;, Michel Machado &lt;michel [at] digirati.com.br&gt; </p>
<p> This manpage maintained by Bert Hubert &lt;ahu [at] ds9a.nl&gt;</p>
