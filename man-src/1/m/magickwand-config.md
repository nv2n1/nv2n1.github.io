---
title: "magickwand-config(1)"
name: "magickwand-config"
section: "1"
letter: "m"
url: "/docs/linux/man/1-magickwand-config/"
description: "MagickWand-config – get information about the installed version of the Magick Wand"
---

<p>MagickWand-config &#8211; get information about the installed version of the Magick Wand</p>
<h2>Synopsis</h2>
<p><code>MagickWand-config </code> <code>[&#8211;cflags]</code> <code>[&#8211;cppflags]</code> <code>[&#8211;exec-prefix]</code> <code>[&#8211;ldflags]</code> <code>[&#8211;libs]</code> <code>[&#8211;prefix]</code> <code>[&#8211;version]</code></p>
<h2>Description</h2>
<p><code>MagickWand-config</code> prints the compiler and linker flags required to compile and link programs that use the <code>Wand</code> Application Programmer Interface.</p>
<h2>Examples</h2>
<p>To print the version of the installed distribution of <code>Wand</code>, use: </p>
<pre> MagickWand-config --version</pre>
<p>&nbsp;<wbr>&nbsp;<wbr> To compile a program that calls the <code>Wand</code> Application Programmer Interface, use: </p>
<pre> cc `MagickWand-config --cflags --cppflags --ldflags --libs` program.c</pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;cflags</code></p>
<dd>Print the compiler flags that were used to compile <code>libWand</code>.</p>
<dt><code>&#8211;cppflags</code></p>
<dd>Print the preprocessor flags that are needed to find the <code>Wand</code> C include files and defines to ensure that the Wand data structures match between your program and the installed libraries.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd>Print the directory under which target specific binaries and executables are installed.</p>
<dt><code>&#8211;ldflags</code></p>
<dd>Print the linker flags that are needed to link with the <code>Wand</code> library.</p>
<dt><code>&#8211;libs</code></p>
<dd>Print the linker flags that are needed to link a program with <code>libWand</code>.</p>
<dt><code>&#8211;version</code></p>
<dd>Print the version of the <code>Wand</code> distribution to standard output.</dl>
<h2>Copyright</h2>
<p>See <a rel="nofollow" href="http://www.imagemagick.org/script/license.php">http://www.imagemagick.org/script/license.php</a></p>
<h2>Authors</h2>
<p>John Cristy, ImageMagick Studio LLC</p>
