---
title: "cmap(5)"
name: "cmap"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cmap/"
description: "cmap – format of .cmap files (color maps)"
---

<p>cmap &#8211; format of .cmap files (color maps)</p>
<h2>Description</h2>
<p>Color-map files define the mapping between eight-bit color numbers and red, green and blue intensities used for those numbers. They are read by Magic as part of system startup, and also by the <code>:load</code> and <code>:save</code> commands in color-map windows. Color-map file names usually have the form <i>x</i><code>.</code><i>y</i><code>.</code><i>z</i><code>.cmap</code><i>n</i>, where <i>x</i> is a class of technology files, <i>y</i> is a class of displays, <i>z</i> is a class of monitors, and <i>n</i> is a version number (currently <code>1</code>). The version number will change in the future if the formap of color-map files ever changes. Normally, <i>x</i> and <i>y</i> correspond to the corresponding parts of a display styles file. For example, the color map file <code>mos.7bit.std.cmap1</code> is used today for most nMOS and CMOS technology files using displays that support at least seven bits of color per pixel and standard-phosphor monitors. It corresponds to the display styles file <code>mos.7bit.dstyle5</code>. Color-map files are stored in ASCII form, with each line containing four decimal integers separated by white space. The first three integers are red, green, and blue intensities, and the fourth field is a color number. For current displays the intensities must be integers between 0 and 255. The color numbers must increase from line to line, and the last line must have a color number of 255. The red, green, and blue intensities on the first line are used for all colors from 0 up to and including the color number on that line. For other lines, the intensities on that line are used for all colors starting one color above the color number on the previous line and continuing up and through the color number on the current line. For example, consider the color map below: </p>
<pre>255 0 0 2
0 0 255 3
255 255 255256</pre>
<p>This color map indicates that colors 0, 1, and 2 are to be red, color 3 is to be blue, and all other colors are to be white. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-magic/">magic</a>(1), <a href="/docs/linux/man/5-dstyle/">dstyle</a>(5) </p>
