---
title: "docker-update(1)"
name: "docker-update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-update/"
description: "docker-update – Update configuration of one or more containers"
---

<h2 class="name">NAME</h2>
<p> docker-update &#8211; Update configuration of one or more containers </p>
<h2>SYNOPSIS</h2>
<p> <code>docker update [OPTIONS] CONTAINER [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Alias for docker container update. </p>
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
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
