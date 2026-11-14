---
title: "flow-expire(1)"
name: "flow-expire"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-expire/"
description: "flow-expire – Manage storage of flow file archives by expiring old data."
---

<h2>NAME</h2>
<p> flow-expire &#8211; Manage storage of flow file archives by expiring old data.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-expire</code> [ <code>-h</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-e</code><i> expire_count</i> ] [ <code>-E</code><i> expire_size</i> ] <code>-w</code><i> workdir</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-expire</code> utility will remove the oldest flow files in a directory based on either a count of files or space utilization. The directory is recursively searched for flow files. Files that do not have a flow-tools signature will be ignored. The internal timestamp is used so backups or copies of the flow files that do not retain the original timestamp will not impact the operation of <code>flow-expire</code>. <code>flow-expire</code> is typically used to manage storage in a distributed environment where flows are collected on a different server than they are archived.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-e</code><i> expire_count</i></p>
<dd> Retain the maximum number of files so that the total file count is less than <i>expire_count</i>.</p>
<dt><code>-E</code><i> expire_size</i></p>
<dd> Retain the maximum number of files so that the total storage is less than <i>expire_size</i>. The letters b,K,M,G can be used as multipliers, ie 16 Megabytes is 16M.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-w</code><i> workdir</i></p>
<dd> Work in <i>workdir</i>.</dl>
<h2>EXAMPLES</h2>
<p> Remove the oldest flow files in <i>/flows/krc4</i> until the total storage is less then 2 Gigabytes. </p>
<p> <code>flow-expire -E2Gig -w /flows/krc4</code> </p>
<p> Remove the oldest flow files in <i>/flows/krc4</i> until the total number of files is less then 100. </p>
<p> <code>flow-expire -e100 -w /flows/krc4</code></p>
<h2>BUGS</h2>
<p> Empty directories are not removed.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
