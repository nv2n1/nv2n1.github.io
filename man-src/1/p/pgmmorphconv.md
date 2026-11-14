---
title: "pgmmorphconv(1)"
name: "pgmmorphconv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmmorphconv/"
description: "pgmmorphconv – perform morphological convolutions: dilation, erosion"
---

<h2 class="name">NAME</h2>
<p> pgmmorphconv &#8211; perform morphological convolutions: dilation, erosion</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmmorphconv</code> [ <code>-erode</code> | <code>-dilate</code> | <code>-open</code> | <code>-close</code> ] <i>templatefile</i> [<i>pgmfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmmorphconv</code> performs morphological convolutions on a PGM image: dilation and erosion. </p>
<p> <code>pgmmorphconv</code> performs a &quot;topological&quot; convolution. For each pixel of the input, <code>pgmmorphconv</code> generates an output pixel in the same position. To determine the intensity of the output pixel, <code>pgmmorphconv</code> lays the template image over the input image such that the middle pixel of the template is over the input pixel in question. <code>pgmmorphconv</code> looks at the input pixels underneath each white pixel in the template. For a dilation, the maximum intensity of all those pixels is the intensity of the output pixel. For an erosion, it is the minimum. </p>
<p> Thus, the dilation effect is that bright areas of the input get bigger and dark areas smaller. The erosion effect is the opposite. The simplest template image would be one with a white pixel in the middle and the rest black. This would produce an output image identical to the input. Another simple template image is a fully white square. This causes bright or dark areas to expand in all directions. A template image that is white on the left side and black on the right would smear the image to the right. </p>
<p> The template file named by <i>templatefile</i> contains the template image as a PBM image. It must have an odd number of rows and an odd number of columns, so there is a definite middle pixel. It must contain at least one white pixel. </p>
<p> This is similar to the continuous convolution done by <code>pnmconvol</code>, except that with <code>pnmconvol</code> the output intensity is a weighted average of nearby input pixels instead of a minimum or maximum. </p>
<p> This convolution changes the three Minkowski integrals in a predefined way, and can be used to filter an image to enhance certain features, to ease their automatic recognition. </p>
<p> The options <code>-erode</code> and <code>-dilate</code> obviously produce an erosion or dilation, respectively. </p>
<p> The <code>-open</code> option causes <code>pgmmorphconv</code> to perform first an erode and then a dilate operation. The <code>-close</code> option causes a dilate first and then an erode. If you specify none of these options, it is the same as <code>-dilate</code>. </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pgmminkowski/">pgmminkowski</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
</dl>
<p> For more information about morphological convolutions, see e.g. </p>
<dl>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>K. Michielsen and H. De Raedt,&nbsp;<wbr>&quot;Integral-Geometry Morphological Image Analysis&quot;,�&nbsp;<wbr>Phys. Rep. 347, 461-538&nbsp;<wbr>(2001). </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>J.S. Kole, K. Michielsen, and H. De Raedt,&nbsp;<wbr>&quot;Morphological Image Analysis of Quantum Motion in Billiards&quot;, Phys. Rev. E 63, 016201-1 &#8211; 016201-7&nbsp;<wbr>(2001)&nbsp;<wbr> </p>
</dl>
<h2>AUTHORS</h2>
<p> Luuk van Dijk, 2001. </p>
<p> Based on work which is Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
