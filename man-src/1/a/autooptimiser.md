---
title: "autooptimiser(1)"
name: "autooptimiser"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autooptimiser/"
description: "autooptimiser – Optimize image positions"
---

<h2 class="name">NAME</h2>
<p> autooptimiser &#8211; Optimize image positions </p>
<h2>SYNOPSIS</h2>
<p> <code>autooptimiser</code> [options] <i>project.pto</i> </p>
<p> (<code>&#8211;</code> can be specified to read the project from stdio.)</p>
<h2>DESCRIPTION</h2>
<p> autooptimiser works similarly to PToptimizer but with extra command-line options. </p>
<p> It is also different in that PToptimizer appends its output onto the input file in the form of &#8216;o&#8217; lines which need further processing. autooptimiser simply updates the project and writes it to a new file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>file.pto</i></p>
<dd> Output file. If omitted, stdout is used.</dl>
<p> Optimisation options (if not specified, no optimisation takes place):</p>
<dl>
<dt><code>-a</code></p>
<dd> Auto align mode, includes various optimisation stages, depending on the amount and distribution of the control points</p>
<dt><code>-p</code></p>
<dd> Pairwise optimisation of yaw, pitch and roll, starting from first image</p>
<dt><code>-m</code></p>
<dd> Optimise photometric parameters</p>
<dt><code>-n</code></p>
<dd> Optimize parameters specified in script file (like PToptimizer).</dl>
<p> Post-processing options:</p>
<dl>
<dt><code>-l</code></p>
<dd> Level horizon (works best for horizontal panoramas)</p>
<dt><code>-s</code></p>
<dd> Automatically select a suitable output projection and size</dl>
<p> Other options:</p>
<dl>
<dt><code>-q</code></p>
<dd> Quiet operation (no progress is reported)</p>
<dt><code>-v</code> <i></i><font SIZE="-1"><i>HFOV</i></font><i></i></p>
<dd> Specify horizontal field of view of input images. Used if the .pto file contains invalid <font SIZE="-1">HFOV</font> values (autopano-SIFT writes .pto files with invalid <font SIZE="-1">HFOV</font>)</dl>
<p> When <code>-a</code>, <code>-l</code>, <code>-m</code> and <code>-s</code> options are used together, an operation similar to the one of the &#8220;Align&#8221; button in hugin is performed.</p>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
