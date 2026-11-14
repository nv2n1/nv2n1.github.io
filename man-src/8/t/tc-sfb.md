---
title: "tc-sfb(8)"
name: "tc-sfb"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-sfb/"
description: "sfb – Stochastic Fair Blue"
---

<p>sfb &#8211; Stochastic Fair Blue</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; blue</code> <code>rehash</code> milliseconds <code>db</code> milliseconds <code>limit</code> packets <code>max</code> packets <code>target</code> packets <code>increment</code> float <code>decrement</code> float <code>penalty_rate</code> packets per second <code>penalty_burst</code> packets </p>
<h2>Description</h2>
<p>Stochastic Fair Blue is a classless qdisc to manage congestion based on packet loss and link utilization history while trying to prevent non-responsive flows (i.e. flows that do not react to congestion marking or dropped packets) from impacting performance of responsive flows. Unlike RED, where the marking probability has to be configured, BLUE tries to determine the ideal marking probability automatically. </p>
<h2>Algorithm</h2>
<p>The <code>BLUE</code> algorithm maintains a probability which is used to mark or drop packets that are to be queued. If the queue overflows, the mark/drop probability is increased. If the queue becomes empty, the probability is decreased. The <code>Stochastic Fair Blue</code> (SFB) algorithm is designed to protect TCP flows against non-responsive flows. </p>
<p> This SFB implementation maintains 8 levels of 16 bins each for accounting. Each flow is mapped into a bin of each level using a per-level hash value. </p>
<p> Every bin maintains a marking probability, which gets increased or decreased based on bin occupancy. If the number of packets exceeds the size of that bin, the marking probability is increased. If the number drops to zero, it is decreased. </p>
<p> The marking probability is based on the minimum value of all bins a flow is mapped into, thus, when a flow does not respond to marking or gradual packet drops, the marking probability quickly reaches one. </p>
<p> In this case, the flow is rate-limited to <code>penalty_rate</code> packets per second.</p>
<h2>Limitations</h2>
<p>Due to SFBs nature, it is possible for responsive flows to share all of its bins with a non-responsive flow, causing the responsive flow to be misidentified as being non-responsive. </p>
<p> The probability of a responsive flow to be misidentified is dependent on the number of non-responsive flows, M. It is (1 &#8211; (1 &#8211; (1 / 16.0)) ** M) **8, so for example with 10 non-responsive flows approximately 0.2% of responsive flows will be misidentified. </p>
<p> To mitigate this, SFB performs performs periodic re-hashing to avoid misclassification for prolonged periods of time. </p>
<p> The default hashing method will use source and destination ip addresses and port numbers if possible, and also supports tunneling protocols. Alternatively, an external classifier can be configured, too.</p>
<h2>Parameters</h2>
<dl>
<dt>rehash</p>
<dd>Time interval in milliseconds when queue perturbation occurs to avoid erroneously detecting unrelated, responsive flows as being part of a non-responsive flow for prolonged periods of time. Defaults to 10 minutes.</p>
<dt>db</p>
<dd>Double buffering warmup wait time, in milliseconds. To avoid destroying the probability history when rehashing is performed, this implementation maintains a second set of levels/bins as described in section 4.4 of the SFB reference. While one set is used to manage the queue, a second set is warmed up: Whenever a flow is then determined to be non-responsive, the marking probabilities in the second set are updated. When the rehashing happens, these bins will be used to manage the queue and all non-responsive flows can be rate-limited immediately. This value determines how much time has to pass before the 2nd set will start to be warmed up. Defaults to one minute, should be lower than <code>rehash.</code></p>
<dt>limit</p>
<dd>Hard limit on the real (not average) total queue size in packets. Further packets are dropped. Defaults to the transmit queue length of the device the qdisc is attached to.</p>
<dt>max</p>
<dd>Maximum length of a buckets queue, in packets, before packets start being dropped. Should be slightly larger than <code>target</code> , but should not be set to values exceeding 1.5 times that of <code>target .</code> Defaults to 25.</p>
<dt>target</p>
<dd>The desired average bin length. If the bin queue length reaches this value, the marking probability is increased by <code>increment.</code> The default value depends on the <code>max</code> setting, with max set to 25 <code>target</code> will default to 20.</p>
<dt>increment</p>
<dd>A value used to increase the marking probability when the queue appears to be over-used. Must be between 0 and 1.0. Defaults to 0.00050.</p>
<dt>decrement</p>
<dd>Value used to decrease the marking probability when the queue is found to be empty. Must be between 0 and 1.0. Defaults to 0.00005.</p>
<dt>penalty_rate</p>
<dd>The maximum number of packets belonging to flows identified as being non-responsive that can be enqueued per second. Once this number has been reached, further packets of such non-responsive flows are dropped. Set this to a reasonable fraction of your uplink throughput; the default value of 10 packets is probably too small.</p>
<dt>penalty_burst</p>
<dd>The number of packets a flow is permitted to exceed the penalty rate before packets start being dropped. Defaults to 20 packets. </p>
</dl>
<h2>Statistics</h2>
<p>This qdisc exposes additional statistics via &#8216;tc -s qdisc&#8217; output. These are:</p>
<dl>
<dt>earlydrop</p>
<dd>The number of packets dropped before a per-flow queue was full.</p>
<dt>ratedrop</p>
<dd>The number of packets dropped because of rate-limiting. If this value is high, there are many non-reactive flows being sent through sfb. In such cases, it might be better to embed sfb within a classful qdisc to better control such flows using a different, shaping qdisc.</p>
<dt>bucketdrop</p>
<dd>The number of packets dropped because a per-flow queue was full. High bucketdrop may point to a high number of aggressive, short-lived flows.</p>
<dt>queuedrop</p>
<dd>The number of packets dropped due to reaching limit. This should normally be 0.</p>
<dt>marked</p>
<dd>The number of packets marked with ECN.</p>
<dt>maxqlen</p>
<dd>The length of the current longest per-flow (virtual) queue.</p>
<dt>maxprob</p>
<dd>The maximum per-flow drop probability. 1 means that some flows have been detected as non-reactive. </p>
</dl>
<h2>Notes</h2>
<p>SFB automatically enables use of Explicit Congestion Notification (ECN). Also, this SFB implementation does not queue packets itself. Rather, packets are enqueued to the inner qdisc (defaults to pfifo). Because sfb maintains virtual queue states, the inner qdisc must not drop a packet previously queued. Furthermore, if a buckets queue has a very high marking rate, this implementation will start dropping packets instead of marking them, as such a situation points to either bad congestion, or an unresponsive flow. </p>
<h2>EXAMPLE &amp; USAGE</h2>
<p>To attach to interface $DEV, using default options: </p>
<p> # tc qdisc add dev $DEV handle 1: root sfb </p>
<p> Only use destination ip addresses for assigning packets to bins, perturbing hash results every 10 minutes: </p>
<p> # tc filter add dev $DEV parent 1: handle 1 flow hash keys dst perturb 600</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8), <code><a href="/docs/linux/man/8-tc-sfq/">tc-sfq</a></code>(8)</p>
<h2>Sources</h2>
<dl>
<dt>o</p>
<dd>W. Feng, D. Kandlur, D. Saha, K. Shin, BLUE: A New Class of Active Queue Management Algorithms, U. Michigan CSE-TR-387-99, April 1999. </p>
</dl>
<h2>Authors</h2>
<p>This SFB implementation was contributed by Juliusz Chroboczek and Eric Dumazet.</p>
