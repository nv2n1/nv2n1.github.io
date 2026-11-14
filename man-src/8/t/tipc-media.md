---
title: "tipc-media(8)"
name: "tipc-media"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-media/"
description: "tipc-media – list or modify media properties"
---

<p>tipc-media &#8211; list or modify media properties</p>
<h2>Synopsis</h2>
<p> <code>tipc media set</code> { <code>priority </code> <i>PRIORITY</i> | <code>tolerance</code> <i>TOLERANCE</i> | <code>window</code> <i>WINDOW </i>} <code>media </code><i>MEDIA</i><br />
 <code>tipc media get</code> { <code>priority</code> | <code>tolerance</code> | <code>window</code> } <code>media</code> <i>MEDIA</i><br />
 <code>tipc media list</code> </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last valid command. For example <code>tipc media &#8211;help</code> will show media help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant.</dl>
<h2>Description</h2>
<h3>Media properties</h3>
<dl>
<dt><code>priority</code></p>
<dd>Default link priority inherited by all bearers subsequently enabled on a media. For more info about link priority see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8)</p>
<dt><code>tolerance</code></p>
<dd>Default link tolerance inherited by all bearers subsequently enabled on a media. For more info about link tolerance see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8)</p>
<dt><code>window</code></p>
<dd>Default link window inherited by all bearers subsequently enabled on a media. For more info about link window see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8) </p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-bearer/">tipc-bearer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
