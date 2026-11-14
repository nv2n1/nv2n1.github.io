---
title: "sge_schedule(5)"
name: "sge_schedule"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_schedule/"
description: "sge_schedule – format of the xxQS_NAMExx schedule file"
---

<p>sge_schedule &#8211; format of the xxQS_NAMExx schedule file</p>
<h2>Description</h2>
<p>The <i>schedule</i> file is written by the qmaster when <code>MONITOR=1</code> is set in the <code>params</code> item of </p>
<p> Note that the file tends to grow rapidly, and should be truncated/rotated, e.g. with <i><a href="/docs/linux/man/1-logrotate/">logrotate</a></i>(1). Also it should probably be placed on local disk, not an NFS-mounted filesystem, for instance, because of the large number of small writes it typically gets &#8211; e.g. make a symbolic link into the qmaster spool area (assuming that is local). </p>
<p> See for a tool to process the data and produce information on reservations.</p>
<h2>Format</h2>
<p>A line containing<br />
 <code>::::::::</code><br />
 indicates the start of a scheduling interval. It is followed by lines showing the resource usage considered for the interval. They contain the following fields, delimited by &#8216;<code>:</code>&#8216;.</p>
<dl>
<dt><code>job id</code></p>
<dd>The numeric job id;</p>
<dt><code>task id</code></p>
<dd>The task id (1 for serial jobs);</p>
<dt><code>reason</code></p>
<dd>The for listing the utilization. One of the following, depending on the job&#8217;s state:</p>
<dl>
<dd>
<dl>
<dt><code>RUNNING</code></p>
<dd>Running before the interval;</p>
<dt><code>SUSPENDED</code></p>
<dd>Suspended before the interval;</p>
<dt><code>MIGRATING</code></p>
<dd>To be preempted/migrated (currently unused);</p>
<dt><code>STARTING</code></p>
<dd>To be started;</p>
<dt><code>RESERVING</code></p>
<dd>Having resources reserved through advance or normal resource reservation.</dl>
</dl>
<dt><code>start time</code></p>
<dd>Start of resource utilization, in seconds after the epoch;</p>
<dt><code>end time</code></p>
<dd>End of resource utilization, as above;</p>
<dt><code>level</code></p>
<dd>The level at which resources are considered. One of:</p>
<dl>
<dd>
<dl>
<dt><code>Q</code></p>
<dd>Queue;</p>
<dt><code>H</code></p>
<dd>Host;</p>
<dt><code>G</code></p>
<dd>Global;</p>
<dt><code>P</code></p>
<dd>Parallel environment.</dl>
</dl>
<dt><code>object name</code></p>
<dd>Name of the relevant queue, host, parallel environment, or &quot;global&quot;;</p>
<dt><code>resource name</code></p>
<dd>Complex name in use or being reserved;</p>
<dt><code>utilization</code></p>
<dd>Amount of the named complex.</dl>
<h2>Files</h2>
<p><i>$SGE_ROOT/$SGE_$CELL/common/schedule</i></p>
<h2>See Also</h2>
