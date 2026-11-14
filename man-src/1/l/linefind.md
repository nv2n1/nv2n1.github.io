---
title: "linefind(1)"
name: "linefind"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linefind/"
description: "linefind – Detect vertical features in images"
---

<h2 class="name">NAME</h2>
<p> linefind &#8211; Detect vertical features in images </p>
<h2>SYNOPSIS</h2>
<p> <code>linefind</code> [options] -o <i>output.pto</i> <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>linefind</code> is a detector for vertical features in images. It tries to find vertical lines using the same algorithm as Calibrate_lens_gui and assigns vertical control points to them. The detection runs on the source images, if the input images are rectilinear images. In the other cases (e. g. fisheye images) the input images are reprojected to an equirectangular projection and the detection works on the reprojected images. It uses the roll value, saved in the pto project file, to determine what is &#8220;top&#8221; and &#8220;bottom&#8221;. So before running linefind check that your roll values are correct (E. g. when using images straight from the camera, use a roll value of 0 for landscape and a value of 90 or 270 for portrait images. If your camera has an orientation sensor, Hugin can detect this information automatically and sets the roll value accordingly when adding such images into Hugin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o|&#8211;output</code> output.pto</p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &#8216;&lt;filename&gt;_line.pto&#8217;.</p>
<dt><code>-l|&#8211;lines</code> num</p>
<dd> The maximum number of lines added per image (default: 5) Attention: Keep in mind that more vertical control points will dominate the optimisation in favour of &#8220;normal&#8221; control points.</p>
<dt><code>-i|&#8211;image</code> num</p>
<dd> Image number(s) to process. Normally linefind tries to find vertical lines in all images of the project file. If you want to limit the detection to some selected images, you can use this parameter. Can be used multiple times.</p>
<dt><code>-h|&#8211;help</code></p>
<dd> shows help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes, line detection code based on calibrate_lens by Tim Nugent </p>
<h2>Index</h2>
