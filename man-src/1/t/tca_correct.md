---
title: "tca_correct(1)"
name: "tca_correct"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tca_correct/"
description: "tca_correct – Calculate transverse chromatic aberration"
---

<h2 class="name">NAME</h2>
<p> tca_correct &#8211; Calculate transverse chromatic aberration </p>
<h2>SYNOPSIS</h2>
<p> <code>tca_correct</code> [options] <i>inputfile</i> </p>
<p> &lt;inputfile&gt; is the base name of 4 image files:</p>
<dl>
<dt>&lt;inputfile&gt;</p>
<dd> Colour file to compute <font SIZE="-1">TCA</font> parameters</p>
<dt>red_&lt;inputfile&gt;</p>
<dd> Red channel of &lt;inputfile&gt;</p>
<dt>green_&lt;inputfile&gt;</p>
<dd> Green channel of &lt;inputfile&gt;</p>
<dt>blue_&lt;inputfile&gt;</p>
<dd> Blue channel of &lt;inputfile&gt;</dl>
<p> The channel images must be colour images with 3 identical channels. If any of -R, -G, or -B is given, this file name is used instead of the derived name. </p>
<p> Output: commandline arguments for fulla</p>
<h2>DESCRIPTION</h2>
<p> Generates fulla command-line parameters for correction of transverse chromatic aberration (<font SIZE="-1">TCA</font>) from sample photos. Ideal sample photos would have a lot of contrast over the entire image area, little saturated colour and no blown highlights.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display help</p>
<dt><code>-l</code></p>
<dd> input file is <font SIZE="-1">PTO</font> file instead of image</p>
<dt><code>-m</code> <i>method</i></p>
<dd> optimization method (0 normal, 1 newfit)</p>
<dt><code>-o</code> <i>optvars</i></p>
<dd> string of variables to optimize (&#8220;abcvde&#8221;)</p>
<dt><code>-r</code></p>
<dd> Reset values (this will zero a,b,c,d,e params and set v to 10) makes sense only with -l option</p>
<dt><code>-s</code> <i>&lt;scale</i>&gt;</p>
<dd> Scale for corner detection</p>
<dt><code>-n</code> <i>&lt;number</i>&gt;</p>
<dd> number of points per grid cell (default: 10)</p>
<dt><code>-g</code> <i>&lt;number</i>&gt;</p>
<dd> divide image in &lt;number&gt;x&lt;number&gt; grid cells (default: 10)</p>
<dt><code>-t</code> <i>num</i></p>
<dd> Remove all control points with an error higher than num pixels (default: 1.5)</p>
<dt><code>-v</code></p>
<dd> Verbose</p>
<dt><code>-w</code> <i>filename</i></p>
<dd> write <font SIZE="-1">PTO</font> file</p>
<dt><code>-R</code> <i>&lt;r</i>&gt;</p>
<dd> Use this file as red channel</p>
<dt><code>-G</code> <i>&lt;g</i>&gt;</p>
<dd> Use this file as green channel</p>
<dt><code>-B</code> <i>&lt;b</i>&gt;</p>
<dd> Use this file as blue channel</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo and others. </p>
<h2>Index</h2>
