---
title: "tc-red(8)"
name: "tc-red"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-red/"
description: "red – Random Early Detection"
---

<p>red &#8211; Random Early Detection</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; red</code> <code>limit</code> bytes <code>[ min</code> bytes <code>] [ max</code> bytes <code>] avpkt</code> bytes <code>[ burst</code> packets <code>] [ ecn ] [ harddrop ] [ nodrop ] [ bandwidth</code> rate <code>] [ probability</code> chance <code>] [ adaptive ] [ qevent early_drop block</code> index <code>] [ qevent mark block</code> index <code>]</code> </p>
<h2>Description</h2>
<p>Random Early Detection is a classless qdisc which manages its queue size smartly. Regular queues simply drop packets from the tail when they are full, which may not be the optimal behaviour. RED also performs tail drop, but does so in a more gradual way. </p>
<p> Once the queue hits a certain average length, packets enqueued have a configurable chance of being marked (which may mean dropped). This chance increases linearly up to a point called the <code>max</code> average queue length, although the queue might get bigger. </p>
<p> This has a host of benefits over simple taildrop, while not being processor intensive. It prevents synchronous retransmits after a burst in traffic, which cause further retransmits, etc. </p>
<p> The goal is to have a small queue size, which is good for interactivity while not disturbing TCP/IP traffic with too many sudden drops after a burst of traffic. </p>
<p> Depending on if ECN is configured, marking either means dropping or purely marking a packet as overlimit.</p>
<h2>Algorithm</h2>
<p>The average queue size is used for determining the marking probability. This is calculated using an Exponential Weighted Moving Average, which can be more or less sensitive to bursts. </p>
<p> When the average queue size is below <code>min</code> bytes, no packet will ever be marked. When it exceeds <code>min,</code> the probability of doing so climbs linearly up to <code>probability,</code> until the average queue size hits <code>max</code> bytes. Because <code>probability</code> is normally not set to 100%, the queue size might conceivably rise above <code>max</code> bytes, so the <code>limit</code> parameter is provided to set a hard maximum for the size of the queue.</p>
<h2>Parameters</h2>
<dl>
<dt>min</p>
<dd>Average queue size at which marking becomes a possibility. Defaults to <code>max</code> /3 </p>
<dt>max</p>
<dd>At this average queue size, the marking probability is maximal. Should be at least twice <code>min</code> to prevent synchronous retransmits, higher for low <code>min.</code> Default to <code>limit</code> /4</p>
<dt>probability</p>
<dd>Maximum probability for marking, specified as a floating point number from 0.0 to 1.0. Suggested values are 0.01 or 0.02 (1 or 2%, respectively). Default : 0.02</p>
<dt>limit</p>
<dd>Hard limit on the real (not average) queue size in bytes. Further packets are dropped. Should be set higher than max+burst. It is advised to set this a few times higher than <code>max.</code></p>
<dt>burst</p>
<dd>Used for determining how fast the average queue size is influenced by the real queue size. Larger values make the calculation more sluggish, allowing longer bursts of traffic before marking starts. Real life experiments support the following guideline: (min+min+max)/(3*avpkt).</p>
<dt>avpkt</p>
<dd>Specified in bytes. Used with burst to determine the time constant for average queue size calculations. 1000 is a good value.</p>
<dt>bandwidth</p>
<dd>This rate is used for calculating the average queue size after some idle time. Should be set to the bandwidth of your interface. Does not mean that RED will shape for you! Optional. Default : 10Mbit</p>
<dt>ecn</p>
<dd>As mentioned before, RED can either &#8216;mark&#8217; or &#8216;drop&#8217;. Explicit Congestion Notification allows RED to notify remote hosts that their rate exceeds the amount of bandwidth available. Non-ECN capable hosts can only be notified by dropping a packet. If this parameter is specified, packets which indicate that their hosts honor ECN will only be marked and not dropped, unless the queue size hits <code>limit</code> bytes. Recommended.</p>
<dt>harddrop</p>
<dd>If average flow queue size is above <code>max</code> bytes, this parameter forces a drop instead of ecn marking.</p>
<dt>nodrop</p>
<dd>With this parameter, traffic that should be marked, but is not ECN-capable, is enqueued. Without the parameter it is early-dropped.</p>
<dt>adaptive</p>
<dd>(Added in linux-3.3) Sets RED in adaptive mode as described in <a rel="nofollow" href="http://icir.org/floyd/papers/adaptiveRed.pdf">http://icir.org/floyd/papers/adaptiveRed.pdf</a> </p>
<pre>Goal of Adaptive RED is to make 'probability' dynamic value between 1% and 50% to reach the target average queue :
<code>(max - min) / 2</code></pre>
</dl>
<h2>Qevents</h2>
<p>See tc (8) for some general notes about qevents. The RED qdisc supports the following qevents: </p>
<dl>
<dt>early_drop</p>
<dd>The associated block is executed when packets are early-dropped. This includes non-ECT packets in ECN mode.</p>
<dt>mark</p>
<dd>The associated block is executed when packets are marked in ECN mode. </p>
</dl>
<h2>Example</h2>
<p># tc qdisc add dev eth0 parent 1:1 handle 10: red<br />
&nbsp;limit 400000 min 30000 max 90000 avpkt 1000<br />
&nbsp;burst 55 ecn adaptive bandwidth 10Mbit </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-choke/">tc-choke</a></code>(8) </p>
<h2>Sources</h2>
<dl>
<dt>o</p>
<dd>Floyd, S., and Jacobson, V., Random Early Detection gateways for Congestion Avoidance. <a rel="nofollow" href="http://www.aciri.org/floyd/papers/red/red.html">http://www.aciri.org/floyd/papers/red/red.html</a></p>
<dt>o</p>
<dd>Some changes to the algorithm by Alexey N. Kuznetsov.</p>
<dt>o</p>
<dd>Adaptive RED : <a rel="nofollow" href="http://icir.org/floyd/papers/adaptiveRed.pdf">http://icir.org/floyd/papers/adaptiveRed.pdf</a> </p>
</dl>
<h2>Authors</h2>
<p>Alexey N. Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt;, Alexey Makarenko &lt;makar [at] phoenix.kharkov.ua&gt;, J Hadi Salim &lt;hadi [at] nortelnetworks.com&gt;, Eric Dumazet &lt;eric.dumazet [at] gmail.com&gt;. This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
