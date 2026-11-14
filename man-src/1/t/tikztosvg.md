---
title: "tikztosvg(1)"
name: "tikztosvg"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tikztosvg/"
description: "tikztosvg – Render TikZ diagrams to SVG."
---

<h2 class="name">NAME</h2>
<p> tikztosvg &#8211; Render TikZ diagrams to SVG. </p>
<h2>SYNOPSIS</h2>
<p> <code>tikztosvg</code> [<i>OPTION</i>]&#8230; <i>INPUT_PATH</i></p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-tikztosvg/">tikztosvg</a>(1) command renders TikZ diagrams to SVG. </p>
<p> If <i>INPUT_PATH</i> is set to <i>&#8211;</i> the input will be read from stdin.</p>
<h2>OPTIONS</h2>
<p> <code>-o, &#8211;output</code>=<i>OUTPUT_PATH</i></p>
<dl>
<dt>
<dd> Write output to file <i>OUTPUT_PATH</i>. If set to <i>&#8211;</i> the output will be written to stdout. Defaults to the base name of the input file suffixed with the <i>.svg</i> extension. The file is resolved relative to the working directory.</dl>
<p> <code>-p, &#8211;package</code>=+<i>PACKAGE</i></p>
<dl>
<dt>
<dd> Include <i>
