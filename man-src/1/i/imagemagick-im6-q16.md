---
title: "imagemagick-im6-q16(1)"
name: "imagemagick-im6-q16"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imagemagick-im6-q16/"
description: "ImageMagick – is a free software suite for the creation, modification and display of bitmap images."
---

<p>ImageMagick &#8211; is a free software suite for the creation, modification and display of bitmap images. </p>
<h2>Synopsis</h2>
<p><code>convert-im6.q16</code> <i>input-file</i> [<i>options</i>] <i>output-file</i></p>
<h2>Overview</h2>
<p>Use ImageMagick&#174; to create, edit, compose, or convert bitmap images. It can read and write images in a variety of formats (over 200) including PNG, JPEG, GIF, HEIC, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG. Use ImageMagick to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and B\[&#8216;e]zier curves. </p>
<p> The functionality of ImageMagick is typically utilized from the command-line or you can use the features from programs written in your favorite language. Choose from these interfaces: G2F (Ada), MagickCore (C), MagickWand (C), ChMagick (Ch), ImageMagickObject (COM+), Magick++ (C++), JMagick (Java), JuliaIO (Julia), L-Magick (Lisp), Lua (LuaJIT), NMagick (Neko/haXe), Magick.NET (.NET), PascalMagick (Pascal), PerlMagick (Perl), MagickWand for PHP (PHP), IMagick (PHP), PythonMagick (Python), magick (R), RMagick (Ruby), or TclMagick (Tcl/TK). With a language interface, use ImageMagick to modify or create images dynamically and automagically. </p>
<p> ImageMagick utilizes multiple computational threads to increase performance and can read, process, or write mega-, giga-, or tera-pixel image sizes. </p>
<p> ImageMagick is free software delivered as a ready-to-run binary distribution or as source code that you may use, copy, modify, and distribute in both open and proprietary applications. It is distributed under a derived Apache 2.0 license. </p>
<p> The ImageMagick development process ensures a stable API and ABI. Before each ImageMagick release, we perform a comprehensive security assessment that includes memory error, thread data race detection, and continuous fuzzing to help prevent security vulnerabilities. </p>
<p> The current release is ImageMagick 6.9.10-11. It runs on Linux, Windows, Mac Os X, iOS, Android OS, and others. </p>
<p> The authoritative ImageMagick version 6 web site is <a rel="nofollow" href="https://legacy.imagemagick.org.">https://legacy.imagemagick.org.</a> The authoritative source code repository is <a rel="nofollow" href="https://github.com/ImageMagick/ImageMagick6.">https://github.com/ImageMagick/ImageMagick6.</a> We maintain a source code mirror at <a rel="nofollow" href="https://gitlab.com/ImageMagick/ImageMagick6.">https://gitlab.com/ImageMagick/ImageMagick6.</a> </p>
<p> The design of ImageMagick is an evolutionary process, with the design and implementation efforts serving to influence and guide further progress in the other. With ImageMagick version 7 we aim to improve the design based on lessons learned from the version 6 implementation. </p>
<p> In the paragraphs below, find a short description for each command-line tool.Cl ick on the program name to get details on the program usage and a list of comman d-line options that alters how the program performs. If you are just getting acq uainted with ImageMagick, start at the top of the list, the convert program, and<br />
&nbsp;work your way down. Also be sure to peruse Anthony Thyssen&#8217;s tutorial on how to<br />
&nbsp;use ImageMagick utilities to convert, compose, or edit images from the command- line.</p>
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
<p> For more information about the ImageMagick, point your browser to file:///usr/share/doc/imagemagick-6-common/html/index.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/.">http://imagemagick.org/.</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-convert-im6-q16/">convert-im6.q16</a>(1), <a href="/docs/linux/man/1-identify-im6-q16/">identify-im6.q16</a>(1), <a href="/docs/linux/man/1-composite-im6-q16/">composite-im6.q16</a>(1), <a href="/docs/linux/man/1-montage-im6-q16/">montage-im6.q16</a>(1), <a href="/docs/linux/man/1-compare-im6-q16/">compare-im6.q16</a>(1), <a href="/docs/linux/man/1-display-im6-q16/">display-im6.q16</a>(1), <a href="/docs/linux/man/1-animate-im6-q16/">animate-im6.q16</a>(1), <a href="/docs/linux/man/1-import-im6-q16/">import-im6.q16</a>(1), <a href="/docs/linux/man/1-conjure-im6-q16/">conjure-im6.q16</a>(1), <a href="/docs/linux/man/5-quantize/">quantize</a>(5), <a href="/docs/linux/man/4-miff/">miff</a>(4) </p>
<h2>Copyright</h2>
<p><code>Copyright (C) 1999-2020 ImageMagick Studio LLC. Additional copyrights and licenses apply to this software, see file:///usr/share/doc/imagemagick-6-common/html/www/license.html (on debian system you may install the imagemagick-6 package) or <a rel="nofollow" href="http://imagemagick.org/script/license.php">http://imagemagick.org/script/license.php</a></code></p>
