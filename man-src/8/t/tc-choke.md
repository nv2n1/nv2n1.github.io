---
title: "tc-choke(8)"
name: "tc-choke"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-choke/"
description: "choke – choose and keep scheduler"
---

<p>choke &#8211; choose and keep scheduler</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; choke</code> <code>limit</code> packets <code>min</code> packets <code>max</code> packets <code>avpkt</code> bytes <code>burst</code> packets <code>[ ecn ] [ bandwidth</code> rate <code>] probability</code> chance </p>
<h2>Description</h2>
<p>CHOKe (CHOose and Keep for responsive flows, CHOose and Kill for unresponsive flows) is a classless qdisc designed to both identify and penalize flows that monopolize the queue. CHOKe is a variation of RED, and the configuration is similar to RED. </p>
<h2>Algorithm</h2>
<p>Once the queue hits a certain average length, a random packet is drawn from the queue. If both the to-be-queued and the drawn packet belong to the same flow, both packets are dropped. Otherwise, if the queue length is still below the maximum length, the new packet has a configurable chance of being marked (which may mean dropped). If the queue length exceeds <code>max</code>, the new packet will always be marked (or dropped). If the queue length exceeds <code>limit</code>, the new packet is always dropped. </p>
<p> The marking probability computation is the same as used by the RED qdisc.</p>
<h2>Parameters</h2>
<p>The parameters are the same as for RED, except that RED uses bytes whereas choke counts packets. See <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) for a description.</p>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>R. Pan, B. Prabhakar, and K. Psounis, &quot;CHOKe, A Stateless Active Queue Management Scheme for Approximating Fair Bandwidth Allocation&quot;, IEEE INFOCOM, 2000.</p>
<dt>o</p>
<dd>A. Tang, J. Wang, S. Low, &quot;Understanding CHOKe: Throughput and Spatial Characteristics&quot;, IEEE/ACM Transactions on Networking, 2004 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) </p>
<h2>Author</h2>
<p>sched_choke was contributed by Stephen Hemminger.</p>
