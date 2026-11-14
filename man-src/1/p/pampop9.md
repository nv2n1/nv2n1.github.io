---
title: "pampop9(1)"
name: "pampop9"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pampop9/"
description: "pampop9 – simulate a multi-lens camera such as the Pop9"
---

<h2 class="name">NAME</h2>
<p> pampop9 &#8211; simulate a multi-lens camera such as the Pop9</p>
<h2>SYNOPSIS</h2>
<p> <code>pampop9</code> <i>pnmfile|-</i> <i>xtiles</i> <i>ytiles</i> <i>xdelta</i> <i>ydelta</i> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pampop9</code> tiles your starting image <i>xtiles</i> by <i>ytiles</i> times. Each of these tiles is taken from a slightly different offset within the source, as determined by the <i>xdelta</i> and <i>ydelta</i> arguments. </p>
<p> The top line of tiles in the output is taken from the top of the source image, the second starts with the <i>ydelta</i> row of the source image, the next with the 2*<i>ydelta</i> row, and so on. Similarly, the first column of tiles in the output is taken from the left of the source image, the next starts with the <i>xdelta</i> column, the next with the 2*<i>xdelta</i> column, and so on. </p>
<h2>EXAMPLES</h2>
<p> With a 100 x 100 source image, then the output image from <code>pampop9</code> <i>3 3 10 10</i> will appear to be a three-by-three grid, each tile being 80 x 80 pixels. If the origin is taken to be the top-left corner, then the top row of tiles will take start at (0, 0) (10, 0) (20, 0) within the source image, the middle row will start at (0, 10) (10, 10) (20, 10), and the bottom row at (0, 20) (10, 20) (20, 20). </p>
<h2>HISTORY</h2>
<p> <code>pampop9</code> was new in Netpbm 10.15 (April 2003). It was adapted slightly from <code>pampup9</code>, which was distributed by Robert Tinsley. At that time, it was distributed via <a rel="nofollow" href="http://www.thepoacher.net/code/#pampup9.">http://www.thepoacher.net/code/#pampup9.</a> By October 2004, that URL no longer was valid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtile/">pnmtile</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2003 by Robert Tinsley. This software is released under the GPL (<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.fsf.org/licenses/gpl.txt">http://www.fsf.org/licenses/gpl.txt</a> ). </p>
<h2>Index</h2>
