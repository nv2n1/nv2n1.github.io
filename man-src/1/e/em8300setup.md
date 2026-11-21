---
title: "em8300setup(1)"
name: "em8300setup"
section: "1"
letter: "e"
url: "/docs/linux/man/1-em8300setup/"
description: "em8300setup – program to configure and upload microcode images to em8300-based MPEG decoder cards"
---

<h2>SYNOPSIS</h2>
<p> <code>em8300setup</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>em8300setup</code> is a program that configures and uploads microcode images to em8300-based MPEG decoder cards, such as the Creative Labs DXR3 or the Sigma Designs Hollywood+. With no option, this program tries to upload a microcode image from the (system-dependent) default location, which is not relevant if you extracted your own microcodes. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>-p6</code>, <code>-n</code></dt>
<dd> Set video output mode to respectively PAL, PAL60 or NTSC.</dd>
<dt><code>-a</code>, <code>-d</code>, <code>-3</code></dt>
<dd> Set audio output mode to respectively analog, digital PCM or digital AC3.</dd>
<dt><code>-o</code>, <code>-w</code></dt>
<dd> Set aspect ratio to respectively normal (4:3) or wide-screen (16:9).</dd>
<dt><code>-S</code>, <code>-s</code></dt>
<dd> Set sub-pictures respectively on or off.</dd>
<dt><code>-q</code></dt>
<dd> Query the current settings for all the options above and exit with no change.</dd>
<dt><code>-f</code> <i>filename</i></dt>
<dd> Specify a microcode image to upload. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Nicolas Boullis &lt;nboullis [at] debian.org&gt;, for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
