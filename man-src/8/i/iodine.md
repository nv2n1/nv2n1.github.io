---
title: "iodine(8)"
name: "iodine"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iodine/"
description: "iodine – tunnel IPv4 over DNS"
---

<p>iodine &#8211; tunnel IPv4 over DNS</p>
<h2>Synopsis</h2>
<p><code>iodine [-v]</code> <code>iodine [-h]</code> <code>iodine [-4] [-6] [-f] [-r] [-u</code> <i>user</i> <code>] [-P</code> <i>password</i> <code>] [-m</code> <i>fragsize</i> <code>] [-t</code> <i>chrootdir</i> <code>] [-d</code> <i>device</i> <code>] [-R</code> <i>rdomain</i> <code>] [-m</code> <i>fragsize</i> <code>] [-M</code> <i>namelen</i> <code>] [-z</code> <i>context</i> <code>] [-F</code> <i>pidfile</i> <code>] [-T</code> <i>dnstype</i> <code>] [-O</code> <i>downenc</i> <code>] [-L</code> <i>0|1</i> <code>] [-I</code> <i>interval</i> <code>]</code> <code>[</code> <i>nameserver</i> <code>]</code> <i>topdomain</i> </p>
<h2>Description</h2>
<p><code>iodine</code> lets you tunnel IPv4 data through a DNS server. This can be useful in situations where Internet access is firewalled, but DNS queries are allowed. It needs a TUN/TAP device to operate. The bandwidth is asymmetrical, with a measured maximum of 680 kbit/s upstream and 2.3 Mbit/s downstream in a wired LAN test network. Realistic sustained throughput on a Wifi network using a carrier-grade DNS cache has been measured at some 50 kbit/s upstream and over 200 kbit/s downstream. <code>iodine</code> is the client application, <code>iodined</code> is the server. </p>
<p> Note: server and client are required to speak the exact same protocol. In most cases, this means running the same iodine version. Unfortunately, implementing backward and forward protocol compatibility is usually not feasible.</p>
<h2>Options</h2>
<h3>Common Options:</h3>
<dl>
<dt><code>-v</code></p>
<dd>Print version info and exit.</p>
<dt><code>-h</code></p>
<dd>Print usage info and exit.</p>
<dt><code>-f</code></p>
<dd>Keep running in foreground.</p>
<dt><code>-u user</code></p>
<dd>Drop privileges and run as user &#8216;user&#8217; after setting up tunnel.</p>
<dt><code>-t chrootdir</code></p>
<dd>Chroot to &#8216;chrootdir&#8217; after setting up tunnel.</p>
<dt><code>-d device</code></p>
<dd>Use the TUN device &#8216;device&#8217; instead of the normal one, which is dnsX on Linux and otherwise tunX.</p>
<dt><code>-P password</code></p>
<dd>Use &#8216;password&#8217; to authenticate. If not used, <code>stdin</code> will be used as input. Only the first 32 characters will be used.</p>
<dt><code>-z context</code></p>
<dd>Apply SELinux &#8216;context&#8217; after initialization.</p>
<dt><code>-F pidfile</code></p>
<dd>Create &#8216;pidfile&#8217; and write process id in it.</dl>
<h3>Client Options:</h3>
<dl>
<dt><code>-4</code></p>
<dd>Force IPv4 DNS queries</p>
<dt><code>-6</code></p>
<dd>Force IPv6 DNS queries</p>
<dt><code>-r</code></p>
<dd>Skip raw UDP mode. If not used, iodine will try getting the public IP address of the iodined host and test if it is reachable directly. If it is, traffic will be sent to the server instead of the DNS relay.</p>
<dt><code>-R rdomain</code></p>
<dd>Use OpenBSD routing domain &#8216;rdomain&#8217; for the DNS connection.</p>
<dt><code>-m fragsize</code></p>
<dd>Force maximum downstream fragment size. Not setting this will cause the client to automatically probe the maximum accepted downstream fragment size.</p>
<dt><code>-M namelen</code></p>
<dd>Maximum length of upstream hostnames, default 255. Usable range ca. 100 to 255. Use this option to scale back upstream bandwidth in favor of downstream bandwidth. Also useful for DNS servers that perform unreliably when using full-length hostnames, noticeable when fragment size autoprobe returns very different results each time.</p>
<dt><code>-T dnstype</code></p>
<dd>DNS request type override. By default, autodetection will probe for working DNS request types, and will select the request type that is expected to provide the most bandwidth. However, it may turn out that a DNS relay imposes limits that skew the picture, which may lead to an &quot;unexpected&quot; DNS request type providing more bandwidth. In that case, use this option to override the autodetection. In (expected) decreasing bandwidth order, the supported DNS request types are: <i>NULL</i>, <i>PRIVATE</i>, <i>TXT</i>, <i>SRV</i>, <i>MX</i>, <i>CNAME</i> and <i>A</i> (returning CNAME). Note that <i>SRV</i>, <i>MX</i> and <i>A</i> may/will cause additional lookups by &quot;smart&quot; caching nameservers to get an actual IP address, which may either slow down or fail completely. The <i>PRIVATE</i> type uses value 65399 (in the &#8216;private use&#8217; range) and requires servers implementing RFC 3597.</p>
<dt><code>-O downenc</code></p>
<dd>Force downstream encoding type for all query type responses except NULL. Default is autodetected, but may not spot all problems for the more advanced codecs. Use this option to override the autodetection. <i>Base32</i> is the lowest-grade codec and should always work; this is used when autodetection fails. <i>Base64</i> provides more bandwidth, but may not work on all nameservers. <i>Base64u</i> is equal to Base64 except in using underscore (&#8216;_&#8217;) instead of plus sign (&#8216;+&#8217;), possibly working where <i>Base64</i> does not. <i>Base128</i> uses high byte values (mostly accented letters in iso8859-1), which might work with some nameservers. For TXT queries, <i>Raw</i> will provide maximum performance, but this will only work if the nameserver path is fully 8-bit-clean for responses that are assumed to be &quot;legible text&quot;.</p>
<dt><code>-L 0|1</code></p>
<dd>Lazy-mode switch. -L1 (default): Use lazy mode for improved performance and decreased latency. A very small minority of DNS relays appears to be unable to handle the lazy mode traffic pattern, resulting in no or very little data coming through. The iodine client will detect this and try to switch back to legacy mode, but this may not always work. In these situations use -L0 to force running in legacy mode (implies -I1).</p>
<dt><code>-I interval</code></p>
<dd>Maximum interval between requests (pings) so that intermediate DNS servers will not time out. Default is 4 in lazy mode, which will work fine in most cases. When too many SERVFAIL errors occur, iodine will automatically reduce this to 1. To get absolute minimum DNS traffic, increase well above 4, but not so high that SERVFAIL errors start to occur. There are some DNS relays with very small timeouts, notably dnsadvantage.com (ultradns), that will give SERVFAIL errors even with -I1; data will still get trough, and these errors can be ignored. Maximum useful value is 59, since iodined will close a client&#8217;s connection after 60 seconds of inactivity.</dl>
<h2>Environment</h2>
<h3>Iodine_Pass</h3>
<p>If the environment variable <code>IODINE_PASS</code> is set, iodine will use the value it is set to as password instead of asking for one. The <code>-P</code> option still has precedence.</p>
<h2>See Also</h2>
<p>The README file in the source distribution contains some more elaborate information.</p>
<h2>Bugs</h2>
<p>File bugs at <a rel="nofollow" href="http://dev.kryo.se/iodine/">http://dev.kryo.se/iodine/</a></p>
<h2>Authors</h2>
<p>Erik Ekman &lt;yarrick [at] kryo.se&gt; and Bjorn Andersson &lt;flex [at] kryo.se&gt;. Major contributions by Anne Bezemer.</p>
