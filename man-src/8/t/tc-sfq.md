---
title: "tc-sfq(8)"
name: "tc-sfq"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-sfq/"
description: "sfq – Stochastic Fairness Queueing"
---

<p>sfq &#8211; Stochastic Fairness Queueing</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230;</code> <code>[ divisor</code> hashtablesize <code>] [ limit</code> packets <code>] [ perturb</code> seconds <code>] [ quantum</code> bytes <code>] [ flows</code> number <code>] [ depth</code> number <code>] [ headdrop</code> <code>] [ redflowlimit</code> bytes <code>] [ min</code> bytes <code>] [ max</code> bytes <code>] [ avpkt</code> bytes <code>] [ burst</code> packets <code>] [ probability</code> P <code>] [ ecn</code> <code>] [ harddrop ]</code></p>
<h2>Description</h2>
<p>Stochastic Fairness Queueing is a classless queueing discipline available for traffic control with the <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) command. </p>
<p> SFQ does not shape traffic but only schedules the transmission of packets, based on &#8216;flows&#8217;. The goal is to ensure fairness so that each flow is able to send data in turn, thus preventing any single flow from drowning out the rest. </p>
<p> This may in fact have some effect in mitigating a Denial of Service attempt. </p>
<p> SFQ is work-conserving and therefore always delivers a packet if it has one available.</p>
<h2>Algorithm</h2>
<p>On enqueueing, each packet is assigned to a hash bucket, based on the packets hash value. This hash value is either obtained from an external flow classifier (use <code>tc filter</code> to set them), or a default internal classifier if no external classifier has been configured. </p>
<p> When the internal classifier is used, sfq uses</p>
<dl>
<dt>(i)</p>
<dd>Source address</p>
<dt>(ii)</p>
<dd>Destination address</p>
<dt>(iii)</p>
<dd>Source and Destination port</dl>
<p> If these are available. SFQ knows about ipv4 and ipv6 and also UDP, TCP and ESP. Packets with other protocols are hashed based on the 32bits representation of their destination and source. A flow corresponds mostly to a TCP/IP connection. </p>
<p> Each of these buckets should represent a unique flow. Because multiple flows may get hashed to the same bucket, sfqs internal hashing algorithm may be perturbed at configurable intervals so that the unfairness lasts only for a short while. Perturbation may however cause some inadvertent packet reordering to occur. After linux-3.3, there is no packet reordering problem, but possible packet drops if rehashing hits one limit (number of flows or packets per flow) </p>
<p> When dequeuing, each hashbucket with data is queried in a round robin fashion. </p>
<p> Before linux-3.3, the compile time maximum length of the SFQ is 128 packets, which can be spread over at most 128 buckets of 1024 available. In case of overflow, tail-drop is performed on the fullest bucket, thus maintaining fairness. </p>
<p> After linux-3.3, maximum length of SFQ is 65535 packets, and divisor limit is 65536. In case of overflow, tail-drop is performed on the fullest bucket, unless headdrop was requested.</p>
<h2>Parameters</h2>
<dl>
<dt>divisor</p>
<dd>Can be used to set a different hash table size, available from kernel 2.6.39 onwards. The specified divisor must be a power of two and cannot be larger than 65536. Default value: 1024.</p>
<dt>limit</p>
<dd>Upper limit of the SFQ. Can be used to reduce the default length of 127 packets. After linux-3.3, it can be raised.</p>
<dt>depth</p>
<dd>Limit of packets per flow (after linux-3.3). Default to 127 and can be lowered.</p>
<dt>perturb</p>
<dd>Interval in seconds for queue algorithm perturbation. Defaults to 0, which means that no perturbation occurs. Do not set too low for each perturbation may cause some packet reordering or losses. Advised value: 60 This value has no effect when external flow classification is used. Its better to increase divisor value to lower risk of hash collisions.</p>
<dt>quantum</p>
<dd>Amount of bytes a flow is allowed to dequeue during a round of the round robin process. Defaults to the MTU of the interface which is also the advised value and the minimum value.</p>
<dt>flows</p>
<dd>After linux-3.3, it is possible to change the default limit of flows. Default value is 127</p>
<dt>headdrop</p>
<dd>Default SFQ behavior is to perform tail-drop of packets from a flow. You can ask a headdrop instead, as this is known to provide a better feedback for TCP flows.</p>
<dt>redflowlimit</p>
<dd>Configure the optional RED module on top of each SFQ flow. Random Early Detection principle is to perform packet marks or drops in a probabilistic way. (man tc-red for details about RED) </p>
<pre>redflowlimit configures the hard limit on the real (not average) queue size per SFQ flow in bytes.</pre>
<dt>min</p>
<dd>Average queue size at which marking becomes a possibility. Defaults to <code>max</code> /3</p>
<dt>max</p>
<dd>At this average queue size, the marking probability is maximal. Defaults to <code>redflowlimit</code> /4</p>
<dt>probability</p>
<dd>Maximum probability for marking, specified as a floating point number from 0.0 to 1.0. Default value is 0.02</p>
<dt>avpkt</p>
<dd>Specified in bytes. Used with burst to determine the time constant for average queue size calculations. Default value is 1000</p>
<dt>burst</p>
<dd>Used for determining how fast the average queue size is influenced by the real queue size. </p>
<pre>Default value is :
<code>(2 * min + max) / (3 * avpkt)</code></pre>
<dt>ecn</p>
<dd>RED can either &#8216;mark&#8217; or &#8216;drop&#8217;. Explicit Congestion Notification allows RED to notify remote hosts that their rate exceeds the amount of bandwidth available. Non-ECN capable hosts can only be notified by dropping a packet. If this parameter is specified, packets which indicate that their hosts honor ECN will only be marked and not dropped, unless the queue size hits <code>depth</code> packets.</p>
<dt>harddrop</p>
<dd>If average flow queue size is above <code>max</code> bytes, this parameter forces a drop instead of ecn marking.</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>To attach to device ppp0: </p>
<p> # tc qdisc add dev ppp0 root sfq </p>
<p> Please note that SFQ, like all non-shaping (work-conserving) qdiscs, is only useful if it owns the queue. This is the case when the link speed equals the actually available bandwidth. This holds for regular phone modems, ISDN connections and direct non-switched ethernet links. </p>
<p> Most often, cable modems and DSL devices do not fall into this category. The same holds for when connected to a switch and trying to send data to a congested segment also connected to the switch. </p>
<p> In this case, the effective queue does not reside within Linux and is therefore not available for scheduling. </p>
<p> Embed SFQ in a classful qdisc to make sure it owns the queue. </p>
<p> It is possible to use external classifiers with sfq, for example to hash traffic based only on source/destination ip addresses: </p>
<p> # tc filter add &#8230; flow hash keys src,dst perturb 30 divisor 1024 </p>
<p> Note that the given divisor should match the one used by sfq. If you have changed the sfq default of 1024, use the same value for the flow hash filter, too. </p>
<p> Example of sfq with optional RED mode : </p>
<p> # tc qdisc add dev eth0 parent 1:1 handle 10: sfq limit 3000 flows 512 divisor 16384<br />
&nbsp;<wbr>&nbsp;redflowlimit 100000 min 8000 max 60000 probability 0.20 ecn headdrop</p>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>Paul E. McKenney &quot;Stochastic Fairness Queuing&quot;, IEEE INFOCOMM&#8217;90 Proceedings, San Francisco, 1990. </p>
<dt>o</p>
<dd>Paul E. McKenney &quot;Stochastic Fairness Queuing&quot;, &quot;Interworking: Research and Experience&quot;, v.2, 1991, p.113-131. </p>
<dt>o</p>
<dd>See also: M. Shreedhar and George Varghese &quot;Efficient Fair Queuing using Deficit Round Robin&quot;, Proc. SIGCOMM 95. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) </p>
<h2>Authors</h2>
<p>Alexey N. Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt;, Eric Dumazet &lt;eric.dumazet [at] gmail.com&gt;. </p>
<p> This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
