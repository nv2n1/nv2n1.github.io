---
title: "ntfsls(8)"
name: "ntfsls"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsls/"
description: "ntfsls – list directory contents on an NTFS filesystem"
---

<p>ntfsls &#8211; list directory contents on an NTFS filesystem</p>
<h2>Synopsis</h2>
<p><code>ntfsls</code> [<i>options</i>] <i>device</i> </p>
<p> <code>ntfsls</code> [ <code>-a</code> | <code>&#8211;all</code> ] [ <code>-F</code> | <code>&#8211;classify</code> ] [ <code>-f</code> | <code>&#8211;force</code> ] [ <code>-h</code> | <code>&#8211;help</code> ] [ <code>-i</code> | <code>&#8211;inode</code> ] [ <code>-l</code> | <code>&#8211;long</code> ] [ <code>-p</code> | <code>&#8211;path</code> <i>PATH</i> ] [ <code>-q</code> | <code>&#8211;quiet</code> ] [ <code>-s</code> | <code>&#8211;system</code> ] [ <code>-V</code> | <code>&#8211;version</code> ] [ <code>-v</code> | <code>&#8211;verbose</code> ] [ <code>-x</code> | <code>&#8211;dos</code> ] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfsls</code> is used to list information about the files specified by the <i>PATH</i> option (the root directory by default). <i>DEVICE</i> is the special file corresponding to the device (e.g <i>/dev/hdXX</i>) or an NTFS image file.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsls</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>Display all files. If this option is not specified file names in the POSIX namespace will not be displayed.</p>
<dt><code>-F</code>, <code>&#8211;classify</code></p>
<dd>Append indicator (one of */=@|) to entries.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Force execution. For example necessary to run on an NTFS partition stored in a normal file.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print the usage information of <code>ntfsls</code> and exit.</p>
<dt><code>-i</code>, <code>&#8211;inode</code></p>
<dd>Print inode number of each file. This is the MFT reference number in NTFS terminology.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd>Use a long listing format.</p>
<dt><code>-p</code>, <code>&#8211;path</code> PATH</p>
<dd>The directory whose contents to list or the file (including the path) about which to display information.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd>Show the contents of all directories beneath the specified directory.</p>
<dt><code>-s</code>, <code>&#8211;system</code></p>
<dd>Unless this options is specified, all files beginning with a dollar sign character will not be listed as these files are usually system files.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version number of <code>ntfsls</code> and exit.</p>
<dt><code>-x</code>, <code>&#8211;dos</code></p>
<dd>Display short file names, i.e. files in the DOS namespace, instead of long file names, i.e. files in the WIN32 namespace.</dl>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfsls</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p>This version of <code>ntfsls</code> was written by Lode Leroy, Anton Altaparmakov, Richard Russon, Carmelo Kintana and Giang Nguyen. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfsls</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
