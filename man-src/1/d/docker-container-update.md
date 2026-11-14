---
title: "docker-container-update(1)"
name: "docker-container-update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-update/"
description: "docker-container-update – Update configuration of one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-container-update &#8211; Update configuration of one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container update [OPTIONS] CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>docker container update</code> command dynamically updates container configuration. You can use this command to prevent containers from consuming too many resources from their Docker host. With a single command, you can place limits on a single container or on many. To specify more than one container, provide space-separated list of container names or IDs. </p>
<p> With the exception of the <code>&#8211;kernel-memory</code> option, you can specify these options on a running or a stopped container. On kernel version older than 4.6, You can only update <code>&#8211;kernel-memory</code> on a stopped container or on a running container with kernel memory initialized. </p>
<h2>OPTIONS</h2>
<h2>kernel-memory</h2>
<p> Kernel memory limit (format: &lt;number&gt;[&lt;unit&gt;], where unit = b, k, m or g) </p>
<p> Note that on kernel version older than 4.6, you can not update kernel memory on a running container if the container is started without kernel memory initialized, in this case, it can only be updated after it&#8217;s stopped. The new setting takes effect when the container is started. </p>
<h2>memory</h2>
<p> Memory limit (format: , where unit = b, k, m or g) </p>
<p> Note that the memory should be smaller than the already set swap memory limit. If you want update a memory limit bigger than the already set swap memory limit, you should update swap memory limit at the same time. If you don&#8217;t set swap memory limit on docker create/run but only memory limit, the swap memory is double the memory limit. </p>
<h2>EXAMPLES</h2>
<p> The following sections illustrate ways to use this command. </p>
<h3>Update a container&#8217;s cpu-shares</h3>
<p> To limit a container&#8217;s cpu-shares to 512, first identify the container name or ID. You can use <code>docker ps</code> to find these values. You can also use the ID returned from the <code>docker run</code> command. Then, do the following: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container update --cpu-shares 512 abebf7571666
</pre>
</dl>
<h3>Update a container with cpu-shares and memory</h3>
<p> To update multiple resource configurations for multiple containers: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container update --cpu-shares 512 -m 300M abebf7571666 hopeful_morse
</pre>
</dl>
<h3>Update a container&#8217;s kernel memory constraints</h3>
<p> You can update a container&#8217;s kernel memory limit using the <code>&#8211;kernel-memory</code> option. On kernel version older than 4.6, this option can be updated on a running container only if the container was started with <code>&#8211;kernel-memory</code>. If the container was started <i>without</i> <code>&#8211;kernel-memory</code> you need to stop the container before updating kernel memory. </p>
<p> NOTE: The <code>&#8211;kernel-memory</code> option has been deprecated since Docker 20.10. </p>
<p> For example, if you started a container with this command: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -dit --name test --kernel-memory 50M ubuntu bash
</pre>
</dl>
<p> You can update kernel memory while the container is running: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container update --kernel-memory 80M test
</pre>
</dl>
<p> If you started a container <i>without</i> kernel memory initialized: </p>
<dl>
<dt>
<dd>
<pre>
$ docker run -dit --name test2 --memory 300M ubuntu bash
</pre>
</dl>
<p> Update kernel memory of running container test2 will fail. You need to stop the container before updating the <code>&#8211;kernel-memory</code> setting. The next time you start it, the container uses the new value. </p>
<p> Kernel version newer than (include) 4.6 does not have this limitation, you can use &#8211;kernel-memory the same way as other options. </p>
<h3>Update a container&#8217;s restart policy</h3>
<p> You can change a container&#8217;s restart policy on a running container. The new restart policy takes effect instantly after you run docker container update on a container. </p>
<p> To update restart policy for one or more containers: </p>
<dl>
<dt>
<dd>
<pre>
$ docker container update --restart=on-failure:3 abebf7571666 hopeful_morse
</pre>
</dl>
<p> Note that if the container is started with &quot;&#8211;rm&quot; flag, you cannot update the restart policy for it. The AutoRemove and RestartPolicy are mutually exclusive for the container. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;blkio-weight</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)</p>
<p> <code>&#8211;cpu-period</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU CFS (Completely Fair Scheduler) period</p>
<p> <code>&#8211;cpu-quota</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit CPU CFS (Completely Fair Scheduler) quota</p>
<p> <code>&#8211;cpu-rt-period</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit the CPU real-time period in microseconds</p>
<p> <code>&#8211;cpu-rt-runtime</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit the CPU real-time runtime in microseconds</p>
<p> <code>-c</code>, <code>&#8211;cpu-shares</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPU shares (relative weight)</p>
<p> <code>&#8211;cpus</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of CPUs</p>
<p> <code>&#8211;cpuset-cpus</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>CPUs in which to allow execution (0-3, 0,1)</p>
<p> <code>&#8211;cpuset-mems</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>MEMs in which to allow execution (0-3, 0,1)</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for update</p>
<p> <code>&#8211;kernel-memory</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Kernel memory limit</p>
<p> <code>-m</code>, <code>&#8211;memory</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Memory limit</p>
<p> <code>&#8211;memory-reservation</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Memory soft limit</p>
<p> <code>&#8211;memory-swap</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Swap limit equal to memory plus swap: &#8216;-1&#8217; to enable unlimited swap</p>
<p> <code>&#8211;pids-limit</code>=0 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Tune container pids limit (set -1 for unlimited)</p>
<p> <code>&#8211;restart</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Restart policy to apply when a container exits</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
