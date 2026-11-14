---
title: "composeglyphs(1)"
name: "composeglyphs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-composeglyphs/"
description: "composeglyphs – generate an encoding vector or new font for postscript"
---

<h2 class="name">NAME</h2>
<p> composeglyphs &#8211; generate an encoding vector or new font for postscript </p>
<h2>SYNOPSIS</h2>
<p> <code>composeglyphs</code> <code>-e</code> <i>encoding.afm</i> <code>-E</code> <i>encoding.ps</i> </p>
<p> <code>composeglyphs</code> <code>-i</code> <i>input.afm</i> <code>-o</code> <i>output.ps</i> <code>-c</code> <i>composite.afm</i> <code>-n</code> <i>newname</i> <code>-e</code> <i>base_encoding.afm</i> <code>-t</code> <i>target_encoding.afm</i> <code>-a</code> <i>output.afm</i></p>
<h2>DESCRIPTION</h2>
<p> <code>composeglyphs</code> is a script to generate either an encoding vector or a new font for postscript. It requires a pre-existing AFM and allows for the use of composite characters that that AFM does not already provide.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code> <i>encoding.afm</i></p>
<dd> The base encoding AFM to use.</p>
<dt><code>-E</code> <i>encoding.ps</i></p>
<dd> The encoding vector to output.</p>
<dt><code>-i</code> <i>input.afm</i></p>
<dd> The AFM of the original font.</p>
<dt><code>-o</code> <i>output.ps</i></p>
<dd> The font program to generate.</p>
<dt><code>-c</code> <i>composite.afm</i></p>
<dd> The AFM containing supplementary composite character information.</p>
<dt><code>-n</code> <i>newname</i></p>
<dd> The name of the new font.</p>
<dt><code>-t</code> <i>target_encoding.afm</i></p>
<dd> The target encoding.</p>
<dt><code>-a</code> <i>output.afm</i></p>
<dd> The name of the AFM file to generate.</dl>
<h2>NOTES</h2>
<p> <code>composeglyphs</code> is a part of <code>Ogonkify</code>, which comes with the <code>a2ps </code> distribution. </p>
<p> If you create new AFMs or modify existing ones, the author asks that you kindly send him a copy so that he may include them in the distribution.</p>
<h2>AUTHOR</h2>
<p> Juliusz Chroboczek &lt;jec [at] dcs.ed.ac.uk&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-ogonkify/">ogonkify</a></code>(1) </p>
<p> The full documentation for <code>Ogonkify</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>a2ps </code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info Ogonkify</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
