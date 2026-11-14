---
title: "docker-container-port(1)"
name: "docker-container-port"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-port/"
description: "docker-container-port – List port mappings or a specific mapping for the container"
---

<h2 class="name">NAME</h2>
<p> docker-container-port &#8211; List port mappings or a specific mapping for the container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container port CONTAINER [PRIVATE_PORT[/PROTO]]</code> </p>
<h2>DESCRIPTION</h2>
<p> List port mappings for the CONTAINER, or lookup the public-facing port that is NAT-ed to the PRIVATE_PORT </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                            NAMES
b650456536c7        busybox:latest      top                 54 minutes ago      Up 54 minutes       0.0.0.0:1234-&gt;9876/tcp, 0.0.0.0:4321-&gt;7890/tcp   test
</pre>
</dl>
<h2>Find out all the ports mapped</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container port test
7890/tcp -&gt; 0.0.0.0:4321
9876/tcp -&gt; 0.0.0.0:1234
</pre>
</dl>
<h2>Find out a specific mapping</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container port test 7890/tcp
0.0.0.0:4321
$ docker container port test 7890
0.0.0.0:4321
</pre>
</dl>
<h2>An example showing error for non-existent mapping</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container port test 7890/udp
2014/06/24 11:53:36 Error: No public port '7890/udp' published for test
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for port</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
