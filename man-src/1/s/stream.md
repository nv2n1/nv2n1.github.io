---
title: "stream(1)"
name: "stream"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stream/"
description: "stream – a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats."
---

<h2 class="name">NAME</h2>
<p> stream &#8211; a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>stream-im6.q16</code> [<i>options</i>] <i>input-file</i> <i>output-file</i></p>
<dd></dl>
<h2>OVERVIEW</h2>
<p> <code>Stream</code> is a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats. It writes the pixel components as they are read from the input image a row at a time making <code>stream-im6.q16</code> desirable when working with large images or when you require raw pixel components. </p>
<p> For more information about the stream command, point your browser to file:///usr/share/doc/imagemagick-6-common/html/www/stream.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/stream.php.">https://www.imagemagick.org/script/stream.php.</a></p>
<h2>DESCRIPTION</h2>
<p> Image Settings:<br />
&nbsp;<wbr>&nbsp;-authenticate value&nbsp;<wbr>&nbsp;decrypt image with this password<br />
&nbsp;<wbr>&nbsp;-channel type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply option to select image channels<br />
&nbsp;<wbr>&nbsp;-colorspace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alternate image colorspace<br />
&nbsp;<wbr>&nbsp;-compress type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of pixel compression when writing the image<br />
&nbsp;<wbr>&nbsp;-define format:option<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;define one or more image format options<br />
&nbsp;<wbr>&nbsp;-density geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical density of the image<br />
&nbsp;<wbr>&nbsp;-depth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image depth<br />
&nbsp;<wbr>&nbsp;-extract geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extract area from image<br />
&nbsp;<wbr>&nbsp;-identify&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;identify the format and characteristics of the image<br />
&nbsp;<wbr>&nbsp;-interlace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of image interlacing scheme<br />
&nbsp;<wbr>&nbsp;-interpolate method&nbsp;<wbr>&nbsp;pixel color interpolation method<br />
&nbsp;<wbr>&nbsp;-limit type value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pixel cache resource limit<br />
&nbsp;<wbr>&nbsp;-map components&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;one or more pixel components<br />
&nbsp;<wbr>&nbsp;-monitor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;monitor progress<br />
&nbsp;<wbr>&nbsp;-quantize colorspace reduce colors in this colorspace<br />
&nbsp;<wbr>&nbsp;-quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suppress all warning messages<br />
&nbsp;<wbr>&nbsp;-regard-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pay attention to warning messages<br />
&nbsp;<wbr>&nbsp;-respect-parentheses settings remain in effect until parenthesis boundary<br />
&nbsp;<wbr>&nbsp;-sampling-factor geometry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical sampling factor<br />
&nbsp;<wbr>&nbsp;-seed value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seed a new sequence of pseudo-random numbers<br />
&nbsp;<wbr>&nbsp;-set attribute value set an image attribute<br />
&nbsp;<wbr>&nbsp;-size geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;width and height of image<br />
&nbsp;<wbr>&nbsp;-storage-type type&nbsp;<wbr>&nbsp;<wbr>&nbsp;pixel storage type<br />
&nbsp;<wbr>&nbsp;-synchronize&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronize image to storage device<br />
&nbsp;<wbr>&nbsp;-taint&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;declare the image as modified<br />
&nbsp;<wbr>&nbsp;-transparent-color color<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent color<br />
&nbsp;<wbr>&nbsp;-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print detailed information about the image<br />
&nbsp;<wbr>&nbsp;-virtual-pixel method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;virtual pixel access method </p>
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
<p> <code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/license.php">https://www.imagemagick.org/script/license.php</a></code> </p>
<h2>Index</h2>
