---
title: "docker-latest-update(1)"
name: "docker-latest-update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-update/"
description: "docker-update – Update configuration of one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-update &#8211; Update configuration of one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker update</code> [<code>&#8211;blkio-weight</code>[=<i>[BLKIO-WEIGHT]</i>]] [<code>&#8211;cpu-shares</code>[=<i>0</i>]] [<code>&#8211;cpu-period</code>[=<i>0</i>]] [<code>&#8211;cpu-quota</code>[=<i>0</i>]] [<code>&#8211;cpuset-cpus</code>[=<i>CPUSET-CPUS</i>]] [<code>&#8211;cpuset-mems</code>[=<i>CPUSET-MEMS</i>]] [<code>&#8211;help</code>] [<code>&#8211;kernel-memory</code>[=<i>KERNEL-MEMORY</i>]] [<code>-m</code>|<code>&#8211;memory</code>[=<i>MEMORY</i>]] [<code>&#8211;memory-reservation</code>[=<i>MEMORY-RESERVATION</i>]] [<code>&#8211;memory-swap</code>[=<i>MEMORY-SWAP</i>]] [<code>&#8211;restart</code>[=<i>&quot;&quot;</i>]] CONTAINER [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The docker update command dynamically updates container configuration. you can Use this command to prevent containers from consuming too many resources from their Docker host. With a single command, you can place limits on a single container or on many. To specify more than one container, provide space-separated list of container names or IDs. </p>
<p> With the exception of the &#8211;kernel-memory value, you can specify these options on a running or a stopped container. You can only update &#8211;kernel-memory on a stopped container. When you run docker update on stopped container, the next time you restart it, the container uses those values. </p>
<p> Another configuration you can change with this command is restart policy, new restart policy will take effect instantly after you run docker update on a container. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;blkio-weight</code>=0<br />
Block IO weight&nbsp;<wbr>(relative weight)&nbsp;<wbr>accepts a weight value between 10 and 1000. </p>
<p> <code>&#8211;cpu-shares</code>=0<br />
CPU shares&nbsp;<wbr>(relative weight) </p>
<p> <code>&#8211;cpu-period</code>=0<br />
Limit the CPU CFS&nbsp;<wbr>(Completely Fair Scheduler)&nbsp;<wbr>period </p>
<p> <code>&#8211;cpu-quota</code>=0<br />
Limit the CPU CFS&nbsp;<wbr>(Completely Fair Scheduler)&nbsp;<wbr>quota </p>
<p> <code>&#8211;cpuset-cpus</code>=&quot;&quot;<br />
CPUs in which to allow execution&nbsp;<wbr>(0-3, 0,1) </p>
<p> <code>&#8211;cpuset-mems</code>=&quot;&quot;<br />
Memory nodes(MEMs)&nbsp;<wbr>in which to allow execution&nbsp;<wbr>(0-3, 0,1). Only effective on NUMA systems. </p>
<p> <code>&#8211;help</code><br />
Print usage statement </p>
<p> <code>&#8211;kernel-memory</code>=&quot;&quot;<br />
Kernel memory limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;[&lt;unit&gt;], where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> Note that you can not update kernel memory to a running container, it can only be updated to a stopped container, and affect after it&#8217;s started. </p>
<p> <code>-m</code>, <code>&#8211;memory</code>=&quot;&quot;<br />
Memory limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;&lt;optional unit&gt;, where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> <code>&#8211;memory-reservation</code>=&quot;&quot;<br />
Memory soft limit&nbsp;<wbr>(format:&nbsp;<wbr>&lt;number&gt;[&lt;unit&gt;], where unit&nbsp;<wbr>=&nbsp;<wbr>b, k, m or g) </p>
<p> <code>&#8211;memory-swap</code>=&quot;&quot;<br />
Total memory limit&nbsp;<wbr>(memory&nbsp;<wbr>+&nbsp;<wbr>swap) </p>
<p> <code>&#8211;restart</code>=&quot;&quot;<br />
Restart policy to apply when a container exits&nbsp;<wbr>(no, on-failure[:max-retry], always, unless-stopped). </p>
<h2>EXAMPLES</h2>
<p> The following sections illustrate ways to use this command. </p>
<h3>Update a container with cpu-shares=512</h3>
<p> To limit a container&#8217;s cpu-shares to 512, first identify the container name or ID. You can use <code>docker ps</code> to find these values. You can also use the ID returned from the <code>docker run</code> command. Then, do the following: </p>
<dl>
<dt>
<dd>
<pre>
$ docker update --cpu-shares 512 abebf7571666
</pre>
</dl>
<h3>Update a container with cpu-shares and memory</h3>
<p> To update multiple resource configurations for multiple containers: </p>
<dl>
<dt>
<dd>
<pre>
$ docker update --cpu-shares 512 -m 300M abebf7571666 hopeful_morse
</pre>
</dl>
<h3>Update a container&#8217;s restart policy</h3>
<p> To update restart policy for one or more containers: </p>
<dl>
<dt>
<dd>
<pre>
$ docker update --restart=on-failure:3 abebf7571666 hopeful_morse
</pre>
</dl>
<h2>Index</h2>
