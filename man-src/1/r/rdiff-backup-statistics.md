---
title: "rdiff-backup-statistics(1)"
name: "rdiff-backup-statistics"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdiff-backup-statistics/"
description: "rdiff-backup-statistics – summarize rdiff-backup statistics files"
---

<h2>NAME</h2>
<p> rdiff-backup-statistics &#8211; summarize rdiff-backup statistics files</p>
<h2>SYNOPSIS</h2>
<p> <code>rdiff-backup-statistics</code> <code>[&#8211;begin-time</code><i> time</i><code>]</code> <code>[&#8211;end-time</code><i> time</i><code>]</code> <code>[&#8211;minimum-ratio</code><i> ratio</i><code>]</code> <code>[&#8211;null-separator]</code> <code>[&#8211;quiet]</code> <i>repository</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>rdiff-backup-statistics</code> reads the matching statistics files in a backup repository made by <code>rdiff-backup</code> and prints some summary statistics to the screen. It does not alter the repository in any way. </p>
<p> The required argument is the pathname of the root of an rdiff-backup repository. For instance, if you ran &quot;rdiff-backup in out&quot;, you could later run &quot;rdiff-backup-statistics out&quot;. </p>
<p> The output has two parts. The first is simply an average of the all matching session_statistics files. The meaning of these fields is explained in the FAQ included in the package, and also at <i><a rel="nofollow" href="http://rdiff-backup.nongnu.org/FAQ.html#statistics">http://rdiff-backup.nongnu.org/FAQ.html#statistics</a></i>. </p>
<p> The second section lists some particularly significant files (including directories). These files are either contain a lot of data, take up increment space, or contain a lot of changed files. All the files that are above the minimum ratio (default 5%) will be listed. </p>
<p> If a file or directory is listed, its contributions are subtracted from its parent. That is why the percentage listed after a directory can be larger than the percentage of its parent. Without this, the root directory would always be the largest, and the output would be boring. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;begin-time</code><i> time</i></p>
<dd> Do not read statistics files older than <i>time</i>. By default, all statistics files will be read. <i>time</i> should be in the same format taken by &#8211;restore-as-of. (See <code>TIME FORMATS</code> in the rdiff-backup man page for details.)</p>
<dt><code>&#8211;end-time</code><i> time</i></p>
<dd> Like <code>&#8211;begin-time</code> but exclude statistics files later than <i>time</i>.</p>
<dt><code>&#8211;minimum-ratio</code><i> ratio</i></p>
<dd> Print all directories contributing more than the given ratio to the total. The default value is .05, or 5 percent.</p>
<dt><code>&#8211;null-separator</code></p>
<dd> Specify that the lines of the file_statistics file are separated by nulls (
