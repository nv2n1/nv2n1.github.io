---

title: "inetutils-traceroute(1)"
name: "inetutils-traceroute"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inetutils-traceroute/"
description: "traceroute – trace the route to a host"
---

<p>GNU Network Utilities</p>

<p> <code>traceroute</code> &#8211; trace the route to a host </p>
<h2>SYNOPSIS</h2>
<p> <code>traceroute</code> [<i>option &#8230;</i> ] <i>host</i></p>
<h2>DESCRIPTION</h2>
<p> Print the route packets trace to network <i>host</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f , -first-hop = </code><i>start</i></dt>
<dd> Set the initial hop distance, that is the time-to-live.</dd>
<dt><code>-g , -gateways = </code><i>gates</i></dt>
<dd> List of gateways for loose source routing.</dd>
<dt><code>-I , -icmp</code></dt>
<dd> Use ICMP ECHO as probe.</dd>
<dt><code>-m , -max-hop = </code><i>num</i></dt>
<dd> Set the maximal hop count (default is 64).</dd>
<dt><code>-M , -type = </code><i>method</i></dt>
<dd> Use the <i>method</i> <code>( icmp</code> or the default <code>udp</code> for traceroute operations.</dd>
<dt><code>-p , -port = </code><i>port</i></dt>
<dd> Use the destination <i>port</i> port (default is 33434).</dd>
<dt><code>-q , -tries = </code><i>num</i></dt>
<dd> Send <i>num</i> probe packets per hop (default is 3).</dd>
<dt><code>&#8211;resolve-hostnames</code></dt>
<dd> Resolve hostnames.</dd>
<dt><code>-t , -tos = </code><i>class</i></dt>
<dd> Set the type of service (TOS) to <i>class</i></dd>
<dt><code>-w , -wait = </code><i>timeout</i></dt>
<dd> Wait <i>timeout</i> seconds for responses (default is 3).</dd>
<dt><code>-? , -help</code></dt>
<dd> Give this help list.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give a short usage message.</dd>
<dt><code>-V , -version</code></dt>
<dd> Print program version.</dd></dl>
