---
title: "magick-config(1)"
name: "magick-config"
section: "1"
letter: "m"
url: "/docs/linux/man/1-magick-config/"
description: "Magick-config – get information about the installed version of ImageMagick"
---

<p>Magick-config &#8211; get information about the installed version of ImageMagick</p>
<h2>Synopsis</h2>
<p><code>Magick-config </code> <code>[&#8211;cflags]</code> <code>[&#8211;cppflags]</code> <code>[&#8211;exec-prefix]</code> <code>[&#8211;ldflags]</code> <code>[&#8211;libs]</code> <code>[&#8211;prefix]</code> <code>[&#8211;version]</code></p>
<h2>Description</h2>
<p><code>Magick-config</code> prints the compiler and linker flags required to compile and link programs that use the <code>ImageMagick</code> Application Programmer Interface.</p>
<h2>Examples</h2>
<p>To print the version of the installed distribution of <code>ImageMagick</code>, use: </p>
<pre> Magick-config --version</pre>
<p>&nbsp;<wbr>&nbsp;<wbr> To compile a program that calls the <code>ImageMagick</code> Application Programmer Interface, use: </p>
<pre> cc `Magick-config --cflags --cppflags --ldflags --libs` program.c</pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;cflags</code></dt>
<dd>Print the compiler flags that were used to compile <code>libMagick</code>.</dd>
<dt><code>&#8211;cppflags</code></dt>
<dd>Print the preprocessor flags that are needed to find the <code>ImageMagick</code> C include files and defines to ensure that the ImageMagick data structures match between your program and the installed libraries.</dd>
<dt><code>&#8211;exec-prefix</code></dt>
<dd>Print the directory under which target specific binaries and executables are installed.</dd>
<dt><code>&#8211;ldflags</code></dt>
<dd>Print the linker flags that are needed to link with the <code>ImageMagick</code> library.</dd>
<dt><code>&#8211;libs</code></dt>
<dd>Print the linker flags that are needed to link a program with <code>libMagick</code>.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print the version of the <code>ImageMagick</code> distribution to standard output.</dd></dl>
<h2>License</h2>
<p>See <a rel="nofollow" href="http://www.imagemagick.org/script/license.php.">http://www.imagemagick.org/script/license.php.</a></p>
<h2>Authors</h2>
<p>John Cristy, ImageMagick Studio LLC</p>
