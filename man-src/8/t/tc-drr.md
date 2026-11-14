---
title: "tc-drr(8)"
name: "tc-drr"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-drr/"
description: "drr – deficit round robin scheduler"
---

<p>drr &#8211; deficit round robin scheduler</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; add drr</code> <code>[ quantum</code> bytes <code>]</code> </p>
<h2>Description</h2>
<p>The Deficit Round Robin Scheduler is a classful queuing discipline as a more flexible replacement for Stochastic Fairness Queuing. Unlike SFQ, there are no built-in queues &#8212; you need to add classes and then set up filters to classify packets accordingly. This can be useful e.g. for using RED qdiscs with different settings for particular traffic. There is no default class &#8212; if a packet cannot be classified, it is dropped. </p>
<h2>Algorithm</h2>
<p>Each class is assigned a deficit counter, initialized to <code>quantum.</code> </p>
<p> DRR maintains an (internal) &#8221;active&#8221; list of classes whose qdiscs are non-empty. This list is used for dequeuing. A packet is dequeued from the class at the head of the list if the packet size is smaller or equal to the deficit counter. If the counter is too small, it is increased by <code>quantum</code> and the scheduler moves on to the next class in the active list.</p>
<h2>Parameters</h2>
<dl>
<dt>quantum</p>
<dd>Amount of bytes a flow is allowed to dequeue before the scheduler moves to the next class. Defaults to the MTU of the interface. The minimum value is 1. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>To attach to device eth0, using the interface MTU as its quantum: </p>
<p> # tc qdisc add dev eth0 handle 1 root drr </p>
<p> Adding two classes: </p>
<p> # tc class add dev eth0 parent 1: classid 1:1 drr<br />
 # tc class add dev eth0 parent 1: classid 1:2 drr </p>
<p> You also need to add at least one filter to classify packets. </p>
<p> # tc filter add dev eth0 protocol .. classid 1:1 </p>
<p> Like SFQ, DRR is only useful when it owns the queue &#8212; it is a pure scheduler and does not delay packets. Attaching non-work-conserving qdiscs like tbf to it does not make sense &#8212; other qdiscs in the active list will also become inactive until the dequeue operation succeeds. Embed DRR within another qdisc like HTB or HFSC to ensure it owns the queue. </p>
<p> You can mimic SFQ behavior by assigning packets to the attached classes using the flow filter: </p>
<p> <code>tc qdisc add dev .. drr</code> </p>
<p> <code>for i in .. 1024;do</code><br />
 <code> tc class add dev .. classid $handle:$(print %x $i)</code><br />
 <code> tc qdisc add dev .. fifo limit 16</code><br />
 <code>done</code> </p>
<p> <code>tc filter add .. protocol ip .. $handle flow hash keys src,dst,proto,proto-src,proto-dst divisor 1024 perturb 10</code></p>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>M. Shreedhar and George Varghese &quot;Efficient Fair Queuing using Deficit Round Robin&quot;, Proc. SIGCOMM 95. </p>
</dl>
<h2>Notes</h2>
<p>This implementation does not drop packets from the longest queue on overrun, as limits are handled by the individual child qdiscs. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-htb/">tc-htb</a></code>(8), <code><a href="/docs/linux/man/8-tc-sfq/">tc-sfq</a></code>(8) </p>
<h2>Author</h2>
<p>sched_drr was written by Patrick McHardy.</p>
