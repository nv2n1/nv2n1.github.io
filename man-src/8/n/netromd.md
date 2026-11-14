---
title: "netromd(8)"
name: "netromd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netromd/"
description: "netromd – Send and receive NET/ROM routing messages"
---

<p>netromd &#8211; Send and receive NET/ROM routing messages</p>
<h2>Synopsis</h2>
<p><code>netromd [-c] [-d] [-i] [-l] [-p pause] [-q quality] [-t interval] [-v]</code></p>
<h2>Description</h2>
<p>For a NET/ROM based network to operate correctly, a periodic broadcast of routing information needs to occur. Typically this occurs once every hour on every port which is expected to carry NET/ROM traffic. The purpose of <code>netromd</code> is to send and receive NET/ROM routing broadcasts. To operate correctly a set of parameters that corresponds to each AX.25 port needs to be passed to the program. This information is encoded in a configuration file, by default which is /etc/ax25/nrbroadcast with each line representing one port, see the manual page for <code><a href="/docs/linux/man/5-nrbroadcast/">nrbroadcast</a></code>(5). </p>
<p> To cut down the length of these routing broadcasts, only the information about the highest quality neighbour for a particular node is transmitted. The transmission is also limited to those node that have a certain minimum value in their obsolesence count, this value is decremented every time a routing broadcast is transmitted, and is refreshed by receiving a routing broadcast which contains that particular node. </p>
<p> The value of the default quality is traditionally assigned a value that represents the quality of the radio links on that port. A higher number representing better radio links with 255 (the maximum) reserved for wire connections. The practise in the UK is to set the default quality to a low value, typically 10, and manually set up the trusted neighbouring nodes in the neighbour list manually. The worst quality for auto-updates value is a way to filter out low quality (ie distant) nodes. </p>
<p> The verbose flag may be either 0 or 1, representing no and yes. By specifying no, the program will only generate a routing message containing information about the node on which it is running, by specifying the yes option, all the information in the nodes routing tables will be transmitted. The quality advertised for the other node callsigns on this machine may be set using the -q option. </p>
<p> Between each transmission <code>netromd</code> pauses for five seconds (default) in order to avoid flooding the channels that it must broadcast on. The value of this delay is settable with the -p option.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Forces strict compliance to Software 2000 specifications. At present this only determines how node mnemonics with lower case characters will be handled. With compliance enabled mixed case node mnemonics will be ignored. The default is to accept node mnemonics of mixed case.</p>
<dt><code>-d</code></p>
<dd>Switches on debugging messages, the default is off. Logging must be enabled for them to be output.</p>
<dt><code>-i</code></p>
<dd>Transmit a routing broadcast immediately, the default is to wait for the time interval to elapse before transmitting the first routing broadcast.</p>
<dt><code>-l</code></p>
<dd>Enables logging of errors and debug messages to the system log. The default is off.</p>
<dt><code>-p pause</code></p>
<dd>Sets the delay between transmissions of individual routing broadcast packets. The default is five seconds.</p>
<dt><code>-q quality</code></p>
<dd>Sets the quality of the subsidiary nodes relative to the main node. The default is 255.</p>
<dt><code>-t interval</code></p>
<dd>The time interval between routing broadcasts, in minutes. The default is 60 minutes.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<pre>/proc/net/nr_neigh
<br>
/proc/net/nr_nodes
<br>
/etc/ax25/axports
<br>
/etc/ax25/nrbroadcast</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/5-nrbroadcast/">nrbroadcast</a></code>(5), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/8-nrparms/">nrparms</a></code>(8).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
