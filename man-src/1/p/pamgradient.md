---
title: "pamgradient(1)"
name: "pamgradient"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamgradient/"
description: "pamgradient – create a four-corner gradient PAM image"
---

<p>&nbsp;<wbr>&nbsp;<wbr></p>
<h2 class="name">NAME</h2>
<p> pamgradient &#8211; create a four-corner gradient PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamgradient</code> [<code>-maxval=</code><i>maxval</i>] <i>color-tl</i> <i>color-tr</i> <i>color-bl</i> <i>color-br</i> <i>width</i> <i>height</i> </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamgradient</code> creates an image of the specified dimensions <i>width</i> by <i>height</i> which contains a smooth, two-dimensional gradient between the specified colors of the four corners (from top left to bottom right). </p>
<p> Specify the colors as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> If all four colors are gray values, <code>pamgradient</code> creates a grayscale image (PAM tuple type GRAYSCALE). Otherwise, it creates a color image (PAM tuple type RGB). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-maxval=</code><i>maxval</i></p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr> maxval of the generated image. (See <code><a href="/docs/linux/man/1-pam/">PAM</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pnm/">PNM</a></code>(1)<br />
&nbsp;<wbr>specifications). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamgradient/">pamgradient</a></code>(1) , <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) , <code><a href="/docs/linux/man/1-ppmrainbow/">ppmrainbow</a></code>(1) , <code><a href="/docs/linux/man/1-pgmramp/">pgmramp</a></code>(1) , <code><a href="/docs/linux/man/1-ppmpat/">ppmpat</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>NOTE</h2>
<p> Only the top left corner of the generated image has exactly the specified color. The color of the top right corner is a bit shifted to the left, the bottom left corner a bit up, and the bottom right corner left and up. This ensures nice transitions when combining adjacent (very narrow) gradients, and doesn&#8217;t play a role when the gradient butts against a solid surface. </p>
<p> This effect is created by the integer arithmetic used for the interpolation of the color values, and since it doesn&#8217;t make a difference for all practical purposes I might as well sell it as a feature. </p>
<h2>HISTORY</h2>
<p> <code>pamgradient</code> was new in Netpbm 10.31 (December 2005). </p>
<h2>AUTHOR</h2>
<p> pamgradient was written by Daniel Haude in October 2005. </p>
<h2>Index</h2>
