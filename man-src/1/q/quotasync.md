---
title: "quotasync(1)"
name: "quotasync"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quotasync/"
description: "quotasync – synchronize in-kernel file system usage and limits to disk format"
---

<h2>NAME</h2>
<p> quotasync &#8211; synchronize in-kernel file system usage and limits to disk format</p>
<h2>SYNOPSIS</h2>
<p> <code>quotasync</code> [ <code>-ug</code> ] <i>mount-point</i>&#8230;<br />
 <code>quotasync</code> [ <code>-ug</code> ] <code>-a</code><br />
 <code>quotasync</code> <code>-h</code> | <code>-V</code></p>
<h2>DESCRIPTION</h2>
<p> <code>quotasync</code> flushes file system usage and limits from kernel memory to quota files stored in the file system. By default only the user quotas are synchronized. </p>
<p> This tool can be useful if you want to display accurate quotas by tools that parse quota files, like <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;user</code></p>
<dd> Synchronize user usage and limits.</p>
<dt><code>-g, &#8211;group</code></p>
<dd> Synchronize group usage and limits.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Synchronize usage and limits on all file systems. You have to specify this option or to specify desired file systems.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show program version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show program usage and exit.</dl>
<h2>DIAGNOSTICS</h2>
<p> If requested synchronization fails, or invalid option is given, <code>quotasync</code> will terminate with non-zero exit code. Otherwise it will return zero.</p>
<h2>FILES</h2>
<dl>
<dt><code>aquota.user or aquota.group</code></p>
<dd> Quota file at the file system root (version 2 quota, non-XFS/GFS2 file systems).</p>
<dt><code>quota.user or quota.group</code></p>
<dd> Quota file at the file system root (version 1 quota, non-XFS/GFS2 file systems).</p>
<dt><code>/etc/mtab</code></p>
<dd> List of mounted file systems maintained by user space.</p>
<dt><code>/proc/mounts</code></p>
<dd> List of mounted file systems maintained by kernel.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8), <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8). </p>
<h2>Index</h2>
