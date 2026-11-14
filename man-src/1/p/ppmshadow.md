---
title: "ppmshadow(1)"
name: "ppmshadow"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmshadow/"
description: "ppmshadow – add simulated shadows to a portable pixmap image"
---

<h2 class="name">NAME</h2>
<p> ppmshadow &#8211; add simulated shadows to a portable pixmap image </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmshadow</code> [<code>-b</code> <i>blur_size</i>] [<code>-k</code>] [<code>-t</code>] [<code>-x</code> <i>xoffset</i>] [<code>-y</code> <i>yoffset</i>] [<code>-u</code>] [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>ppmshadow</code> adds a simulated shadow to an image, giving the appearance that the contents of the image float above the page, casting a diffuse shadow on the background. Shadows can either be black, as cast by opaque objects, or translucent, where the shadow takes on the colour of the object which casts it. You can specify the extent of the shadow and its displacement from the image with command line options. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> blur_size</i></p>
<dd>
<p> Sets the distance of the light source from the image. Larger values move the light source closer, casting a more diffuse shadow, while smaller settings move the light further away, yielding a sharper shadow. <i>blur_size</i> defaults to 11 pixels.<br />
&nbsp;</p>
<dt><code>-k</code></p>
<dd> Keep the intermediate temporary image files. When debugging, these intermediate files provide many clues as to the source of an error. See <code>FILES </code> below for a list of the contents of each file.<br />
&nbsp;</p>
<dt><code>-t</code></p>
<dd> Consider the non-background material in the image translucent &#8212; it casts shadows of its own colour rather than a black shadow, which is default. This often results in fuzzy, difficult-to-read images but in some circumstances may look better.<br />
&nbsp;</p>
<dt><code>-u</code></p>
<dd> Print command syntax and a summary of options.<br />
&nbsp;</p>
<dt><code>-x</code><i> xoffset</i></p>
<dd> Specifies the displacement of the light source to the left of the image. Larger settings of <code>xoffset</code> displace the shadow to the right, as would be cast by a light further to the left. If not specified, the horizontal offset is half of <i>blur_size </i> (above), to the left.<br />
&nbsp;</p>
<dt><code>-y</code><i> yoffset</i></p>
<dd> Specifies the displacement of the light source above the top of the image. Larger settings displace the shadow downward, corresponding to moving the light further above the top of the image. If you don&#8217;t specify <code>-y</code>, the vertical offset defaults to the same as the horizontal offset (above), upward. </p>
</dl>
<h2>FILES</h2>
<p> Input is an anymap named by the <i>pnmfile</i> command line argument; if you don&#8217;t specify <i>pnmfile</i>, the input is the Standard Input file. </p>
<p> Output is a always a PPM file, written to Standard Output. </p>
<p> <code>pnmfile</code> creates a number of temporary files as it executes. It creates them in the /tmp directory, with names of the form: </p>
<p> <code>_PPMshadow</code><i>pid</i><code>&#8211;</code><i>N</i><code>.ppm</code> </p>
<p> where <i>pid</i> is the process number of the <code>ppmshadow</code> process and <i>N </i> is a number identifying the file as described below. In normal operation, <code>ppmshadow</code> deletes temporary files as soon as it is done with them and leaves no debris around after it completes. To preserve the intermediate files for debugging, use the <code>-k </code> command line option. </p>
<p> <i>N</i> in the filename means:</p>
<dl>
<dt><code>1</code></p>
<dd> Positive binary mask</p>
<dt><code>2</code></p>
<dd> Convolution kernel for blurring shadow</p>
<dt><code>3</code></p>
<dd> Blurred shadow image</p>
<dt><code>4</code></p>
<dd> Clipped shadow image, offset as requested</p>
<dt><code>5</code></p>
<dd> Blank image with background of source image</p>
<dt><code>6</code></p>
<dd> Offset shadow</p>
<dt><code>7</code></p>
<dd> Inverse mask file</p>
<dt><code>8</code></p>
<dd> Original image times inverse mask</p>
<dt><code>9</code></p>
<dd> Generated shadow times positive mask</p>
<dt><code>10</code></p>
<dd> Shadow times background colour </p>
</dl>
<h2>LIMITATIONS</h2>
<p> The source image must contain sufficient space on the edges in the direction in which the shadow is cast to contain the shadow &#8212; if it doesn&#8217;t some of the internal steps may fail. You can usually expand the border of a too-tightly-cropped image with <code>pnmmargin</code> before processing it with <code>ppmshadow</code>. </p>
<p> Black pixels and pixels with the same color as the image background don&#8217;t cast a shadow. If this causes unintentional &quot;holes&quot; in the shadow, fill the offending areas with a color which differs from black or the background by RGB values of 1, which will be imperceptible to the viewer. Since the comparison is exact, the modified areas will now cast shadows. </p>
<p> The background color of the source image (which is preserved in the output) is deemed to be the color of the pixel at the top left of the input image. If that pixel isn&#8217;t part of the background, simply add a one-pixel border at the top of the image, generate the shadow image, then delete the border from it. </p>
<p> If something goes wrong along the way, the error messages from the various Netpbm programs <code>ppmshadow</code> calls will, in general, provide little or no clue as to where <code>ppmshadow</code> went astray. In this case, Specify the <code>-k</code> option and examine the intermediate results in the temporary files (which this option causes to be preserved). If you manually run the commands that <code>ppmshadow</code> runs on these files, you can figure out where the problem is. In problem cases where you want to manually tweak the image generation process along the way, you can keep the intermediate files with the <code>-k </code> option, modify them appropriately with an image editor, then recombine them with the steps used by the code in <code>ppmshadow</code>. See the <code>ppmshadow.doc</code> document for additional details and examples of the intermediate files. </p>
<p> Shadows are by default black, as cast by opaque material in the image occluding white light. Use the <code>-t</code> option to simulate translucent material, where the shadow takes on the colour of the object that casts it. If the contrast between the image and background is insufficient, the <code>-t</code> option may yield unattractive results which resemble simple blurring of the original image. </p>
<p> Because Netpbm used to have a maximum maxval of 255, which meant that the largest convolution kernel <code>pnmconvol</code> could use was 11 by 11, <code>ppmshadow</code> includes a horrid, CPU-time-burning kludge which, if a blur of greater than 11 is requested, performs an initial convolution with an 11×11 kernel, then calls <code>pnmsmooth</code> (which is actually a script that calls pnmconvol with a 3×3 kernel) as many times as the requested blur exceeds 11. It&#8217;s ugly, but it gets the job done on those rare occasions where you need a blur greater than 11. </p>
<p> If you wish to generate an image at high resolution, then scale it to publication size with <code>pnmscale</code> in order to eliminate jagged edges by resampling, it&#8217;s best to generate the shadow in the original high resolution image, prior to scaling it down in size. If you scale first and then add the shadow, you&#8217;ll get an unsightly jagged stripe between the edge of material and its shadow, due to resampled pixels intermediate between the image and background obscuring the shadow. </p>
<h2>EXIT STATUS</h2>
<p> <code>ppmshadow</code> returns status 0 if processing was completed without errors, and a nonzero Unix error code if an error prevented generation of output. Some errors may result in the script aborting, usually displaying error messages from various Netpbm components it uses, without returning a nonzero error code. When this happens, the output file will be empty, so be sure to test this if you need to know if the program succeeded. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-pnmmargin/">pnmmargin</a></code>(1), <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> John Walker &lt;<a rel="nofollow" href="http://www.fourmilab.ch">http://www.fourmilab.ch</a>&gt; August 8, 1997</p>
<h2>COPYRIGHT</h2>
<p> This software is in the public domain. Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. </p>
<h2>Index</h2>
