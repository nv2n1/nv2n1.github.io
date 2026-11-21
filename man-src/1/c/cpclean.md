---

title: "cpclean(1)"
name: "cpclean"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpclean/"
description: "cpclean – Remove wrong control points by statistical methods"
---

<p> <code>cpclean</code> [options] <i>input.pto</i></p>
<p> <code>cpclean</code> uses statistical methods to remove wrong control points. </p>
<p> Step 1 optimises all images pairs, calculates for each pair mean and standard deviation and removes all control points with error bigger than mean+n*sigma. </p>
<p> Step 2 optimises the whole panorama, calculates mean and standard deviation for all control points and removes all control points with error bigger than mean+n*sigma.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> output.pto</dt>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &#8216;&lt;filename&gt;_clean.pto&#8217;.</dd>
<dt><code>-n</code> num</dt>
<dd> distance factor for checking (default: 2)</dd>
<dt><code>-p</code></dt>
<dd> do only pairwise optimisation (skip step 2)</dd>
<dt><code>-w</code></dt>
<dd> do optimise whole panorama (skip step 1)</dd>
<dt><code>-s</code></dt>
<dd> skip optimisation step when optimising the whole panorama</dd>
<dt><code>-l</code></dt>
<dd> also include line control points for calculation and filtering in step 2</dd>
<dt><code>-h</code></dt>
<dd> shows help</dd></dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
