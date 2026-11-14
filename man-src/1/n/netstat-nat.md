---
title: "netstat-nat(1)"
name: "netstat-nat"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netstat-nat/"
description: "netstat-nat – Show the natted connections on a linux iptable firewall"
---

<h2>NAME</h2>
<p> netstat-nat &#8211; Show the natted connections on a linux iptable firewall</p>
<h2>SYNOPSIS</h2>
<p> <code>netstat-nat [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>netstat-nat</i> Displays NAT connections managed by netfilter/iptables which comes with the &gt; 2.4.x linux kernels. </p>
<p> The program reads its information from &#8216;/proc/net/ip_conntrack&#8217; or &#8216;/proc/net/nf_conntrack&#8217;, which is the temporary conntrack-storage of netfilter.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> displays help</p>
<dt><code>-n</code></p>
<dd> don&#8217;t resolve IPs/portnumbers to host/portnames</p>
<dt><code>-p &lt;protocol&gt;</code></p>
<dd> display NAT connections with protocol selection (see /etc/protocols)</p>
<dt><code>-s &lt;source host&gt;</code></p>
<dd> display connections by source IP/hostname</p>
<dt><code>-d &lt;destination host&gt;</code></p>
<dd> display connections by destination IP/hostname</p>
<dt><code>-S</code></p>
<dd> display SNAT connections</p>
<dt><code>-D</code></p>
<dd> display DNAT connections</p>
<dt><code>-L</code></p>
<dd> display only connections to NAT box self (doesn&#8217;t show SNAT &amp; DNAT)</p>
<dt><code>-R</code></p>
<dd> display only connections routed through the NAT box (doesn&#8217;t show SNAT &amp; DNAT)</p>
<dt><code>-x</code></p>
<dd> extended view of hostnames</p>
<dt><code>-r &lt;src|dst|src-port|dst-port|state&gt;</code></p>
<dd> sort connections</p>
<dt><code>-o</code></p>
<dd> no output header</p>
<dt><code>-N</code></p>
<dd> display NAT box connection information (only valid with SNAT &amp; DNAT)</p>
<dt><code>-v</code></p>
<dd> prints version</dl>
<h2>FILES</h2>
<p> /proc/net/ip_conntrack or /proc/net/nf_conntrack</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.tweegy.nl/projects/netstat-nat/">http://www.tweegy.nl/projects/netstat-nat/</a><br />
 <a rel="nofollow" href="http://www.netfilter.org/">http://www.netfilter.org/</a></p>
<h2>AUTHOR</h2>
<p> netstat-nat has been written by D.Wijsman danny [at] tweegy.nl<br />
 The manual page has been written by marceln [at] xs4all.nl </p>
<h2>Index</h2>
