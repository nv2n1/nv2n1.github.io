---
title: "radump(1)"
name: "radump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radump/"
description: "radump – tcpdump processing of the user data buffers from an argus(8) data file/stream."
---

<h2>NAME</h2>
<p> <code>radump</code> &#8211; tcpdump processing of the user data buffers from an <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file/stream. </p>
<h2>SYNOPSIS</h2>
<p> <code>radump</code> <code>-r</code> <i>argus-file [</i><code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Radump</code> reads <code>argus</code> data from an <i>argus</i> data stream or file, and prints out tcpdump style decoding of the user data buffers. </p>
<h2>OPTIONS</h2>
<p> Radump, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. </p>
<h2>EXAMPLE INVOCATION</h2>
<p> This example dumps the user capture buffers of arp traffic seen in the file. When there is no user buffer, or if the decoder can;t decode it, the length will 0. </p>
<pre><code>
% radump - r argus.file - s suser : 64 duser : 64 - N 5 - arp srcUdata dstUdata s[38] = "who-has 192.168.0.66 tell 192.168.0.68" d[36] = "192.168.0.68 is-at c8:2a:14:58:7a:55" s[37] = "who-has 192.168.0.1 tell 192.168.0.68" d[36] = "192.168.0.68 is-at 80:71:1f:3c:c3:88" s[37] = "who-has 192.168.0.1 tell 192.168.0.66" d[0] = "" s[37] = "who-has 192.168.0.1 tell 192.168.0.78" d[0] = "" s[38] = "who-has 192.168.0.34 tell 192.168.0.66" d[0] = ""
</code></pre>
<p> This example decodes the user capture buffers of DNS traffic seen in the file.<br />
% radump &#8211; s stime pkts suser : 64 duser : 64 &#8211; r ~ / argus / data / argus * 00.out.gz &#8211; port domain StartTime TotPkts srcUdata dstUdata 17 : 48 : 36.589949 2 s[37] = &#8220;48936+ [_] A? www.cylab.cmu.edu. (35)&#8221; d[32] = &#8220;48936 1/3/0 A 128.2.129.188 (64)&#8221; 17 : 48 : 36.590557 2 s[30] = &#8220;3018+ [_] A? qosient.com. (29)&#8221; d[31] = &#8220;3018 1/2/0 A 216.92.14.146 (64)&#8221; 17 : 48 : 36.708172 2 s[39] = &#8220;27243+ [_] A? ajax.googleapis.com. (37)&#8221; d[26] = &#8220;27243 2/4/4 CNAME[|domain]&#8221; 17 : 48 : 36.776033 2 s[31] = &#8220;45149+ [_] A? nsmwiki.org. (29)&#8221; d[33] = &#8220;45149 1/3/0 A 69.163.152.168 (64)&#8221; 17 : 48 : 36.776501 2 s[40] = &#8220;51781+ [_] A? www.surveymonkey.com. (38)&#8221; d[31] = &#8220;51781 1/13/0 A 75.98.93.51 (64)&#8221; 17 : 48 : 36.776655 2 s[31] = &#8220;38953+ [_] A? www.cmu.edu. (29)&#8221; d[51] = &#8220;38953 3/2/1 CNAME WWW-CMU.ANDREW.cmu.edu.,[|domain]&#8221; 17 : 48 : 36.777014 2 s[32] = &#8220;64748+ [_] A? www.cert.org. (30)&#8221; d[33] = &#8220;64748 1/2/0 A 192.88.209.244 (64)&#8221; 17 : 48 : 36.978293 2 s[44] = &#8220;53009+ [_] A? www.google-analytics.com. (42)&#8221; d[27] = &#8220;53009 17/4/4 CNAME[|domain]&#8221;</p>
<p> This example decodes the user capture buffers of HTTP traffic seen in the file. </p>
<pre><code>
radump - s stime proto dport pkts suser : 32 duser : 32 - r ~ / argus / data / argus * 00.out.gz - L0 - N5 - port http StartTime Proto Dport TotPkts srcUdata dstUdata 17 : 48 : 36.592155 tcp http 27 s[32] = "GET /research/cydat.html" d[32] = "HTTP/1.1 200 OK..Date: M" 17 : 48 : 36.632662 tcp http 24 s[32] = "GET /argus/ HTTP/1.1..Ho" d[32] = "HTTP/1.1 200 OK..Date: M" 17 : 48 : 36.705481 tcp http 23 s[32] = "GET /files/css/public.cs" d[32] = "HTTP/1.1 200 OK..Date: M" 17 : 48 : 36.705669 tcp http 11 s[32] = "GET /files/css/public_1c" d[32] = "HTTP/1.1 200 OK..Date: M" 17 : 48 : 36.705987 tcp http 15 s[32] = "GET /files/js/home.js HT" d[32] = "HTTP/1.1 200 OK..Date: M"
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
<h2>Index</h2>
