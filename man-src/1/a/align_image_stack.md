---

title: "align_image_stack(1)"
name: "align_image_stack"
section: "1"
letter: "a"
url: "/docs/linux/man/1-align_image_stack/"
description: "align_image_stack – Align overlapping images for HDR or focus stack creation"
---

<p> align_image_stack &#8211; Align overlapping images for HDR or focus stack creation </p>
<h2>SYNOPSIS</h2>
<p> <code>align_image_stack</code> [options] <i>input files</i></p>
<h2>DESCRIPTION</h2>
<p> align_image_stack is used for the alignment of slightly misaligned images or for the registration of a stereo images pair. When several differently exposed images are taken in the process of creating a High Dynamic Range image, the images are not perfectly aligned, and the quality of the <font SIZE="-1">HDR</font> image created will suffer from this. align_image_stack uses the tools available to hugin to optimize the roll, pitch and yaw, as well as some parameters of the lens geometry, to align the images.</p>
<h2>OPTIONS</h2>
<p> Modes of operation:</p>
<dl>
<dt><code>-p</code> <i>file</i></dt>
<dd> Output .pto file (useful for debugging, or further refinement)</dd>
<dt><code>-a</code> <i>prefix</i></dt>
<dd> Output aligned images as prefix_xxxx.tif</dd>
<dt><code>-o</code> <i>output</i></dt>
<dd> Align images and merge them to <font SIZE="-1">HDR,</font> generate output.hdr</dd></dl>
<p> Modifiers:</p>
<dl>
<dt><code>-v</code></dt>
<dd> Verbose, print progress messages. Repeat for higher verbosity</dd>
<dt><code>-e</code></dt>
<dd> Assume input images are full frame fish eye (default: rectilinear)</dd>
<dt><code>-t</code> <i>num</i></dt>
<dd> Remove all control points with an error higher than num pixels (default: 3)</dd>
<dt><code>&#8211;corr=num</code></dt>
<dd> Correlation threshold for identifying control points (default: 0.9)</dd>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>HFOV</i></font><i></i></dt>
<dd> Approximate horizontal field of view of input images, use if <font SIZE="-1">EXIF</font> info not complete</dd>
<dt><code>-m</code></dt>
<dd> Optimize field of view for all images, except for first. Useful for aligning focus stacks with slightly different magnification.</dd>
<dt><code>-d</code></dt>
<dd> Optimize radial distortion for all images, except for first.</dd>
<dt><code>-i</code></dt>
<dd> Optimize image center shift for all images, except for first.</dd>
<dt><code>-x</code></dt>
<dd> Optimize X coordinate of camera position</dd>
<dt><code>-y</code></dt>
<dd> Optimize Y coordinate of camera position</dd>
<dt><code>-z</code></dt>
<dd> Optimize Z coordinate of camera position</dd>
<dt><code>-S</code></dt>
<dd> Assume stereo images &#8211; allow horizontal shift of control points.</dd>
<dt><code>-A</code></dt>
<dd> Align stereo window &#8211; assumes -S</dd>
<dt><code>-P</code></dt>
<dd> Align stereo window with pop-out effect &#8211; assumes -S</dd>
<dt><code>-C</code></dt>
<dd> Auto crop the image to the area covered by all images</dd>
<dt><code>-c</code> <i>num</i></dt>
<dd> Number of control points (per grid) to create between adjacent images (default: 8)</dd>
<dt><code>-l</code></dt>
<dd> Assume linear input files</dd>
<dt><code>-s</code> <i>scale</i></dt>
<dd> Scale down image by 2^scale (default: 1 [2x down-sampling])</dd>
<dt><code>-g</code> <i>gsize</i></dt>
<dd> Break image into a rectangular grid (gsize x gsize) and attempt to find num control points in each section (default: 5 [5&#215;5 grid])</dd>
<dt><code>&#8211;threads=NUM</code></dt>
<dd> Use <font SIZE="-1">NUM</font> threads</dd>
<dt><code>&#8211;gpu</code></dt>
<dd> Use <font SIZE="-1">GPU</font> for remapping</dd>
<dt><code>-h</code></dt>
<dd> Display help summary.</dd></dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. Stereo functionality added by Vladimir Nadvornik. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
