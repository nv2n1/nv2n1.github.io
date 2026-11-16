---
title: "varnishhist(1)"
name: "varnishhist"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishhist/"
description: "varnishhist – Varnish request histogram"
---

<h2>NAME</h2>
<p> varnishhist &#8211; Varnish request histogram</p>
<h2>SYNOPSIS</h2>
<p> varnishhist [-C] [-d] [-g &lt;request|vxid&gt;] [-h] [-L limit] [-n name] [-N filename] [-p period] [-P &lt;size|responsetime|tag:field_num:min:max&gt;] [-q query] [-r filename] [-T seconds] [-V]</p>
<h2>DESCRIPTION</h2>
<p> The varnishhist utility reads <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) shared memory logs and presents a continuously updated histogram showing the distribution of the last N requests by their processing. The value of N and the vertical scale are displayed in the top left corner. The horizontal scale is logarithmic. Hits are marked with a pipe character (&quot;|&quot;), and misses are marked with a hash character (&quot;#&quot;). </p>
<p> The following options are available:</p>
<dl>
<dt><code>-C</code></dt>
<dd> Do all regular expression and string matching caseless.</dd>
<dt><code>-d</code></dt>
<dd> Start processing log records at the head of the log instead of the tail.</dd>
<dt><code>-g</code><i>&nbsp;<wbr>&lt;request|vxid&gt;</i></dt>
<dd> The grouping of the log records. The default is to group by vxid.</dd>
<dt><code>-h</code></dt>
<dd> Print program usage and exit</dd>
<dt><code>-L</code><i>&nbsp;<wbr>limit</i></dt>
<dd> Sets the upper limit of incomplete transactions kept before the oldest transaction is force completed. A warning record is synthesized when this happens. This setting keeps an upper bound on the memory usage of running queries. Defaults to 1000 transactions.</dd>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></dt>
<dd> Specify the name of the varnishd instance to get logs from. If -n is not specified, the host name is used.</dd>
<dt><code>-N</code><i>&nbsp;<wbr>filename</i></dt>
<dd> Specify the filename of a stale VSM instance. When using this option the abandonment checking is disabled.</dd>
<dt><code>-p</code><i>&nbsp;<wbr>period</i></dt>
<dd> Specified the number of seconds between screen refreshes. Default is 1 second, and can be changed at runtime by pressing the [1-9] keys.</dd>
<dt><code>-P</code><i>&nbsp;<wbr>&lt;size|responsetime|tag:field_num:min:max&gt;</i></dt>
<dd> Either specify &quot;size&quot; or &quot;responsetime&quot; profile or create a new one. Define the tag we&#8217;ll look for, and the field number of the value we are interested in. min and max are the boundaries of the graph (these are power of tens).</dd>
<dt><code>-q</code><i>&nbsp;<wbr>query</i></dt>
<dd> Specifies the VSL query to use.</dd>
<dt><code>-r</code><i>&nbsp;<wbr>filename</i></dt>
<dd> Read log in binary file format from this file. The file can be created with <code>varnishlog -B -w filename</code>.</dd>
<dt><code>-T</code><i>&nbsp;<wbr>seconds</i></dt>
<dd> Sets the transaction timeout in seconds. This defines the maximum number of seconds elapsed between a Begin tag and the End tag. If the timeout expires, a warning record is synthesized and the transaction is force completed. Defaults to 120 seconds.</dd>
<dt><code>-V</code></dt>
<dd> Print version information and exit.</dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishstat/">varnishstat</a>(1)</dd>
<dt>&bull;</dt>
<dd> <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1)</dd></dl>
<h2>HISTORY</h2>
<p> The varnishhist utility was developed by Poul-Henning Kamp in cooperation with Verdens Gang AS and Varnish Software AS. This manual page was written by Dag-Erling Smørgrav.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</dt>
<dd> Copyright (c) 2006 Verdens Gang AS</dd>
<dt>&bull;</dt>
<dd> Copyright (c) 2006-2014 Varnish Software AS </dd>
</dl>
<h2>Index</h2>
