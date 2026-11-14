---
title: "docker-latest-pause(1)"
name: "docker-latest-pause"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-pause/"
description: "docker-pause – Pause all processes within a container"
---

<h2 class="name">NAME</h2>
<p> docker-pause &#8211; Pause all processes within a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker pause</code> CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The docker pause command uses the cgroups freezer to suspend all processes in a container. Traditionally when suspending a process the SIGSTOP signal is used, which is observable by the process being suspended. With the cgroups freezer the process is unaware, and unable to capture, that it is being suspended, and subsequently resumed. </p>
<p> See the &lt;<a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroups/freezer-subsystem.txt">https://www.kernel.org/doc/Documentation/cgroups/freezer-subsystem.txt</a>&gt; for further details. </p>
<h2>OPTIONS</h2>
<p> There are no available options. </p>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-unpause/">docker-unpause</a>(1)</code> to unpause all processes within a container. </p>
<h2>HISTORY</h2>
<p> June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
