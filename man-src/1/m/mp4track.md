---
title: "mp4track(1)"
name: "mp4track"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp4track/"
description: "mp4track – manual page for mp4track – MP4v2 2.0.0"
---

<h2>NAME</h2>
<p> mp4track &#8211; manual page for mp4track &#8211; MP4v2 2.0.0</p>
<h2>SYNOPSIS</h2>
<p> <code>mp4track</code> [<i>OPTION</i>]&#8230; [<i>PARAMETERS</i>]&#8230; <i>ACTION file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each mp4 file specified, perform the specified ACTION. An action must be specified. Some options are not applicable to some actions. </p>
<p> ACTIONS</p>
<dl>
<dt><code>&#8211;list</code></p>
<dd> list all tracks in mp4</p>
<dt><code>&#8211;enabled</code> BOOL</p>
<dd> set trak.tkhd.flags (enabled bit)</p>
<dt><code>&#8211;inmovie</code> BOOL</p>
<dd> set trak.tkhd.flags (inMovie bit)</p>
<dt><code>&#8211;inpreview</code> BOOL</p>
<dd> set trak.tkhd.flags (inPreview bit)</p>
<dt><code>&#8211;layer</code> NUM</p>
<dd> set trak.tkhd.layer</p>
<dt><code>&#8211;altgroup</code> NUM</p>
<dd> set trak.tkhd.alternate_group</p>
<dt><code>&#8211;volume</code> FLOAT</p>
<dd> set trak.tkhd.volume</p>
<dt><code>&#8211;width</code> FLOAT</p>
<dd> set trak.tkhd.width</p>
<dt><code>&#8211;height</code> FLOAT</p>
<dd> set trak.tkhd.height</p>
<dt><code>&#8211;language</code> CODE</p>
<dd> set trak.mdia.mdhd.language</p>
<dt><code>&#8211;hdlrname</code> STR</p>
<dd> set trak.mdia.hdlr.name</p>
<dt><code>&#8211;udtaname</code> STR</p>
<dd> set trak.udta.name.value</p>
<dt><code>&#8211;udtaname-remove</code></p>
<dd> remove trak.udta.name atom</p>
<dt><code>&#8211;colr-list</code></p>
<dd> list all colr-boxes in mp4</p>
<dt><code>&#8211;colr-add</code></p>
<dd> add colr-box to a video track</p>
<dt><code>&#8211;colr-set</code></p>
<dd> set colr-box parms</p>
<dt><code>&#8211;colr-remove</code></p>
<dd> remove colr-box from track</p>
<dt><code>&#8211;pasp-list</code></p>
<dd> list all pasp-boxes in mp4</p>
<dt><code>&#8211;pasp-add</code></p>
<dd> add pasp-box to a video track</p>
<dt><code>&#8211;pasp-set</code></p>
<dd> set pasp-box parms</p>
<dt><code>&#8211;pasp-remove</code></p>
<dd> remove pasp-box from track</dl>
<p> PARAMETERS</p>
<dl>
<dt><code>&#8211;track-any</code></p>
<dd> act on any/all tracks</p>
<dt><code>&#8211;track-index</code> IDX</p>
<dd> act on track index IDX</p>
<dt><code>&#8211;track-id</code> ID</p>
<dd> act on track id ID</p>
<dt><code>&#8211;colr-parms</code> CSV</p>
<dd> where CSV is IDX1,IDX2,IDX3</p>
<dt><code>&#8211;colr-parm-hd</code></p>
<dd> equivalent to <code>&#8211;colr-parms</code>=<i>1</i>,1,1</p>
<dt><code>&#8211;colr-parm-sd</code></p>
<dd> equivalent to <code>&#8211;colr-parms</code>=<i>6</i>,1,6</p>
<dt><code>&#8211;pasp-parms</code> CSV</p>
<dd> where CSV is hSPACING,vSPACING</dl>
<p> OPTIONS</p>
<dl>
<dt><code>-z</code>, <code>&#8211;optimize</code></p>
<dd> optimize mp4 file after modification</p>
<dt><code>-y</code>, <code>&#8211;dryrun</code></p>
<dd> do not actually create or modify any files</p>
<dt><code>-k</code>, <code>&#8211;keepgoing</code></p>
<dd> continue batch processing even after errors</p>
<dt><code>-o</code>, <code>&#8211;overwrite</code></p>
<dd> overwrite existing files when creating</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> force overwrite even if file is read-only</p>
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
