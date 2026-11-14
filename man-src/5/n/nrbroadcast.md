---
title: "nrbroadcast(5)"
name: "nrbroadcast"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nrbroadcast/"
description: "nrbroadcast – NET/ROM routing broadcast configuration file."
---

<p>nrbroadcast &#8211; NET/ROM routing broadcast configuration file.</p>
<h2>Description</h2>
<p><code>Nrbroadcast</code> is an ASCII file that contains information about each of the physical AX.25 ports that are to have NET/ROM routing broadcasts transmitted from them. </p>
<p> Each line has the following format, each field being delimited by white space: </p>
<dl>
<dd>port minobs defqual worstqual verbose</dl>
<p> The field descriptions are: </p>
<dl>
<dd>
<dl>
<dt><code>port</code></p>
<dd>the port name of the AX.25 port to broadcast on.</p>
<dt><code>minobs</code></p>
<dd>this is the minimum obsolescence count of a routing table entry to be broadcast on this port.</p>
<dt><code>defqual</code></p>
<dd>this is the default quality of an incoming routing broadcast from an unknown neighbour.</p>
<dt><code>worstqual</code></p>
<dd>this is the worst quality node received from a routing broadcast that will be added to our routing table.</p>
<dt><code>verbose</code></p>
<dd>whether the routes to all of my nodes in my routing table, or just the nodes resident on my machine are to be broadcast.</dl>
</dl>
<h2>Files</h2>
<p>/etc/ax25/nrbroadcast<br />
 /etc/ax25/axports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/8-netromd/">netromd</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8). </p>
