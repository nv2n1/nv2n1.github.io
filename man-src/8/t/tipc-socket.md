---
title: "tipc-socket(8)"
name: "tipc-socket"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-socket/"
description: "tipc-socket – show TIPC socket (port) information"
---

<p>tipc-socket &#8211; show TIPC socket (port) information</p>
<h2>Synopsis</h2>
<p><code>tipc socket list</code> </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last valid command. For example <code>tipc socket &#8211;help</code> will show socket help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant. </p>
</dl>
<h2>Description</h2>
<p>A TIPC socket is represented by an unsigned integer.</p>
<dl>
<dt></dl>
<h3>Bound state</h3>
<dd>A bound socket has a logical TIPC port name associated with it.</p>
<dl>
<dt></dl>
<h3>Connected state</h3>
<dd>A connected socket is directly connected to another socket creating a point to point connection between TIPC sockets. If the connection to X was made using a logical port name Y that name will show up as <code>connected to </code>X <code>via </code>Y </p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8) <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8),</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
