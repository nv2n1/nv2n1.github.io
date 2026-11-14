---
title: "aecho(1)"
name: "aecho"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aecho/"
description: "aecho – send AppleTalk Echo Protocol packets to network hosts"
---

<h2 class="name">NAME</h2>
<p> aecho &#8211; send AppleTalk Echo Protocol packets to network hosts </p>
<h2>SYNOPSIS</h2>
<p> <code>aecho</code> [ <code>-c</code><i> count</i> ] ( <code>address</code> | <code>nbpname</code> )</p>
<h2>DESCRIPTION</h2>
<p> <code>aecho</code> repeatedly sends an Apple Echo Protocol (AEP) packet to the host specified by the given AppleTalk <code>address</code> or <code>nbpname</code> and reports whether a reply was received. Requests are sent at the rate of one per second. </p>
<p> <code>address</code> is parsed by <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3). <code>nbpname</code> is parsed by <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3). The nbp type defaults to `<code>Workstation</code>&#8216;. </p>
<p> When <code>aecho</code> is terminated, it reports the number of packets sent, the number of responses received, and the percentage of packets lost. If any responses were received, the minimum, average, and maximum round trip times are reported.</p>
<h2>EXAMPLE</h2>
<p> Check to see if a particular host is up and responding to AEP packets: </p>
<dl>
<dt>
<dd>
<pre><code>
example % aecho bloodsport 11 bytes from 8195.13 : aep_seq = 0. time = 10. ms 11 bytes from 8195.13 : aep_seq = 1. time = 10. ms 11 bytes from 8195.13 : aep_seq = 2. time = 10. ms 11 bytes from 8195.13 : aep_seq = 3. time = 10. ms 11 bytes from 8195.13 : aep_seq = 4. time = 10. ms 11 bytes from 8195.13 : aep_seq = 5. time = 9. ms ^ C-- --8195.13 AEP Statistics-- --6 packets sent, 6 packets received, 0 % packet loss round - trip(ms) min / avg / max = 9 / 9 / 10
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-c</code><i> count</i></p>
<dl>
<dt>
<dd> Stop after <i>count</i> packets.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ping/">ping</a></code>(1), <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3), <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3), <code><a href="/docs/linux/man/4-aep/">aep</a></code>(4), <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8). </p>
<h2>Index</h2>
