---
title: "docker-latest-stop(1)"
name: "docker-latest-stop"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-stop/"
description: "docker-stop – Stop a container by sending SIGTERM and then SIGKILL after a grace period"
---

<h2 class="name">NAME</h2>
<p> docker-stop &#8211; Stop a container by sending SIGTERM and then SIGKILL after a grace period </p>
<h2>SYNOPSIS</h2>
<p> <code>docker stop</code> [<code>&#8211;help</code>] [<code>-t</code>|<code>&#8211;time</code>[=<i>10</i>]] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Stop a container (Send SIGTERM, and then SIGKILL after<br />
&nbsp;<wbr>grace period) </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-t</code>, <code>&#8211;time</code>=<i>10</i><br />
&nbsp;<wbr>&nbsp;<wbr>Number of seconds to wait for the container to stop before killing it. Default is 10 seconds. </p>
<p> #See also <code><a href="/docs/linux/man/1-docker-start/">docker-start</a>(1)</code> to restart a stopped container. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
