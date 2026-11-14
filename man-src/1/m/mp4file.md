---
title: "mp4file(1)"
name: "mp4file"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4file/"
description: "mp4file – manual page for mp4file – MP4v2 2.0.0"
---

<h2>NAME</h2>
<p> mp4file &#8211; manual page for mp4file &#8211; MP4v2 2.0.0</p>
<h2>SYNOPSIS</h2>
<p> <code>mp4file</code> [<i>OPTION</i>]&#8230; <i>ACTION file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each mp4 file specified, perform the specified ACTION. An action must be specified. Some options are not applicable to some actions. </p>
<p> ACTIONS</p>
<dl>
<dt><code>&#8211;list</code></p>
<dd> list (summary information)</p>
<dt><code>&#8211;optimize</code></p>
<dd> optimize mp4 structure</p>
<dt><code>&#8211;dump</code></p>
<dd> dump mp4 structure in human-readable format</dl>
<p> OPTIONS</p>
<dl>
<dt><code>-y</code>, <code>&#8211;dryrun</code></p>
<dd> do not actually create or modify any files</p>
<dt><code>-k</code>, <code>&#8211;keepgoing</code></p>
<dd> continue batch processing even after errors</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> equivalent to <code>&#8211;verbose</code> 0</p>
<dt><code>-d</code>, <code>&#8211;debug</code> NUM</p>
<dd> increase debug or long-option to set NUM</p>
<dt><code>-v</code>, <code>&#8211;verbose</code> NUM</p>
<dd> increase verbosity or long-option to set NUM</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print brief help or long-option for extended help</p>
<dt><code>&#8211;version</code></p>
<dd> print version information and exit</dl>
<p> DEBUG LEVELS (for raw mp4 file I/O)</p>
<dl>
<dt>0</p>
<dd> supressed</p>
<dt>1</p>
<dd> add warnings and errors (default)</p>
<dt>2</p>
<dd> add table details</p>
<dt>3</p>
<dd> add implicits</p>
<dt>4</p>
<dd> everything</dl>
<p> VERBOSE LEVELS</p>
<dl>
<dt>0</p>
<dd> warnings and errors</p>
<dt>1</p>
<dd> normal informative messages (default)</p>
<dt>2</p>
<dd> more informative messages</p>
<dt>3</p>
<dd> everything </p>
</dl>
<h2>Index</h2>
