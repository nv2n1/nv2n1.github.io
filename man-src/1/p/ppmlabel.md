---
title: "ppmlabel(1)"
name: "ppmlabel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmlabel/"
description: "ppmlabel – add text to a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmlabel &#8211; add text to a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmlabel</code> [<code>-angle</code> <i>angle</i>] [<code>-background</code> <code>transparent</code> | <i>colour</i>] [<code>-colour</code> <i>colour</i>] [<code>-file</code> <i>filename</i>] [<code>-size</code> <i>textsize</i>] [<code>-text</code> <i>&#8216;text </i> <i>string&#8217;</i>] [<code>-x</code> <i>column</i>] [<code>-y</code> <i>row</i>]<i> &#8230; </i> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ppmlabel</code> uses the text drawing facilities of <code>ppmdraw</code> to add text to a portable pixmap. The location, size, baseline angle, colour of the text and background colour (if any) are controlled by command line arguments. The text can be specified on the command line or read from files. Any number of separate text strings can be added by one invocation of <code>ppmlabel</code>, limited only by the maximum length of the command line. </p>
<p> If no <i>ppmfile</i> is specified, <code>ppmdraw</code> reads its input pixmap from standard input.</p>
<h2>OPTIONS</h2>
<p> The arguments on the <code>ppmlabel</code> command line are not options in the strict sense; they are commands which control the placement and appearance of the text being added to the input pixmap. They are executed left to right, and any number of arguments may appear. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<dl>
<dt><code>-angle</code><i> angle</i></p>
<dd> Sets the angle of the baseline of subsequent text. <i>angle</i> is specified as an integral number of degrees, measured counterclockwise from the row axis of the pixmap.</p>
<dt><code>-background transparent | </code><i>colour</i></p>
<dd> If the argument is <code>&#8220;</code>transparent<code>&#8221;,</code> text is drawn over the existing pixels in the pixmap. If a <i>colour</i> is given (see the <code>-colour</code> switch below for information on how to specify colours), rectangles enclosing subsequent text are filled with that colour.</p>
<dt><code>-colour</code><i> colour</i></p>
<dd> Sets the colour for subsequent text. The <i>colour</i> can be specified in five ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A name, assuming that a pointer to an X11-style colour names file was compiled in.</p>
<dt>&bull;</p>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</p>
<dt>&bull;</p>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</p>
<dt>&bull;</p>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</p>
<dt>&bull;</p>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.)</dl>
</dl>
<dt><code>-file</code><i> filename</i></p>
<dd> Reads text from the file <i>filename</i> and draws it on successive lines.</p>
<dt><code>-size</code><i> textsize</i></p>
<dd> Sets the height of the tallest characters above the baseline to <i>textsize</i> pixels.</p>
<dt><code>-text</code><i> &#8216;text string&#8217;</i></p>
<dd> Draws the given text string (which must be quoted if it contains spaces). The location for subsequent text is advanced by 1.75 times the current <i>textsize</i>, which allows drawing multiple lines of text in a reasonable manner without specifying the position of each line.</p>
<dt><code>-x</code><i> column</i></p>
<dd> Sets the column at which subsequent text will be left justified. Depending on the shape of the first character, the actual text may begin a few pixels to the right of this point.</p>
<dt><code>-y</code><i> row</i></p>
<dd> Sets the row which will form the baseline of subsequent text. Characters with descenders, such as &#8220;y&#8221;, will extend below this line.</dl>
<h2>BUGS</h2>
<p> Text strings are restricted to 7 bit ASCII. The text font used by <code>ppmdraw</code> doesn&#8217;t include definitions for 8 bit ISO 8859/1 characters. </p>
<p> When drawing multiple lines of text with a non-transparent background, it should probably fill the space between the lines with the background colour. This is tricky to get right when the text is rotated to a non-orthogonal angle. </p>
<p> The -size, -x, and -y options MUST precede the -text option specifying the string they apply to, or they will be silently ignored in favor of the defaults.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <center> Copyright (C) 1995 by John Walker (kelvin [at] fourmilab.ch)<br />
 WWW home page: <a rel="nofollow" href="http://www.fourmilab.ch/">http://www.fourmilab.ch/</a><br />
 </center> </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<h2>Index</h2>
