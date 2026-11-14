---
title: "dh_compress(1)"
name: "dh_compress"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_compress/"
description: "dh_compress – compress files and fix symlinks in package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_compress &#8211; compress files and fix symlinks in package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_compress</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>] [<code>-A</code>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_compress</code> is a debhelper program that is responsible for compressing the files in package build directories, and makes sure that any symlinks that pointed to the files before they were compressed are updated to point to the new files. </p>
<p> By default, <code>dh_compress</code> compresses files that Debian policy mandates should be compressed, namely all files in <i>usr/share/info</i>, <i>usr/share/man</i>, files in <i>usr/share/doc</i> that are larger than 4k in size, (except the <i>copyright</i> file, <i>.html</i> and other web files, image files, and files that appear to be already compressed based on their extensions), and all <i>changelog</i> files. Plus <font SIZE="-1">PCF</font> fonts underneath <i>usr/share/fonts/X11/</i></p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.compress</p>
<dd> These files are deprecated. </p>
<p> If this file exists, the default files are not compressed. Instead, the file is ran as a shell script, and all filenames that the shell script outputs will be compressed. The shell script will be run from inside the package build directory. Note though that using <code>-X</code> is a much better idea in general; you should only use a <i>debian/package.compress</i> file if you really need to.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being compressed. For example, <code>-X.tiff</code> will exclude <font SIZE="-1">TIFF</font> files from compression. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Compress all files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><i>file</i> &#8230;</p>
<dd> Add these files to the list of files to compress.</dl>
<h2>CONFORMS TO</h2>
<p> Debian policy, version 3.0</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
