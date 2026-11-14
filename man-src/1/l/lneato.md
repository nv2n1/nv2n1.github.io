---
title: "lneato(1)"
name: "lneato"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lneato/"
description: "lneato – A Customizable Graph Editor"
---

<h2 class="name">NAME</h2>
<p> lneato &#8211; A Customizable Graph Editor </p>
<h2>SYNOPSIS</h2>
<p> <code>lneato</code> [ <code>-V</code> ] [ <code>-lm</code><i>mode</i> ] [ <code>-el</code><i>lev</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lneato</code> is a graph editor for the X Window System. It may be run as a standalone editor, or as a front end for applications that use graphs. It can control multiple windows viewing different graphs. </p>
<p> <code>lneato</code> is written on top of <code>neato</code> and <code>lefty</code>. <code>lefty</code> is a general-purpose programmable editor for technical pictures. It has an interpretive programming language similar to AWK and C. The user interface and graph editing operations of <code>lneato</code> are written as <code>lefty</code> functions. Programmer-defined graph operations may be loaded as well. Graph layouts are made by <code>neato</code>, which runs as a separate process that communicates with <code>lefty</code> through pipes. </p>
<p> If the input graph contains xdot attributes, <code>lneato</code> will use that to display the graph. Otherwise, it runs <code>neato</code> to obtain layout information.</p>
<h2>USAGE</h2>
<p> The file name is optional. If present, the graph contained in that file is displayed in the <code>lneato</code> window.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Prints the version.</p>
<dt><code>-lm</code><i>mode</i></p>
<dd> Sets the layout mode. The <i>mode</i> can be <code>sync</code> or <code>async</code>. The default is <code>async</code>.</p>
<dt><code>-el</code><i>lev</i></p>
<dd> Sets the mesage level. The <i>lev</i> can be <code>0</code> or <code>1</code>. The default is <code>0</code>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-neato/">neato</a>(1), <a href="/docs/linux/man/1-lefty/">lefty</a>(1), <a href="/docs/linux/man/1-dotty/">dotty</a>(1), <a href="/docs/linux/man/3-xdot/">xdot</a>(3),<br />
 <i>dotty</i> user guide. </p>
<h2>Index</h2>
