---
title: "sge_share_mon(1)"
name: "sge_share_mon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge_share_mon/"
description: "sge_share_mon – print xxQS_NAMExx live share tree"
---

<h2 class="name">NAME</h2>
<p> sge_share_mon &#8211; print xxQS_NAMExx live share tree </p>
<h2>SYNOPSIS</h2>
<p> <code>sge_share_mon</code> [<code>-c</code> <i>count</i>] [<code>-d</code> <i>delimiter</i>] [<code>-f</code> <i>field</i>,<i>field</i>&#8230;] [<code>-h</code>] [<code>-i</code> <i>interval</i>] [<code>-l</code> <i>delimiter</i>] [<code>-m</code> <i>output_mode</i>] [<code>-n</code>] [<code>-o</code> <i>output_file</i>] [<code>-r</code> <i>delimiter</i>] [<code>-s</code> <i>string_format</i>] [<code>-t</code>] [<code>-u</code>] [<code>-x</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>sge_share_mon</i> prints the live state of the xxQS_NAMExx share tree (as opposed to static graphical view). It does so for a given number (default infinite) of intervals; use <code>-c 1</code> for a snapshot.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c&nbsp;</code><i>count</i></dt>
<dd> Print <i>count</i> collections (default infinite).</dd>
<dt><code>-d&nbsp;</code><i>delimiter</i></dt>
<dd> Delimit output columns with string <i>delimiter</i> (default a tab).</dd>
<dt><code>-f&nbsp;</code><i>field</i>,&#8230;</dt>
<dd> Print the given <i>field</i>s. The available fields in the default order are <code>curr_time</code>, <code>usage_time</code>, <code>node_name</code>, <code>user_name</code>, <code>project_name</code>, <code>shares</code>, <code>job_count</code>, <code>level%</code>, <code>total%</code>, <code>long_target_share</code>, <code>short_target_share</code>, <code>actual_share</code>, <code>usage</code>, <code>cpu</code>, <code>mem</code>, <code>io</code>, <code>ltcpu</code>, <code>ltmem</code>, <code>ltio</code>.</dd>
<dt><code>-h</code></dt>
<dd> Print a header listing field names.</dd>
<dt><code>-i&nbsp;</code><i>interval</i></dt>
<dd> Collect over <i>interval</i> seconds (default 15)</dd>
<dt><code>-l&nbsp;</code><i>delimiter</i></dt>
<dd> Delimit nodes output with string <i>delimiter</i> (default a carriage return).</dd>
<dt><code>-m&nbsp;</code><i>output_mode</i></dt>
<dd> Open <i>output_file</i> in <i><a href="/docs/linux/man/3-fopen/">fopen</a></i>(3) mode <i>output_mode</i> (default <code>w</code>). The meaningful alternative is <code>a</code> to append to the file.</dd>
<dt><code>-n</code></dt>
<dd> Print in the form <i>name</i>=<i>value</i></dd>
<dt><code>-o&nbsp;</code><i>output_file</i></dt>
<dd> Print to file <i>output_file</i> (default standard output).</dd>
<dt><code>-r&nbsp;</code><i>delimiter</i></dt>
<dd> Delimit collection records with string <i>delimiter</i> (default a carriage return).</dd>
<dt><code>-s&nbsp;</code><i>string_format</i></dt>
<dd> <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format for strings (default <code>%s</code>)</dd>
<dt><code>-t</code></dt>
<dd> Show times formatted per <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3). (Default is seconds since the epoch.)</dd>
<dt><code>-u</code></dt>
<dd> Print decayed usage (since timestamp) in nodes.</dd>
<dt><code>-x</code></dt>
<dd> Don&#8217;t print non-leaf nodes.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-fopen/">fopen</a></i>(3), <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3), </p>
<h2>Index</h2>
