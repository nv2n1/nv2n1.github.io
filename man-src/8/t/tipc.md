---
title: "tipc(8)"
name: "tipc"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc/"
description: "tipc – a TIPC configuration and management tool"
---

<p>tipc &#8211; a TIPC configuration and management tool</p>
<h2>Synopsis</h2>
<p><code>tipc</code> [ <i>OPTIONS</i> ] <i>COMMAND</i> <i>ARGUMENTS</i> </p>
<pre><code>COMMAND := {

    bearer | link | media | nametable | node | socket }

OPTIONS := {

    -h[help] }
</code></pre>
<h2>Description</h2>
<p>The Transparent Inter-Process Communication (TIPC) protocol offers total address transparency between processes which allows applications in a clustered computer environment to communicate quickly and reliably with each other, regardless of their location within the cluster. TIPC originated at the telecommunications manufacturer Ericsson. The first open source version of TIPC was created in 2000 when Ericsson released its first Linux version of TIPC. TIPC was introduced in the mainline Linux kernel in 2006 and is now widely used both within and outside of Ericsson. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last given command. For example <code>tipc bearer &#8211;help</code> will show bearer help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant. </p>
<dt><code>-j,</code> -json</p>
<dd>Output results in JavaScript Object Notation (JSON). </p>
<dt><code>-p,</code> -pretty</p>
<dd>The default JSON format is compact and more efficient to parse but hard for most users to read. This flag adds indentation for readability. </p>
</dl>
<h2>Commands</h2>
<dl>
<dt><code>BEARER</code></p>
<dd>&#8211; Show or modify TIPC bearers </p>
<dt><code>LINK</code></p>
<dd>&#8211; Show or modify TIPC links </p>
<dt><code>MEDIA</code></p>
<dd>&#8211; Show or modify TIPC media </p>
<dt><code>NAMETABLE</code></p>
<dd>&#8211; Show TIPC nametable </p>
<dt><code>NODE</code></p>
<dd>&#8211; Show or modify TIPC node parameters </p>
<dt><code>SOCKET</code></p>
<dd>&#8211; Show TIPC sockets </p>
</dl>
<h2>Arguments</h2>
<p>Command arguments are described in a command specific man page and typically consists of nested commands along with key value pairs. If no arguments are given a command typically shows its help text. The explicit help option <code>-h</code> or <code>&#8211;help</code> can occur anywhere among the arguments and will show help for the last valid command given.</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
