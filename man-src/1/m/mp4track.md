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
<dt><code>&#8211;list</code></dt>
<dd> list all tracks in mp4</dd>
<dt><code>&#8211;enabled</code> BOOL</dt>
<dd> set trak.tkhd.flags (enabled bit)</dd>
<dt><code>&#8211;inmovie</code> BOOL</dt>
<dd> set trak.tkhd.flags (inMovie bit)</dd>
<dt><code>&#8211;inpreview</code> BOOL</dt>
<dd> set trak.tkhd.flags (inPreview bit)</dd>
<dt><code>&#8211;layer</code> NUM</dt>
<dd> set trak.tkhd.layer</dd>
<dt><code>&#8211;altgroup</code> NUM</dt>
<dd> set trak.tkhd.alternate_group</dd>
<dt><code>&#8211;volume</code> FLOAT</dt>
<dd> set trak.tkhd.volume</dd>
<dt><code>&#8211;width</code> FLOAT</dt>
<dd> set trak.tkhd.width</dd>
<dt><code>&#8211;height</code> FLOAT</dt>
<dd> set trak.tkhd.height</dd>
<dt><code>&#8211;language</code> CODE</dt>
<dd> set trak.mdia.mdhd.language</dd>
<dt><code>&#8211;hdlrname</code> STR</dt>
<dd> set trak.mdia.hdlr.name</dd>
<dt><code>&#8211;udtaname</code> STR</dt>
<dd> set trak.udta.name.value</dd>
<dt><code>&#8211;udtaname-remove</code></dt>
<dd> remove trak.udta.name atom</dd>
<dt><code>&#8211;colr-list</code></dt>
<dd> list all colr-boxes in mp4</dd>
<dt><code>&#8211;colr-add</code></dt>
<dd> add colr-box to a video track</dd>
<dt><code>&#8211;colr-set</code></dt>
<dd> set colr-box parms</dd>
<dt><code>&#8211;colr-remove</code></dt>
<dd> remove colr-box from track</dd>
<dt><code>&#8211;pasp-list</code></dt>
<dd> list all pasp-boxes in mp4</dd>
<dt><code>&#8211;pasp-add</code></dt>
<dd> add pasp-box to a video track</dd>
<dt><code>&#8211;pasp-set</code></dt>
<dd> set pasp-box parms</dd>
<dt><code>&#8211;pasp-remove</code></dt>
<dd> remove pasp-box from track</dd></dl>
<p> PARAMETERS</p>
<dl>
<dt><code>&#8211;track-any</code></dt>
<dd> act on any/all tracks</dd>
<dt><code>&#8211;track-index</code> IDX</dt>
<dd> act on track index IDX</dd>
<dt><code>&#8211;track-id</code> ID</dt>
<dd> act on track id ID</dd>
<dt><code>&#8211;colr-parms</code> CSV</dt>
<dd> where CSV is IDX1,IDX2,IDX3</dd>
<dt><code>&#8211;colr-parm-hd</code></dt>
<dd> equivalent to <code>&#8211;colr-parms</code>=<i>1</i>,1,1</dd>
<dt><code>&#8211;colr-parm-sd</code></dt>
<dd> equivalent to <code>&#8211;colr-parms</code>=<i>6</i>,1,6</dd>
<dt><code>&#8211;pasp-parms</code> CSV</dt>
<dd> where CSV is hSPACING,vSPACING</dd></dl>
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
