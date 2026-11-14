---
title: "docker-container-top(1)"
name: "docker-container-top"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-top/"
description: "docker-container-top – Display the running processes of a container"
---

<h2 class="name">NAME</h2>
<p> docker-container-top &#8211; Display the running processes of a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container top CONTAINER [ps OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Display the running process of the container. ps-OPTION can be any of the options you would pass to a Linux ps command. </p>
<p> All displayed information is from host&#8217;s point of view. </p>
<h2>EXAMPLES</h2>
<p> Run <code>docker container top</code> with the ps option of -x: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container top 8601afda2b -x
PID      TTY       STAT       TIME         COMMAND
16623    ?         Ss         0:00         sleep 99999
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for top</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
