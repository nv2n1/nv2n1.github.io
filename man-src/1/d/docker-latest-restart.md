---
title: "docker-latest-restart(1)"
name: "docker-latest-restart"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-restart/"
description: "docker-restart – Restart one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-restart &#8211; Restart one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker restart</code> [<code>&#8211;help</code>] [<code>-t</code>|<code>&#8211;time</code>[=<i>10</i>]] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Restart each container listed. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-t</code>, <code>&#8211;time</code>=<i>10</i><br />
Number of seconds to try to stop for before killing the container. Once killed it will then be restarted. Default is 10 seconds. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
