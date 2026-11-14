---
title: "ppmcolors(1)"
name: "ppmcolors"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmcolors/"
description: "ppmcolors – generate a color map of all colors of a certain maxval"
---

<h2 class="name">NAME</h2>
<p> ppmcolors &#8211; generate a color map of all colors of a certain maxval</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmcolors</code> [<code>-maxval=</code><i>maxval</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> <code>ppmcolors</code> generates a PPM color map containing all the colors representable with a certain maxval. </p>
<p> A PPM color map is a regular PPM image that is used by some programs to define a set of colors. </p>
<p> <code>ppmcolors</code> generates a one row PPM image that contains one pixel of each color representable by the maxval you choose. The maxval of the PPM image is that maxval. Note that you can change the maxval of the color map by running the output of <code>ppmcolors</code> through <code>pnmdepth</code>. As long as the new maxval is a multiple of the original, the resulting set of colors will be identical. If the new maxval is not a multiple, the resulting set of colors will be slightly different. </p>
<p> When you select a maxval of 5 (which is the default), you get a color map of the set of &quot;web safe&quot; colors as defined by Netscape. Most web browsers guarantee that they can produce at least these 216 colors (215 plus black). </p>
<p> <code>pnmcolormap</code> is another program to generate a color map. It chooses a set of colors designed to represent the colors in a specified image (or simply the set of all the colors in that image, if you choose). </p>
<p> <code>pgmramp</code> performs a similar function for PGM images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-maxval=</code><i>maxval</i></p>
<dd> This is the maxval of the generated color map. Default is 5. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-pnmcolormap/">pnmcolormap</a></code>(1), <code><a href="/docs/linux/man/1-ppmcie/">ppmcie</a></code>(1), <code><a href="/docs/linux/man/1-ppmrainbow/">ppmrainbow</a></code>(1), <code><a href="/docs/linux/man/1-pgmramp/">pgmramp</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> By Bryan Henderson, December 2001. </p>
<h2>Index</h2>
