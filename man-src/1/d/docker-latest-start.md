---
title: "docker-latest-start(1)"
name: "docker-latest-start"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-start/"
description: "docker-start – Start one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-start &#8211; Start one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker start</code> [<code>-a</code>|<code>&#8211;attach</code>] [<code>&#8211;detach-keys</code>[=<i>[]</i>]] [<code>&#8211;help</code>] [<code>-i</code>|<code>&#8211;interactive</code>] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Start one or more containers. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;attach</code>=<i>true</i>|<i>false</i><br />
Attach container&#8217;s STDOUT and STDERR and forward all signals to the<br />
process. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;detach-keys</code>=&quot;&quot;<br />
Override the key sequence for detaching a container. Format is a single character&nbsp;<wbr>[a-Z]&nbsp;<wbr>or ctrl-&lt;value&gt;&nbsp;<wbr>where&nbsp;<wbr>&lt;value&gt;&nbsp;<wbr>is one of: a-z,&nbsp;<wbr>@,&nbsp;<wbr>^,&nbsp;<wbr>[, , or&nbsp;<wbr>_. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-i</code>, <code>&#8211;interactive</code>=<i>true</i>|<i>false</i><br />
Attach container&#8217;s STDIN. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-stop/">docker-stop</a>(1)</code> to stop a container. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
