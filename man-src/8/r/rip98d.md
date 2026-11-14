---
title: "rip98d(8)"
name: "rip98d"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rip98d/"
description: "rip98d – Send and receive RIP98 routing messages"
---

<p>rip98d &#8211; Send and receive RIP98 routing messages</p>
<h2>Synopsis</h2>
<p><code>rip98d [-d] [-l] [-r] [-t interval] [-v]</code></p>
<h2>Description</h2>
<p>The RIP98 routing protocol was devised by John Wiseman G8BPQ as an alternative to both traditional RIP and RSPF for use in an RF environment. Its main advantage is that each routing element only takes six bytes and is therefore much more efficient in terms of bandwidth than other routing protocols. </p>
<p> In operation <code>rip98d</code> that each neighbour that also uses RIP98 must be listed. RIP98 is not a broadcast protocol and each neighbour is individually contacted. Any incoming RIP98 message is also validated against this list. The list of neighbours is held in /etc/ax25/rip98d.conf, and each line is either the name or the dotted decimal IP address of the neighbour. </p>
<p> The time interval between RIP98 transmissions is set to one hour by default but other intervals can be set with the -t option. The routes advertised and received can be restricted by the -r option which only allows processing of ampr.org addresses. At present <code>rip98d</code> is under development and any feedback on its operation would be welcome.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Set debugging on. Information is only output if the logging option is also enabled.</p>
<dt><code>-l</code></p>
<dd>Enable logging to the system log, the default is off.</p>
<dt><code>-r</code></p>
<dd>Restricts the transmitting and receiving of routes to ampr.org (44.x.x.x) addresses only.</p>
<dt><code>-t interval</code></p>
<dd>The time interval between routing broadcasts, in minutes. The default is 60 minutes.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<pre>/proc/net/route
<br>
/etc/ax25/rip98d.conf</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rip98-conf/">rip98.conf</a></code>(5), <code><a href="/docs/linux/man/8-arp/">arp</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-route/">route</a></code>(8).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
