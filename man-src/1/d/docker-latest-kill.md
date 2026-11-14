---
title: "docker-latest-kill(1)"
name: "docker-latest-kill"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-kill/"
description: "docker-kill – Kill a running container using SIGKILL or a specified signal"
---

<h2 class="name">NAME</h2>
<p> docker-kill &#8211; Kill a running container using SIGKILL or a specified signal </p>
<h2>SYNOPSIS</h2>
<p> <code>docker kill</code> [<code>&#8211;help</code>] [<code>-s</code>|<code>&#8211;signal</code>[=<i>&quot;KILL&quot;</i>]] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The main process inside each container specified will be sent SIGKILL,<br />
&nbsp;<wbr>or any signal specified with option &#8211;signal. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-s</code>, <code>&#8211;signal</code>=&quot;<i>KILL</i>&quot;<br />
Signal to send to the container </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com)<br />
&nbsp;<wbr>based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
