---
title: "traceroute(1)"
name: "traceroute"
section: "1"
letter: "t"
url: "/docs/linux/man/1-traceroute/"
description: "traceroute – trace the route to a host"
---

<p>GNU Network Utilities</p>
<h2 class="name">NAME</h2>
<p> <code>traceroute</code> &#8211; trace the route to a host </p>
<h2>SYNOPSIS</h2>
<p> <code>traceroute</code> [<i>option &#8230;</i> ] <i>host</i></p>
<h2>DESCRIPTION</h2>
<p> Print the route packets trace to network <i>host</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f , -first-hop = </code><i>start</i></p>
<dd> Set the initial hop distance, that is the time-to-live.</p>
<dt><code>-g , -gateways = </code><i>gates</i></p>
<dd> List of gateways for loose source routing.</p>
<dt><code>-I , -icmp</code></p>
<dd> Use ICMP ECHO as probe.</p>
<dt><code>-m , -max-hop = </code><i>num</i></p>
<dd> Set the maximal hop count (default is 64).</p>
<dt><code>-M , -type = </code><i>method</i></p>
<dd> Use the <i>method</i> <code>( icmp</code> or the default <code>udp</code> for traceroute operations.</p>
<dt><code>-p , -port = </code><i>port</i></p>
<dd> Use the destination <i>port</i> port (default is 33434).</p>
<dt><code>-q , -tries = </code><i>num</i></p>
<dd> Send <i>num</i> probe packets per hop (default is 3).</p>
<dt><code>&#8211;resolve-hostnames</code></p>
<dd> Resolve hostnames.</p>
<dt><code>-t , -tos = </code><i>class</i></p>
<dd> Set the type of service (TOS) to <i>class</i></p>
<dt><code>-w , -wait = </code><i>timeout</i></p>
<dd> Wait <i>timeout</i> seconds for responses (default is 3).</p>
<dt><code>-? , -help</code></p>
<dd> Give this help list.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give a short usage message.</p>
<dt><code>-V , -version</code></p>
<dd> Print program version.</dl>
<h2>Index</h2>
