---
title: "xfs_bmap(8)"
name: "xfs_bmap"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_bmap/"
description: "xfs_bmap – print block mapping for an XFS file"
---

<p>xfs_bmap &#8211; print block mapping for an XFS file</p>
<h2>Synopsis</h2>
<p><code>xfs_bmap</code> [ <code>-adlpv</code> ] [ <code>-n</code> <i>num_extents</i> ] <i>file</i><br/>
 <code>xfs_bmap -V</code></p>
<h2>Description</h2>
<p><code>xfs_bmap</code> prints the map of disk blocks used by files in an XFS filesystem. The map lists each <i>extent</i> used by the file, as well as regions in the file that do not have any corresponding blocks (holes). Each line of the listings takes the following form:</p>
<dl>
<dd><i>extent</i>: [<i>startoffset</i>..<i>endoffset</i>]: <i>startblock</i>..<i>endblock</i></dd></dl>
<p> Holes are marked by replacing the <i>startblock</i>..<i>endblock</i> with <i>hole</i>. All the file offsets and disk blocks are in units of 512-byte blocks, no matter what the filesystem&#8217;s block size is. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd>If this option is specified, information about the file&#8217;s attribute fork is printed instead of the default data fork.</dd>
<dt><code>-c</code></dt>
<dd>If this option is specified, information about the file&#8217;s copy on write fork is printed instead of the default data fork.</dd>
<dt><code>-d</code></dt>
<dd>If portions of the file have been migrated offline by a DMAPI application, a DMAPI read event will be generated to bring those portions back online before the disk block map is printed. However if the <code>-d</code> option is used, no DMAPI read event will be generated for a DMAPI file and offline portions will be reported as holes.</dd>
<dt><code>-e</code></dt>
<dd>If this option is used, <code>xfs_bmap</code> obtains all delayed allocation extents, and does not flush dirty pages to disk before querying extent data. With the <code>-v</code> option, the <i>flags</i> column will show which extents have not yet been allocated.</dd>
<dt><code>-l</code></dt>
<dd>If this option is used, then</dd>
<dd>
</dd><dl>
<dd>&lt;<i>nblocks</i>&gt; blocks</dd></dl>
<dd>will be appended to each line. <i>nblocks</i> is the length of the extent described on the line in units of 512-byte blocks.</dd>
<dd>This flag has no effect if the <code>-v</code> option is used.</dd>
<dt><code>-n</code><i> num_extents</i></dt>
<dd>If this option is given, <code>xfs_bmap</code> obtains the extent list of the file in groups of <i>num_extents</i> extents. In the absence of <code>-n</code>, <code>xfs_bmap</code> queries the system for the number of extents in the file and uses that value to compute the group size.</dd>
<dt><code>-p</code></dt>
<dd>If this option is used, <code>xfs_bmap</code> obtains all unwritten (preallocated) extents that do not contain written data. With the <code>-v</code> option, the <i>flags</i> column will show which extents are preallocated/unwritten.</dd>
<dt><code>-v</code></dt>
<dd>Shows verbose information. When this flag is specified, additional AG specific information is appended to each line in the following form:</dd>
<dd>
</dd><dl>
<dd><i>agno</i> (<i>startagoffset</i>..<i>endagoffset</i>) <i>nblocks</i> <i>flags</i></dd></dl>
<dd>A second <code>-v</code> option will print out the <i>flags</i> legend.</dd>
<dt><code>-V</code></dt>
<dd>Prints the version number and exits.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xfs_fsr/">xfs_fsr</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
