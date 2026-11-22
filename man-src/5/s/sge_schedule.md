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
<p> Note that the file tends to grow rapidly, and should be truncated/rotated, e.g. with <i>logrotate</i>(1). Also it should probably be placed on local disk, not an NFS-mounted filesystem, for instance, because of the large number of small writes it typically gets &#8211; e.g. make a symbolic link into the qmaster spool area (assuming that is local). </p>
<p> See for a tool to process the data and produce information on reservations.</p>
<h2>Format</h2>
<p>A line containing<br/>
 <code>::::::::</code><br/>
 indicates the start of a scheduling interval. It is followed by lines showing the resource usage considered for the interval. They contain the following fields, delimited by &#8216;<code>:</code>&#8216;.</p>
<dl>
<dt><code>job id</code></dt>
<dd>The numeric job id;</dd>
<dt><code>task id</code></dt>
<dd>The task id (1 for serial jobs);</dd>
<dt><code>reason</code></dt>
<dd>The for listing the utilization. One of the following, depending on the job&#8217;s state:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>RUNNING</code></dt>
<dd>Running before the interval;</dd>
<dt><code>SUSPENDED</code></dt>
<dd>Suspended before the interval;</dd>
<dt><code>MIGRATING</code></dt>
<dd>To be preempted/migrated (currently unused);</dd>
<dt><code>STARTING</code></dt>
<dd>To be started;</dd>
<dt><code>RESERVING</code></dt>
<dd>Having resources reserved through advance or normal resource reservation.</dd></dl>
</dl>
<dt><code>start time</code></dt>
<dd>Start of resource utilization, in seconds after the epoch;</dd>
<dt><code>end time</code></dt>
<dd>End of resource utilization, as above;</dd>
<dt><code>level</code></dt>
<dd>The level at which resources are considered. One of:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>Q</code></dt>
<dd>Queue;</dd>
<dt><code>H</code></dt>
<dd>Host;</dd>
<dt><code>G</code></dt>
<dd>Global;</dd>
<dt><code>P</code></dt>
<dd>Parallel environment.</dd></dl>
</dl>
<dt><code>object name</code></dt>
<dd>Name of the relevant queue, host, parallel environment, or &quot;global&quot;;</dd>
<dt><code>resource name</code></dt>
<dd>Complex name in use or being reserved;</dd>
<dt><code>utilization</code></dt>
<dd>Amount of the named complex.</dd></dl>
<h2>Files</h2>
<p><i>$SGE_ROOT/$SGE_$CELL/common/schedule</i></p>
<h2>See Also</h2>
