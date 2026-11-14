---
title: "icns2png(1)"
name: "icns2png"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icns2png/"
description: "icns2png – convert Mac OS icns files to png images"
---

<h2>NAME</h2>
<p> icns2png &#8211; convert Mac OS icns files to png images</p>
<h2>SYNOPSIS</h2>
<p> <code>icns2png</code> [<i>-x|-l</i>] [<i>options</i>] [<i>file </i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> icns2png extracts images from mac .icns files, and exports them to png format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> List the contents of one or more icns images</p>
<dt> <code>-x</code>, <code>&#8211;extract</code> Extract one or more icons to png images</p>
<dt><code>-o</code>, <code>&#8211;output</code></p>
<dd>
<dd>Where to place extracted files. If not specified, icons will be extracted to the same path as the source file.</p>
<dt><code>-d</code>, <code>&#8211;depth</code></p>
<dd> Sets the pixel depth of the icons to extract. (1,4,8,32)</p>
<dt><code>-s</code>, <code>&#8211;size</code></p>
<dd> Sets the width and height of the icons to extract. (16,48,etc) Sizes 16&#215;12, 16&#215;16, 32&#215;32, 48&#215;48, 128&#215;128, etc. are also valid.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays this help message.</p>
<dt> <code>-v</code>, <code>&#8211;version</code> Displays the version information</dl>
<h2>EXAMPLES</h2>
<dd>icns2png <code>-x</code> anicon.icns # Extract all icon found in anicon.icns<br />
 icns2png <code>-x</code> <code>-s</code> 48 anicon.icns # Extract all 48&#215;48 32-bit icons<br />
 icns2png <code>-x</code> <code>-s</code> 32 <code>-d</code> 1 anicon.icns # Extract all 32&#215;32 1-bit icons<br />
 icns2png <code>-l</code> anicon.icns # Lists the icons contained in anicon.icns</p>
<h2>AUTHOR</h2>
<p> Written by Mathew Eis</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2008 Mathew Eis<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
