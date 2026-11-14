---
title: "tc-gate(8)"
name: "tc-gate"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-gate/"
description: "gate – Stream Gate Action"
---

<p>gate &#8211; Stream Gate Action</p>
<h2>Synopsis</h2>
<p><code>tc &#8230; action gate</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>[ base-time</code> BASETIME ] <code>[ clockid</code> CLOCKID ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;gate state&gt; &lt;interval 1&gt; [ &lt;internal priority&gt; &lt;max octets&gt; ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;gate state&gt; &lt;interval 2&gt; [ &lt;internal priority&gt; &lt;max octets&gt; ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;gate state&gt; &lt;interval 3&gt; [ &lt;internal priority&gt; &lt;max octets&gt; ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>&#8230;&#8230;</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>sched-entry</code> &lt;gate state&gt; &lt;interval N&gt; [ &lt;internal priority&gt; &lt;max octets&gt; ] </p>
<h2>Description</h2>
<p>GATE action allows specified ingress frames can be passed at specific time slot, or be dropped at specific time slot. Tc filter filters the ingress frames, then tc gate action would specify which time slot and how many bytes these frames can be passed to device and which time slot frames would be dropped. Gate action also assign a base-time to tell when the entry list start. Then gate action would start to repeat the gate entry list cyclically at the start base-time. For the software simulation, gate action requires the user assign reference time clock type. </p>
<h2>Parameters</h2>
<dl>
<dt>base-time</p>
<dd>Specifies the instant in nanoseconds, defining the time when the schedule starts. If &#8216;base-time&#8217; is a time in the past, the schedule will start at </p>
<p> base-time + (N * cycle-time) </p>
<p> where N is the smallest integer so the resulting time is greater than &quot;now&quot;, and &quot;cycle-time&quot; is the sum of all the intervals of the entries in the schedule. Without base-time specified, will default to be 0. </p>
<dt>clockid</p>
<dd>Specifies the clock to be used by qdisc&#8217;s internal timer for measuring time and scheduling events. Not valid if gate action is used for offloading filter. For example, tc filter command with <code>skip_sw</code> parameter. </p>
<dt>sched-entry</p>
<dd>There may multiple <code>sched-entry</code> parameters in a single schedule. Each one has the format: </p>
<p> sched-entry &lt;gate state&gt; &lt;interval&gt; [ &lt;internal priority&gt; &lt;max octets&gt; ] </p>
<p> &lt;gate state&gt; means gate states. &#8216;open&#8217; keep gate open, &#8216;close&#8217; keep gate close.<br />
 &lt;interval&gt; means how much nano seconds for this time slot.<br />
 &lt;internal priority&gt; means internal priority value. Present of the internal receiving queue for this stream. &quot;-1&quot; means wildcard. &lt;internal priority&gt; and &lt;max octets&gt; can be omit default to be &quot;-1&quot; which both<br />
&nbsp;value to be&nbsp;&quot;-1&quot;&nbsp;for this&nbsp;&lt;sched-entry&gt;.<br />
 &lt;max octets&gt; means how many octets size could pass in this time slot. Dropped if overlimited. &quot;-1&quot; means wildcard. &lt;max octets&gt; can be omit default to be &quot;-1&quot; which value to be &quot;-1&quot; for this &lt;sched-entry&gt;.<br />
 Note that &lt;internal priority&gt; and &lt;max octets&gt; are nothing meaning for gate state is &quot;close&quot; in a &quot;sched-entry&quot;. All frames are dropped when &quot;sched-entry&quot; with &quot;close&quot; state. </p>
</dl>
<h2>Examples</h2>
<p>The following example shows tc filter frames source ip match to the 192.168.0.20 will keep the gate open for 200ms and limit the traffic to 8MB in this sched-entry. Then keep the traffic gate to be close for 100ms. Frames arrived at gate close state would be dropped. Then the cycle would run the gate entries periodically. The schedule will start at instant 200.0s using the reference CLOCK_TAI. The schedule is composed of two entries each of 300ms duration. # tc qdisc add dev eth0 ingress # tc filter add dev eth0 parent ffff: protocol ip \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flower skip_hw src_ip 192.168.0.20&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action gate index 2 clockid CLOCK_TAI&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base-time 200000000000ns&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry open 200000000ns -1 8000000b&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched-entry close 100000000ns Following commands is an example to filter a stream source mac match to the 10:00:80:00:00:00 icmp frames will be dropped at any time with cycle 200ms. With a default basetime 0 and clockid is CLOCK_TAI as default. # tc qdisc add dev eth0 ingress # tc filter add dev eth0 parent ffff: protocol ip \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>flower ip_proto icmp dst_mac 10:00:80:00:00:00 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action gate index 12 sched-entry close 200000000ns</p>
<h2>Authors</h2>
<p>Po Liu &lt;Po.Liu [at] nxp.com&gt;</p>
