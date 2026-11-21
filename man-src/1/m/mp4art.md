---
title: "mp4art(1)"
name: "mp4art"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4art/"
description: "mp4art – manual page for mp4art – MP4v2 2.0.0"
---

<h2>NAME</h2>
<p> mp4art &#8211; manual page for mp4art &#8211; MP4v2 2.0.0</p>
<h2>SYNOPSIS</h2>
<p> <code>mp4art</code> [<i>OPTION</i>]&#8230; <i>ACTION file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each mp4 (m4a) file specified, perform the specified ACTION. An action must be specified. Some options are not applicable for some actions. </p>
<p> ACTIONS</p>
<dl>
<dt><code>&#8211;list</code></dt>
<dd> list all covr-boxes</dd>
<dt><code>&#8211;add</code> IMG</dt>
<dd> add covr-box from IMG file</dd>
<dt><code>&#8211;replace</code> IMG</dt>
<dd> replace covr-box with IMG file</dd>
<dt><code>&#8211;remove</code></dt>
<dd> remove covr-box</dd>
<dt><code>&#8211;extract</code></dt>
<dd> extract covr-box</dd></dl>
<p> ACTION PARAMETERS</p>
<dl>
<dt><code>&#8211;art-any</code></dt>
<dd> act on all covr-boxes (default)</dd>
<dt><code>&#8211;art-index</code> IDX</dt>
<dd> act on covr-box index IDX</dd></dl>
<p> OPTIONS</p>
<dl>
<dt><code>-z</code>, <code>&#8211;optimize</code></dt>
<dd> optimize mp4 file after modification</dd>
<dt><code>-y</code>, <code>&#8211;dryrun</code></dt>
<dd> do not actually create or modify any files</dd>
<dt><code>-k</code>, <code>&#8211;keepgoing</code></dt>
<dd> continue batch processing even after errors</dd>
<dt><code>-o</code>, <code>&#8211;overwrite</code></dt>
<dd> overwrite existing files when creating</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> force overwrite even if file is read-only</dd>
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
