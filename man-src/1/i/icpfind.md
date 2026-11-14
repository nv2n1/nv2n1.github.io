---
title: "icpfind(1)"
name: "icpfind"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icpfind/"
description: "icpfind – Use heuristic control-point detection strategies"
---

<h2 class="name">NAME</h2>
<p> icpfind &#8211; Use heuristic control-point detection strategies </p>
<h2>SYNOPSIS</h2>
<p> <code>icpfind</code> [options] -o <i>output.pto</i> <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>icpfind</code> is a command-line tool to use the various different control point detectors and heuristic control point detector strategies defined in the Hugin Parameters for Control Point Detectors dialog. It does not introduce new functionality, it allows running the different control points detectors from the command-line and not only in the <font SIZE="-1">GUI. </font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code>, <code>&#8211;output=file.pto</code></p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Required</p>
<dt><code>-s</code>, <code>&#8211;setting=NUMBER</code></p>
<dd> Setting to use as defined by the order in the Hugin <font SIZE="-1">GUI</font> Preferences, expects an integer. The first setting in the Preferences has the number 0, the next is 1 and so on. If left undefined then the setting defined as default in the Hugin Preferences is used.</p>
<dt><code>-m</code>, <code>&#8211;matches=NUMBER</code></p>
<dd> Number of control points per pair of photos</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Shows help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
