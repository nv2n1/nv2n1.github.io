---
title: "tipc-nametable(8)"
name: "tipc-nametable"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-nametable/"
description: "tipc-nametable – show TIPC nametable"
---

<p>tipc-nametable &#8211; show TIPC nametable</p>
<h2>Synopsis</h2>
<p><code>tipc nametable show</code> </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>
<dt><code>-j,</code> -json</p>
<dd>Output results in JavaScript Object Notation (JSON). </p>
<dt><code>-p,</code> -pretty</p>
<dd>The default JSON format is compact and more efficient to parse but hard for most users to read. This flag adds indentation for readability. </p>
<p> Show help about last valid command. For example <code>tipc nametable &#8211;help</code> will show nametable help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant. </p>
</dl>
<h2>Description</h2>
<p>The nametable shows TIPC publication information.</p>
<h3>Nametable format</h3>
<dl>
<dt><code>Type</code></p>
<dd>The 32-bit type field of the port name. The type field often indicates the class of service provided by a port.</p>
<dt><code>Lower</code></p>
<dd>The lower bound of the 32-bit instance field of the port name. The instance field is often used as as a sub-class indicator.</p>
<dt><code>Upper</code></p>
<dd>The upper bound of the 32-bit instance field of the port name. The instance field is often used as as a sub-class indicator. A difference in <code>lower </code>and <code>upper</code> means the socket is bound to the port name range [lower,upper]</p>
<dt><code>Port Identity</code></p>
<dd>The unique socket (port) identifier within the TIPC cluster. The <code>port identity</code> consists of a node identity followed by a socket reference number.</p>
<dt><code>Publication</code></p>
<dd>The <code>publication</code> ID is a random number used internally to represent a publication.</p>
<dt><code>Scope</code></p>
<dd>The publication <code>scope</code> specifies the visibility of a bound port name. The <code>scope</code> can be specified to comprise three different domains: <code>node</code>, <code>cluster </code>and <code>zone.</code> Applications residing within the specified <code>scope</code> can see and access the port using the displayed port name. </p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
