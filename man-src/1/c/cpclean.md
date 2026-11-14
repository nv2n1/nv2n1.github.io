---
title: "cpclean(1)"
name: "cpclean"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpclean/"
description: "cpclean – Remove wrong control points by statistical methods"
---

<h2 class="name">NAME</h2>
<p> cpclean &#8211; Remove wrong control points by statistical methods </p>
<h2>SYNOPSIS</h2>
<p> <code>cpclean</code> [options] <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>cpclean</code> uses statistical methods to remove wrong control points. </p>
<p> Step 1 optimises all images pairs, calculates for each pair mean and standard deviation and removes all control points with error bigger than mean+n*sigma. </p>
<p> Step 2 optimises the whole panorama, calculates mean and standard deviation for all control points and removes all control points with error bigger than mean+n*sigma.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> output.pto</p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &#8216;&lt;filename&gt;_clean.pto&#8217;.</p>
<dt><code>-n</code> num</p>
<dd> distance factor for checking (default: 2)</p>
<dt><code>-p</code></p>
<dd> do only pairwise optimisation (skip step 2)</p>
<dt><code>-w</code></p>
<dd> do optimise whole panorama (skip step 1)</p>
<dt><code>-s</code></p>
<dd> skip optimisation step when optimising the whole panorama</p>
<dt><code>-l</code></p>
<dd> also include line control points for calculation and filtering in step 2</p>
<dt><code>-h</code></p>
<dd> shows help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
