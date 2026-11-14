---
title: "rxecho(5)"
name: "rxecho"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rxecho/"
description: "rxecho.conf – control rxecho AX.25 packet routing."
---

<p>rxecho.conf &#8211; control rxecho AX.25 packet routing.</p>
<h2>Description</h2>
<p><code>Rxecho.conf</code> controls the copying of packets between AX.25 ports performed by the program rxecho. The format of the configuration file is: </p>
<p> portin<tt>&nbsp;<wbr>&nbsp;<wbr></tt>portout<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>* | callsign&#8230;</p>
<p> Each entry in the file represents a one-way packet flow between ports. Any packet received on portin is copied to portout, if its destination callsign or the next callsign to digipeat the frame is in the list of callsigns. If the callsign list is replaced by a lq*rq then all packets are copied. The configuration file may contain comments that begin with a #.</p>
<h2>Files</h2>
<p>/etc/ax25/rxecho.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-axports/">axports</a></code>(8), <code><a href="/docs/linux/man/8-rxecho/">rxecho</a></code>(8). </p>
