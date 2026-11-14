---
title: "ppmfade(1)"
name: "ppmfade"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmfade/"
description: "ppmfade – generate a transition between two image files using special effects."
---

<h2 class="name">NAME</h2>
<p> ppmfade &#8211; generate a transition between two image files using special effects. </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmfade</code> [ <code>-f </code> <i>first.ppm</i> ] [ <code>-l </code> <i>last.ppm</i> ] [ <code>-mix</code>|<code>-spread</code>|<code>-shift</code>|<code>-relief</code>|<code>-oil</code>|<code>-edge</code>|<code>-bentley</code>|<code>-block</code> ] [ <code>-base </code> <i>name</i> ] </p>
<h2>DESCRIPTION</h2>
<p> This program generates a transition between either two input images or between one input image and black. You can use the 30 intermediate images generated to show a smooth transition between segments of a movie. The input and output images are in the Portable Pixmap (PPM) format. If you specify both input images, they should both be the same size. If you want to fade from black to an image, specify only the last image. If you want to fade from an image to black, specify only the first image. <code>ppmfade </code> names the resulting image files <i>base</i><code>.</code><i>nnnn</i> <code>.ppm</code>, where <i>nnnn </i> is a number varying between 0001 and 0030 and <i>base</i> is what you specify with via the <code>-base</code> option (default <code>fade</code>). </p>
<p> Another way to convert by steps from one image to another is morphing. You can use <code>xmorph</code> to do that. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f first.ppm</code></p>
<dd> This is the image file (PPM format) to be used at the beginning of the transition. If not specified, the fade will start from black.</p>
<dt><code>-l last.ppm</code></p>
<dd> This is the image file (PPM format) to be used at the ending of the transition. If not specified, the fade will end with black.</p>
<dt><code>-mix</code></p>
<dd> The two images are superimposed with the brightness of the first image decreasing from full to none and the brightness of the final image increasing from none to full. The transition is quadratic in brightness with faster transition in the beginning and slower at the end.</p>
<dt><code>-spread</code></p>
<dd> The pixels in the first image will be moved (spread) further and further from their original location and then moved into the proper location in the final image. This is the default transition.</p>
<dt><code>-shift</code></p>
<dd> The pixels in the first image will be shifted further and further horizontally from their original location and then moved into the proper location in the final image.</p>
<dt><code>-relief</code></p>
<dd> The first image is faded to a Laplacian relief filtered version of the first image. This is then faded to a Laplacian relief filtered version of the second image and finally faded to the final image.</p>
<dt><code>-oil</code></p>
<dd> The first image is faded to an &quot;oil transfer&quot; version of the first image. This is then faded to an &quot;oil transfer&quot; version of the second image and finally faded to the final image.</p>
<dt><code>-edge</code></p>
<dd> The first image is faded to an edge detected version of the first image. This is then faded to an edge detected version of the second image and finally faded to the final image.</p>
<dt><code>-bentley</code></p>
<dd> The first image is faded to a &quot;Bentley Effect&quot; version of the first image. This is then faded to a &quot;Bentley Effect&quot; version of the second image and finally faded to the final image.</p>
<dt><code>-block</code></p>
<dd> The first image is defocused to small blocks. The small blocks are converted to match a defocused version of the last image. The block version of the last image is then focused to the final image.</p>
<dt><code>-base</code><i>name</i></p>
<dd> This forms part of the output filenames, as described above.</p>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> <code>ppmfade -f teapot.ppm -l pyr.ppm</code> </p>
<p> Fade from teapot.ppm to pyr.ppm generating fade.0001.ppm to fade.0030.ppm using the &quot;spread&quot; transition. </p>
<p> <code>ppmfade -l teapot.ppm</code> </p>
<p> Fade from black to teapot.ppm generating fade.0001.ppm to fade.0030.ppm. </p>
<p> <code>ppmfade -f teapot.ppm -base end</code> </p>
<p> Fade from teapot.ppm to black generating end.0001.ppm to end.0030.ppm. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tontsc/">tontsc</a></code>(1), <code><a href="/docs/linux/man/1-sgifade/">sgifade</a></code>(1), <code><a href="/docs/linux/man/1-smart_vfr/">smart_vfr</a></code>(1), <code><a href="/docs/linux/man/1-xmorph/">xmorph</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), </p>
<h2>AUTHOR</h2>
<p> Wesley C. Barris (wesb [at] msc.edu)<br />
 Army High Performance Computing Research Center (AHPCRC)<br />
 Minnesota Supercomputer Center, Inc. </p>
<h2>Index</h2>
