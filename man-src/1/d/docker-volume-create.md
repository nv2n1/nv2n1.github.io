---
title: "docker-volume-create(1)"
name: "docker-volume-create"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-volume-create/"
description: "docker-volume-create – Create a volume"
---

<h2 class="name">NAME</h2>
<p> docker-volume-create &#8211; Create a volume </p>
<h2>SYNOPSIS</h2>
<p> <code>docker volume create [OPTIONS] [VOLUME]</code> </p>
<h2>DESCRIPTION</h2>
<p> Creates a new volume that containers can consume and store data in. If a name is not specified, Docker generates a random name. You create a volume and then configure the container to use it, for example: </p>
<dl>
<dt>
<dd>
<pre>
$ docker volume create hello
hello
$ docker run -d -v hello:/world busybox ls /world
</pre>
</dl>
<p> The mount is created inside the container&#8217;s /src directory. Docker does not support relative paths for mount points inside the container. </p>
<p> Multiple containers can use the same volume in the same time period. This is useful if two containers need access to shared data. For example, if one container writes and the other reads the data. </p>
<h2>Driver specific options</h2>
<p> Some volume drivers may take options to customize the volume creation. Use the -o or &#8211;opt flags to pass driver options: </p>
<dl>
<dt>
<dd>
<pre>
$ docker volume create --driver fake --opt tardis=blue --opt timey=wimey
</pre>
</dl>
<p> These options are passed directly to the volume driver. Options for different volume drivers may do different things (or nothing at all). </p>
<p> The built-in local driver on Windows does not support any options. </p>
<p> The built-in local driver on Linux accepts options similar to the linux mount command: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker volume create-- driver local-- opt type = tmpfs-- opt device = tmpfs-- opt o = size = 100m, uid = 1000
</code></pre>
</dl>
<p> Another example: </p>
<dl>
<dt>
<dd>
<pre>
$ docker volume create --driver local --opt type=btrfs --opt device=/dev/sda2
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-d</code>, <code>&#8211;driver</code>=&quot;local&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Specify volume driver name</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for create</p>
<p> <code>&#8211;label</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set metadata for a volume</p>
<p> <code>-o</code>, <code>&#8211;opt</code>=map[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set driver specific options</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-volume/">docker-volume</a>(1)</code> </p>
<h2>Index</h2>
