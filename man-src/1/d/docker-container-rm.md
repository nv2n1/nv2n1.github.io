---
title: "docker-container-rm(1)"
name: "docker-container-rm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-rm/"
description: "docker-container-rm – Remove one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-container-rm &#8211; Remove one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container rm [OPTIONS] CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>docker container rm</code> will remove one or more containers from the host node. The container name or ID can be used. This does not remove images. You cannot remove a running container unless you use the <code>-f</code> option. To see all containers on a host use the <code>docker container ls -a</code> command. </p>
<h2>EXAMPLES</h2>
<h2>Removing a container using its ID</h2>
<p> To remove a container using its ID, find either from a <code>docker ps -a</code> command, or use the ID returned from the <code>docker run</code> command, or retrieve it from a file used to store it using the <code>docker run &#8211;cidfile</code>: </p>
<dl>
<dt>
<dd>
<pre>
docker container rm abebf7571666
</pre>
</dl>
<h2>Removing a container using the container name</h2>
<p> The name of the container can be found using the <code>docker ps -a</code> command. The use that name as follows: </p>
<dl>
<dt>
<dd>
<pre>
docker container rm hopeful_morse
</pre>
</dl>
<h2>Removing a container and all associated volumes</h2>
<dl>
<dt>
<dd>
<pre>
$ docker container rm -v redis
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
$ docker container rm -v hello
</pre>
</dl>
<p> In this example, the volume for /foo will remain in tact, but the volume for /bar will be removed. The same behavior holds for volumes inherited with &#8211;volumes-from. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;force</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Force the removal of a running container (uses SIGKILL)</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for rm</p>
<p> <code>-l</code>, <code>&#8211;link</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Remove the specified link</p>
<p> <code>-v</code>, <code>&#8211;volumes</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Remove anonymous volumes associated with the container</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
