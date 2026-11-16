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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print a summary of the options</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print the version number</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Print status/progress information</dd>
<dt><code>-s</code>, <code>&#8211;standard</code></dt>
<dd> Output address/netmask pairs</dd>
<dt><code>-c</code>, <code>&#8211;cidr</code></dt>
<dd> Output CIDR format address lists</dd>
<dt><code>-i</code>, <code>&#8211;cisco</code></dt>
<dd> Output Cisco style address lists</dd>
<dt><code>-r</code>, <code>&#8211;range</code></dt>
<dd> Output ip address ranges</dd>
<dt><code>-x</code>, <code>&#8211;hex</code></dt>
<dd> Output address/netmask pairs in hex</dd>
<dt><code>-o</code>, <code>&#8211;octal</code></dt>
<dd> Output address/netmask pairs in octal</dd>
<dt><code>-b</code>, <code>&#8211;binary</code></dt>
<dd> Output address/netmask pairs in binary</dd>
<dt><code>-n</code>, <code>&#8211;nodns</code></dt>
<dd> Disable DNS lookups for addresses</dd></dl>
<h2>DEFINITIONS</h2>
<p> A <i>spec</i> is an address specification, it can look like:</p>
<dl>
<dt><i>address</i></dt>
<dd> One address.</dd>
<dt><i>address1</i>:<i>address2</i></dt>
<dd> All addresses from <i>address1</i> to <i>address2</i>.</dd>
<dt><i>address1</i>:+<i>address2</i></dt>
<dd> All addresses from <i>address1</i> to <i>address1</i>+<i>address2</i>.</dd>
<dt><i>address</i>/<i>mask</i></dt>
<dd> A group starting at <i>address</i> spanning <i>mask</i>.</dd></dl>
<p> An <i>address</i> is an internet network address, it can look like:</p>
<dl>
<dt><i><a href="ftp://ftp.gnu.org">ftp.gnu.org</a></i></dt>
<dd> An internet hostname.</dd>
<dt><i>209.81.8.252</i></dt>
<dd> A standard dotted quad internet address notation.</dd>
<dt><i>100</i></dt>
<dd> A decimal number (100 in this case).</dd>
<dt><i>0100</i></dt>
<dd> An octal number preceded by &quot;0&quot; (64 in this case).</dd>
<dt><i>0x100</i></dt>
<dd> A hexadecimal number preceded by &quot;0x&quot; (256 in this case).</dd></dl>
<p> A <i>mask</i> is a network mask, it can look like:</p>
<dl>
<dt><i>255.255.224.0</i></dt>
<dd> A dotted quad netmask (<code>netmask</code> will complain if it is not a valid netmask).</dd>
<dt><i>0.0.31.255</i></dt>
<dd> A Cisco style inverse netmask (with the same checks).</dd>
<dt><i>8</i></dt>
<dd> The number of bits set to one from the left (CIDR notation).</dd>
<dt><i>010</i></dt>
<dd> The number of bits set to one from the left in octal.</dd>
<dt><i>0x10</i></dt>
<dd> The number of bits set to one from the left in hexadecimal.</dd></dl>
<h2>AUTHOR</h2>
<p> <i>netmask</i> was written by Robert Stone. Some algorithm design and optimization was provided by Tom Lear. This manual page was written by Robert Stone.</p>
<h2>BUGS</h2>
<p> Let me know if you find any. This man page is a bit more simplistic than I&#8217;d like, but I&#8217;ve forgotten most of the groff I once knew.</p>
<h2>SEE ALSO</h2>
<p> <code>ipchains</code>(1), <code>ipfwadm</code>(8), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code>routed</code>(8), <code>gated</code>(8), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8) </p>
<h2>Index</h2>
