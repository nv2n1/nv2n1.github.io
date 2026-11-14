---
title: "bro-cut(1)"
name: "bro-cut"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bro-cut/"
description: "bro-cut – parse Bro logs"
---

<h2>NAME</h2>
<p> bro-cut &#8211; parse Bro logs</p>
<h2>SYNOPSIS</h2>
<p> <code>bro-cut</code> [<i>options</i>] [<i>columns</i>]</p>
<h2>DESCRIPTION</h2>
<p> Extracts the given columns from ASCII Bro logs on standard input, and outputs them to standard output. If no columns are given, all are selected. By default, <code>bro-cut</code> does not include format header blocks in the output. </p>
<p> Columns are specified as a list of space-separated field names. The order of field names given to <code>bro-cut</code> determines the output order, which means <code>bro-cut</code> can be used to reorder columns. </p>
<p> The ASCII Bro logs read on standard input must have intact format header blocks because <code>bro-cut</code> needs this information to correctly interpret the log file format. In fact, <code>bro-cut</code> can process the concatenation of multiple ASCII log files that have different column layouts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Include the first format header block into the output.</p>
<dt><code>-C</code></p>
<dd> Include all format header blocks into the output.</p>
<dt><code>-d</code></p>
<dd> Convert time values into human-readable format.</p>
<dt> <code>-D</code> &lt;fmt&gt; Like <code>-d</code>, but specify format for time (see <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for syntax).</p>
<dt> <code>-F</code> &lt;ofs&gt; Sets a different output field separator.</p>
<dt><code>-n</code></p>
<dd>
<dd>Print all fields except those specified.</p>
<dt><code>-u</code></p>
<dd> Like <code>-d</code>, but print timestamps in UTC instead of local time.</p>
<dt> <code>-U</code> &lt;fmt&gt; Like <code>-D</code>, but print timestamps in UTC instead of local time.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>BRO_CUT_TIMEFMT</code></p>
<dd>
<dd>For time conversion option <code>-d</code> or <code>-u</code>, the format string can be specified by setting this environment variable.</dl>
<h2>EXAMPLES</h2>
<p> Output three columns and convert time values:<br />
 cat conn.log | bro-cut -d ts id.orig_h id.orig_p </p>
<p> Output all columns and convert time values with a custom format string:<br />
 cat conn.log | bro-cut -D &quot;%Y-%m-%d %H:%M:%S&quot;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-strftime/">strftime</a>(3)</p>
<h2>AUTHOR</h2>
<p> <code>bro-cut</code> was written by The Bro Project &lt;info [at] bro.org&gt;. </p>
<h2>Index</h2>
