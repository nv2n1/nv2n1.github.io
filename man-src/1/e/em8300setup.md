---
title: "em8300setup(1)"
name: "em8300setup"
section: "1"
letter: "e"
url: "/docs/linux/man/1-em8300setup/"
description: "em8300setup – program to configure and upload microcode images to em8300-based MPEG decoder cards"
---

<h2 class="name">NAME</h2>
<p> em8300setup &#8211; program to configure and upload microcode images to em8300-based MPEG decoder cards</p>
<h2>SYNOPSIS</h2>
<p> <code>em8300setup</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>em8300setup</code> is a program that configures and uploads microcode images to em8300-based MPEG decoder cards, such as the Creative Labs DXR3 or the Sigma Designs Hollywood+. With no option, this program tries to upload a microcode image from the (system-dependent) default location, which is not relevant if you extracted your own microcodes. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>-p6</code>, <code>-n</code></p>
<dd> Set video output mode to respectively PAL, PAL60 or NTSC.</p>
<dt><code>-a</code>, <code>-d</code>, <code>-3</code></p>
<dd> Set audio output mode to respectively analog, digital PCM or digital AC3.</p>
<dt><code>-o</code>, <code>-w</code></p>
<dd> Set aspect ratio to respectively normal (4:3) or wide-screen (16:9).</p>
<dt><code>-S</code>, <code>-s</code></p>
<dd> Set sub-pictures respectively on or off.</p>
<dt><code>-q</code></p>
<dd> Query the current settings for all the options above and exit with no change.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd> Specify a microcode image to upload. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Nicolas Boullis &lt;nboullis [at] debian.org&gt;, for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
