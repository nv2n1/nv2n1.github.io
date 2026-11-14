---
title: "setvtrgb(1)"
name: "setvtrgb"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setvtrgb/"
description: "setvtrgb – customize the console color map"
---

<h2 class="name">NAME</h2>
<p> setvtrgb &#8211; customize the console color map </p>
<h2>SYNOPSIS</h2>
<p> <code>setvtrgb</code> vga </p>
<p> <code>setvtrgb</code> <i>FILE</i>|-</p>
<h2>DESCRIPTION</h2>
<p> <code>setvtrgb</code> sets the console color map in all virtual terminals according to custom values specified in a file or standard input. With the `vga&#8217; parameter, it can also be used to restore the settings built into the kernel. </p>
<p> When invoked with a filename or `-&#8216;, <code>setvtrgb</code> expects input as follows: </p>
<p>&nbsp;<wbr>&nbsp;color0_r,color1_r,&#8230;,color15_r<br />
&nbsp;<wbr>&nbsp;color0_g,color1_g,&#8230;,color15_g<br />
&nbsp;<wbr>&nbsp;color0_b,color1_b,&#8230;,color15_b </p>
<p> where colorN_{r,g,b} is the red/green/blue portion of the respective color in decimal notation in the 0..255 range. To pre-seed a file in the correct format, you can use </p>
<p>&nbsp;<wbr>&nbsp;cat&nbsp;/sys/module/vt/parameters/default_{red,grn,blu} </p>
<p> The meanings of the color values are defined as follows: </p>
<p>&nbsp;<wbr>&nbsp;+&#8212;&#8212;&#8211;+&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;+<br />
&nbsp;<wbr>&nbsp;| Normal | Bright | Color&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;+&#8212;&#8212;&#8211;+&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;+<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 | Black&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;9 | Red&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;10 | Green&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;11 | Yellow&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12 | Blue&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;13 | Magenta |<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;14 | Cyan&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;15 | White&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;+</p>
<h2>AUTHOR</h2>
<p> setvtrgb is Copyright &#169; 2011 Alexey Gladkov &lt;gladkov.alexey [at] gmail.com&gt;, with portions by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; and Seth Forshee &lt;seth.forshee [at] canonical.com&gt; at Canonical Ltd. </p>
<p> This manual page was written by Michael Schutte &lt;michi [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
