---
title: "tc-codel(8)"
name: "tc-codel"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-codel/"
description: "CoDel – Controlled-Delay Active Queue Management algorithm"
---

<p>CoDel &#8211; Controlled-Delay Active Queue Management algorithm</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; codel</code> [ <code>limit</code> PACKETS ] [ <code>target</code> TIME ] [ <code>interval</code> TIME ] [ <code>ecn</code> | <code>noecn</code> ] [ <code>ce_threshold</code> TIME ] </p>
<h2>Description</h2>
<p>CoDel (pronounced &quot;coddle&quot;) is an adaptive &quot;no-knobs&quot; active queue management algorithm (AQM) scheme that was developed to address the shortcomings of RED and its variants. It was developed with the following goals in mind:<br />
&nbsp;o It should be parameterless.<br />
&nbsp;o It should keep delays low while permitting bursts of traffic.<br />
&nbsp;o It should control delay.<br />
&nbsp;o It should adapt dynamically to changing link rates with no impact on utilization.<br />
&nbsp;o It should be simple and efficient and should scale from simple to complex routers. </p>
<h2>Algorithm</h2>
<p>CoDel comes with three major innovations. Instead of using queue size or queue average, it uses the local minimum queue as a measure of the standing/persistent queue. Second, it uses a single state-tracking variable of the minimum delay to see where it is relative to the standing queue delay. Third, instead of measuring queue size in bytes or packets, it is measured in packet-sojourn time in the queue. </p>
<p> CoDel measures the minimum local queue delay (i.e. standing queue delay) and compares it to the value of the given acceptable queue delay <code>target.</code> As long as the minimum queue delay is less than <code>target</code> or the buffer contains fewer than MTU worth of bytes, packets are not dropped. Codel enters a dropping mode when the minimum queue delay has exceeded <code>target</code> for a time greater than <code>interval.</code> In this mode, packets are dropped at different drop times which is set by a control law. The control law ensures that the packet drops cause a linear change in the throughput. Once the minimum delay goes below <code>target,</code> packets are no longer dropped. </p>
<p> Additional details can be found in the paper cited below.</p>
<h2>Parameters</h2>
<h3>limit</h3>
<p>hard limit on the real queue size. When this limit is reached, incoming packets are dropped. If the value is lowered, packets are dropped so that the new limit is met. Default is 1000 packets.</p>
<h3>target</h3>
<p>is the acceptable minimum standing/persistent queue delay. This minimum delay is identified by tracking the local minimum queue delay that packets experience. Default and recommended value is 5ms.</p>
<h3>interval</h3>
<p>is used to ensure that the measured minimum delay does not become too stale. The minimum delay must be experienced in the last epoch of length <code>interval.</code> It should be set on the order of the worst-case RTT through the bottleneck to give endpoints sufficient time to react. Default value is 100ms.</p>
<h3>ecn | noecn</h3>
<p>can be used to mark packets instead of dropping them. If <code>ecn</code> has been enabled, <code>noecn</code> can be used to turn it off and vice-a-versa. By default, <code>ecn</code> is turned off.</p>
<h3>ce_threshold</h3>
<p>sets a threshold above which all packets are marked with ECN Congestion Experienced. This is useful for DCTCP-style congestion control algorithms that require marking at very shallow queueing thresholds.</p>
<h2>Examples</h2>
<p>&nbsp;#&nbsp;tc qdisc add dev eth0 root codel<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc codel 801b: dev eth0 root refcnt 2 limit 1000p target 5.0ms interval 100.0ms<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 245801662 bytes 275853 pkt&nbsp;(dropped 0, overlimits 0 requeues 24)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 24<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count 0 lastcount 0 ldelay 2us drop_next 0us<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maxpacket 7306 ecn_mark 0 drop_overlimit 0<br />
&nbsp;#&nbsp;tc qdisc add dev eth0 root codel limit 100 target 4ms interval 30ms ecn<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc codel 801c: dev eth0 root refcnt 2 limit 100p target 4.0ms interval 30.0ms ecn<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 237573074 bytes 268561 pkt&nbsp;(dropped 0, overlimits 0 requeues 5)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count 0 lastcount 0 ldelay 76us drop_next 0us<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maxpacket 2962 ecn_mark 0 drop_overlimit 0 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) </p>
<h2>Sources</h2>
<p>o Kathleen Nichols and Van Jacobson, &quot;Controlling Queue Delay&quot;, ACM Queue, <a rel="nofollow" href="http://queue.acm.org/detail.cfm?id=2209336">http://queue.acm.org/detail.cfm?id=2209336</a></p>
<h2>Authors</h2>
<p>CoDel was implemented by Eric Dumazet and David Taht. This manpage was written by Vijay Subramanian. Please reports corrections to the Linux Networking mailing list &lt;netdev [at] vger.kernel.org&gt;.</p>
