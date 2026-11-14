---
title: "imagemagick(1)"
name: "imagemagick"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imagemagick/"
description: "ImageMagick – is a free software suite for the creation, modification and display of bitmap images."
---

<p>ImageMagick &#8211; is a free software suite for the creation, modification and display of bitmap images.</p>
<h2>Synopsis</h2>
<p><code>convert</code> <i>input-file</i> [<i>options</i>] <i>output-file</i></p>
<h2>Overview</h2>
<p>ImageMagick&#174;, is a software suite to create, edit, and compose bitmap images. It can read, convert and write images in a variety of formats (about 100) including GIF, JPEG, JPEG-2000, PNG, PDF, PhotoCD, TIFF, and DPX. Use ImageMagick to translate, flip, mirror, rotate, scale, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and B\[&#8216;e]zier curves. </p>
<p> ImageMagick is free software delivered as a ready-to-run binary distribution or as source code that you can freely use, copy, modify, and distribute. Its license is compatible with the GPL. It runs on all major operating systems. </p>
<p> The functionality of ImageMagick is typically utilized from the command line or you can use the features from programs written in your favorite programming language. Choose from these interfaces: MagickCore (C), MagickWand (C), ChMagick (Ch), Magick++ (C++), JMagick (Java), L-Magick (Lisp), PascalMagick (Pascal), PerlMagick (Perl), MagickWand for PHP (PHP), PythonMagick (Python), RMagick (Ruby), or TclMagick (Tcl/TK). With a language interface, use ImageMagick to modify or create images automagically and dynamically. </p>
<p> ImageMagick includes a number of command-line utilities for manipulating images. Most of you are probably accustom to editing images one at a time with a graphical user interface (GUI) with such programs as gimp or Photoshop. However, a GUI is not always convenient. Suppose you want to process an image dynamically from a web script or you want to apply the same operations to many images or repeat a specific operation at different times to the same or different image. For these types of operations, the command-line image processing utility is appropriate. </p>
<p> In the paragraphs below, find a short description for each command-line tool.Cl ick on the program name to get details on the program usage and a list of comman d-line options that alters how the program performs. If you are just getting acq uainted with ImageMagick, start at the top of the list, the convert program, and<br />
&nbsp;<wbr>work your way down. Also be sure to peruse Anthony Thyssen&#8217;s tutorial on how to<br />
&nbsp;<wbr>use ImageMagick utilities to convert, compose, or edit images from the command- line.</p>
<dl>
<dt><code>convert</code></p>
<dd>convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more.</p>
<dt><code>identify</code></p>
<dd>describes the format and characteristics of one or more image files.</p>
<dt><code>mogrify</code></p>
<dd>resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more. Mogrify overwrites the original image file, whereas, convert writes to a different image file.</p>
<dt><code>composite</code></p>
<dd>overlaps one image over another.</p>
<dt><code>montage</code></p>
<dd>create a composite image by combining several separate images. The images are tiled on the composite image optionally adorned with a border, frame, image name, and more.</p>
<dt><code>compare</code></p>
<dd>mathematically and visually annotate the difference between an image and its reconstruction.. </p>
<dt><code>stream</code></p>
<dd>is a lightweight tool to stream one or more pixel components of the image or portion of the image to your choice of storage formats. It writes the pixel components as they are read from the input image a row at a time making stream desirable when working with large images or when you require raw pixel components. </p>
<dt><code>display</code></p>
<dd>displays an image or image sequence on any X server.</p>
<dt><code>animate</code></p>
<dd>animates an image sequence on any X server.</p>
<dt><code>import</code></p>
<dd>saves any visible window on an X server and outputs it as an image file. You can capture a single window, the entire screen, or any rectangular portion of the screen.</p>
<dt><code>conjure</code></p>
<dd>interprets and executes scripts written in the Magick Scripting Language (MSL).</dl>
<p> For more information about the ImageMagick, point your browser to file:///usr/share/doc/ImageMagick-6.7.8/index.html or <a rel="nofollow" href="http://www.imagemagick.org/.">http://www.imagemagick.org/.</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-convert/">convert</a>(1), <a href="/docs/linux/man/1-identify/">identify</a>(1), <a href="/docs/linux/man/1-composite/">composite</a>(1), <a href="/docs/linux/man/1-montage/">montage</a>(1), <a href="/docs/linux/man/1-compare/">compare</a>(1), <a href="/docs/linux/man/1-display/">display</a>(1), <a href="/docs/linux/man/1-animate/">animate</a>(1), <a href="/docs/linux/man/1-import/">import</a>(1), <a href="/docs/linux/man/1-conjure/">conjure</a>(1), <a href="/docs/linux/man/5-quantize/">quantize</a>(5), <a href="/docs/linux/man/4-miff/">miff</a>(4) </p>
<h2>Copyright</h2>
<p><code>Copyright (C) 1999-2012 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/ImageMagick-6.7.8/www/license.html or <a rel="nofollow" href="http://www.imagemagick.org/script/license.php">http://www.imagemagick.org/script/license.php</a></code></p>
