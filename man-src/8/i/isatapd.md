---
title: "isatapd(8)"
name: "isatapd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isatapd/"
description: "isatapd – ISATAP IPv6 Router and Prefix Discovery"
---

<p>isatapd &#8211; ISATAP IPv6 Router and Prefix Discovery</p>
<h2>Synopsis</h2>
<p><code>isatapd</code> [<code>OPTIONS</code>] &#8230; [<code>ADDRS</code>] &#8230; </p>
<h2>Descripton</h2>
<p><code>isatapd</code> implements the ISATAP IPv6 Router and Prefix Discovery procedures specified in Section 8.3 of [RFC5214]. It uses a Potential Router List (PRL) that records the IPv4 addresses of candidate default routers available on the ISATAP link. PRL discovery is through domain name lookup in the site name service, through manual configuration of IPv4 addresses, or a combination of both. </p>
<p> This program is used on ISATAP hosts and non-default routers; it sends Router Solicitation (RS) messages over the ISATAP interface to elicit Router Advertisements (RAs) from default routers. </p>
<p> This program is also intended for use on hosts and routers that follow the specifications for Virtual Enterprise Traversal (VET) (draft-templin-autoconf-dhcp).</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-d ifname</code> or <code>&#8211;dev ifname</code></p>
<dd>Supply the name of an ISATAP/VET netwok interface associated with the Potential Router List. By default, isatapd uses the name &quot;is0&quot;. </p>
<dt><code>-p prlname</code> or <code>&#8211;prl prlname</code></p>
<dd>Supply the Potential Router List (PRL) name for use on this ISATAP/VET interface (e.g., isatap.example.com). There is no default PRL name, and this option may be ommitted if IPv4 addresses are manually configured. </p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd>Only display advertised IPv6 prefixes. Display nothing in case of failure. That is mostly useful when calling the program from a shell script. </p>
<dt><code>-r attempts</code> or <code>&#8211;retry attempts</code></p>
<dd>Send ICMPv6 Router Solicitations that many times until a Router Advertisement is received. (If no advertisement is received, isatapd will initiate the sending sequence again after delaying 120 seconds.) By default, isatapd will try 3 times (MAX_RTR_SOLICITATIONS from RFC2461) before delaying 120 seconds and trying again. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and license and exit. </p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd>Display verbose information. That is the default. </p>
<dt><code>-w wait_ms</code> or <code>&#8211;wait wait_ms</code></p>
<dd>Wait <i>wait_ms</i> milliseconds for a response before retrying. By default, isatapd waits 4 second between each attempts (RTR_SOLICITATION_INTERVAL from RFC2461). </p>
<dt><code>ADDRS</code></p>
<dd>A list of IPv4 addresses of ISATAP default routers. This list is in addition to any IPv4 addresses discovered through domain name resolution in the site name service. </p>
</dl>
<h2>Security</h2>
<p>isatapd must be <i>setuid</i> <i>root</i> to allow use by non privileged users. It will drop its root privileges before any attempt is made to send or receive data from the network to reduce the possible impact of a security vulnerability.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ndisc6/">ndisc6</a>(8), <a href="/docs/linux/man/8-rdisc6/">rdisc6</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>Author</h2>
<p>Kwong-Sang Yin &lt;kwong-sang.yin [at] boeing.com&gt; </p>
<p> Fred Templin &lt;fred.l.templin at boeing.com&gt; </p>
<p> $Id: isatapd.8 483 2009-05-29 14:00:00Z fltemplin $ </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a></p>
