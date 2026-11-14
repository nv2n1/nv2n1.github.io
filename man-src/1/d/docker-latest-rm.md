---
title: "docker-latest-rm(1)"
name: "docker-latest-rm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-rm/"
description: "docker-rm – Remove one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-rm &#8211; Remove one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker rm</code> [<code>-f</code>|<code>&#8211;force</code>] [<code>-l</code>|<code>&#8211;link</code>] [<code>-v</code>|<code>&#8211;volumes</code>] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>docker rm</code> will remove one or more containers from the host node. The container name or ID can be used. This does not remove images. You cannot remove a running container unless you use the <code>-f</code> option. To see all containers on a host use the <code>docker ps -a</code> command. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-f</code>, <code>&#8211;force</code>=<i>true</i>|<i>false</i><br />
Force the removal of a running container&nbsp;<wbr>(uses SIGKILL). The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-l</code>, <code>&#8211;link</code>=<i>true</i>|<i>false</i><br />
Remove the specified link and not the underlying container. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>-v</code>, <code>&#8211;volumes</code>=<i>true</i>|<i>false</i><br />
Remove the volumes associated with the container. The default is&nbsp;<wbr><i>false</i>. </p>
<h2>EXAMPLES</h2>
<h2>Removing a container using its ID</h2>
<p> To remove a container using its ID, find either from a <code>docker ps -a</code> command, or use the ID returned from the <code>docker run</code> command, or retrieve it from a file used to store it using the <code>docker run &#8211;cidfile</code>: </p>
<dl>
<dt>
<dd>
<pre>
docker rm abebf7571666
</pre>
</dl>
<h2>Removing a container using the container name</h2>
<p> The name of the container can be found using the <code>docker ps -a</code> command. The use that name as follows: </p>
<dl>
<dt>
<dd>
<pre>
docker rm hopeful_morse
</pre>
</dl>
<h2>Removing a container and all associated volumes</h2>
<dl>
<dt>
<dd>
<pre>
$ docker rm -v redis
redis
</pre>
</dl>
<p> This command will remove the container and any volumes associated with it. Note that if a volume was specified with a name, it will not be removed. </p>
<dl>
<dt>
<dd>
<pre>
$ docker create -v awesome:/foo -v /bar --name hello redis
hello
$ docker rm -v hello
</pre>
</dl>
<p> In this example, the volume for /foo will remain in tact, but the volume for /bar will be removed. The same behavior holds for volumes inherited with &#8211;volumes-from. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; July 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; August 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; </p>
<h2>Index</h2>
