---
title: "ale(1)"
name: "ale"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ale/"
description: "ale – a synthetic capture engine and renderer"
---

<h2 class="name">NAME</h2>
<p> ale &#8211; a synthetic capture engine and renderer </p>
<h2>SYNOPSIS</h2>
<p> <code>ale</code> [<i>OPTIONS</i>] <i>original-frame</i> [<i>supplemental-frames</i> &#8230;] <i>output-file</i> </p>
<p> <code>ale</code> [<i>HELP OPTIONS</i>] </p>
<p> <code>ale &#8211;version</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ALE</code> is a free software synthetic capture engine and renderer accepting, as input, a sequence of image frames, and producing, as output, rendered images, registration data, and 3D models (currently experimental). </p>
<h2>EXAMPLES</h2>
<p> <code>ale &#8211;hu</code></p>
<dl>
<dt>
<dd> Print the help page on program usage.</dl>
<p> <code>ale 001.ppm 002.ppm 003.ppm out.ppm</code></p>
<dl>
<dt>
<dd> Render output file <code>out.ppm</code> from inputs <code>001.ppm</code>, <code>002.ppm</code>, and <code>003.ppm</code>.</dl>
<p> <code>ale &#8211;scale 2 001.ppm 002.ppm 003.ppm out.png</code></p>
<dl>
<dt>
<dd> Render output file <code>out.png</code> at 2x scale.</dl>
<p> <code>ale &#8211;perturb-upper=0 &#8211;trans-load=a.t &#8211;projective frame*.png out.png</code></p>
<dl>
<dt>
<dd> Render output file <code>out.png</code> from inputs <code>frame*.png</code>, using projective transformations as described in the file <code>a.t</code>.</dl>
<p> <code>ale &#8211;3dv 0 out.png &#8211;projective frame*.png null:</code></p>
<dl>
<dt>
<dd> Render output file <code>out.png</code> from inputs <code>frame*.png</code>, using a 3D scene model to determine transformations.</dl>
<p> <code>ale &#8211;visp last:sinc*lanc:6 sf:0 out/ .jpg in/*.jpg null:</code></p>
<dl>
<dt>
<dd> Render a video stream from files <code>in/*.jpg</code> to the directory <code>out/</code>, stabilizing to the first frame, with a lanczos-windowed sinc filter.</dl>
<h2>USAGE</h2>
<p> <code>ale</code> is a wrapper script that calls the executable <code>ale-bin</code> after extracting exposure EXIF information from image files (when the <code>exiftool</code> utility is available) and converting from raw formats (when the <code>dcraw</code> utility is available). </p>
<p> When <code>ale-bin</code> has been linked with ImageMagick, input and output files may be of any kind supported by ImageMagick. Otherwise, only PPM files can be read and written by <code>ale-bin</code>. </p>
<h2>OPTIONS</h2>
<p> <i>OPTIONS</i> are summarized via built-in help pages (see <code>HELP OPTIONS</code> below). More detailed manuals describing options and internal algorithms are available for certain versions of ALE. See <code>SEE ALSO</code> below for more details on other manuals. </p>
<h2>HELP OPTIONS</h2>
<p> A listing of available help options can be obtained by invoking <code>ale &#8211;hu</code>. </p>
<h2>ENVIRONMENT</h2>
<p> The wrapper script <code>ale</code> recognizes the following environment variables: </p>
<p> <code>ALE_BIN</code></p>
<dl>
<dt>
<dd> ALE executable to use.</dl>
<p> <code>DCRAW</code></p>
<dl>
<dt>
<dd> dcraw raw extraction tool to use.</dl>
<p> <code>EXIF_UTILITY</code></p>
<dl>
<dt>
<dd> EXIF extraction utility to use.</dl>
<p> <code>ALE_COUNT_THREADS</code></p>
<dl>
<dt>
<dd> Displays statistics on thread counts when set to a non-zero value.</dl>
<p> <code>PAGER</code></p>
<dl>
<dt>
<dd> Text pager to use (e.g., for displaying help pages).</dl>
<h2>SEE ALSO</h2>
<p> More detailed manuals for certain versions of ALE are distributed with source packages, and may also be available from: </p>
<p> <a rel="nofollow" href="http://auricle.dyndns.org/ALE/manuals/">http://auricle.dyndns.org/ALE/manuals/</a> </p>
<h2>Index</h2>
