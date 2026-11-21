---
title: "rmcp_ping(1)"
name: "rmcp_ping"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmcp_ping/"
description: "rmcp_ping – IPMI RMCP Ping program"
---

<h2>SYNOPSIS</h2>
<p> <code>rmcp_ping</code> [<code>-p</code> <i>port</i>] [<code>-t</code> <i>waittime</i>] [<code>-s</code> <i>starttag</i>] [<code>-d</code>] <i>destination</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>rmcp_ping</code> program sends an RMCP ping packet onces a second to the destination, printing unique responses it receives. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p&nbsp;<wbr></code><i>port</i></dt>
<dd> Set the destination <i>port</i>. This is the standard RMCP port by default, 623.</dd>
<dt><code>-t&nbsp;<wbr></code><i>waittime</i></dt>
<dd> Sets the number of seconds to wait for a response. Ten by default.</dd>
<dt><code>-s&nbsp;<wbr></code><i>starttag</i></dt>
<dd> There is an 8-bit tag value in every ping packet (0-254, 255 is reserved), this program will cycle through the values starting at starttag. This is zero by default</dd>
<dt><code>-d</code></dt>
<dd> Turns on debugging to standard output.</dd>
<dt><i>destination</i></dt>
<dd> The target address, default is the broadcast address (default 255.255.255.255) </dd>
</dl>
<h2>AUTHOR</h2>
<p> Corey Minyard &lt;cminyard [at] mvista.org&gt; </p>
