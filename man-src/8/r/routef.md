---
title: "routef(8)"
name: "routef"
section: "8"
letter: "r"
url: "/docs/linux/man/8-routef/"
---

routel - list routes with pretty output format 
 routef - flush routes

<h2>Syntax</h2>

routel [<i>tablenr</i> [<i>raw ip args...</i>]] 
 routef

<h2>Description</h2>

These programs are a set of helper scripts you can use instead of raw iproute2 commands. 
 The routel script will list routes in a format that some might consider easier to interpret then the ip route list equivalent. 
 The routef script does not take any arguments and will simply flush the routing table down the drain. Beware! This means deleting all routes which will make your network unusable! 

<h2>Authors</h2>

The routel script was written by Stephen R. van den Berg &lt;srb [at] cuci.nl&gt;, 1999/04/18 and donated to the public domain. 
 This manual page was written by Andreas Henriksson &lt;andreas [at] fatal.se&gt;, for the Debian GNU/Linux system.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-ip/">ip</a>(8) 
