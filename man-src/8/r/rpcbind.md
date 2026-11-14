---
title: "rpcbind(8)"
name: "rpcbind"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpcbind/"
description: "rpcbind – universal addresses to RPC program number mapper"
---

<p><code>rpcbind</code> &#8211; universal addresses to RPC program number mapper</p>
<h2>Synopsis</h2>
<p>[-<code>adhiLls</code> ]</p>
<h2>Description</h2>
<p>The utility is a server that converts <code>RPC</code> program numbers into universal addresses. It must be running on the host to be able to make <code>RPC</code> calls on a server on that machine. </p>
<p> When an <code>RPC</code> service is started, it tells the address at which it is listening, and the <code>RPC</code> program numbers it is prepared to serve. When a client wishes to make an <code>RPC</code> call to a given program number, it first contacts on the server machine to determine the address where <code>RPC</code> requests should be sent. </p>
<p> The utility should be started before any other RPC service. Normally, standard <code>RPC</code> servers are started by port monitors, so must be started before port monitors are invoked. </p>
<p> When is started, it checks that certain name-to-address translation-calls function correctly. If they fail, the network configuration databases may be corrupt. Since <code>RPC</code> services cannot function correctly in this situation, reports the condition and terminates. </p>
<p> The utility can only be started by the super-user.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>When debugging (-<code>d</code> ) do an abort on errors.</p>
<dt><code>-d</code></p>
<dd>Run in debug mode. In this mode, will log additional information during operation, and will abort on certain errors if &#8211;<code>a</code> is also specified. With this option, the name-to-address translation consistency checks are shown in detail.</p>
<dt><code>-f</code></p>
<dd>Do not fork and become a background process.</p>
<dt><code>-h</code></p>
<dd>Specify specific IP addresses to bind to for UDP requests. This option may be specified multiple times and is typically necessary when running on a multi-homed host. If no &#8211;<code>h</code> option is specified, will bind to <code>INADDR_ANY</code> which could lead to problems on a multi-homed host due to returning a UDP packet from a different IP address than it was sent to. Note that when specifying IP addresses with &#8211;<code>h</code> will automatically add <code>127.0.0.1</code> and if IPv6 is enabled, <code>::1</code> to the list.</p>
<dt><code>-i</code></p>
<dd>&#8220;Insecure&#8221; mode. Allow calls to SET and UNSET from any host. Normally accepts these requests only from the loopback interface for security reasons. This change is necessary for programs that were compiled with earlier versions of the rpc library and do not make those requests using the loopback interface.</p>
<dt><code>-l</code></p>
<dd>Turn on libwrap connection logging.</p>
<dt><code>-s</code></p>
<dd>Cause to change to the user daemon as soon as possible. This causes to use non-privileged ports for outgoing connections, preventing non-privileged clients from using to connect to services from a privileged port.</p>
<dt><code>-w</code></p>
<dd>Cause to do a &quot;warm start&quot; by read a state file when starts up. The state file is created when terminates.</dl>
<h2>Notes</h2>
<p>All RPC servers must be restarted if is restarted.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-rpcinfo/">rpcinfo</a>(8)</p>
<h2>Linux Port</h2>
<dl>
</dl>
