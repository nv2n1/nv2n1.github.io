---
title: "docker-latest-top(1)"
name: "docker-latest-top"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-top/"
description: "docker-top – Display the running processes of a container"
---

<h2 class="name">NAME</h2>
<p> docker-top &#8211; Display the running processes of a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker top</code> [<code>&#8211;help</code>] CONTAINER [ps OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> Display the running process of the container. ps-OPTION can be any of the options you would pass to a Linux ps command. </p>
<p> All displayed information is from host&#8217;s point of view. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<h2>EXAMPLES</h2>
<p> Run <code>docker top</code> with the ps option of -x: </p>
<dl>
<dt>
<dd>
<pre>
$ docker top 8601afda2b -x
PID      TTY       STAT       TIME         COMMAND
16623    ?         Ss         0:00         sleep 99999
</pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; June 2015, updated by Ma Shimiao &lt;mashimiao.fnst [at] cn.fujitsu.com&gt; December 2015, updated by Pavel Pospisil &lt;pospispa [at] gmail.com&gt; </p>
<h2>Index</h2>
