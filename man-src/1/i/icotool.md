---
title: "icotool(1)"
name: "icotool"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icotool/"
description: "icotool – Convert and create Win32 icon and cursor files"
---

<h2 class="name">NAME</h2>
<p> icotool &#8211; Convert and create Win32 icon and cursor files </p>
<h2>SYNOPSIS</h2>
<p> <code>icotool</code> [<i>OPTION</i>]&#8230;<i> </i>[<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page document describes the <code>icotool</code> command. </p>
<p> The <code>icotool</code> program converts and creates icon (.ico) and cursor (.cur) files. At the moment icons can only be created from and extracted into PNG files. This is done using libpng. </p>
<p> Icon and cursor files are used mainly on the Microsoft Windows(R) platform. Each icons or cursors file may contain multiple images of various resolutions and with different number of colors. Cursor files differ from icon files in that they also contain information about the hotspot of each image. </p>
<p> Recent versions of Microsoft&#8217;s Internet Explorer use icons for small site logotypes. The browser fetches a file called favicon.ico from a web site, and uses the images in this file to represent the site in menus and site lists. (This file is placed in the web site&#8217;s root directory, like any other file.) Browsers like Galeon have copied this behaviour and now also fetches .ico files and use them for site logotypes. </p>
<p> As each icon or cursor file may contains multiple images of different dimensions and depth, a conversion may result in multiple PNG files being created. Correspondingly, multiple PNG files can be specified when creating an icon/cursor file.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-x, &#8211;extract</code></p>
<dd> This option tells icotool that images from all icon/cursor files given on the command line are to be extracted. Filter options (see below) can be used to control what images that will be extracted.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> This options tells icotool that images in all given icon/cursor files are to be listed. The output will look something like this: </p>
<p>&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=1 &#8211;width=16 &#8211;height=16 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=2 &#8211;width=32 &#8211;height=32 &#8211;bit-depth=8 &#8211;palette-size=256</p>
<dt><code>-c, &#8211;create</code></p>
<dd> This options tells icotool to create an icon/cursor file using all the PNG files given on the command line, in the order they were specified. The number of bits per pixel used in the icon/cursor file will depend on the number of colors used in the PNG file. (If the PNG image has an indexed palette, it doesn&#8217;t necessarily mean that the same palette will be used in the created icon/cursor file.)</p>
<dt><code>-i, &#8211;index=</code><i>N</i></p>
<dd> When listing or extracing files, this options tell icotool to list or extract only the N&#8217;th image in each file. The first image has index 1. </p>
<p> This option has no effect in create mode.</p>
<dt><code>-w, &#8211;width=</code><i>PIXELS</i></p>
<dd> Similar to &#8211;index, but this option allows the image width to be matched instead. This option has no effect in create mode.</p>
<dt><code>-h, &#8211;height=</code><i>PIXELS</i></p>
<dd> Similar to &#8211;index, but this option allows the image height to be matched instead. This option has no effect in create mode.</p>
<dt><code>-b, &#8211;bit-depth=</code><i>COUNT</i></p>
<dd> Similar to &#8211;index, but this option allows the number of bits per pixel in the image to be matched instead. Valid values are 1, 2, 4, 8, 16, 24 and 32. </p>
<p> In create mode, this option will allow you to specify a minimum bit depth for images in the icon file. If you provide the option once it will apply to all input files. If you specify it multiple times, it will apply to all input files following a particular option; in that case you should specify a bit depth for all images.</p>
<dt><code>-p, &#8211;palette-size=</code><i>PIXELS</i></p>
<dd> Similar to &#8211;index, but this option allows the number of colors in the image palette to be matched instead. Images with 24 or 32 bits in icon/cursor files do not have a palette, and will therefore have a palette size equal to 0. </p>
<p> This option has no effect in create mode.</p>
<dt><code>-X, &#8211;hotspot-x=</code><i>COORD</i></p>
<dd> Similar to &#8211;index, but this option allows the x-coordinate of the hotspot to be matched. This option only has effect on cursor files. </p>
<p> In create mode, this can be used to specify the hotspot x-coordinate. If you provide the option once it will apply to all input files. If you specify it multiple times, it will apply to all input files following a particular option; in that case you should specify a hotspot coordinate for all images.</p>
<dt><code>-Y, &#8211;hotspot-y=</code><i>COORD</i></p>
<dd> Similar to &#8211;index, but this option allows the y-coordinate of the hotspot to be matched. This option only has effect on cursor files. </p>
<p> In create mode, this can be used to specify the hotspot y-coordinate. If you provide the option once it will apply to all input files. If you specify it multiple times, it will apply to all input files following a particular option; in that case you should specify a hotspot coordinate for all images.</p>
<dt><code>&#8211;icon</code></p>
<dd> This option specifies that only icon files are to be listed or extracted. In create mode, this option can be used to specify that an icon (instead of a cursor) is to be created. (This is default in create mode.)</p>
<dt><code>&#8211;cursor</code></p>
<dd> This option specifies that only cursor files are to be listed or extracted. In create mode, this can be used to specify that a cursor (instead of an icon) is to be created.</p>
<dt><code>-t, &#8211;alpha-threshold=</code><i>LEVEL</i></p>
<dd> Specifies the maximal alpha level in the PNG image for portions which shall become transparent in the icon created. The default value is 127. This is only used when creating icon files.</p>
<dt><code>-o, &#8211;output=</code><i>PATH</i></p>
<dd> In extract mode, this option specifies a directory where extracted files are to be created. If PATH does not exist, it is assumed that it refers to a non-existing file instead. The first image matched will be extracted to the file with that name. </p>
<p> In create mode, this option specified the name of the output file. The default is to write the binary data to standard out (which icotool will refuse if standard out is the terminal). </p>
<p> If PATH is `-&#8216;, then all output will be printed to standard out. </p>
<p> This option has no effect in list mode.</p>
<dt><code>-r, &#8211;raw=FILENAME</code></p>
<dd> Store input file as raw PNG (Vista icons).</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> List all images in the file `demo.ico&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>icotool -l demo.ico</code><br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=1 &#8211;width=16 &#8211;height=16 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=2 &#8211;width=32 &#8211;height=32 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=3 &#8211;width=48 &#8211;height=48 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=4 &#8211;width=16 &#8211;height=16 &#8211;bit-depth=8 &#8211;palette-size=256<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=5 &#8211;width=32 &#8211;height=32 &#8211;bit-depth=8 &#8211;palette-size=256<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=6 &#8211;width=48 &#8211;height=48 &#8211;bit-depth=8 &#8211;palette-size=256 </p>
<p> List only 16-color images in `demo.ico&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>icotool -l &#8211;palette-size=16 demo.ico</code><br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=1 &#8211;width=16 &#8211;height=16 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=2 &#8211;width=32 &#8211;height=32 &#8211;bit-depth=4 &#8211;palette-size=16<br />
&nbsp;<wbr>&nbsp;&#8211;icon &#8211;index=3 &#8211;width=48 &#8211;height=48 &#8211;bit-depth=4 &#8211;palette-size=16 </p>
<p> Extract all images to current directory, naming the destination files `demo.ico_I_WxHxD.xpm&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>icotool -x -o . demo.ico</code><br />
&nbsp;<wbr>&nbsp;$&nbsp;<code>ls&nbsp;*.png</code><br />
&nbsp;<wbr>&nbsp;demo_1_16x16x4.png&nbsp;<wbr>&nbsp;demo_3_48x48x4.png&nbsp;<wbr>&nbsp;demo_5_32x32x8.png<br />
&nbsp;<wbr>&nbsp;demo_2_32x32x4.png&nbsp;<wbr>&nbsp;demo_4_16x16x8.png&nbsp;<wbr>&nbsp;demo_6_48x48x8.png </p>
<p> Extract all 256-color icon images in all .ico files in the current directory, placing the extracted images in `img/&#8217; </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>icotool -x -o img/&nbsp;-p 256&nbsp;*.ico</code> </p>
<p> Create an icon named `favicon.ico&#8217; with two images: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>icotool -c -o favicon.ico mysite_32x32.png mysite_64x64.png</code></p>
<h2>AUTHOR</h2>
<p> The <code>icoutils</code> were written by Oskar Liljeblad &lt;<i>oskar [at] osk.mine.nu</i>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>TRADEMARKS</h2>
<p> Windows is a registered trademark of Microsoft Corporation in the United States and other countries. </p>
<h2>Index</h2>
