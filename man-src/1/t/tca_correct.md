---
title: "tca_correct(1)"
name: "tca_correct"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tca_correct/"
description: "tca_correct – Calculate transverse chromatic aberration"
---

<h2>SYNOPSIS</h2>
<p> <code>tca_correct</code> [options] <i>inputfile</i> </p>
<p> &lt;inputfile&gt; is the base name of 4 image files:</p>
<dl>
<dt>&lt;inputfile&gt;</dt>
<dd> Colour file to compute <font SIZE="-1">TCA</font> parameters</dd>
<dt>red_&lt;inputfile&gt;</dt>
<dd> Red channel of &lt;inputfile&gt;</dd>
<dt>green_&lt;inputfile&gt;</dt>
<dd> Green channel of &lt;inputfile&gt;</dd>
<dt>blue_&lt;inputfile&gt;</dt>
<dd> Blue channel of &lt;inputfile&gt;</dd></dl>
<p> The channel images must be colour images with 3 identical channels. If any of -R, -G, or -B is given, this file name is used instead of the derived name. </p>
<p> Output: commandline arguments for fulla</p>
<h2>DESCRIPTION</h2>
<p> Generates fulla command-line parameters for correction of transverse chromatic aberration (<font SIZE="-1">TCA</font>) from sample photos. Ideal sample photos would have a lot of contrast over the entire image area, little saturated colour and no blown highlights.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display help</dd>
<dt><code>-l</code></dt>
<dd> input file is <font SIZE="-1">PTO</font> file instead of image</dd>
<dt><code>-m</code> <i>method</i></dt>
<dd> optimization method (0 normal, 1 newfit)</dd>
<dt><code>-o</code> <i>optvars</i></dt>
<dd> string of variables to optimize (&#8220;abcvde&#8221;)</dd>
<dt><code>-r</code></dt>
<dd> Reset values (this will zero a,b,c,d,e params and set v to 10) makes sense only with -l option</dd>
<dt><code>-s</code> <i>&lt;scale</i>&gt;</dt>
<dd> Scale for corner detection</dd>
<dt><code>-n</code> <i>&lt;number</i>&gt;</dt>
<dd> number of points per grid cell (default: 10)</dd>
<dt><code>-g</code> <i>&lt;number</i>&gt;</dt>
<dd> divide image in &lt;number&gt;x&lt;number&gt; grid cells (default: 10)</dd>
<dt><code>-t</code> <i>num</i></dt>
<dd> Remove all control points with an error higher than num pixels (default: 1.5)</dd>
<dt><code>-v</code></dt>
<dd> Verbose</dd>
<dt><code>-w</code> <i>filename</i></dt>
<dd> write <font SIZE="-1">PTO</font> file</dd>
<dt><code>-R</code> <i>&lt;r</i>&gt;</dt>
<dd> Use this file as red channel</dd>
<dt><code>-G</code> <i>&lt;g</i>&gt;</dt>
<dd> Use this file as green channel</dd>
<dt><code>-B</code> <i>&lt;b</i>&gt;</dt>
<dd> Use this file as blue channel</dd></dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo and others. </p>
