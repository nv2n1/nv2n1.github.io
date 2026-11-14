---
title: "nrparms(8)"
name: "nrparms"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nrparms/"
description: "nrparms – Configure the NET/ROM interface."
---

<p>nrparms &#8211; Configure the NET/ROM interface.</p>
<h2>Synopsis</h2>
<p><code>nrparms -nodes node +|- ident quality count port neighbour [digicall&#8230;]</code> </p>
<p> <code>nrparms -routes port nodecall [digicall&#8230;] +|- quality</code> </p>
<p> <code>nrparms -version</code></p>
<h2>Description</h2>
<p>This program is used to manipulate the routing tables of the NET/ROM network layer, or to get and set many of the network and transport layer parameters for the NET/ROM protocol. The program has three basic modes of operation, node setting, neighbour setting and general parameter setting. The syntax for the node and neighbour setting is taken from the original NET/ROM manual and is therefore not very UNIXy but should be familiar to those familiar with NET/ROMs or TheNet. </p>
<p> To set up a new route to a NET/ROM node in the routing tables you must use the nodes option. All of the parameters are needed to add the node. It is probably best to illustrate with an example: </p>
<p> <code>nrparms -nodes GB7BPQ + NMCLUS 120 6 vhf G8ROU-3</code> </p>
<p> This creates a new route to a distant node with the callsign GB7BPQ and the alias NMCLUS, it has a quality of 120 (out of 255) and has an obsolescence count of six and packets for that node should be sent on the AX.25 port named vhf to my immediate neighbour G8ROU-3. The callsigns of the node and the neighbour may be the same. For example to set up the node G8ROU-3 which is also my immediate neighbour, I would use: </p>
<p> <code>nrparms -nodes G8ROU-3 + MATLCK 200 6 vhf G8ROU-3</code> </p>
<p> If the ident of the remote node is not known, it is possible to add a node with a blank ident. To do this an ident of &#8216;*&#8217; must be entered on the command line. Because of the command line expansion that shells do, the * must be escaped by enclosing it in quotes. </p>
<p> It is also possible to remove a route to a distant node with the same command except that the + is replaced by a -. The other parameters must also be present. If the node has not other routes then the node will be deleted, and the neighbour node that the connections go via may also be deleted if no other node route uses it, and it is not a locked neighbour entry. </p>
<p> When setting up a new node, a new neighbour entry may also be created. This will have a default value. For that neighbour to be meaningful in the automatic routing process, it must have a more reasonable entry in the neighbours list. To do this the routes option of the command must be used. An example: </p>
<p> <code>nrparms -routes ax0 G8ROU-3 + 120</code> </p>
<p> This will create (or update) the neighbour entry for G8ROU-3 with a quality of 120 and it will be locked, it will not create a node entry for the neighbour. This quality will be used by the <code><a href="/docs/linux/man/8-netromd/">netromd</a></code>(8) program when calculating route qualities via this neighbour. Normally once a neighbour has zero node routes going via it, it will be deleted. Locking a neighbour prevents the deletion from occurring. To unlock a neighbour entry, the same command is used but with the + replaced by a -.</p>
<h2>Files</h2>
<p>/etc/ax25/axports<br />
 /etc/ax25/nrports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/5-nrports/">nrports</a></code>(5), <code><a href="/docs/linux/man/8-axparms/">axparms</a></code>(8), <code><a href="/docs/linux/man/8-netromd/">netromd</a></code>(8), <code><a href="/docs/linux/man/8-nrctl/">nrctl</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
