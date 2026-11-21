---

title: "mp4file(1)"
name: "mp4file"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4file/"
description: "mp4file – manual page for mp4file – MP4v2 2.0.0"
---

<p> mp4file &#8211; manual page for mp4file &#8211; MP4v2 2.0.0</p>
<h2>SYNOPSIS</h2>
<p> <code>mp4file</code> [<i>OPTION</i>]&#8230; <i>ACTION file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each mp4 file specified, perform the specified ACTION. An action must be specified. Some options are not applicable to some actions. </p>
<p> ACTIONS</p>
<dl>
<dt><code>&#8211;list</code></dt>
<dd> list (summary information)</dd>
<dt><code>&#8211;optimize</code></dt>
<dd> optimize mp4 structure</dd>
<dt><code>&#8211;dump</code></dt>
<dd> dump mp4 structure in human-readable format</dd></dl>
<p> OPTIONS</p>
<dl>
<dt><code>-y</code>, <code>&#8211;dryrun</code></dt>
<dd> do not actually create or modify any files</dd>
<dt><code>-k</code>, <code>&#8211;keepgoing</code></dt>
<dd> continue batch processing even after errors</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> equivalent to <code>&#8211;verbose</code> 0</dd>
<dt><code>-d</code>, <code>&#8211;debug</code> NUM</dt>
<dd> increase debug or long-option to set NUM</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code> NUM</dt>
<dd> increase verbosity or long-option to set NUM</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print brief help or long-option for extended help</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version information and exit</dd></dl>
<p> DEBUG LEVELS (for raw mp4 file I/O)</p>
<dl>
<dt>0</dt>
<dd> supressed</dd>
<dt>1</dt>
<dd> add warnings and errors (default)</dd>
<dt>2</dt>
<dd> add table details</dd>
<dt>3</dt>
<dd> add implicits</dd>
<dt>4</dt>
<dd> everything</dd></dl>
<p> VERBOSE LEVELS</p>
<dl>
<dt>0</dt>
<dd> warnings and errors</dd>
<dt>1</dt>
<dd> normal informative messages (default)</dd>
<dt>2</dt>
<dd> more informative messages</dd>
<dt>3</dt>
<dd> everything </dd>
</dl>
