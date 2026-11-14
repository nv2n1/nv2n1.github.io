---
title: "ppmnorm(1)"
name: "ppmnorm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmnorm/"
description: "pnmnorm – normalize the contrast in a Netbpm image"
---

<h2 class="name">NAME</h2>
<p> pnmnorm &#8211; normalize the contrast in a Netbpm image </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmnorm</code> [<code>-bpercent</code> <i>N</i> | <code>-bvalue</code> <i>N</i>] [<code>-wpercent</code> <i>N</i> | <code>-wvalue</code> <i>N</i>] [<code>-keephues</code>] [<code>-brightmax</code>] </p>
<p> [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PNM image (PBM, PGM, or PPM). Normalizes the contrast by forcing the lightest pixels to white, the darkest pixels to black, and linearly rescaling the ones in between; and produces the same kind of file as output. This is pretty useless for a PBM image. </p>
<p> The program first determines a mapping of old brightness to new brightness. For each possible brightness of a pixel, the program determines a corresponding brightness for the output image. </p>
<p> Then for each pixel in the image, the program computes a color which has the desired output brightness and puts that in the output. With a color image, it is not always possible to compute such a color and retain any semblance of the original hue, so the brightest and dimmest pixels may only approximate the desired brightness. </p>
<p> Note that for a PPM image, this is different from separately normalizing the individual color components. </p>
<h2>OPTIONS</h2>
<p> By default, the darkest 2 percent of all pixels are mapped to black, and the lightest 1 percent are mapped to white. You can override these percentages by using the <code>-bpercent</code> and <code>-wpercent</code> flags, or you can specify the exact pixel values to be mapped by using the <code>-bvalue</code> and <code>-wvalue</code> flags. Appropriate numbers for the flags can be gotten from the <i>ppmhist</i> tool. If you just want to enhance the contrast, then choose values at elbows in the histogram; e.g. if value 29 represents 3% of the image but value 30 represents 20%, choose 30 for <i>bvalue</i>. If you want to lighten the image, then set <i>bvalue</i> to 0 and just fiddle with <i>wvalue</i>; similarly, to darken the image, set <i>wvalue</i> to maxval and play with <i>bvalue</i>. </p>
<p> The <code>-keephues</code> option says to keep each pixel the same hue as it is in the input; just adjust its intensity. By default, <code>pnmnorm</code> normalizes contrast in each component independently (except that the meaning of the <code>-wpercent</code> and <code>-bpercent</code> options are based on the overall intensities of the colors, not each component taken separately). So if you have a color which is intensely red but dimly green, <code>pnmnorm</code> would make the red more intense and the green less intense, so you end up with a different hue than you started with. </p>
<p> If you specify <code>-keephues</code>, <code>pnmnorm</code> would likely leave this pixel alone, since its overall intensity is medium. </p>
<p> <code>-keephues</code> can cause clipping, because a certain color may be below a target intensity while one of its components is saturated. Where that&#8217;s the case, <code>pnmnorm</code> uses the maximum representable intensity for the saturated component and the pixel ends up with less overall intensity, and a different hue, than it is supposed to have. </p>
<p> This option is meaningless on grayscale images. </p>
<p> Before March 2002, there was no <code>-keephues</code> option. </p>
<p> The <code>-brightmax</code> option says to use the intensity of the most intense RGB component of a pixel as the pixel&#8217;s brightness. By default, <code>pnmnorm</code> uses the luminosity of the color as its brightness. </p>
<p> This option is meaningless on grayscale images. </p>
<p> Before March 2002, there was no <code>-brightmax</code> option. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmhist/">ppmhist</a></code>(1), <code><a href="/docs/linux/man/1-pgmhist/">pgmhist</a></code>(1), <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1), <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1), <code><a href="/docs/linux/man/1-ppmdim/">ppmdim</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>Index</h2>
