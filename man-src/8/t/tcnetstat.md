---
title: "tcnetstat(8)"
name: "tcnetstat"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcnetstat/"
---

tcnetstat - Print information about network connections protected by tcpcrypt

<h2>Synopsis</h2>

tcnetstat

<h2>Description</h2>

The tcnetstat utility prints the session id of each TCP connection that is currently being protected by the tcpcrypt protocol.

<h2>Options</h2>

Where the tcpcrypt protocol is implemented by the tcpcryptd daemon, this utility communicates with the daemon via a &quot;control socket&quot;, configurable with -u socket_address. If socket_address begins with &quot;/&quot;, it is interpreted as a filesystem path pointing to a unix-domain socket; if it is of the form &quot;:port&quot;, it is interpreted as the internet address localhost:port.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-tcpcryptd/">tcpcryptd</a>(8), &lt;<a rel="nofollow" HREF="http://tcpcrypt.org/">http://tcpcrypt.org/</a>&gt; 
