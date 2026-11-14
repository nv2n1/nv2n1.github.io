---
title: "nodesave(8)"
name: "nodesave"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nodesave/"
description: "nodesave – Saves NET/ROM routing information"
---

<p>nodesave &#8211; Saves NET/ROM routing information</p>
<h2>Synopsis</h2>
<p><code>nodesave [-p path] [-v] [filename]</code></p>
<h2>Description</h2>
<p><code>Nodesave</code> saves the contents of the /proc filesystem entries for the NET/ROM routing tables. The output of the program is in the form of a Bourne shell script that calls <a href="/docs/linux/man/8-nrparms/">nrparms</a>(8) to recreate the NET/ROM routing information. If no filename is given on the command line, the program writes the script to stdout. </p>
<p> Typically <code>nodesave</code> would be used when taking a system off-air so that the NET/ROM routing may be quickly restored when the system is brought back on-line.</p>
<h2>Options</h2>
<dl>
<dt><code>-p path</code></p>
<dd>Set the path to the nrparms binary. This only affects the output of the program. Default is /usr/sbin.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<pre>/proc/net/nr_neigh
<br>
/proc/net/nr_nodes</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/8-netromd/">netromd</a></code>(8), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8). </p>
<h2>Author</h2>
<p>Tomi Manninen OH2BNS &lt;oh2bns [at] sral.fi&gt;</p>
