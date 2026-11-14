---
title: "rsparms(8)"
name: "rsparms"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rsparms/"
description: "rsparms – Configure the Rose interface."
---

<p>rsparms &#8211; Configure the Rose interface.</p>
<h2>Synopsis</h2>
<p><code>rsparms -nodes add|del address[/mask] port neigh [digis&#8230;]</code> </p>
<p> <code>rsparms -nodes list</code> </p>
<p> <code>rsparms -call &lt;callsign&gt;|none</code> </p>
<p> <code>rsparms -version</code></p>
<h2>Description</h2>
<p>This program is used to manipulate the routing tables of the Rose network layer. To set up a new route to a Rose node in the routing tables you must use the nodes option. All of the parameters are needed to add the node. It is probably best to illustrate with an example: </p>
<p> <code>rsparms -nodes add 2080192303 144 F1OAT-11</code> </p>
<p> This creates a new route to a distant node with the address 2080192303 and the packets for that node should be sent on AX.25 port 144 to my immediate neighbour F1OAT-11 without going through any digi-praters. For example to set up the same node but via a digi-peater I would use: </p>
<p> <code>rsparms -nodes add 2080192303 144 F1OAT-11 F6PRA-9</code> </p>
<p> It is also possible to remove a route to a distant node with the same command except that the lqaddrq is replaced by a lqdelrq. The other parameters must also be present. If the node has no other routes then the node will be deleted, and the neighbour node that the connections go via may also be deleted if no other node route uses it. </p>
<p> You may list the configured Rose routes using the following syntax: </p>
<p> <code>rsparms -nodes list</code> </p>
<p> This program may also be used to set up a common AX.25 level 2 callsign that will be used for the ROSE node. By default no special level 2 callsign is set, but setting it will replace any existing level 2 callsign and register another one. Setting the callsign to lqnonerq will remove the level 2 callsign. For example: </p>
<p> <code>rsparms -call VK2KTJ-10</code> </p>
<p> would set the callsign used by Rose internode traffic to VK2KTJ-10.</p>
<h2>Options</h2>
<dl>
<dt><code>-version</code></p>
<dd>Display the version information.</dl>
<h2>Files</h2>
<p>/etc/ax25/axports<br />
 /etc/ax25/rsports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/5-rsports/">rsports</a></code>(5), <code><a href="/docs/linux/man/8-rsctl/">rsctl</a></code>(8), <code><a href="/docs/linux/man/8-rsparms/">rsparms</a></code>(8).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
