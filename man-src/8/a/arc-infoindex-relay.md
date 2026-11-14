---
title: "arc-infoindex-relay(8)"
name: "arc-infoindex-relay"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arc-infoindex-relay/"
description: "arc-infoindex-relay – ARC Information Index Relay Helper"
---

<p>arc-infoindex-relay &#8211; ARC Information Index Relay Helper</p>
<h2>Description</h2>
<p>The <code>arc-infoindex-relay</code> command is used internally by the ARC Information System to relay queries and responses between the slapd server and the arc-infoindex-server </p>
<h2>Synopsis</h2>
<p><code>arc-infoindex-relay</code> <i>server-fifo</i> </p>
<h2>Arguments</h2>
<dl>
<dt><code>server-fifo</code></p>
<dd>The FIFO on which the arc-infoindex-server accepts queries</dl>
<h2>Extended Description</h2>
<p><code>arc-infoindex-relay</code> acts as a bridge between the slapd server and the arc-infoindex-server in the NorduGrid ARC Information system. For each index served by the arc-infoindex-server a shell backend database should be configured in the slapd configuration. </p>
<p> Here is a sample configuration: </p>
<pre>database shell
suffix &quot;Mds-Vo-name=Sweden,o=Grid&quot;
bind /usr/sbin/arc-infoindex-relay /var/run/arc/infosys/giis-fifo
add /usr/sbin/arc-infoindex-relay /var/run/arc/infosys/giis-fifo
search /usr/sbin/arc-infoindex-relay /var/run/arc/infosys/giis-fifo
access to * by * write</pre>
<p>When a query for the configured database is received by the slapd server, the server will call out to the arc-infoindex-relay. The arc-infoindex-relay will then open a unique return FIFO for this query and then forward the query and the name of the return FIFO to the arc-infoindex-server through the configured server FIFO. When the arc-infoindex-server has processed the query it will return the result to the arc-infoindex-relay using the return FIFO. The arc-infoindex-relay then closes the return FIFO and forwards the response to the slapd server.</p>
<h2>Copyright</h2>
<p>APACHE LICENSE Version 2.0</p>
<h2>Author</h2>
<p>Mattias Ellert &lt;mattias.ellert [at] fysast.uu.se&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arc-infoindex-server/">arc-infoindex-server</a></code>(8) </p>
