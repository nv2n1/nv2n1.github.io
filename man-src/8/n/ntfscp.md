---
title: "ntfscp(8)"
name: "ntfscp"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfscp/"
description: "ntfscp – copy file to an NTFS volume."
---

<p>ntfscp &#8211; copy file to an NTFS volume.</p>
<h2>Synopsis</h2>
<p><code>ntfscp</code> [<i>options</i>] <i>device source_file destination</i></p>
<h2>Description</h2>
<p><code>ntfscp</code> will copy file to an NTFS volume. <i>destination</i> can be either file or directory. In case if <i>destination</i> is directory specified by name then <i>source_file</i> is copied into this directory, in case if <i>destination</i> is directory and specified by inode number then unnamed data attribute is created for this inode and <i>source_file</i> is copied into it (WARNING: it&#8217;s unusual to have unnamed data streams in the directories, think twice before specifying directory by inode number).</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfscp</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;attribute</code> NUM</p>
<dd>Write to this attribute.</p>
<dt><code>-i</code>, <code>&#8211;inode</code></p>
<dd>Treat <i>destination</i> as inode number.</p>
<dt><code>-m</code>, <code>&#8211;min-fragments</code></p>
<dd>Minimize fragmentation when allocating space to the attribute. This is mostly useful when creating big files.</p>
<dt><code>-N</code>, <code>&#8211;attr-name</code> NAME</p>
<dd>Write to attribute with this name.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Use this option to make a test run before doing the real copy operation. Volume will be opened read-only and no write will be done.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not working with a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-t</code>, <code>&#8211;timestamp</code></p>
<dd>Copy the modification time of source_file to destination. This is not compatible with <code>&#8211;attr-name</code> and <code>&#8211;attribute</code>.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license <code>ntfscp</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</dl>
<h2>Data Streams</h2>
<p>All data on NTFS is stored in streams, which can have names. A file can have more than one data streams, but exactly one must have no name. The size of a file is the size of its unnamed data stream. Usually when you don&#8217;t specify stream name you are access to unnamed data stream. If you want access to named data stream you need to add &quot;:stream_name&quot; to the filename. For example: by opening &quot;some.mp3:artist&quot; you will open stream &quot;artist&quot; in &quot;some.mp3&quot;. But windows usually prevent you from accessing to named data streams, so you need to use some program like FAR or utils from cygwin to access named data streams.</p>
<h2>Examples</h2>
<p>Copy new_boot.ini from /home/user as boot.ini to the root of an /dev/hda1 NTFS volume:</p>
<dl>
<dd><code>ntfscp /dev/hda1 /home/user/new_boot.ini boot.ini</code></dl>
<p> Copy myfile to C:\some\path\myfile:stream (assume that /dev/hda1 letter in windows is C):</p>
<dl>
<dd><code>ntfscp -N stream /dev/hda1 myfile /some/path</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfscp</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfscp</code> was written by Yura Pakhuchiy, with contributions from Anton Altaparmakov and Hil Liao. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Dedication</h2>
<p>With love to Marina Sapego.</p>
<h2>Availability</h2>
<p><code>ntfscp</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g">https://github.com/tuxera/ntfs-3g</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
