---
title: "identify-im6-q16(1)"
name: "identify-im6-q16"
section: "1"
letter: "i"
url: "/docs/linux/man/1-identify-im6-q16/"
description: "identify – describes the format and characteristics of one or more image files."
---

<p>identify &#8211; describes the format and characteristics of one or more image files. </p>
<h2>Synopsis</h2>
<dl>
<dt><code>identify-im6.q16</code> [<i>options</i>] <i>input-file</i></p>
<dd></dl>
<h2>Overview</h2>
<p>The <code>identify-im6.q16</code> program is a member of the <a href="/docs/linux/man/1-imagemagick-ims6-q16/">ImageMagick-ims6.q16</a>(1) suite of tools. It describes the format and characteristics of one or more image files. It also reports if an image is incomplete or corrupt. The information returned includes the image number, the file name, the width and height of the image, whether the image is colormapped or not, the number of colors in the image (by default off use <i>-define unique=true</i> option), the number of bytes in the image, the format of the image (JPEG, PNM, etc.), and finally the number of seconds it took to read and process the image. Many more attributes are available with the verbose option. </p>
<p> For more information about the identify command, point your browser to file:///usr/share/doc/imagemagick-6-common/html/www/identify.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/identify.php.">https://www.imagemagick.org/script/identify.php.</a></p>
<h2>Description</h2>
<p>Image Settings:<br />
&nbsp;<wbr>&nbsp;-alpha option&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on, activate, off, deactivate, set, opaque, copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent, extract, background, or shape<br />
&nbsp;<wbr>&nbsp;-antialias&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;remove pixel-aliasing<br />
&nbsp;<wbr>&nbsp;-authenticate value&nbsp;<wbr>&nbsp;decrypt image with this password<br />
&nbsp;<wbr>&nbsp;-channel type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply option to select image channels<br />
&nbsp;<wbr>&nbsp;-clip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clip along the first path from the 8BIM profile<br />
&nbsp;<wbr>&nbsp;-clip-mask filename&nbsp;<wbr>&nbsp;associate a clip mask with the image<br />
&nbsp;<wbr>&nbsp;-clip-path id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clip along a named path from the 8BIM profile<br />
&nbsp;<wbr>&nbsp;-colorspace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alternate image colorspace<br />
&nbsp;<wbr>&nbsp;-crop geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cut out a rectangular region of the image<br />
&nbsp;<wbr>&nbsp;-define format:option<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;define one or more image format options<br />
&nbsp;<wbr>&nbsp;-define unique=true&nbsp;<wbr>&nbsp;return the number of unique colors in the image<br />
&nbsp;<wbr>&nbsp;-density geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical density of the image<br />
&nbsp;<wbr>&nbsp;-depth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image depth<br />
&nbsp;<wbr>&nbsp;-endian type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;endianness&nbsp;(MSB or LSB)&nbsp;of the image<br />
&nbsp;<wbr>&nbsp;-extract geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extract area from image<br />
&nbsp;<wbr>&nbsp;-features distance&nbsp;<wbr>&nbsp;<wbr>&nbsp;analyze image features&nbsp;(e.g. contrast, correlation)<br />
&nbsp;<wbr>&nbsp;-format&nbsp;&quot;string&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;output formatted image characteristics<br />
&nbsp;<wbr>&nbsp;-fuzz distance&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;colors within this distance are considered equal<br />
&nbsp;<wbr>&nbsp;-gamma value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of gamma correction<br />
&nbsp;<wbr>&nbsp;-interlace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of image interlacing scheme<br />
&nbsp;<wbr>&nbsp;-interpolate method&nbsp;<wbr>&nbsp;pixel color interpolation method<br />
&nbsp;<wbr>&nbsp;-limit type value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pixel cache resource limit<br />
&nbsp;<wbr>&nbsp;-list type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Color, Configure, Delegate, Format, Magic, Module,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Resource, or Type<br />
&nbsp;<wbr>&nbsp;-mask filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;associate a mask with the image<br />
&nbsp;<wbr>&nbsp;-matte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;store matte channel if the image has one<br />
&nbsp;<wbr>&nbsp;-moments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;report image moments<br />
&nbsp;<wbr>&nbsp;-monitor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;monitor progress<br />
&nbsp;<wbr>&nbsp;-ping&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;efficiently determine image attributes<br />
&nbsp;<wbr>&nbsp;-precision value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maximum number of significant digits to print<br />
&nbsp;<wbr>&nbsp;-quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suppress all warning messages<br />
&nbsp;<wbr>&nbsp;-regard-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pay attention to warning messages<br />
&nbsp;<wbr>&nbsp;-respect-parentheses settings remain in effect until parenthesis boundary<br />
&nbsp;<wbr>&nbsp;-sampling-factor geometry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical sampling factor<br />
&nbsp;<wbr>&nbsp;-seed value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seed a new sequence of pseudo-random numbers<br />
&nbsp;<wbr>&nbsp;-set attribute value set an image attribute<br />
&nbsp;<wbr>&nbsp;-size geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;width and height of image<br />
&nbsp;<wbr>&nbsp;-strip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strip image of all profiles and comments<br />
&nbsp;<wbr>&nbsp;-unique&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display the number of unique colors in the image<br />
&nbsp;<wbr>&nbsp;-units type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the units of image resolution<br />
&nbsp;<wbr>&nbsp;-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print detailed information about the image<br />
&nbsp;<wbr>&nbsp;-virtual-pixel method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;virtual pixel access method </p>
<p> Image Operators:<br />
&nbsp;<wbr>&nbsp;-grayscale method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convert image to grayscale<br />
&nbsp;<wbr>&nbsp;-negate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replace each pixel with its complementary color&nbsp; </p>
<p> Miscellaneous Options:<br />
&nbsp;<wbr>&nbsp;-debug events&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display copious debugging information<br />
&nbsp;<wbr>&nbsp;-help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print program options<br />
&nbsp;<wbr>&nbsp;-list type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print a list of supported option arguments<br />
&nbsp;<wbr>&nbsp;-log format&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;format of debugging information<br />
&nbsp;<wbr>&nbsp;-version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print version information </p>
<p> By default, the image format of `file&#8217; is determined by its magic number. To specify a particular image format, precede the filename with an image format name and a colon (i.e. ps:image) or specify the image type as the filename suffix (i.e. image.ps). Specify &#8216;file&#8217; as &#8216;-&#8216; for standard input or output.</p>
<h2>Note</h2>
<p>Although some options appear to modify the file to be identified, the identify command is strictly <code>read only</code>. For instance, the crop option crops the in-memory image and then describes the result. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-imagemagick-im6-q16/">ImageMagick-im6.q16</a>(1) </p>
<h2>Copyright</h2>
<p><code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="https://www.imagemagick.org/script/license.php">https://www.imagemagick.org/script/license.php</a></code></p>
