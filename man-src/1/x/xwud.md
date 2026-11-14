---
title: "xwud(1)"
name: "xwud"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xwud/"
description: "xwud – image displayer for X"
---

<h2 class="name">NAME</h2>
<p> xwud &#8211; image displayer for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xwud</code> [-in <i>file</i>] [-noclick] [-geometry <i>geom</i>] [-display <i>display</i>] [-new] [-std &lt;maptype&gt;] [-raw] [-vis &lt;vis-type-or-id&gt;] [-scale] [-help] [-rv] [-plane <i>number</i>] [-fg <i>color</i>] [-bg <i>color</i>] [-dumpheader] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xwud</i> is an X Window System image undumping utility. <i>Xwud</i> allows X users to display in a window an image saved in a specially formatted dump file, such as produced by <i><a href="/docs/linux/man/1-xwd/">xwd</a>(1)</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-bg </code><i>color</i></p>
<dd> If a bitmap image (or a single plane of an image) is displayed, this option can be used to specify the color to display for the &quot;0&quot; bits in the image.</dl>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option allows you to specify the server to connect to; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-dumpheader</code></p>
<dd> This option prints out the XWD header information only. Nothing is displayed.</dl>
<dl>
<dt><code>-fg </code><i>color</i></p>
<dd> If a bitmap image (or a single plane of an image) is displayed, this option can be used to specify the color to display for the &quot;1&quot; bits in the image.</dl>
<dl>
<dt><code>-geometry </code><i>geom</i></p>
<dd> This option allows you to specify the size and position of the window. Typically you will only want to specify the position, and let the size default to the actual size of the image.</dl>
<dl>
<dt><code>-help</code></p>
<dd> Print out a short description of the allowable options.</dl>
<dl>
<dt><code>-in </code><i>file</i></p>
<dd> This option allows the user to explicitly specify the input file on the command line. If no input file is given, the standard input is assumed.</dl>
<dl>
<dt><code>-new</code></p>
<dd> This option forces creation of a new colormap for displaying the image. If the image characteristics happen to match those of the display, this can get the image on the screen faster, but at the cost of using a new colormap (which on most displays will cause other windows to go technicolor).</dl>
<dl>
<dt><code>-noclick</code></p>
<dd> Clicking any button in the window will terminate the application, unless this option is specified. Termination can always be achieved by typing &#8216;q&#8217;, &#8216;Q&#8217;, or ctrl-c.</dl>
<dl>
<dt><code>-plane </code><i>number</i></p>
<dd> You can select a single bit plane of the image to display with this option. Planes are numbered with zero being the least significant bit.</dl>
<dl>
<dt><code>-raw</code></p>
<dd> This option forces the image to be displayed with whatever color values happen to currently exist on the screen. This option is mostly useful when undumping an image back onto the same screen that the image originally came from, while the original windows are still on the screen, and results in getting the image on the screen faster.</dl>
<dl>
<dt><code>-rv</code></p>
<dd> If a bitmap image (or a single plane of an image) is displayed, this option forces the foreground and background colors to be swapped. This may be needed when displaying a bitmap image which has the color sense of pixel values &quot;0&quot; and &quot;1&quot; reversed from what they are on your display.</dl>
<dl>
<dt><code>-scale</code></p>
<dd> Allow the window to be resized, and scale the image to the size of the window.</dl>
<dl>
<dt><code>-std </code><i>maptype</i></p>
<dd> This option causes the image to be displayed using the specified Standard Colormap. The property name is obtained by converting the type to upper case, prepending &quot;RGB_&quot;, and appending &quot;_MAP&quot;. Typical types are &quot;best&quot;, &quot;default&quot;, and &quot;gray&quot;. See <i><a href="/docs/linux/man/1-xstdcmap/">xstdcmap</a>(1)</i> for one way of creating Standard Colormaps.</dl>
<dl>
<dt><code>-version</code></p>
<dd> This option causes <i>xwd</i> to print its version information and exit.</dl>
<dl>
<dt><code>-vis </code><i>vis-type-or-id</i></p>
<dd> This option allows you to specify a particular visual or visual class. The default is to pick the &quot;best&quot; one. A particular class can be specified: &quot;StaticGray&quot;, &quot;GrayScale&quot;, &quot;StaticColor&quot;, &quot;PseudoColor&quot;, &quot;DirectColor&quot;, or &quot;TrueColor&quot;. Or &quot;Match&quot; can be specified, meaning use the same class as the source image. Alternatively, an exact visual id (specific to the server) can be specified, either as a hexadecimal number (prefixed with &quot;0x&quot;) or as a decimal number. Finally, &quot;default&quot; can be specified, meaning to use the same class as the colormap of the root window. Case is not significant in any of these strings.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> To get default display.</dl>
<h2>FILES</h2>
<dl>
<dt><code>XWDFile.h</code></p>
<dd> X Window Dump File format definition file.</dl>
<h2>BUGS</h2>
<p> xwud doesn&#8217;t handle big/deep images very well on servers that don&#8217;t have the BIG-REQUESTS extension.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xwd/">xwd</a>(1), <a href="/docs/linux/man/1-xstdcmap/">xstdcmap</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>AUTHOR</h2>
<p> Bob Scheifler, MIT X Consortium </p>
<h2>Index</h2>
