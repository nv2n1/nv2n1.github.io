---
title: "ndisc6(8)"
name: "ndisc6"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ndisc6/"
description: "ndisc6 – ICMPv6 Neighbor Discovery tool"
---

<p>ndisc6 &#8211; ICMPv6 Neighbor Discovery tool</p>
<h2>Synopsis</h2>
<p><code>ndisc6</code> [<code>-1mnqv</code>] [<code>-r attempts</code>] [<code>-s source_ip</code>] [<code>-w wait_ms</code>] &lt;<code>IPv6 address</code>&gt; &lt;<code>iface</code>&gt; </p>
<h2>Descripton</h2>
<p><code>NDisc6</code> is an Unix program which implements the ICMPv6 Neighbor Discovery in userland (it is normally done by the kernel). It is used to lookup the link-layer address (layer 2 address, MAC in the case of Ethernet) of any on-link IPv6 node. </p>
<p> The IPv6 address of the node must be specified, as well as the networking interface on which to perform the lookup.</p>
<h2>Options</h2>
<dl>
<dt><code>-1</code> or <code>&#8211;single</code></p>
<dd>Exit as soon as the first advertisement is received (default). </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-m</code> or <code>&#8211;multiple</code></p>
<dd>Wait for possible duplicate advertisements and print all of them. </p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd>If the first parameter is not a valid IPv6 address, do not try to resolve it as a DNS hostname. </p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd>Only display link-layer address. Display nothing in case of failure. That is mostly useful when calling the program from a shell script. </p>
<dt><code>-r attempts</code> or <code>&#8211;retry attempts</code></p>
<dd>Send ICMPv6 Neighbor Discovery that many times until a reply is received, or abort. By default, ndisc6 will try 3 times before aborting (MAX_MULTICAST_SOLICIT and MAX_UNICAST_SOLICIT from RFC2461). </p>
<dt><code>-s source_ip</code> or <code>&#8211;source source_ip</code></p>
<dd>Specify the IPv6 address to be used as the source for the neighbor solicitation packets. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and license and exit. </p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd>Display verbose information. That is the default. </p>
<dt><code>-w wait_ms</code> or <code>&#8211;wait wait_ms</code></p>
<dd>Wait <i>wait_ms</i> milliseconds for a response before retrying. By default, ndisc6 waits 1 second between each attempts (RETRANS_TIMER from RFC2461). </p>
</dl>
<p> If <code>ndisc6</code> does not receive any response after the specified number of attempts waiting for <i>wait_ms</i> milliseconds each time, it will exit with code 2. On error, it exits with code 1. Otherwise it exits with code 0. This makes it possible to use the exit code to see if a host is on-link or not.</p>
<h2>Diagnostics</h2>
<p>If you get no response while you know the remote host is up, it is most likely that it is not on-link, that is to say, you must cross one or more routers to reach it. By design, IPv6 nodes ignore ICMPv6 Neighbor Discovery packets received from nodes not on the same link (i.e. Ethernet segment), for the sake of security. Technically, that is done by ensuring that the Hop limit (TTL) is 255. </p>
<p> Note that you cannot use <code>ndisc6</code> to lookup the local host&#8217;s link-layer address.</p>
<h2>Security</h2>
<p><code>ndisc6</code> should be <i>setuid</i> <i>root</i> to allow use by non-privileged users. It will drop its root privileges before any attempt is made to send or receive data from the network to reduce the possible impact of a security vulnerability.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ping6/">ping6</a>(8), <a href="/docs/linux/man/8-rdisc6/">rdisc6</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a></p>
