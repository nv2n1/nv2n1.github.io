---
title: "docker-container-unpause(1)"
name: "docker-container-unpause"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-unpause/"
description: "docker-container-unpause – Unpause all processes within one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-container-unpause &#8211; Unpause all processes within one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container unpause CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> The docker container unpause command un-suspends all processes in a container. On Linux, it does this using the freezer cgroup. </p>
<p> See the freezer cgroup documentation &lt;<a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt">https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt</a>&gt; for further details. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for unpause</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
