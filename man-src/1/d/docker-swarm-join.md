---
title: "docker-swarm-join(1)"
name: "docker-swarm-join"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-swarm-join/"
description: "docker-swarm-join – Join a swarm as a node and/or manager"
---

<h2 class="name">NAME</h2>
<p> docker-swarm-join &#8211; Join a swarm as a node and/or manager </p>
<h2>SYNOPSIS</h2>
<p> <code>docker swarm join [OPTIONS] HOST:PORT</code> </p>
<h2>DESCRIPTION</h2>
<p> Join a swarm as a node and/or manager </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;advertise-addr</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Advertised address (format: [:port])</p>
<p> <code>&#8211;availability</code>=&quot;active&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Availability of the node (&quot;active&quot;|&quot;pause&quot;|&quot;drain&quot;)</p>
<p> <code>&#8211;data-path-addr</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Address or interface to use for data path traffic (format: )</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for join</p>
<p> <code>&#8211;listen-addr</code>=0.0.0.0:2377 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Listen address (format: [:port])</p>
<p> <code>&#8211;token</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Token for entry into the swarm</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-swarm/">docker-swarm</a>(1)</code> </p>
<h2>Index</h2>
