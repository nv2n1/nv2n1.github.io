---
title: "tc-taprio(8)"
name: "tc-taprio"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-taprio/"
description: "TAPRIO – Time Aware Priority Shaper"
---

<p>TAPRIO &#8211; Time Aware Priority Shaper</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> dev <code>parent</code> classid <code>[ handle</code> major: <code>] taprio num_tc</code> tcs<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>map</code> P0 P1 P2 &#8230; <code>queues</code> count1 [at] offset1 count2 [at] offset2 &#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>base-time</code> base-time <code>clockid</code> clockid<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;command 1&gt; &lt;gate mask 1&gt; &lt;interval 1&gt;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;command 2&gt; &lt;gate mask 2&gt; &lt;interval 2&gt;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;command 3&gt; &lt;gate mask 3&gt; &lt;interval 3&gt;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;command N&gt; &lt;gate mask N&gt; &lt;interval N&gt; </p>
<h2>Description</h2>
<p>The TAPRIO qdisc implements a simplified version of the scheduling state machine defined by IEEE 802.1Q-2018 Section 8.6.9, which allows configuration of a sequence of gate states, where each gate state allows outgoing traffic for a subset (potentially empty) of traffic classes. How traffic is mapped to different hardware queues is similar to <code><a href="/docs/linux/man/8-mqprio/">mqprio</a>(8)</code> and so the <code>map</code> and <code>queues</code> parameters have the same meaning. The other parameters specify the schedule, and at what point in time it should start (it can behave as the schedule started in the past). </p>
<h2>Parameters</h2>
<dl>
<dt>num_tc</p>
<dd>Number of traffic classes to use. Up to 16 classes supported. </p>
<dt>map</p>
<dd>The priority to traffic class map. Maps priorities 0..15 to a specified traffic class. See <code><a href="/docs/linux/man/8-mqprio/">mqprio</a>(8)</code> for more details. </p>
<dt>queues</p>
<dd>Provide count and offset of queue range for each traffic class. In the format, <code>count [at] offset.</code> Queue ranges for each traffic classes cannot overlap and must be a contiguous range of queues. </p>
<dt>base-time</p>
<dd>Specifies the instant in nanoseconds, using the reference of <code>clockid,</code> defining the time when the schedule starts. If &#8216;base-time&#8217; is a time in the past, the schedule will start at </p>
<p> base-time + (N * cycle-time) </p>
<p> where N is the smallest integer so the resulting time is greater than &quot;now&quot;, and &quot;cycle-time&quot; is the sum of all the intervals of the entries in the schedule; </p>
<dt>clockid</p>
<dd>Specifies the clock to be used by qdisc&#8217;s internal timer for measuring time and scheduling events. This argument must be omitted when using the full-offload feature (flags 0x2), since in that case, the clockid is implicitly /dev/ptpN (where N is given by <code>ethtool -T eth0 | grep &#8216;PTP Hardware Clock&#8217;</code> ), and therefore not necessarily synchronized with the system&#8217;s CLOCK_TAI. </p>
<dt>sched-entry</p>
<dd>There may multiple <code>sched-entry</code> parameters in a single schedule. Each one has the </p>
<p> sched-entry &lt;command&gt; &lt;gatemask&gt; &lt;interval&gt; </p>
<p> format. The only supported &lt;command&gt; is &quot;S&quot;, which means &quot;SetGateStates&quot;, following the IEEE 802.1Q-2018 definition (Table 8-7). &lt;gate mask&gt; is a bitmask where each bit is a associated with a traffic class, so bit 0 (the least significant bit) being &quot;on&quot; means that traffic class 0 is &quot;active&quot; for that schedule entry. &lt;interval&gt; is a time duration, in nanoseconds, that specifies for how long that state defined by &lt;command&gt; and &lt;gate mask&gt; should be held before moving to the next entry. </p>
<dt>flags</p>
<dd>This is a bit mask which specifies different modes for taprio.</p>
<dl>
<dd>
<dl>
<dt><i>0x1</i></p>
<dd>Enables the txtime-assist feature. In this mode, taprio will set the transmit timestamp depending on the interval in which the packet needs to be transmitted. It will then utililize the <code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> qdisc to sort and transmit the packets at the right time. The second example can be used as a reference to configure this mode.</p>
<dt><i>0x2</i></p>
<dd>Enables the full-offload feature. In this mode, taprio will pass the gate control list to the NIC which will execute it cyclically in hardware. When using full-offload, there is no need to specify the <code>clockid</code> argument. </p>
<p> The txtime-assist and full-offload features are mutually exclusive, i.e. setting flags to 0x3 is invalid.</dl>
</dl>
<dt>txtime-delay</p>
<dd>This parameter is specific to the txtime offload mode. It specifies the maximum time a packet might take to reach the network card from the taprio qdisc. The value should always be greater than the delta specified in the <code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> qdisc. </p>
</dl>
<h2>Examples</h2>
<p>The following example shows how an traffic schedule with three traffic classes (&quot;num_tc 3&quot;), which are separated different traffic classes, we are going to call these TC 0, TC 1 and TC 2. We could read the &quot;map&quot; parameter below as: traffic with priority 3 is classified as TC 0, priority 2 is classified as TC 1 and the rest is classified as TC 2. The schedule will start at instant 1528743495910289987 using the reference CLOCK_TAI. The schedule is composed of three entries each of 300us duration. # tc qdisc replace dev eth0 parent root handle 100 taprio \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_tc 3&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map 2 2 1 0 2 2 2 2 2 2 2 2 2 2 2 2&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;queues 1@0 1@1 2@2&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base-time 1528743495910289987&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 01 300000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 02 300000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 04 300000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clockid CLOCK_TAI Following is an example to enable the txtime offload mode in taprio. See <code><a href="/docs/linux/man/8-etf/">etf</a>(8)</code> for more information about configuring the ETF qdisc. # tc qdisc replace dev eth0 parent root handle 100 taprio \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_tc 3&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map 2 2 1 0 2 2 2 2 2 2 2 2 2 2 2 2&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;queues 1@0 1@0 1@0&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base-time 1528743495910289987&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 01 300000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 02 300000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 04 400000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags 0x1&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;txtime-delay 200000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clockid CLOCK_TAI # tc qdisc replace dev $IFACE parent 100:1 etf skip_skb_check \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offload delta 200000 clockid CLOCK_TAI The following is a schedule in full offload mode. The <code>base-time</code> is 200 ns and the <code>cycle-time</code> is implicitly calculated as the sum of all <code>sched-entry</code> durations (i.e. 20 us + 20 us + 60 us = 100 us). Although the base-time is in the past, the hardware will start executing the schedule at a PTP time equal to the smallest integer multiple of 100 us, plus 200 ns, that is larger than the NIC&#8217;s current PTP time. # tc qdisc add dev eth0 parent root taprio \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_tc 8&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map 0 1 2 3 4 5 6 7&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;queues 1@0 1@1 1@2 1@3 1@4 1@5 1@6 1@7&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base-time 200&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S 80 20000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S a0 20000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry S df 60000&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags 0x2 </p>
<h2>Authors</h2>
<p>Vinicius Costa Gomes &lt;vinicius.gomes [at] intel.com&gt;</p>
