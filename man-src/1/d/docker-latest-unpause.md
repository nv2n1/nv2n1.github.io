---
title: "docker-latest-unpause(1)"
name: "docker-latest-unpause"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-unpause/"
description: "docker-unpause – Unpause all processes within a container"
---

<h2 class="name">NAME</h2>
<p> docker-unpause &#8211; Unpause all processes within a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker unpause</code> CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The docker unpause command uses the cgroups freezer to un-suspend all processes in a container. </p>
<p> See the &lt;<a rel="nofollow" href="https://www.kernel.org/doc/Documentation/cgroups/freezer-subsystem.txt">https://www.kernel.org/doc/Documentation/cgroups/freezer-subsystem.txt</a>&gt; for further details. </p>
<h2>OPTIONS</h2>
<p> There are no available options. </p>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-pause/">docker-pause</a>(1)</code> to pause all processes within a container. </p>
<h2>HISTORY</h2>
<p> June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
