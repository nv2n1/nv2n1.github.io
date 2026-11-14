---
title: "flow-cat(1)"
name: "flow-cat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-cat/"
description: "flow-cat – Concatenate flow files"
---

<h2>NAME</h2>
<p> flow-cat &#8211; Concatenate flow files</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-cat</code> [ <code>-aghmp</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-o</code><i> filename</i> ] [ <code>-t</code><i> start_time</i> ] [ <code>-T</code><i> start_time</i> ] [ <code>-z</code><i> z_level</i> ] [ <i>file</i><code>|</code><i>directory</i><i>&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-cat</code> utility processes files and/or directories of files in the flow-tools format. The resulting concatenated data set is written to the standard output or <i>file</i> specified by <code>-o</code>. If <i>file</i> is a single dash (`-&#8216;) or absent, flow-cat will read from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Do not ignore filenames that begin with <i>tmp</i>.</p>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-g</code></p>
<dd> Sort file list by capture start time before processing.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-m</code></p>
<dd> Disable the use of mmap().</p>
<dt><code>-p</code></p>
<dd> Preload headers. Use to preserve meta information such as lost flows.</p>
<dt><code>-o</code><i> file</i></p>
<dd> Write to <i>file</i> instead of the standard out.</p>
<dt><code>-t</code><i> start_time</i></p>
<dd> Select flow files up to <i>start_time</i>. If used with -T select files between <i>start_time</i> and <i>end_time</i>.</p>
<dt><code>-T</code><i> end_time</i></p>
<dd> Select flow files after <i>end_time</i>. If used with -t select files between <i>start_time</i> and <i>end_time</i>.</p>
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</p>
<dt><i>file</i><code>|</code><i>directory&#8230;</i></p>
<dd> Process the files and/or directory.</dl>
<h2>TIME/DATE PARSING</h2>
<p> start_time and end_time parsing is implemented with <i>getdate.y</i>, a commonly used function to process free-form time date specifications. Example usage borrowed from <code>cvs</code>: 1 month ago 2 hours ago 400000 seconds ago last year last Monday yesterday a fortnight ago 3/31/92 10:00:07 PST January 23, 1987 10:05pm 22:00 GMT</p>
<h2>EXAMPLES</h2>
<p> Concatenate all flow files begining with ft-v05.2001-05.01, use flow-print to display the results. </p>
<p> <code>flow-cat ft-v05.2001-05-01.* | flow-print</code> </p>
<p> Concatenate flow files in <i>/flows/krc4</i>, store store the output in <i>compressed.flows</i> at compression level 9 (best). The headers are preloaded so various metadata such as the flow count is correct in the result. Filenames begining with <i>tmp</i> which are typically in-progress flow files from <code>flow-capture</code> are not processed. </p>
<p> <code>flow-cat -p -z9 /flows/krc4 &gt; compressed.flows</code></p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
