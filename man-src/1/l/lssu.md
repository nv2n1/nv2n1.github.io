---
title: "lssu(1)"
name: "lssu"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lssu/"
description: "lssu – list usage state of NILFS2 segments"
---

<h2>NAME</h2>
<p> lssu &#8211; list usage state of NILFS2 segments</p>
<h2>SYNOPSIS</h2>
<p> <code>lssu</code> [<i>options</i>] [<i>device</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lssu</code> is a utility for displaying usage state of NILFS2 segments in <i>device</i>, where a segment is contiguous lump of disk blocks and an allocation unit of NILFS2 disk space. When <i>device</i> is omitted, <i>/proc/mounts</i> is examined to find a NILFS2 file system. </p>
<p> This command will fail if the <i>device</i> has no active mounts of a NILFS2 file system.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Do not hide clean segments.</p>
<dt><code>-i </code><i>index</i></p>
<dd> Skip <i>index</i> segments at start of input.</p>
<dt><code>-n </code><i>lines</i></p>
<dd> List only <i>lines</i> input segments.</p>
<dt><code>-h</code></p>
<dd> Display help message and exit.</dl>
<h2>FIELD DESCRIPTION</h2>
<p> Every line of the <code>lssu</code> output consists of the following fields:</p>
<dl>
<dt><code>SEGNUM</code></p>
<dd> Segment number.</p>
<dt><code>DATE</code></p>
<dd> Creation date.</p>
<dt><code>TIME</code></p>
<dd> Creation time.</p>
<dt><code>STAT</code></p>
<dd> State of the segment. It consists of three flags whose meaning is shown below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> The segment is active, meaning that it is recently created and cannot be reclaimed by the garbage collector.</p>
<dt><code>d</code></p>
<dd> The segment is dirty, meaning that it is in use.</p>
<dt><code>e</code></p>
<dd> The segment is erroneous, meaning that it has once caused an I/O error. NILFS2 avoids allocating the segments with this flag.</dl>
</dl>
<dt><code>NBLOCKS</code></p>
<dd> Number of in-use blocks of the segment.</dl>
<h2>AUTHOR</h2>
<p> Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>AVAILABILITY</h2>
<p> <code>lssu</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/8-dumpseg/">dumpseg</a></code>(8). </p>
<h2>Index</h2>
