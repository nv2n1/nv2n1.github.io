---
title: "docker-container-pause(1)"
name: "docker-container-pause"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-pause/"
description: "docker-container-pause – Pause all processes within one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-container-pause &#8211; Pause all processes within one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container pause CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> The docker container pause command suspends all processes in the specified containers. On Linux, this uses the freezer cgroup. Traditionally, when suspending a process the SIGSTOP signal is used, which is observable by the process being suspended. With the freezer cgroup the process is unaware, and unable to capture, that it is being suspended, and subsequently resumed. On Windows, only Hyper-V containers can be paused. </p>
<p> See the freezer cgroup documentation &lt;<a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt">https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt</a>&gt; for further details. </p>
<p> <code><a href="/docs/linux/man/1-docker-container-unpause/">docker-container-unpause</a>(1)</code> to unpause all processes within a container. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for pause</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
