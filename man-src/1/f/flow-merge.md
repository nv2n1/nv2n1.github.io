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
<dt><code>-a</code></dt>
<dd> Do not ignore filenames that begin with <i>tmp</i>.</dd>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></dt>
<dd> Byte order of output.</dd>
<dt><code>-C</code><i> Comment</i></dt>
<dd> Add a comment.</dd>
<dt><code>-d</code><i> debug_level</i></dt>
<dd> Enable debugging.</dd>
<dt><code>-g</code></dt>
<dd> Sort file list by capture start time before processing.</dd>
<dt><code>-h</code></dt>
<dd> Display help.</dd>
<dt><code>-m</code></dt>
<dd> Disable the use of mmap().</dd>
<dt><code>-p</code></dt>
<dd> Preload headers. Use to preserve meta information such as lost flows.</dd>
<dt><code>-o</code><i> file</i></dt>
<dd> Write to <i>file</i> instead of the standard out.</dd>
<dt><code>-z</code><i> z_level</i></dt>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dd>
<dt><i>file</i><code>|</code><i>directory&#8230;</i></dt>
<dd> Process the files and/or directory.</dd></dl>
<h2>EXAMPLES</h2>
<p> Merge all flow files begining with ft-v05.2001-05.01, use flow-print to display the results. </p>
<p> <code>flow-merge ft-v05.2001-05-01.* | flow-print</code></p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Larry Lidz &lt;ellidz [at] eridu.uchicago.edu&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
