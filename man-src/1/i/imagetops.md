---
title: "imagetops(1)"
name: "imagetops"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imagetops/"
description: "imagetops – generic image to ps filter"
---

<h2 class="name">NAME</h2>
<p> imagetops &#8211; generic image to ps filter </p>
<h2>SYNOPSIS</h2>
<p> <code>imagetops</code>&nbsp;[<code>-gray</code>]&nbsp;[<code>arguments for pnmtops</code>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>imagetops</code> is a generic image to ps filter. It can be used as print filter in KDE. </p>
<p> <code>imagetops</code> works in two steps:</p>
<dl>
<dt> 1.</p>
<dd> the given file is converted to PNM format by analyzing the file format and calling the appropriate conversion program.</p>
<dt> 2.</p>
<dd> the file in PNM format is converted to PS format by calling <code>pnmtops</code>.</dl>
<p> The supported mime types are: jpeg, png, x-png, bmp, x-bmp, gif and tiff. </p>
<p> <code>imagetops</code> supports reading the parameters via stdin. A temporary file in <i>$TMPDIR</i> (or <i>/tmp</i> if unset) is created then.</p>
<h2>OPTIONS</h2>
<h3>Options:</h3>
<dl>
<dt><code>-gray</code></p>
<dd> convert image to grayscale</dl>
<h3>Arguments:</h3>
<dl>
<dt><code>arguments for pnmtops</code></p>
<dd> arguments passed to pnmtops</p>
<dt><i>filename</i></p>
<dd> image file to convert</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bmptoppm/">bmptoppm</a></code>(1),&nbsp;<code><a href="/docs/linux/man/1-giftopnm/">giftopnm</a></code>(1),&nbsp;<code><a href="/docs/linux/man/1-jpegtopnm/">jpegtopnm</a></code>(1),&nbsp;<code><a href="/docs/linux/man/1-pngtopnm/">pngtopnm</a></code>(1),&nbsp;<code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1),&nbsp; <code><a href="/docs/linux/man/1-pnmtops/">pnmtops</a></code>(1)</p>
<h2>AUTHORS</h2>
<pre>
The KDE project
<br>
<br>
</pre>
<p> Please use <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a> to report bugs. </p>
<p> This manual page was written by Holger Hartmann &lt;Holger_Hartmann [at] gmx.de&gt; for the <code>Debian</code> Project (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On <code>Debian</code> systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
