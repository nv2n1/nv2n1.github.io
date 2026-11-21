---
title: "mkzftree(1)"
name: "mkzftree"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkzftree/"
description: "mkzftree – Create a zisofs/RockRidge compressed file tree"
---

<h2 class="name">NAME</h2>
<p> mkzftree &#8211; Create a zisofs/RockRidge compressed file tree </p>
<h2>SYNOPSIS</h2>
<p> <code>mkzftree</code> [<i>OPTIONS</i>]&#8230; <i>INPUT</i> <i>OUTPUT</i></p>
<h2>DESCRIPTION</h2>
<p> Takes an input file tree (<i>INPUT</i>) and create a corresponding compressed file tree (<i>OUTPUT</i>) that can be used with an appropriately patched <code>mkisofs</code>(8) to create a transparent-compression ISO 9660/Rock Ridge filesystem using the &quot;ZF&quot; compression records.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Always compress all files, even if they get larger when compressed.</dd>
<dt><code>-z</code> <i>level</i>, <code>&#8211;level</code> <i>level</i></dt>
<dd> Select compression level (1-9, default is 9). Lower compression levels are faster, but typically result in larger output.</dd>
<dt><code>-u</code>, <code>&#8211;uncompress</code></dt>
<dd> Uncompress an already compressed tree. This can be used to read a compressed filesystem on a system which cannot read them natively.</dd>
<dt><code>-p</code> <i>parallelism</i>, <code>&#8211;parallelism</code> <i>parallelism</i></dt>
<dd> Compress in parallel. The <i>parallelism</i> value indicates how many compression threads are allowed to run.</dd>
<dt><code>-x</code>, <code>&#8211;one-filesystem</code></dt>
<dd> Do not cross filesystem boundaries, but create directory stubs at mount points.</dd>
<dt><code>-X</code>, <code>&#8211;strict-one-filesystem</code></dt>
<dd> Do not cross filesystem boundaries, and do not create directory stubs at mount points.</dd>
<dt><code>-C</code> <i>path</i>, <code>&#8211;crib-path</code> <i>path</i></dt>
<dd> Steal (&quot;crib&quot;) files from another directory if it looks (based on name, size, type and modification time) like they match entries in the new filesystem. The &quot;crib tree&quot; is usually the compressed version of an older version of the same workload; this thus allows for &quot;incremental rebuilds&quot; of a compressed filesystem tree. The files are hardlinked from the crib tree to the output tree, so if it is desirable to keep the link count correct the crib path should be deleted before running <code>mkisofs</code>. The crib tree must be on the same filesystem as the output tree.</dd>
<dt><code>-l</code>, <code>&#8211;local</code></dt>
<dd> Do not recurse into subdirectories, but create the directories themselves.</dd>
<dt><code>-L</code>, <code>&#8211;strict-local</code></dt>
<dd> Do not recurse into subdirectories, and do not create directories.</dd>
<dt><code>-F</code>, <code>&#8211;file</code></dt>
<dd> Indicates that <i>INPUT</i> may not necessarily be a directory; this allows operation on a single file. Note especially that if <i>-F</i> is specified, and <i>INPUT</i> is a symlink, the symlink itself will be copied rather than whatever it happens to point to.</dd>
<dt><code>-s</code>, <code>&#8211;sloppy</code></dt>
<dd> Treat file modes, times and ownership data as less than precious information and don&#8217;t abort if they cannot be set. This may be useful if running <code>mkisofs</code> on an input tree you do not own.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Increase the program verbosity.</dd>
<dt><code>-V</code> <i>value</i>, <code>&#8211;verbosity</code> <i>value</i></dt>
<dd> Set the program verbosity to <i>value</i>.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Issue no messages whatsoever, including error messages. This is the same as specifying <i>-V 0</i>.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display a brief help message.</dd>
<dt><code>-w</code>, <code>&#8211;version</code></dt>
<dd> Display the release version.</dd></dl>
<h2>BUGS</h2>
<p> Long options (beginning with <i>&#8212;</i>) may not work on all systems. See the message printed out by <i>mkzftree -h</i> to see if this applies to your system. </p>
<p> Inode change times (ctimes) are not copied. This is a system limitation and applies to all file copy programs. </p>
<p> If using the parallel option (<i>-z</i>) the access times (atimes) on directories may or may not be copied. If it is important that the atimes on directories are copied exactly, avoid using <i>-z</i>.</p>
<h2>AUTHOR</h2>
<p> Written by H. Peter Anvin &lt;hpa [at] zytor.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2002 H. Peter Anvin.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>mkisofs</code>(8) </p>
