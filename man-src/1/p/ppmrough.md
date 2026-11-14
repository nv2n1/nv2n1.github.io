---
title: "ppmrough(1)"
name: "ppmrough"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmrough/"
description: "ppmrough – create PPM image of two colors with a ragged border between them"
---

<h2 class="name">NAME</h2>
<p> ppmrough &#8211; create PPM image of two colors with a ragged border between them</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmrough</code> </p>
<p> [<code>-left </code><i>pixels</i>] </p>
<p> [<code>-right </code><i>pixels</i>] </p>
<p> [<code>-top </code><i>pixels</i>] </p>
<p> [<code>-bottom </code><i>pixels</i>] </p>
<p> [<code>-width </code><i>pixels</i>] </p>
<p> [<code>-height </code><i>pixels</i>] </p>
<p> [<code>-bg </code><i>rgb:##/##/##</i>] </p>
<p> [<code>-fg </code><i>rgb:##/##/##</i>] </p>
<p> [<code>-var </code><i>pixels</i>] </p>
<p> [<code>-randomseed </code><i>seed</i>] </p>
<p> [<code>-verbose</code>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmrough</code> generates a PPM image of the specified width, height, and colors. <code>ppmrough</code> tiles the image into semi-rectangular regions with a ragged borders between them. It calculates the fluctuations with the <code>rand()</code> standard C library function. </p>
<p> <code>ppmrough</code> writes the PPM image to Standard Output. </p>
<p> The maxval of the output image is 255 (You can change this with <code>pamdepth</code>). </p>
<p> Use the options <code>-left</code> or <code>-right</code>, respectively, to make vertical borders, and <code>-top</code> or <code>-bottom</code>, respectively, to generate horizontal borders inside the image. Each of these options needs an integer value <i>pixels</i> that determines the average distance of the interior border to the related edge of the image. You may combine the <code>-left</code>, <code>-right</code>, <code>-top</code>, and <code>-bottom</code> options to generate an image with more than one border. The algorithm ensures that you can concatenate two images produced with the same (i.e. <code>-left</code>) value without dislocations. </p>
<p> You specify the dimensions of the generated image with the <code>-width</code> and <code>-height</code> options. </p>
<p> Use the <code>-bg</code> and <code>-fg</code> options to set the background (margin) color and the foreground (interior) color, respectively. If you don&#8217;t specify any of the <code>-left</code>, <code>-right</code>, <code>-top</code>, and <code>-bottom</code> options, all pixels are set to foreground color. The defaults are white foreground and black background. </p>
<p> Use the <code>-var</code> option to control the &#8216;raggedness&#8217; of the border. The less its value is the smoother the border is. You can initialize the pseudo-random generator with the <code>-init</code> option. </p>
<p> You could use <code>ppmrough</code> with <code>ppmtopgm</code> to create a PGM alpha mask and use it to roughen up the edges of another image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-left=</code><i>pixels</i></p>
<dd>
&nbsp;<wbr>Specifies the mean distance of the border from the left margin (default: no border). </p>
<dt><code>-right=</code><i>pixels</i></p>
<dd> Specifies the mean distance of the border from the right margin (default: no border). </p>
<dt><code>-top=</code><i>pixels</i></p>
<dd> Specifies the mean distance of the border from the top margin (default: no border). </p>
<dt><code>-bottom=</code><i>pixels</i></p>
<dd> Specifies the mean distance of the border from the bottom margin (default: no border). </p>
<dt><code>-width=</code><i>pixels</i></p>
<dd> Specifies the width of the image (default: 100). </p>
<dt><code>-height=</code><i>pixels</i></p>
<dd> Specifies the height of the image (default: 100). </p>
<dt><code>-bg=</code><i>color</i></p>
<dd> Background color. Specify this the same way you specify a color with<br />
&nbsp;<wbr>&nbsp;<wbr><code>ppmmake</code>.&nbsp;<wbr>&nbsp;<wbr>Default is black. </p>
<dt><code>-fg=</code><i>color</i></p>
<dd> Foreground color. Specify this the same way you specify a color with<br />
&nbsp;<wbr>&nbsp;<wbr><code>ppmmake</code>.&nbsp;<wbr>&nbsp;<wbr>Default is white. </p>
<dt><code>-var=</code><i>pixels</i></p>
<dd>
&nbsp;<wbr>Specifies the variance of the ragged border&nbsp;<wbr>(default: 10). Must be a positive integer. Set <i>pixels</i> to 1 to get a straight border. </p>
<dt><code>-randomseed=</code><i>seed</i></p>
<dd> Use this option to initialize the pseudo-random number generator (the Standard C library <code>srand()</code> function) with <i>seed</i>. </p>
<p> Before Netpbm 10.61 (December 2012), this is called <code>-init</code>, and that still works. </p>
<dt><code>-verbose</code></p>
<dd> Run <code>ppmrough</code> in verbose mode. It reports all parameters on Standard Error. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) , <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.9 (September 2002). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002 by Eckard Specht. </p>
<h2>Index</h2>
