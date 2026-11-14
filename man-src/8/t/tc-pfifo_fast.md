---
title: "tc-pfifo_fast(8)"
name: "tc-pfifo_fast"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-pfifo_fast/"
description: "pfifo_fast – three-band first in, first out queue"
---

<p>pfifo_fast &#8211; three-band first in, first out queue</p>
<h2>Description</h2>
<p>pfifo_fast is the default qdisc of each interface. Whenever an interface is created, the pfifo_fast qdisc is automatically used as a queue. If another qdisc is attached, it preempts the default pfifo_fast, which automatically returns to function when an existing qdisc is detached. In this sense this qdisc is magic, and unlike other qdiscs. </p>
<h2>Algorithm</h2>
<p>The algorithm is very similar to that of the classful <code><a href="/docs/linux/man/8-tc-prio/">tc-prio</a></code>(8) qdisc. <code>pfifo_fast</code> is like three <code><a href="/docs/linux/man/8-tc-pfifo/">tc-pfifo</a></code>(8) queues side by side, where packets can be enqueued in any of the three bands based on their Type of Service bits or assigned priority. </p>
<p> Not all three bands are dequeued simultaneously &#8211; as long as lower bands have traffic, higher bands are never dequeued. This can be used to prioritize interactive traffic or penalize &#8216;lowest cost&#8217; traffic. </p>
<p> Each band can be txqueuelen packets long, as configured with <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) or <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8). Additional packets coming in are not enqueued but are instead dropped. </p>
<p> See <code><a href="/docs/linux/man/8-tc-prio/">tc-prio</a></code>(8) for complete details on how TOS bits are translated into bands.</p>
<h2>Parameters</h2>
<dl>
<dt>txqueuelen</p>
<dd>The length of the three bands depends on the interface txqueuelen, as specified with <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) or <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8). </p>
</dl>
<h2>Bugs</h2>
<p>Does not maintain statistics and does not show up in tc qdisc ls. This is because it is the automatic default in the absence of a configured qdisc. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
<h2>Authors</h2>
<p>Alexey N. Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt; </p>
<p> This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
