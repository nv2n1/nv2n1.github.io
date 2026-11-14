---
title: "knock(1)"
name: "knock"
section: "1"
letter: "k"
url: "/docs/linux/man/1-knock/"
description: "knock – port-knock client"
---

<h2>NAME</h2>
<p> knock &#8211; port-knock client</p>
<h2>SYNOPSIS</h2>
<p> <code>knock [options] &lt;host&gt; &lt;port[:proto]&gt; [port[:proto]] &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>knock</code> is a <i>port-knock</i> client. It sends TCP/UDP packets to each specified <i>port</i> on <i>host</i>, creating a special knock sequence on the listening server (see the <code>knockd</code> manpage for more info on this).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udp</code></p>
<dd> Make all port hits use UDP (default is TCP). If you want each port to use a different protocol (TCP or UDP), then you can specify the protocol on a per-port basis. See the example below.</p>
<dt><code>-d &lt;t&gt;, &#8211;delay &lt;t&gt;</code></p>
<dd> Wait &lt;t&gt; milliseconds between each port hit. This can be used in situations where a router mistakes your stream of SYN packets as a port scan and blocks them. If the packet rate is slowed with &#8211;delay, then the router should let the packets through.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Output verbose status messages.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display the version.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Syntax help.</dl>
<h2>EXAMPLES</h2>
<pre>
knock myserver.example.com 123:tcp 456:udp 789:tcp
knock -u myserver.example.com 8284 4721 18592 42912
</pre>
<h2>SEE ALSO</h2>
<p> <code>knockd</code> is the accompanying port-knock server.</p>
<h2>AUTHOR</h2>
<pre>
Judd Vinet &lt;jvinet [at] zeroflux.org&gt;
</pre>
<h2>Index</h2>
