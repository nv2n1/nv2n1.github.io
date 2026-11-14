---
title: "arc-infoindex-server(8)"
name: "arc-infoindex-server"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arc-infoindex-server/"
description: "arc-infoindex-server – ARC Information Index Server"
---

<p>arc-infoindex-server &#8211; ARC Information Index Server</p>
<h2>Description</h2>
<p>The <code>arc-infoindex-server</code> accepts registrations about local information systems and other arc-infoindex-servers creating an hierarcical information system for discovering Grid resources </p>
<h2>Synopsis</h2>
<p><code>arc-infoindex-relay</code> -c <i>conffile</i> -f <i>fifo</i> </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> conffile</p>
<dd>The configuration file, usually /etc/arc.conf</dl>
<dl>
<dt><code>-f</code> fifo</p>
<dd>The FIFO on which the server will accept queries</dl>
<h2>Extended Description</h2>
<p><code>arc-infoindex-server</code> accepts registrations with information about local information systems and other arc-infoindex-servers. It also responds to status queries returning the list of registered resources and their registration status (valid, invalid or purged). </p>
<p> Queries are accepted on a FIFO and are normally forwarded from a slapd server through an arc-infoindex-relay process. The first line of a query should contain the name of a FIFO on which the response should be returned. The remaining part of the query should be a Globus MDS query in LDIF format. </p>
<p> To stop arc-infoindex-server write the special query &quot;STOP&quot; to the server FIFO.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/arc.conf</code></p>
<dd>Several resource indices can be kept in the same server. Each of them should have an [infosys/index] block in the configuration file. The set of resoures that are allowed to register to each index can be limited using allowreg keys. </p>
<p> Here is an example configuration: </p>
<pre>[infosys/index/Sweden]
allowreg=&quot;*.uu.se:2135&quot;
allowreg=&quot;*.lu.se:2135&quot;
allowreg=&quot;*.liu.se:2135&quot;
allowreg=&quot;*.umu.se:2135&quot;
allowreg=&quot;*.chalmers.se:2135&quot;
allowreg=&quot;*.kth.se:2135&quot;</pre>
</dl>
<h2>Copyright</h2>
<p>APACHE LICENSE Version 2.0</p>
<h2>Author</h2>
<p>Mattias Ellert &lt;mattias.ellert [at] fysast.uu.se&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arc-infoindex-relay/">arc-infoindex-relay</a></code>(8), <code><a href="/docs/linux/man/5-arc-conf/">arc.conf</a></code>(5) </p>
