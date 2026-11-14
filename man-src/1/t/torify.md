---
title: "torify(1)"
name: "torify"
section: "1"
letter: "t"
url: "/docs/linux/man/1-torify/"
description: "torify – wrapper for torsocks and tor"
---

<h2 class="name">NAME</h2>
<p> torify &#8211; wrapper for torsocks and tor </p>
<h2>SYNOPSIS</h2>
<p> <code>torify</code> <i>application</i> [<i>application&#8217;s</i> <i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>torify</code> is a simple wrapper that attempts to find the best underlying Tor wrapper available on a system. It calls torsocks with a tor specific configuration file. </p>
<p> torsocks is an improved wrapper that explicitly rejects UDP, safely resolves DNS lookups and properly socksifies your TCP connections. </p>
<p> Please note that since both method use LD_PRELOAD, torify cannot be applied to suid binaries.</p>
<h2>WARNING</h2>
<p> When used with torsocks, torify should not leak DNS requests or UDP data. </p>
<p> Both will leak ICMP data.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tor/">tor</a></code>(1), <code><a href="/docs/linux/man/1-tor-resolve/">tor-resolve</a></code>(1), <code><a href="/docs/linux/man/1-torsocks/">torsocks</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Peter Palfrader and Jacob Appelbaum wrote this manual. </p>
<h2>Index</h2>
