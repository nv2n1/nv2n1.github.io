---
title: "align_image_stack(1)"
name: "align_image_stack"
section: "1"
letter: "a"
url: "/docs/linux/man/1-align_image_stack/"
description: "align_image_stack – Align overlapping images for HDR or focus stack creation"
---

<h2 class="name">NAME</h2>
<p> align_image_stack &#8211; Align overlapping images for HDR or focus stack creation </p>
<h2>SYNOPSIS</h2>
<p> <code>align_image_stack</code> [options] <i>input files</i></p>
<h2>DESCRIPTION</h2>
<p> align_image_stack is used for the alignment of slightly misaligned images or for the registration of a stereo images pair. When several differently exposed images are taken in the process of creating a High Dynamic Range image, the images are not perfectly aligned, and the quality of the <font SIZE="-1">HDR</font> image created will suffer from this. align_image_stack uses the tools available to hugin to optimize the roll, pitch and yaw, as well as some parameters of the lens geometry, to align the images.</p>
<h2>OPTIONS</h2>
<p> Modes of operation:</p>
<dl>
<dt><code>-p</code> <i>file</i></p>
<dd> Output .pto file (useful for debugging, or further refinement)</p>
<dt><code>-a</code> <i>prefix</i></p>
<dd> Output aligned images as prefix_xxxx.tif</p>
<dt><code>-o</code> <i>output</i></p>
<dd> Align images and merge them to <font SIZE="-1">HDR,</font> generate output.hdr</dl>
<p> Modifiers:</p>
<dl>
<dt><code>-v</code></p>
<dd> Verbose, print progress messages. Repeat for higher verbosity</p>
<dt><code>-e</code></p>
<dd> Assume input images are full frame fish eye (default: rectilinear)</p>
<dt><code>-t</code> <i>num</i></p>
<dd> Remove all control points with an error higher than num pixels (default: 3)</p>
<dt><code>&#8211;corr=num</code></p>
<dd> Correlation threshold for identifying control points (default: 0.9)</p>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>HFOV</i></font><i></i></p>
<dd> Approximate horizontal field of view of input images, use if <font SIZE="-1">EXIF</font> info not complete</p>
<dt><code>-m</code></p>
<dd> Optimize field of view for all images, except for first. Useful for aligning focus stacks with slightly different magnification.</p>
<dt><code>-d</code></p>
<dd> Optimize radial distortion for all images, except for first.</p>
<dt><code>-i</code></p>
<dd> Optimize image center shift for all images, except for first.</p>
<dt><code>-x</code></p>
<dd> Optimize X coordinate of camera position</p>
<dt><code>-y</code></p>
<dd> Optimize Y coordinate of camera position</p>
<dt><code>-z</code></p>
<dd> Optimize Z coordinate of camera position</p>
<dt><code>-S</code></p>
<dd> Assume stereo images &#8211; allow horizontal shift of control points.</p>
<dt><code>-A</code></p>
<dd> Align stereo window &#8211; assumes -S</p>
<dt><code>-P</code></p>
<dd> Align stereo window with pop-out effect &#8211; assumes -S</p>
<dt><code>-C</code></p>
<dd> Auto crop the image to the area covered by all images</p>
<dt><code>-c</code> <i>num</i></p>
<dd> Number of control points (per grid) to create between adjacent images (default: 8)</p>
<dt><code>-l</code></p>
<dd> Assume linear input files</p>
<dt><code>-s</code> <i>scale</i></p>
<dd> Scale down image by 2^scale (default: 1 [2x down-sampling])</p>
<dt><code>-g</code> <i>gsize</i></p>
<dd> Break image into a rectangular grid (gsize x gsize) and attempt to find num control points in each section (default: 5 [5&#215;5 grid])</p>
<dt><code>&#8211;threads=NUM</code></p>
<dd> Use <font SIZE="-1">NUM</font> threads</p>
<dt><code>&#8211;gpu</code></p>
<dd> Use <font SIZE="-1">GPU</font> for remapping</p>
<dt><code>-h</code></p>
<dd> Display help summary.</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. Stereo functionality added by Vladimir Nadvornik. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
