---
title: "rdisc6(8)"
name: "rdisc6"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdisc6/"
description: "rdisc – ICMPv6 Router Discovery tool"
---

<p>rdisc &#8211; ICMPv6 Router Discovery tool</p>
<h2>Synopsis</h2>
<p><code>rdisc6</code> [<code>-qv</code>] [<code>-r attempts</code>] [<code>-s source_ip</code>] [<code>-w wait_ms</code>] [<code>IPv6 address</code>] &lt;<code>iface</code>&gt; </p>
<h2>Descripton</h2>
<p><code>RDisc6</code> is an Unix program which implements the ICMPv6 Router Discovery in userland (it is normally done by the kernel). It is used to lookup the list of on-link routers and IPv6 prefixes. </p>
<p> It can also be used to force the kernel to update the state of a given IPv6-autoconfigured network interface. </p>
<p> The name of the network interface to probe routers for must be specified.</p>
<h2>Options</h2>
<dl>
<dt><code>-1</code> or <code>&#8211;single</code></p>
<dd>Exit as soon as the first advertisement is received. </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-m</code> or <code>&#8211;multiple</code></p>
<dd>Wait for possible multiple advertisements and print all of them (default). </p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd>If the optional parameter is not a valid IPv6 address, do not try to resolve it as a DNS hostname. </p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd>Only display advertised IPv6 prefixes. Display nothing in case of failure. That is mostly useful when calling the program from a shell script. </p>
<dt><code>-r attempts</code> or <code>&#8211;retry attempts</code></p>
<dd>Send ICMPv6 Router Discovery that many times until a reply is received, or abort. By default, rdisc6 will try 3 times before aborting (MAX_RTR_SOLICITATIONS from RFC2461). </p>
<dt><code>-s source_ip</code> or <code>&#8211;source source_ip</code></p>
<dd>Specify the IPv6 address to be used as the source for the router solicitation packets. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and license and exit. </p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd>Display verbose information. That is the default. </p>
<dt><code>-w wait_ms</code> or <code>&#8211;wait wait_ms</code></p>
<dd>Wait <i>wait_ms</i> milliseconds for a response before retrying. By default, rdisc6 waits 4 second between each attempts (RTR_SOLICITATION_INTERVAL from RFC2461). </p>
</dl>
<p> If <code>rdisc6</code> does not receive any response after the specified number of attempts waiting for <i>wait_ms</i> milliseconds each time, it will exit with code 2. On error, it exits with code 1. Otherwise it exits with code 0.</p>
<h2>Security</h2>
<p><code>rdisc6</code> must be <i>setuid</i> <i>root</i> to allow use by non privileged users. It will drop its root privileges before any attempt is made to send or receive data from the network to reduce the possible impact of a security vulnerability.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ndisc6/">ndisc6</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a></p>
