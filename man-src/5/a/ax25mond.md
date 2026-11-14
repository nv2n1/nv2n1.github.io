---
title: "ax25mond(5)"
name: "ax25mond"
section: "5"
letter: "a"
url: "/docs/linux/man/5-ax25mond/"
description: "ax25mond.conf – Specify the sockets which ax25mond will provide."
---

<p>ax25mond.conf &#8211; Specify the sockets which ax25mond will provide.</p>
<h2>Description</h2>
<p>The <code>ax25mond.conf</code> file specifies the internet- and unix-sockets which <a href="/docs/linux/man/8-ax25mond/">ax25mond</a>(8) will provide. Example: </p>
<p> # Create an internet socket on port 1234 where all the<br />
 # AX.25 traffic will be transmitted<br />
 rxtx *:1234<br />
 # Create an unix socket where only the received AX.25<br />
 # traffic will be transmitted<br />
 rx unix:/var/spool/ax25/monitor </p>
<p> You may specify up to 5 sockets (definable in ax25mond.c) and ax25mond will accept up to 50 connects (also definable in ax25mond.c).</p>
<h2>Files</h2>
<p>/etc/ax25/ax25mond.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ax25mond/">ax25mond</a></code>(8). </p>
