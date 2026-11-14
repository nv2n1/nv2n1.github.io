---
title: "flow-merge(1)"
name: "flow-merge"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-merge/"
description: "flow-merge – Merge flow files."
---

<h2>NAME</h2>
<p> flow-merge &#8211; Merge flow files.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-merge</code> [ <code>-aghm</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-o</code><i> filename</i> ] [ <code>-z</code><i> z_level</i> ] [ <i>file</i><code>|</code><i>directory</i><i>&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-merge</code> utility processes files and/or directories of files in the flow-tools format. The resulting merged data set is written to the standard output or <i>file</i> specified by <code>-o</code>. If <i>file</i> is a single dash (`-&#8216;) or absent, flow-merge will read from the standard input. Unlike flow-cat, flow-merge interleaves flow records preserving the relative chronological order.</p>
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
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</p>
<dt><i>file</i><code>|</code><i>directory&#8230;</i></p>
<dd> Process the files and/or directory.</dl>
<h2>EXAMPLES</h2>
<p> Merge all flow files begining with ft-v05.2001-05.01, use flow-print to display the results. </p>
<p> <code>flow-merge ft-v05.2001-05-01.* | flow-print</code></p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Larry Lidz &lt;ellidz [at] eridu.uchicago.edu&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
