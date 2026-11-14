---
title: "netmask(1)"
name: "netmask"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netmask/"
description: "netmask – a netmask generation and conversion program"
---

<h2 class="name">NAME</h2>
<p> netmask &#8211; a netmask generation and conversion program </p>
<h2>SYNOPSIS</h2>
<p> <code>netmask</code> [ <i>options</i> ] <i>spec</i> [ <i>spec</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> This program accepts and produces a variety of common network address and netmask formats. Not only can it convert address and netmask notations, but it will optimize the masks to generate the smallest list of rules. This is very handy if you&#8217;ve ever configured a firewall or router and some nasty network administrator before you decided that base 10 numbers were good places to start and end groups of machines.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a summary of the options</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version number</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print status/progress information</p>
<dt><code>-s</code>, <code>&#8211;standard</code></p>
<dd> Output address/netmask pairs</p>
<dt><code>-c</code>, <code>&#8211;cidr</code></p>
<dd> Output CIDR format address lists</p>
<dt><code>-i</code>, <code>&#8211;cisco</code></p>
<dd> Output Cisco style address lists</p>
<dt><code>-r</code>, <code>&#8211;range</code></p>
<dd> Output ip address ranges</p>
<dt><code>-x</code>, <code>&#8211;hex</code></p>
<dd> Output address/netmask pairs in hex</p>
<dt><code>-o</code>, <code>&#8211;octal</code></p>
<dd> Output address/netmask pairs in octal</p>
<dt><code>-b</code>, <code>&#8211;binary</code></p>
<dd> Output address/netmask pairs in binary</p>
<dt><code>-n</code>, <code>&#8211;nodns</code></p>
<dd> Disable DNS lookups for addresses</dl>
<h2>DEFINITIONS</h2>
<p> A <i>spec</i> is an address specification, it can look like:</p>
<dl>
<dt><i>address</i></p>
<dd> One address.</p>
<dt><i>address1</i>:<i>address2</i></p>
<dd> All addresses from <i>address1</i> to <i>address2</i>.</p>
<dt><i>address1</i>:+<i>address2</i></p>
<dd> All addresses from <i>address1</i> to <i>address1</i>+<i>address2</i>.</p>
<dt><i>address</i>/<i>mask</i></p>
<dd> A group starting at <i>address</i> spanning <i>mask</i>.</dl>
<p> An <i>address</i> is an internet network address, it can look like:</p>
<dl>
<dt><i><a href="ftp://ftp.gnu.org">ftp.gnu.org</a></i></p>
<dd> An internet hostname.</p>
<dt><i>209.81.8.252</i></p>
<dd> A standard dotted quad internet address notation.</p>
<dt><i>100</i></p>
<dd> A decimal number (100 in this case).</p>
<dt><i>0100</i></p>
<dd> An octal number preceded by &quot;0&quot; (64 in this case).</p>
<dt><i>0x100</i></p>
<dd> A hexadecimal number preceded by &quot;0x&quot; (256 in this case).</dl>
<p> A <i>mask</i> is a network mask, it can look like:</p>
<dl>
<dt><i>255.255.224.0</i></p>
<dd> A dotted quad netmask (<code>netmask</code> will complain if it is not a valid netmask).</p>
<dt><i>0.0.31.255</i></p>
<dd> A Cisco style inverse netmask (with the same checks).</p>
<dt><i>8</i></p>
<dd> The number of bits set to one from the left (CIDR notation).</p>
<dt><i>010</i></p>
<dd> The number of bits set to one from the left in octal.</p>
<dt><i>0x10</i></p>
<dd> The number of bits set to one from the left in hexadecimal.</dl>
<h2>AUTHOR</h2>
<p> <i>netmask</i> was written by Robert Stone. Some algorithm design and optimization was provided by Tom Lear. This manual page was written by Robert Stone.</p>
<h2>BUGS</h2>
<p> Let me know if you find any. This man page is a bit more simplistic than I&#8217;d like, but I&#8217;ve forgotten most of the groff I once knew.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipchains/">ipchains</a></code>(1), <code><a href="/docs/linux/man/8-ipfwadm/">ipfwadm</a></code>(8), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code><a href="/docs/linux/man/8-routed/">routed</a></code>(8), <code><a href="/docs/linux/man/8-gated/">gated</a></code>(8), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8) </p>
<h2>Index</h2>
