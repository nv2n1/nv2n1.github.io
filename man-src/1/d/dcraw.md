---
title: "dcraw(1)"
name: "dcraw"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcraw/"
description: "dcraw – command-line decoder for raw digital photos"
---

<h2 class="name">NAME</h2>
<p> dcraw &#8211; command-line decoder for raw digital photos </p>
<h2>SYNOPSIS</h2>
<p> <code>dcraw</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>dcraw</code> decodes raw photos, displays metadata, and extracts thumbnails.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Print verbose messages, not just warnings and errors.</p>
<dt><code>-c</code></p>
<dd> Write decoded images or thumbnails to standard output.</p>
<dt><code>-e</code></p>
<dd> Extract the camera-generated thumbnail, not the raw image. You&#8217;ll get either a JPEG or a PPM file, depending on the camera.</p>
<dt><code>-z</code></p>
<dd> Change the access and modification times of an AVI, JPEG, TIFF or raw file to when the photo was taken, assuming that the camera clock was set to Universal Time.</p>
<dt><code>-i</code></p>
<dd> Identify files but don&#8217;t decode them. Exit status is 0 if <code>dcraw</code> can decode the last file, 1 if it can&#8217;t. <code>-i -v</code> shows metadata.</p>
<dt>
<dd> <code>dcraw</code> cannot decode JPEG files!!</dl>
<h2>REPAIR OPTIONS</h2>
<dl>
<dt><code>-I</code></p>
<dd> Read the raw pixels from standard input in CPU byte order with no header. Use <code>dcraw -E -4</code> to get the raw pixel values.</p>
<dt><code>-P deadpixels.txt</code></p>
<dd> Read the dead pixel list from this file instead of &quot;.badpixels&quot;. See <code>FILES</code> for a description of the format.</p>
<dt><code>-K darkframe.pgm</code></p>
<dd> Subtract a dark frame from the raw data. To generate a dark frame, shoot a raw photo with no light and do <code>dcraw -D -4 -j -t 0</code>.</p>
<dt><code>-k darkness</code></p>
<dd> When shadows appear foggy, you need to raise the darkness level. To measure this, apply <code>pamsumm -mean</code> to the dark frame generated above.</p>
<dt><code>-S saturation</code></p>
<dd> When highlights appear pink, you need to lower the saturation level. To measure this, take a picture of something shiny and do <code>dcraw -D -4 -j -c</code> photo.raw <code>| pamsumm -max</code></p>
<dt>
<dd> The default darkness and saturation are usually correct.</p>
<dt><code>-n noise_threshold</code></p>
<dd> Use wavelets to erase noise while preserving real detail. The best threshold should be somewhere between 100 and 1000.</p>
<dt><code>-C red_mag blue_mag</code></p>
<dd> Enlarge the raw red and blue layers by the given factors, typically 0.999 to 1.001, to correct chromatic aberration.</p>
<dt><code>-H 0</code></p>
<dd> Clip all highlights to solid white (default).</p>
<dt><code>-H 1</code></p>
<dd> Leave highlights unclipped in various shades of pink.</p>
<dt><code>-H 2</code></p>
<dd> Blend clipped and unclipped values together for a gradual fade to white.</p>
<dt><code>-H 3+</code></p>
<dd> Reconstruct highlights. Low numbers favor whites; high numbers favor colors. Try <code>-H 5</code> as a compromise. If that&#8217;s not good enough, do <code>-H 9</code>, cut out the non-white highlights, and paste them into an image generated with <code>-H 3</code>.</dl>
<h2>COLOR OPTIONS</h2>
<p> By default, <code>dcraw</code> uses a fixed white balance based on a color chart illuminated with a standard D65 lamp.</p>
<dl>
<dt><code>-w</code></p>
<dd> Use the white balance specified by the camera. If this is not found, print a warning and use another method.</p>
<dt><code>-a</code></p>
<dd> Calculate the white balance by averaging the entire image.</p>
<dt><code>-A left top width height</code></p>
<dd> Calculate the white balance by averaging a rectangular area. First do <code>dcraw -j -t 0</code> and select an area of neutral grey color.</p>
<dt><code>-r mul0 mul1 mul2 mul3</code></p>
<dd> Specify your own raw white balance. These multipliers can be cut and pasted from the output of <code>dcraw -v</code>.</p>
<dt><code>+M</code> or <code>-M</code></p>
<dd> Use (or don&#8217;t use) any color matrix from the camera metadata. The default is <code>+M</code> if <code>-w</code> is set, <code>-M</code> otherwise. This option only affects Olympus, Leaf, and Phase One cameras.</p>
<dt><code>-o [0-5]</code></p>
<dd> Select the output colorspace when the <code>-p</code> option is not used: </p>
<p> <code> 0</code> &nbsp;<wbr>&nbsp;<wbr>Raw color (unique to each camera)<br />
 <code> 1</code> &nbsp;<wbr>&nbsp;<wbr>sRGB D65 (default)<br />
 <code> 2</code> &nbsp;<wbr>&nbsp;<wbr>Adobe RGB (1998) D65<br />
 <code> 3</code> &nbsp;<wbr>&nbsp;<wbr>Wide Gamut RGB D65<br />
 <code> 4</code> &nbsp;<wbr>&nbsp;<wbr>Kodak ProPhoto RGB D65<br />
 <code> 5</code> &nbsp;<wbr>&nbsp;<wbr>XYZ</p>
<dt><code>-p camera.icm</code>&nbsp;<wbr>[&nbsp;<wbr><code>-o output.icm</code>&nbsp;<wbr>]</p>
<dd> Use ICC profiles to define the camera&#8217;s raw colorspace and the desired output colorspace (sRGB by default).</p>
<dt><code>-p embed</code></p>
<dd> Use the ICC profile embedded in the raw photo.</dl>
<h2>INTERPOLATION OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Show the raw data as a grayscale image with no interpolation. Good for photographing black-and-white documents.</p>
<dt><code>-D</code></p>
<dd> Same as <code>-d</code>, but with the original unscaled pixel values.</p>
<dt><code>-E</code></p>
<dd> Same as <code>-D</code>, but masked pixels are not cropped.</p>
<dt><code>-h</code></p>
<dd> Output a half-size color image. Twice as fast as <code>-q 0</code>.</p>
<dt><code>-q 0</code></p>
<dd> Use high-speed, low-quality bilinear interpolation.</p>
<dt><code>-q 1</code></p>
<dd> Use Variable Number of Gradients (VNG) interpolation.</p>
<dt><code>-q 2</code></p>
<dd> Use Patterned Pixel Grouping (PPG) interpolation.</p>
<dt><code>-q 3</code></p>
<dd> Use Adaptive Homogeneity-Directed (AHD) interpolation.</p>
<dt><code>-f</code></p>
<dd> Interpolate RGB as four colors. Use this if the output shows false 2&#215;2 meshes with VNG or mazes with AHD.</p>
<dt><code>-m number_of_passes</code></p>
<dd> After interpolation, clean up color artifacts by repeatedly applying a 3&#215;3 median filter to the R-G and B-G channels.</dl>
<h2>OUTPUT OPTIONS</h2>
<p> By default, <code>dcraw</code> writes PGM/PPM/PAM with 8-bit samples, a BT.709 gamma curve, a histogram-based white level, and no metadata.</p>
<dl>
<dt><code>-W</code></p>
<dd> Use a fixed white level, ignoring the image histogram.</p>
<dt><code>-b brightness</code></p>
<dd> Divide the white level by this number, 1.0 by default.</p>
<dt><code>-g power toe_slope</code></p>
<dd> Set the gamma curve, by default BT.709 (<code>-g 2.222 4.5</code>). If you prefer sRGB gamma, use <code>-g 2.4 12.92</code>. For a simple power curve, set the toe slope to zero.</p>
<dt><code>-6</code></p>
<dd> Write sixteen bits per sample instead of eight.</p>
<dt><code>-4</code></p>
<dd> Linear 16-bit, same as <code>-6 -W -g 1 1</code>.</p>
<dt><code>-T</code></p>
<dd> Write TIFF with metadata instead of PGM/PPM/PAM.</p>
<dt><code>-t [0-7,90,180,270]</code></p>
<dd> Flip the output image. By default, <code>dcraw</code> applies the flip specified by the camera. <code>-t 0</code> disables all flipping.</p>
<dt><code>-j</code></p>
<dd> For Fuji Super CCD cameras, show the image tilted 45 degrees. For cameras with non-square pixels, do not stretch the image to its correct aspect ratio. In any case, this option guarantees that each output pixel corresponds to one raw pixel.</p>
<dt><code>-s [0..N-1]</code> or <code>-s all</code></p>
<dd> If a file contains N raw images, choose one or &quot;all&quot; to decode. For example, Fuji Super CCD SR cameras generate a second image underexposed four stops to show detail in the highlights.</dl>
<h2>FILES</h2>
<dl>
<dt>:./.badpixels, ../.badpixels, ../../.badpixels, &#8230;</p>
<dd> List of your camera&#8217;s dead pixels, so that <code>dcraw</code> can interpolate around them. Each line specifies the column, row, and UNIX time of death for one pixel. For example: </p>
<pre>
 962   91 1028350000  # died between August 1 and 4, 2002
1285 1067 0           # don't know when this pixel died
</pre>
<p> These coordinates are before any cropping or rotation, so use <code>dcraw -j -t 0</code> to locate dead pixels.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), <code><a href="/docs/linux/man/1-pamsumm/">pamsumm</a></code>(1), <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1), <code><a href="/docs/linux/man/1-pnmtotiff/">pnmtotiff</a></code>(1), <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1), <code><a href="/docs/linux/man/1-gphoto2/">gphoto2</a></code>(1), <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Written by David Coffin, dcoffin a cybercom o net </p>
<h2>Index</h2>
