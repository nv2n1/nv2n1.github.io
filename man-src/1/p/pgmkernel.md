---
title: "pgmkernel(1)"
name: "pgmkernel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmkernel/"
description: "pgmkernel – generate a convolution kernel"
---

<h2 class="name">NAME</h2>
<p> pgmkernel &#8211; generate a convolution kernel </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmkernel</code> [ <code>-weight</code> <i>w</i> ] <i>width </i> [ <i>height </i> ]</p>
<h2>DESCRIPTION</h2>
<p> Generates a portable graymap array of size <i>width </i> x <i>height </i> (or <i>width </i> x <i>width </i> if <i>height </i> is not specified) to be used as a convolution file by <code>pnmconvol</code>. The data in the convolution array K are computed according to the formula: </p>
<p> K(i,j) = 1 / ( 1 + w * sqrt((i-width/2)^2 + (j-height/2)^2)) </p>
<p> where <i>w </i> is a coefficient specified via the <i>-weight </i> flag, and <i>width </i> and <i>height</i> are the X and Y filter sizes. </p>
<p> The output PGM file is always written out in ASCII format.</p>
<h2>OPTIONS</h2>
<p> The optional <i>-weight </i> flag should be a real number greater than -1. The default value is 6.0.</p>
<h2>BUGS</h2>
<p> The computation time is proportional to <i>width </i> * <i>height</i>. This increases rapidly with the increase of the kernel size. A better approach could be using a FFT in these cases.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a>(1), <a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a>(1)</p>
<h2>AUTHOR</h2>
<p> Alberto Accomazzi (alberto [at] cfa.harvard.edu). </p>
<h2>Index</h2>
