---
title: "composite-im6(1)"
name: "composite-im6"
section: "1"
letter: "c"
url: "/docs/linux/man/1-composite-im6/"
description: "composite – overlaps one image over another."
---

<h2 class="name">NAME</h2>
<p> composite &#8211; overlaps one image over another. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>composite-im6.q16</code> <code>[</code> <i>options</i> <code>&#8230; ]</code> <i>change-file base-file</i> <code>[</code> <i>mask-file</i> <code>]</code> <i>output-image</i></p>
<dd></dl>
<h2>OVERVIEW</h2>
<p> The <code>composite-im6.q16</code> program is a member of the <a href="/docs/linux/man/1-imagemagick-ims6-q16/">ImageMagick-ims6.q16</a>(1) suite of tools. Use it to overlap one image over another. </p>
<p> For more information about the composite command, point your browser to file:///usr/share/doc/imagemagick-6-common/html/www/composite.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/script/composite.php.">http://imagemagick.org/script/composite.php.</a></p>
<h2>DESCRIPTION</h2>
<p> Image Settings:<br />
&nbsp;<wbr>&nbsp;-affine matrix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;affine transform matrix<br />
&nbsp;<wbr>&nbsp;-alpha option&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on, activate, off, deactivate, set, opaque, copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent, extract, background, or shape<br />
&nbsp;<wbr>&nbsp;-authenticate value&nbsp;<wbr>&nbsp;decrypt image with this password<br />
&nbsp;<wbr>&nbsp;-blue-primary point&nbsp;<wbr>&nbsp;chromaticity blue primary point<br />
&nbsp;<wbr>&nbsp;-channel type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply option to select image channels<br />
&nbsp;<wbr>&nbsp;-colorspace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alternate image colorspace<br />
&nbsp;<wbr>&nbsp;-comment string&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;annotate image with comment<br />
&nbsp;<wbr>&nbsp;-compose operator&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;composite operator<br />
&nbsp;<wbr>&nbsp;-compress type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of pixel compression when writing the image<br />
&nbsp;<wbr>&nbsp;-decipher filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;convert cipher pixels to plain pixels<br />
&nbsp;<wbr>&nbsp;-define format:option<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;define one or more image format options<br />
&nbsp;<wbr>&nbsp;-depth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image depth<br />
&nbsp;<wbr>&nbsp;-density geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical density of the image<br />
&nbsp;<wbr>&nbsp;-display server&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get image or font from this X server<br />
&nbsp;<wbr>&nbsp;-dispose method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;layer disposal method<br />
&nbsp;<wbr>&nbsp;-dither method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply error diffusion to image<br />
&nbsp;<wbr>&nbsp;-encipher filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;convert plain pixels to cipher pixels<br />
&nbsp;<wbr>&nbsp;-encoding type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;text encoding type<br />
&nbsp;<wbr>&nbsp;-endian type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;endianness&nbsp;(MSB or LSB)&nbsp;of the image<br />
&nbsp;<wbr>&nbsp;-filter type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;use this filter when resizing an image<br />
&nbsp;<wbr>&nbsp;-font name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;render text with this font<br />
&nbsp;<wbr>&nbsp;-format&nbsp;&quot;string&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;output formatted image characteristics<br />
&nbsp;<wbr>&nbsp;-gravity type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;which direction to gravitate towards<br />
&nbsp;<wbr>&nbsp;-green-primary point chromaticity green primary point<br />
&nbsp;<wbr>&nbsp;-interlace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of image interlacing scheme<br />
&nbsp;<wbr>&nbsp;-interpolate method&nbsp;<wbr>&nbsp;pixel color interpolation method<br />
&nbsp;<wbr>&nbsp;-label string&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assign a label to an image<br />
&nbsp;<wbr>&nbsp;-limit type value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pixel cache resource limit<br />
&nbsp;<wbr>&nbsp;-matte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;store matte channel if the image has one<br />
&nbsp;<wbr>&nbsp;-monitor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;monitor progress<br />
&nbsp;<wbr>&nbsp;-page geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size and location of an image canvas&nbsp;(setting)<br />
&nbsp;<wbr>&nbsp;-pointsize value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font point size<br />
&nbsp;<wbr>&nbsp;-quality value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;JPEG/MIFF/PNG compression level<br />
&nbsp;<wbr>&nbsp;-quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suppress all warning messages<br />
&nbsp;<wbr>&nbsp;-red-primary point&nbsp;<wbr>&nbsp;<wbr>&nbsp;chromaticity red primary point<br />
&nbsp;<wbr>&nbsp;-regard-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pay attention to warning messages<br />
&nbsp;<wbr>&nbsp;-repage geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size and location of an image canvas&nbsp;(operator)<br />
&nbsp;<wbr>&nbsp;-respect-parentheses settings remain in effect until parenthesis boundary<br />
&nbsp;<wbr>&nbsp;-sampling-factor geometry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical sampling factor<br />
&nbsp;<wbr>&nbsp;-scene value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image scene number<br />
&nbsp;<wbr>&nbsp;-seed value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seed a new sequence of pseudo-random numbers<br />
&nbsp;<wbr>&nbsp;-size geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;width and height of image<br />
&nbsp;<wbr>&nbsp;-support factor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resize support:&nbsp;&gt;&nbsp;1.0 is blurry,&nbsp;&lt;&nbsp;1.0 is sharp<br />
&nbsp;<wbr>&nbsp;-synchronize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronize image to storage device<br />
&nbsp;<wbr>&nbsp;-taint&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;declare the image as modified<br />
&nbsp;<wbr>&nbsp;-transparent-color color<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent color<br />
&nbsp;<wbr>&nbsp;-treedepth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;color tree depth<br />
&nbsp;<wbr>&nbsp;-tile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;repeat composite operation across and down image<br />
&nbsp;<wbr>&nbsp;-units type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the units of image resolution<br />
&nbsp;<wbr>&nbsp;-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print detailed information about the image<br />
&nbsp;<wbr>&nbsp;-virtual-pixel method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;virtual pixel access method<br />
&nbsp;<wbr>&nbsp;-white-point point&nbsp;<wbr>&nbsp;<wbr>&nbsp;chromaticity white point </p>
<p> Image Operators:<br />
&nbsp;<wbr>&nbsp;-blend geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blend images<br />
&nbsp;<wbr>&nbsp;-border geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;surround image with a border of color<br />
&nbsp;<wbr>&nbsp;-bordercolor color&nbsp;<wbr>&nbsp;<wbr>&nbsp;border color<br />
&nbsp;<wbr>&nbsp;-colors value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;preferred number of colors in the image<br />
&nbsp;<wbr>&nbsp;-displace geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;shift image pixels defined by a displacement map<br />
&nbsp;<wbr>&nbsp;-dissolve value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dissolve the two images a given percent<br />
&nbsp;<wbr>&nbsp;-distort geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shift lookup according to a absolute distortion map<br />
&nbsp;<wbr>&nbsp;-extract geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extract area from image<br />
&nbsp;<wbr>&nbsp;-geometry geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;location of the composite image<br />
&nbsp;<wbr>&nbsp;-identify&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;identify the format and characteristics of the image<br />
&nbsp;<wbr>&nbsp;-monochrome&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform image to black and white<br />
&nbsp;<wbr>&nbsp;-negate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replace each pixel with its complementary color&nbsp;<br />
&nbsp;<wbr>&nbsp;-profile filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;add ICM or IPTC information profile to image<br />
&nbsp;<wbr>&nbsp;-quantize colorspace reduce colors in this colorspace<br />
&nbsp;<wbr>&nbsp;-rotate degrees&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply Paeth rotation to the image<br />
&nbsp;<wbr>&nbsp;-resize geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resize the image<br />
&nbsp;<wbr>&nbsp;-sharpen geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sharpen the image<br />
&nbsp;<wbr>&nbsp;-shave geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shave pixels from the image edges<br />
&nbsp;<wbr>&nbsp;-stegano offset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hide watermark within an image<br />
&nbsp;<wbr>&nbsp;-stereo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;combine two image to create a stereo anaglyph<br />
&nbsp;<wbr>&nbsp;-strip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strip image of all profiles and comments<br />
&nbsp;<wbr>&nbsp;-thumbnail geometry&nbsp;<wbr>&nbsp;create a thumbnail of the image<br />
&nbsp;<wbr>&nbsp;-transform&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;affine transform image<br />
&nbsp;<wbr>&nbsp;-type type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image type<br />
&nbsp;<wbr>&nbsp;-unsharp geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sharpen the image<br />
&nbsp;<wbr>&nbsp;-watermark geometry&nbsp;<wbr>&nbsp;percent brightness and saturation of a watermark<br />
&nbsp;<wbr>&nbsp;-write filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write images to this file </p>
<p> Image Stack Operators:<br />
&nbsp;<wbr>&nbsp;-swap indexes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap two images in the image sequence </p>
<p> Miscellaneous Options:<br />
&nbsp;<wbr>&nbsp;-debug events&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display copious debugging information<br />
&nbsp;<wbr>&nbsp;-help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print program options<br />
&nbsp;<wbr>&nbsp;-log format&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;format of debugging information<br />
&nbsp;<wbr>&nbsp;-list type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print a list of supported option arguments<br />
&nbsp;<wbr>&nbsp;-version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print version information </p>
<p> By default, the image format of `file&#8217; is determined by its magic number. To specify a particular image format, precede the filename with an image format name and a colon (i.e. ps:image) or specify the image type as the filename suffix (i.e. image.ps). Specify &#8216;file&#8217; as &#8216;-&#8216; for standard input or output.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-imagemagick-im6-q16/">ImageMagick-im6.q16</a>(1) </p>
<h2>COPYRIGHT</h2>
<p> <code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/script/license.php">http://imagemagick.org/script/license.php</a></code> </p>
<h2>Index</h2>
