---
title: "fvwm-root(1)"
name: "fvwm-root"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-root/"
description: "fvwm-root – Sets the root window of the current X display to image"
---

<h2 class="name">NAME</h2>
<p> fvwm-root &#8211; Sets the root window of the current X display to image</p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-root</code> [<code>&#8211;retain-pixmap</code>|<code>-r</code>] [<code>&#8211;no-retain-pixmap</code>] [<code>&#8211;dummy</code>|<code>-d</code>] [<code>&#8211;no-dummy</code>] [<code>&#8211;dither</code>] [<code>&#8211;no-dither</code>] [<code>&#8211;color-limit</code> [<i>ncolors</i>] ] [<code>&#8211;no-color-limit</code>] [<code>&#8211;help</code>|<code>-h</code>|<code>-?</code>] [<code>&#8211;version</code>|<code>-V</code>] <i>image_file</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>fvwm-root</i> reads the image file specified in the command line and displays it in the root window. The supported image formats are <i>XBM</i>, <i>XPM</i>, <i>PNG</i> and <i>SVG</i> if appropriated libraries are compiled in. </p>
<p> SVG rendering options (as described in the <code> ICONS AND IMAGES </code> section of the main fvwm documentation) can be utilized. </p>
<h2>OPTIONS</h2>
<p> These command line options are recognized by fvwm-root:</p>
<dl>
<dt><code>&#8211;retain-pixmap</code> | <code>-r</code></p>
<dd> Causes fvwm-root to retain and publish the Pixmap with which the background has been set (the ESETROOT_PMAP_ID and _XROOTPMAP_ID properties are used). This is useful for applications which want to use the root Pixmap on the background to simulate transparency (for example, Eterm and Aterm use this method). This option should also be used for the RootTransparent colorset option, refer to the COLORSETS section of <a href="/docs/linux/man/1-fvwm/">fvwm</a>(1). If this option is not used, fvwm-root sets the _XSETROOT_ID property to None, and some programs, like fvwm modules, may use this to update their background if the background is transparent (Transparent colorset). </p>
<p> Note, a well behaved program, like fvwm, should listen to both _XSETROOT_ID and _XROOTPMAP_ID property changes and update itself correspondingly. However some programs listen only to one of them, so you should either use this option or not depending on what part is implemented by these programs. You should also use this option to get fast root-transparent menus in fvwm.</p>
<dt><code>&#8211;no-retain-pixmap</code></p>
<dd> This is a default. May be useful to explicitly force the default even if &quot;&#8211;retain-pixmap&quot; is specified earlier.</p>
<dt><code>&#8211;dummy</code> | <code>-d</code></p>
<dd> Causes fvwm-root NOT to set the background, but to only free a memory associated with the ESETROOT_PMAP_ID property (if any). In any case the _XSETROOT_ID property is set to None.</p>
<dt><code>&#8211;no-dummy</code></p>
<dd> This is a default. May be useful to explicitly force the default even if &quot;&#8211;dummy&quot; is specified earlier.</p>
<dt><code>&#8211;dither</code></p>
<dd> Causes fvwm-root to dither images for &quot;smoother&quot; rendition on displays with color depth of 16 or lower. This the defaut with color depth less or equal to 8.</p>
<dt><code>&#8211;no-dither</code></p>
<dd> Causes fvwm-root NOT to dither images. This is the default with color depth greater than 8.</p>
<dt><code>&#8211;color-limit </code><i>ncolors</i></p>
<dd> Causes fvwm-root to limit its color use to <i>ncolors</i> (if specified). This option is taken in account only with color depth less or equal to 8 (and a TrueColor or GrayScale visual). The default is to use the same color limit as fvwm. So in normal situation this option is not useful. However, if fvwm use a private colors map, as fvwm-root always use the default colors map you should use this option for limiting colors correctly. If <i>ncolors</i> is not specified a default is used.</p>
<dt><code>&#8211;no-color-limit</code></p>
<dd> Causes fvwm-root NOT to limit its color use.</p>
<dt><code>&#8211;help</code></p>
<dd> Shows a short usage.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows a version number. </p>
</dl>
<h2>COMPATIBILITY</h2>
<p> In the past this utility was called <i>xpmroot</i>. This name is still supported as a symlink. </p>
<h2>BUGS</h2>
<p> Repeated use of fvwm-root with different xpm pixmaps will use up slots in your color table pretty darn fast. </p>
<h2>AUTHOR</h2>
<p> Rob Nation </p>
<p> Rewritten and enhanced by fvwm-workers. </p>
<h2>Index</h2>
