---

title: "netstat-nat(1)"
name: "netstat-nat"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netstat-nat/"
description: "netstat-nat – Show the natted connections on a linux iptable firewall"
---

<p> netstat-nat &#8211; Show the natted connections on a linux iptable firewall</p>
<h2>SYNOPSIS</h2>
<p> <code>netstat-nat [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>netstat-nat</i> Displays NAT connections managed by netfilter/iptables which comes with the &gt; 2.4.x linux kernels. </p>
<p> The program reads its information from &#8216;/proc/net/ip_conntrack&#8217; or &#8216;/proc/net/nf_conntrack&#8217;, which is the temporary conntrack-storage of netfilter.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> displays help</dd>
<dt><code>-n</code></dt>
<dd> don&#8217;t resolve IPs/portnumbers to host/portnames</dd>
<dt><code>-p &lt;protocol&gt;</code></dt>
<dd> display NAT connections with protocol selection (see /etc/protocols)</dd>
<dt><code>-s &lt;source host&gt;</code></dt>
<dd> display connections by source IP/hostname</dd>
<dt><code>-d &lt;destination host&gt;</code></dt>
<dd> display connections by destination IP/hostname</dd>
<dt><code>-S</code></dt>
<dd> display SNAT connections</dd>
<dt><code>-D</code></dt>
<dd> display DNAT connections</dd>
<dt><code>-L</code></dt>
<dd> display only connections to NAT box self (doesn&#8217;t show SNAT &amp; DNAT)</dd>
<dt><code>-R</code></dt>
<dd> display only connections routed through the NAT box (doesn&#8217;t show SNAT &amp; DNAT)</dd>
<dt><code>-x</code></dt>
<dd> extended view of hostnames</dd>
<dt><code>-r &lt;src|dst|src-port|dst-port|state&gt;</code></dt>
<dd> sort connections</dd>
<dt><code>-o</code></dt>
<dd> no output header</dd>
<dt><code>-N</code></dt>
<dd> display NAT box connection information (only valid with SNAT &amp; DNAT)</dd>
<dt><code>-v</code></dt>
<dd> prints version</dd></dl>
<h2>FILES</h2>
<p> /proc/net/ip_conntrack or /proc/net/nf_conntrack</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.tweegy.nl/projects/netstat-nat/">http://www.tweegy.nl/projects/netstat-nat/</a><br/>
 <a rel="nofollow" href="http://www.netfilter.org/">http://www.netfilter.org/</a></p>
<h2>AUTHOR</h2>
<p> netstat-nat has been written by D.Wijsman danny [at] tweegy.nl<br/>
 The manual page has been written by marceln [at] xs4all.nl </p>
