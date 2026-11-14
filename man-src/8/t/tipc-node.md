---
title: "tipc-node(8)"
name: "tipc-node"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-node/"
description: "tipc-node – modify and show local node parameters or list peer nodes"
---

<p>tipc-node &#8211; modify and show local node parameters or list peer nodes</p>
<h2>Synopsis</h2>
<pre><code>tipc node set

{ address

    ADDRESS

    | netid

    NETID

}
tipc node get

{ address | netid }</code></pre>
<p> <code>tipc node list</code> </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last valid command. For example <code>tipc node &#8211;help</code> will show node help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant.</dl>
<h2>Description</h2>
<h3>Node parameters</h3>
<dl>
<dt><code>address</code></p>
<dd>The TIPC logical address. On the form x.y.z where x, y and z are unsigned integers.</p>
<dt><code>netid</code></p>
<dd>Network identity. Can by used to create individual TIPC clusters on the same media. </p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
