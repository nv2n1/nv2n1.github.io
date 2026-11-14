---
title: "animate(1)"
name: "animate"
section: "1"
letter: "a"
url: "/docs/linux/man/1-animate/"
description: "animate – animates an image or image sequence on any X server."
---

<h2 class="name">NAME</h2>
<p> animate &#8211; animates an image or image sequence on any X server. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>animate-im6.q16</code> [<i>options</i>] <i>input-file</i></p>
<dd></dl>
<h2>OVERVIEW</h2>
<p> The <code>animate-im6.q16</code> program is a member of the <a href="/docs/linux/man/1-imagemagick-ims6-q16/">ImageMagick-ims6.q16</a>(1) suite of tools. Use it to animate an image or image sequence on any X server. </p>
<p> For more information about the animate command, point your browser to file:///usr/share/doc/imagemagick-6-common/html/www/animate.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/script/animate.php.">http://imagemagick.org/script/animate.php.</a></p>
<h2>DESCRIPTION</h2>
<p> Image Settings:<br />
&nbsp;<wbr>&nbsp;-alpha option&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on, activate, off, deactivate, set, opaque, copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent, extract, background, or shape<br />
&nbsp;<wbr>&nbsp;-authenticate value&nbsp;<wbr>&nbsp;decrypt image with this password<br />
&nbsp;<wbr>&nbsp;-backdrop&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display image centered on a backdrop<br />
&nbsp;<wbr>&nbsp;-channel type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply option to select image channels<br />
&nbsp;<wbr>&nbsp;-colormap type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Shared or Private<br />
&nbsp;<wbr>&nbsp;-colorspace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alternate image colorspace<br />
&nbsp;<wbr>&nbsp;-decipher filename&nbsp;<wbr>&nbsp;<wbr>&nbsp;convert cipher pixels to plain pixels<br />
&nbsp;<wbr>&nbsp;-define format:option<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;define one or more image format options<br />
&nbsp;<wbr>&nbsp;-delay centiseconds&nbsp;<wbr>&nbsp;display the next image after pausing<br />
&nbsp;<wbr>&nbsp;-density geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical density of the image<br />
&nbsp;<wbr>&nbsp;-depth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image depth<br />
&nbsp;<wbr>&nbsp;-display server&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display image to this X server<br />
&nbsp;<wbr>&nbsp;-dispose method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;layer disposal method<br />
&nbsp;<wbr>&nbsp;-dither method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply error diffusion to image<br />
&nbsp;<wbr>&nbsp;-filter type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;use this filter when resizing an image<br />
&nbsp;<wbr>&nbsp;-format&nbsp;&quot;string&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;output formatted image characteristics<br />
&nbsp;<wbr>&nbsp;-gamma value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;level of gamma correction<br />
&nbsp;<wbr>&nbsp;-geometry geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;preferred size and location of the Image window<br />
&nbsp;<wbr>&nbsp;-gravity type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical backdrop placement<br />
&nbsp;<wbr>&nbsp;-identify&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;identify the format and characteristics of the image<br />
&nbsp;<wbr>&nbsp;-immutable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displayed image cannot be modified<br />
&nbsp;<wbr>&nbsp;-interlace type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type of image interlacing scheme<br />
&nbsp;<wbr>&nbsp;-interpolate method&nbsp;<wbr>&nbsp;pixel color interpolation method<br />
&nbsp;<wbr>&nbsp;-limit type value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pixel cache resource limit<br />
&nbsp;<wbr>&nbsp;-loop iterations&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loop images then exit<br />
&nbsp;<wbr>&nbsp;-matte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;store matte channel if the image has one<br />
&nbsp;<wbr>&nbsp;-map type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display image using this Standard Colormap<br />
&nbsp;<wbr>&nbsp;-monitor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;monitor progress<br />
&nbsp;<wbr>&nbsp;-pause&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seconds to pause before reanimating<br />
&nbsp;<wbr>&nbsp;-page geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size and location of an image canvas&nbsp;(setting)<br />
&nbsp;<wbr>&nbsp;-quantize colorspace reduce colors in this colorspace<br />
&nbsp;<wbr>&nbsp;-quiet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suppress all warning messages<br />
&nbsp;<wbr>&nbsp;-regard-warnings&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pay attention to warning messages<br />
&nbsp;<wbr>&nbsp;-remote command&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execute a command in an remote display process<br />
&nbsp;<wbr>&nbsp;-repage geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size and location of an image canvas&nbsp;(operator)<br />
&nbsp;<wbr>&nbsp;-respect-parentheses settings remain in effect until parenthesis boundary<br />
&nbsp;<wbr>&nbsp;-sampling-factor geometry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;horizontal and vertical sampling factor<br />
&nbsp;<wbr>&nbsp;-scenes range&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;image scene range<br />
&nbsp;<wbr>&nbsp;-seed value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seed a new sequence of pseudo-random numbers<br />
&nbsp;<wbr>&nbsp;-set attribute value set an image attribute<br />
&nbsp;<wbr>&nbsp;-size geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;width and height of image<br />
&nbsp;<wbr>&nbsp;-support factor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resize support:&nbsp;&gt;&nbsp;1.0 is blurry,&nbsp;&lt;&nbsp;1.0 is sharp<br />
&nbsp;<wbr>&nbsp;-transparent-color color<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transparent color<br />
&nbsp;<wbr>&nbsp;-treedepth value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;color tree depth<br />
&nbsp;<wbr>&nbsp;-verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print detailed information about the image<br />
&nbsp;<wbr>&nbsp;-visual type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display image using this visual type<br />
&nbsp;<wbr>&nbsp;-virtual-pixel method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;virtual pixel access method<br />
&nbsp;<wbr>&nbsp;-window id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display image to background of this window </p>
<p> Image Operators:<br />
&nbsp;<wbr>&nbsp;-colors value&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;preferred number of colors in the image<br />
&nbsp;<wbr>&nbsp;-crop geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;preferred size and location of the cropped image<br />
&nbsp;<wbr>&nbsp;-extract geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extract area from image<br />
&nbsp;<wbr>&nbsp;-monochrome&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transform image to black and white<br />
&nbsp;<wbr>&nbsp;-resample geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;change the resolution of an image<br />
&nbsp;<wbr>&nbsp;-resize geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resize the image<br />
&nbsp;<wbr>&nbsp;-rotate degrees&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;apply Paeth rotation to the image<br />
&nbsp;<wbr>&nbsp;-strip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strip image of all profiles and comments<br />
&nbsp;<wbr>&nbsp;-thumbnail geometry&nbsp;<wbr>&nbsp;create a thumbnail of the image<br />
&nbsp;<wbr>&nbsp;-trim&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;trim image edges </p>
<p> Image Sequence Operators:<br />
&nbsp;<wbr>&nbsp;-coalesce&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;merge a sequence of images<br />
&nbsp;<wbr>&nbsp;-flatten&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flatten a sequence of images </p>
<p> Miscellaneous Options:<br />
&nbsp;<wbr>&nbsp;-debug events&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display copious debugging information<br />
&nbsp;<wbr>&nbsp;-help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print program options<br />
&nbsp;<wbr>&nbsp;-log format&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;format of debugging information<br />
&nbsp;<wbr>&nbsp;-list type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print a list of supported option arguments<br />
&nbsp;<wbr>&nbsp;-version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print version information </p>
<p> In addition to those listed above, you can specify these standard X resources as command line options: -background, -bordercolor, -borderwidth, -font, -foreground, -iconGeometry, -iconic, -name, -mattecolor, -shared-memory, or -title. </p>
<p> By default, the image format of `file&#8217; is determined by its magic number. To specify a particular image format, precede the filename with an image format name and a colon (i.e. ps:image) or specify the image type as the filename suffix (i.e. image.ps). Specify &#8216;file&#8217; as &#8216;-&#8216; for standard input or output. </p>
<p> Buttons:<br />
&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;press to map or unmap the Command widget</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-imagemagick-im6-q16/">ImageMagick-im6.q16</a>(1) </p>
<h2>COPYRIGHT</h2>
<p> <code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/script/license.php">http://imagemagick.org/script/license.php</a></code> </p>
<h2>Index</h2>
