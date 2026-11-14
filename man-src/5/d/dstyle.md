---
title: "dstyle(5)"
name: "dstyle"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dstyle/"
description: "dstyle – format of .dstyle files (display styles)"
---

<p>dstyle &#8211; format of .dstyle files (display styles)</p>
<h2>Description</h2>
<p>Display styles indicate how to render information on a screen. Each style describes one way of rendering information, for example as a solid area in red or as a dotted outline in purple. Different styles correspond to mask layers, highlights, labels, menus, window borders, and so on. See &#8220;Magic Maintainer&#8217;s Manual #3: Display Styles, Color Maps, and Glyphs&#8221; for more information on how the styles are used. </p>
<p> Dstyle files usually have names of the form <i>x</i><code>.</code><i>y</i><code>.dstyle</code><i>n</i>, where <i>x</i> is a class of technologies, <i>y</i> is a class of displays, and <i>n</i> is a version number (currently <code>5</code>). The version number may increase in the future if the format of dstyle files changes. For example, the display style file <code>mos.7bit.dstyle5</code> provides all the rendering information for our nMOS and CMOS technologies for color displays with at least 7 bits of color. </p>
<p> Dstyle files are stored in ASCII as a series of lines. Lines beginning with &#8220;#&#8221; are considered to be comments and are ignored. The rest of the lines of the file are divided up into two sections separated by blank lines. There should not be any blank lines within a section.</p>
<h2>Display_Styles Section</h2>
<p>The first section begins with a line <code>display_styles</code> <i>planes</i> where <i>planes</i> is the number of bits of color information per pixel on the screen (between 1 and 8). Each line after that describes one display style and contains eight fields separated by white space: <i>style writeMask color outline fill stipple shortName longName</i> The meanings of the fields are:</p>
<dl>
<dt><i>style</i></p>
<dd>The number of this style, in decimal. Styles 1 through 64 are used to display mask layers in the edit cell. The style number(s) to use for each mask layer is (are) specified in the technology file. Styles 65-128 are used for displaying mask layers in non-edit cells. If style <i>x</i> is used for a mask layer in the edit cell, style <i>x</i>+64 is used for the same mask layer in non-edit cells. Styles above 128 are used by the Magic code for various things like menus and highlights. See the file <i>styles.h</i> in Magic for how styles above 128 are used. When redisplaying, the styles are drawn in order starting at 1, so the order of styles may affect what appears on the screen.</p>
<dt><i>writeMask</i></p>
<dd>This is an octal number specifying which bit-planes are to be modified when this style is rendered. For example, 1 means only information in bit-plane 0 will be affected, and 377 means all eight bit-planes are affected.</p>
<dt><i>color</i></p>
<dd>An octal number specifying the new values to be written into the bit-planes that are modified. This is used along with <i>writeMask</i> to determine the new value of each pixel that&#8217;s being modified: newPixel = (oldPixel &amp; ~writeMask) | (color &amp; writeMask) The red, green, and blue intensities displayed for each pixel are not deterimined directly by the value of the pixel; they come from a color map that maps the eight-bit pixel values into red, green, and blue intensities. Color maps are stored in separate files.</p>
<dt><i>outline</i></p>
<dd>If this field is zero, then no outline is drawn. If the field is non-zero, it specifies that outlines are to be drawn around the rectangular areas rendered in this style, and the octal value gives an eight-bit pattern telling how to draw the outline. For example, 377 means to draw a solid line, 252 means to draw a dotted line, 360 specifies long dashes, etc. This field only indicates <i>which</i> pixels will be modified: the <i>writeMask</i> and <i>color</i> fields indicate how the pixels are modified.</p>
<dt><i>fill</i></p>
<dd>This is a text string specifying how the areas drawn in this style should be filled. It must have one of the values <code>solid</code>, <code>stipple</code>, <code>cross</code>, <code>outline</code>, <code>grid</code>. <code>Solid</code> means that every pixel in the area is to modified according to <i>writeMask</i> and <i>color</i>. <code>Stipple</code> means that the area should be stippled: the stipple pattern given by <i>stipple</i> is used to determine which pixels in the area are to be modified. <code>Cross</code> means that an X is drawn in a solid line between the diagonally-opposite corners of the area being rendered. <code>Outline</code> means that the area should not be filled at all; only an outline is drawn (if specified by <i>outline</i>). <code>Grid</code> is a special style used to draw a grid in the line style given by <i>outline</i>. The styles <code>cross</code> and <code>stipple</code> may be supplemented with an outline by giving a non-zero <i>outline</i> field. The <code>outline</code> and <code>grid</code> styles don&#8217;t make sense without an an outline, and <code>solid</code> doesn&#8217;t make sense with an outline (since all the pixels are modified anyway).</p>
<dt><i>stipple</i></p>
<dd>Used when <i>fill</i> is <code>stipple</code> to specify (in decimal) the stipple number to use.</p>
<dt><i>shortName</i></p>
<dd>This is a one-character name for this style. These names are used in the specification of glyphs and also in a few places in the Magic source code. Most styles have no short name; use a &#8220;-&#8221; in this field for them.</p>
<dt><i>longName</i></p>
<dd>A more human-readable name for the style. It&#8217;s not used at all by Magic.</dl>
<h2>Stipples Section</h2>
<p>The second section of a dstyle file is separated from the first by a blank line. The first line of the second section must be <code>stipples</code> and each additional line specifies one stipple pattern with the syntax <i>number pattern name</i> <i>Number</i> is a decimal number used to name the stipple in the <i>stipple</i> fields of style lines. <i>Number</i> must be no less than 1 and must be no greater than a device-dependent upper limit. Most devices support at least 15 stipple patterns. <i>Pattern</i> consists of eight octal numbers, each from 0-377 and separated by white space. The numbers form an 8-by-8 array of bits indicating which pixels are to be modified when the stipple is used. The <i>name</i> field is just a human-readable description of the stipple; it isn&#8217;t used by Magic.</p>
<h2>Files</h2>
<p>~cad/lib/magic/sys/mos.7bit.dstyle5</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-magic/">magic</a>(1), <a href="/docs/linux/man/5-cmap/">cmap</a>(5), <a href="/docs/linux/man/5-glyphs/">glyphs</a>(5) </p>
