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
<dt><code>-a</code></dt>
<dd> Do not hide clean segments.</dd>
<dt><code>-i </code><i>index</i></dt>
<dd> Skip <i>index</i> segments at start of input.</dd>
<dt><code>-n </code><i>lines</i></dt>
<dd> List only <i>lines</i> input segments.</dd>
<dt><code>-h</code></dt>
<dd> Display help message and exit.</dd></dl>
<h2>FIELD DESCRIPTION</h2>
<p> Every line of the <code>lssu</code> output consists of the following fields:</p>
<dl>
<dt><code>SEGNUM</code></dt>
<dd> Segment number.</dd>
<dt><code>DATE</code></dt>
<dd> Creation date.</dd>
<dt><code>TIME</code></dt>
<dd> Creation time.</dd>
<dt><code>STAT</code></dt>
<dd> State of the segment. It consists of three flags whose meaning is shown below:</dd>
<dl>
<dl>
<dt><code>a</code></dt>
<dd> The segment is active, meaning that it is recently created and cannot be reclaimed by the garbage collector.</dd>
<dt><code>d</code></dt>
<dd> The segment is dirty, meaning that it is in use.</dd>
<dt><code>e</code></dt>
<dd> The segment is erroneous, meaning that it has once caused an I/O error. NILFS2 avoids allocating the segments with this flag.</dd></dl>
</dl>
<dt><code>NBLOCKS</code></dt>
<dd> Number of in-use blocks of the segment.</dd></dl>
<h2>AUTHOR</h2>
<p> Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>AVAILABILITY</h2>
<p> <code>lssu</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/8-dumpseg/">dumpseg</a></code>(8). </p>
<h2>Index</h2>
