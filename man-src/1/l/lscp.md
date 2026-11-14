---
title: "lscp(1)"
name: "lscp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lscp/"
description: "lscp – list NILFS2 checkpoints"
---

<h2>NAME</h2>
<p> lscp &#8211; list NILFS2 checkpoints</p>
<h2>SYNOPSIS</h2>
<p> <code>lscp</code> [<i>options</i>] [<i>device</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lscp</code> is a utility for displaying checkpoints or snapshots of the NILFS2 file system found in <i>device</i>. When <i>device</i> is omitted, <i>/proc/mounts</i> is examined to find a NILFS2 file system. </p>
<p> This command will fail if the <i>device</i> has no active mounts of a NILFS2 file system.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Reverse order.</p>
<dt><code>-s</code></p>
<dd> List only snapshots.</p>
<dt><code>-i </code><i>index</i></p>
<dd> Skip <i>index</i> checkpoints (or snapshots) at start of input.</p>
<dt><code>-n </code><i>lines</i></p>
<dd> List only <i>lines</i> input checkpoints (or snapshots).</p>
<dt><code>-h</code></p>
<dd> Display help message and exit.</dl>
<h2>FIELD DESCRIPTION</h2>
<p> Every line of the <code>lscp</code> output consists of the following seven fields:</p>
<dl>
<dt><code>CNO</code></p>
<dd> Checkpoint number.</p>
<dt><code>DATE</code></p>
<dd> Creation date.</p>
<dt><code>TIME</code></p>
<dd> Creation time.</p>
<dt><code>MODE</code></p>
<dd> Mode of the checkpoint; <code>cp</code> for a plain checkpoint, and <code>ss</code> for a snapshot.</p>
<dt><code>FLG (experimental)</code></p>
<dd> Flags on the checkpoint. At present, character &#8220;i&#8221; is printed in the field if the checkpoint was created only by garbage collection, checkpoint mode change, or other change of internal state. Otherwise &#8220;-&#8221; is printed.</p>
<dt><code>NBLKINC</code></p>
<dd> Number of blocks appended by the checkpoint.</p>
<dt><code>ICNT</code></p>
<dd> Number of inodes included in the entire file system at the time specified by the checkpoint.</dl>
<h2>AUTHOR</h2>
<p> Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>AVAILABILITY</h2>
<p> <code>lscp</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/8-mkcp/">mkcp</a></code>(8), <code><a href="/docs/linux/man/8-chcp/">chcp</a></code>(8), <code><a href="/docs/linux/man/8-rmcp/">rmcp</a></code>(8). </p>
<h2>Index</h2>
