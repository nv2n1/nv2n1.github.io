---
title: "dhcp6relay(8)"
name: "dhcp6relay"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcp6relay/"
description: "dhcp6relay – DHCPv6 relay agent"
---

<p><code>dhcp6relay</code> &#8211; DHCPv6 relay agent</p>
<h2>Synopsis</h2>
<p>[-<code>Ddf</code> ] [-<code>b </code><i>boundaddr</i> ] [-<code>H </code><i>hoplim</i> ] [-<code>r </code><i>relay-IF</i> ] [-<code>s </code><i>serveraddr</i> ] [-<code>S </code><i>script-file</i> ] [-<code>p </code><i>pid-file</i> ] <i>interface &#8230;</i></p>
<h2>Description</h2>
<p>acts as an intermediary to deliver DHCPv6 messages between clients and servers, and is on the same link as a client. needs command line arguments <i>interface &#8230;</i> which specifies the list of links accommodating clients. Options supported by are:</p>
<dl>
<dt><code>-d</code></p>
<dd>Print debugging messages.</p>
<dt><code>-D</code></p>
<dd>Even more debugging information is printed.</p>
<dt><code>-f</code></p>
<dd>Foreground mode (useful when debugging). Although usually prints warning, debugging, or error messages to <a href="/docs/linux/man/8-syslog/">syslog</a>(8), it prints the messages to standard error if this option is specified.</p>
<dt><code>-b </code><i>boundaddr</i></p>
<dd>Specifies the source address to relay packets to servers (or other agents).</p>
<dt><code>-H </code><i>hoplim</i></p>
<dd>Specifies the hop limit of DHCPv6 Solicit messages forwarded to servers.</p>
<dt><code>-r </code><i>relay-IF</i></p>
<dd>Specifies the interface on which messages to servers are sent. When omitted, the same interface as <i>interface</i> will be used. When multiple <i>interface</i> are specified, this option cannot be omitted.</p>
<dt><code>-s </code><i>serveraddr</i></p>
<dd>Specifies the DHCPv6 server address to relay packets to. If not specified, packets are relayed to ff05::1:3 (All DHCPv6 servers).</p>
<dt><code>-S </code><i>script-file</i></p>
<dd>Specifies the script file to be executed when receives a RELAY-REPLY message from a DHCPv6 server. Further detail of the script file syntax is available in <a href="/docs/linux/man/8-dhcp6c/">dhcp6c</a>(8)</p>
<dt><code>-p </code><i>pid-file</i></p>
<dd>Use <i>pid-file</i> to dump the process ID of <code>.</code></dl>
<h2>Files</h2>
<dl>
<dt><code>/var/run/dhcp6relay.pid </code></p>
<dd>is the default file that contains pid of the currently running <code>.</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhcp6c/">dhcp6c</a>(8), <a href="/docs/linux/man/8-dhcp6s/">dhcp6s</a>(8)</p>
<dl>
<dd>Ralph Droms, Editor 2003 <i>Dynamic Host Configuration Protocol for IPv6 (DHCPv6)</i> <i>RFC 3315</i></dl>
<h2>History</h2>
<p>The command first appeared in WIDE/KAME IPv6 protocol stack kit. </p>
<ol>
</ol>
