---
title: "pgmminkowski(1)"
name: "pgmminkowski"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmminkowski/"
description: "pgmminkowski – compute Minkowski integral"
---

<h2 class="name">NAME</h2>
<p> pgmminkowski &#8211; compute Minkowski integral</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmminkowski</code> <i>pgmfile</i> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmminkowski</code> computes the 3 Minkowski integrals of a PGM image. </p>
<p> The Minkowski integrals mathematically characterize the shapes in the image and hence are the basis of &quot;morphological image analysis.&quot; </p>
<p> Hadwiger&#8217;s theorem has it that these integrals are the only motion-invariant, additive and conditionally continuous functions of a two-dimensional image, which means that they are preserved under certain kinds of deformations of the image. On top of that, they are very easy and quickly calculated. This makes them of interest for certain kinds of pattern recognition. </p>
<p> Basically, the Minkowski integrals are the area, total perimeter length, and the Euler characteristic of the image, where these metrics apply to the foreground image, not the rectangular PGM image itself. The foreground image consists of all the pixels in the image that are white. For a grayscale image, there is some threshold of intensity applied to categorize pixels into black and white, and the Minkowski integrals are calculated as a function of this threshold value. The total surface area refers to the number of white pixels in the PGM and the perimeter is the sum of perimeters of each closed white region in the PGM. </p>
<p> For a grayscale image, these numbers are a function of the threshold of what you want to call black or white. <code>pgmminkowski</code> reports these numbers as a function of the threshold for all possible threshold values. Since the total surface area can increase only as a function of the threshold, it is a reparameterization of the threshold. It turns out that if you consider the other two functions, the boundary length and the Euler characteristic, as a function of the first one, the surface, you get two functions that are a fingerprint of the picture. This fingerprint is e.g. sufficient to recognize the difference between pictures of different crystal lattices under a scanning tunnelling electron microscope. </p>
<p> For more information about Minkowski integrals, see e.g. </p>
<dl>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>K. Michielsen and H. De Raedt,&nbsp;<wbr>&quot;Integral-Geometry Morphological Image Analysis&quot;, Phys. Rep. 347, 461-538&nbsp;<wbr>(2001). </p>
<dt>&bull;</p>
<dd>
<p>&nbsp;<wbr>J.S. Kole, K. Michielsen, and H. De Raedt,&nbsp;<wbr>&quot;Morphological Image Analysis of Quantum Motion in Billiards&quot;, Phys. Rev. E 63, 016201-1 &#8211; 016201-7&nbsp;<wbr>(2001)&nbsp;<wbr> </p>
</dl>
<p> The output is suitable for direct use as a datafile in <code>gnuplot</code>. </p>
<p> In addition to the three Minkowski integrals, <code>pgmminkowski</code> also lists the horizontal and vertical edge counts. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmmorphconv/">pgmmorphconv</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pbmminkowski/">pbmminkowski</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> Luuk van Dijk, 2001. </p>
<p> Based on work which is Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
