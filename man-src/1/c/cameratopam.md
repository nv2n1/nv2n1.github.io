---
title: "cameratopam(1)"
name: "cameratopam"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cameratopam/"
description: "cameratopam – convert raw camera image to PAM"
---

<h2 class="name">NAME</h2>
<p> cameratopam &#8211; convert raw camera image to PAM</p>
<h2>SYNOPSIS</h2>
<p> <code>cameratopam</code> </p>
<p> [<i>input_file_name</i>] </p>
<p> [<code>-identify_only</code>] [<code>-quick_interpolate</code>] [<code>-half_size</code>] [<code>-four_color_rgb</code>] [<code>-document_mode</code>] [<code>-balance_auto</code>] [<code>-balance_camera</code>] [<code>-red_scale=</code><i>float</i>] [<code>-blue_scale=</code><i>float</i>] [<code>-bright=</code><i>fraction</i>] [<code>-no_clip_color</code>] [<code>-rgb</code>] [<code>-use_secondary</code>] [<code>-linear</code>] [<code>-verbose</code>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>cameratopam</code> converts from any of dozens of raw camera image formats to PAM. </p>
<p> Digital still cameras often can produce images in a special raw format in addition to something more standard such as TIFF or JFIF (JPEG). Software supplied with the camera allows you to manipulate the image using information which is lost when the camera converts to the common format. A particular camera model often has a unique raw format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-identify_only</code></p>
<dd> Report to Standard Error the format of the input image but don&#8217;t generate an output image. Program fails if it cannot recognize the format. </p>
<dt><code>-verbose</code></p>
<dd> Report to Standard Error details of the processing. </p>
<dt><code>-quick_interpolate</code></p>
<dd> Use simple bilinear interpolation for quick results. The default is to use a slow, high-quality adaptive algorithm. </p>
<dt><code>-half_size</code></p>
<dd> Half-size the output image. Instead of interpolating, reduce each 2&#215;2 block of sensors to one pixel. Much faster than <code>-quick_interpolate</code>. </p>
<dt><code>-four_color_rgb</code></p>
<dd> Interpolate RGB as four colors. This causes a slight loss of detail, so use this only if you see false 2&#215;2 mesh patterns in blue sky. </p>
<dt><code>-document_mode</code></p>
<dd> Show the raw data as a grayscale image with no interpolation. This is good for photographing black and white documents. </p>
<dt><code>-balance_auto</code></p>
<dd> Automatic color balance. The default is to use a fixed color balance based on a white card photographed in sunlight. </p>
<dt><code>-balance_camera</code></p>
<dd> Use the color balance specified by the camera. If <code>cameratopam</code> can&#8217;t find this, it prints a warning and reverts to the default. </p>
<dt><code>-red_scale=</code><i>float</i></p>
<dd>
<dt><code>-blue_scale</code><i>float</i></p>
<dd> Further adjust the color balance by multiplying the red and blue channels by these values. Both default to 1.0. </p>
<dt><code>-bright=</code><i>float</i></p>
<dd> Change the output brightness. Default is 1.0. </p>
<dt><code>-no_clip_color</code></p>
<dd> By default, <code>cameratoapm</code> clips all colors to prevent pink hues in the highlights. Combine this option with <code>-bright=0.25</code> to leave the image data completely unclipped. </p>
<dt><code>-rgb</code></p>
<dd> Write raw camera colors to the output file. By default, <code>cameratoapm</code> converts to sRGB colorspace. </p>
<dt><code>-use_secondary</code></p>
<dd> For cameras based on the Fuji Super CCD SR, this option causes <code>cameratopam</code> to use the secondary sensors, in effect underexposing the image by four stops to reveal detail in the highlights. <code>cameratopam</code> silently ignores this option for all other cameras. </p>
<dt><code>-linear</code></p>
<dd> This option causes <code>cameratopam</code> to generate a variation on PAM that has &#8216;linear&#8217; color samples. In true PAM, each sample in the image raster is gamma-corrected; i.e. it is essentially proportional to brightness. With the <code>linear</code> option, <code>cameratopam</code> generates an image in which the samples are instead proportional to light intensity. </p>
<p> Without <code>-linear</code>, the image maxval is 255, so the image contains one byte per sample. With <code>-linear</code>, the maxval is 65535, so the image contains two bytes per sample. </p>
<p> Without <code>-linear</code>, <code>cameratopam</code> uses a 99th percentile white point. With <code>-linear</code>, it doesn&#8217;t. I don&#8217;t know what that means. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-411toppm/">411toppm</a></code>(1) , <code><a href="/docs/linux/man/1-pamflip/">pamflip</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>cameratopam</code> was new in Netpbm 10.28 (June 2005). </p>
<p> It was derived from the program <code>dcraw</code> by Dave Coffin , by Bryan Henderson in April 2005. Bryan replaced the part that generates the Netpbm output image and removed the Adobe Photoshop output function. Bryan changed the command syntax and made other small changes to make the program consistent with Netpbm. He also split the source code into manageable pieces (<code>dcraw</code> has a single 5000 line source file). </p>
<h2>Index</h2>
