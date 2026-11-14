---
title: "rip98d(5)"
name: "rip98d"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rip98d/"
description: "rip98d.conf – control RIP98 routing messages."
---

<p>rip98d.conf &#8211; control RIP98 routing messages.</p>
<h2>Description</h2>
<p><code>Rip98d.conf</code> controls the transmission of RIP98 routing messages. RIP98 is not a broadcast protocol but instead is transmitted individually to each other known RIP98 capable system. The list of these systems is kept in the RIP98 configuration file as a list of host names or IP numbers that are to be transmitted to, and messages received from.</p>
<h2>Files</h2>
<p>/etc/ax25/rip98d.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arp/">arp</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-rip98d/">rip98d</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8). </p>
