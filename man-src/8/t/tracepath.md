---
title: "tracepath(8)"
name: "tracepath"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tracepath/"
description: "tracepath – traces path to a network host discovering MTU along this path"
---

<p>tracepath &#8211; traces path to a network host discovering MTU along this path</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>tracepath</code> [<code>-4</code>] [<code>-6</code>] [<code>-n</code>] [<code>-b</code>] [<code>-l&nbsp;</code><i>pktlen</i>] [<code>-m&nbsp;</code><i>max_hops</i>] [<code>-p&nbsp;</code><i>port</i>] [<code>-V</code>] {destination}</dl>
<h2>Description</h2>
<dd>It traces the network path to <i>destination</i> discovering MTU along this path. It uses UDP port <i>port</i> or some random port. It is similar to <code>traceroute</code>. However, it does not require superuser privileges and has no fancy options. </p>
<p> <code>tracepath -6</code> is a good replacement for <code>traceroute6</code> and classic example of application of Linux error queues. The situation with IPv4 is worse, because commercial IP routers do not return enough information in ICMP error messages. Probably, it will change, when they are updated. For now it uses Van Jacobson&#8217;s trick, sweeping a range of UDP ports to maintain trace history.</p>
<h2>Options</h2>
<p><code>-4</code></p>
<dl>
<dd>Use IPv4 only.</dl>
<p> <code>-6</code></p>
<dl>
<dd>Use IPv6 only.</dl>
<p> <code>-n</code></p>
<dl>
<dd>Print primarily IP addresses numerically.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Print both: Host names and IP addresses.</dl>
<p> <code>-l</code></p>
<dl>
<dd>Sets the initial packet length to <i>pktlen</i> instead of 65535 for <code>IPv4</code> or 128000 for <code>IPv6</code>.</dl>
<p> <code>-m</code></p>
<dl>
<dd>Set maximum hops (or maximum TTLs) to <i>max_hops</i> instead of 30.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Sets the initial destination port to use.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Print version and exit.</dl>
<h2>Output</h2>
<dl>
<dd>
<pre>root [at] mops:~ # tracepath -6 3ffe:2400:0:109::2
 1?: [LOCALHOST] pmtu 1500
 1: dust.inr.ac.ru 0.411ms
 2: dust.inr.ac.ru asymm 1 0.390ms pmtu 1480
 2: 3ffe:2400:0:109::2 463.514ms reached
 Resume: pmtu 1480 hops 2 back 2</pre>
</dl>
<p> The first column shows the TTL of the probe, followed by colon. Usually the value of TTL is obtained from the reply from the network, but sometimes it does not contain the necessary information and we have to guess it. In this case the number is followed by ?. </p>
<p> The second column shows the network hop which replied to the probe. It is either the address of the router or the word [LOCALHOST], if the probe was not sent to the network. </p>
<p> The rest of the line shows miscellaneous information about the path to the corresponding network hop. It contains the value of RTT, and additionally it can show Path MTU when it changes. If the path is asymmetric or the probe finishes before it reaches the prescribed hop, the difference between number of hops in forward and return direction is shown next to the keyword &quot;async&quot;. This information is not reliable, e.g. the third line shows asymmetry of 1. This is because the first probe with TTL of 2 was rejected at the first hop due to Path MTU Discovery. </p>
<p> The last line summarizes information about all the paths to the destination. It shows detected Path MTU, amount of hops to the destination and our guess about the number of hops from the destination to us, which can be different when the path is asymmetric.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-traceroute/">traceroute</a></code>(8), <code><a href="/docs/linux/man/8-traceroute6/">traceroute6</a></code>(8), <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8).</p>
<h2>Author</h2>
<p><code>tracepath</code> was written by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;.</p>
<h2>Security</h2>
<p>No security issues. </p>
<p> This lapidary deserves to be elaborated. <code>tracepath</code> is not a privileged program, unlike <code>traceroute</code>, <code>ping</code> and other beasts of their kind. <code>tracepath</code> may be executed by everyone who has enough access to the network to send UDP datagrams to the desired destination using the given port.</p>
<h2>Availability</h2>
<p><code>tracepath</code> is part of <i>iputils</i> package.</p>
