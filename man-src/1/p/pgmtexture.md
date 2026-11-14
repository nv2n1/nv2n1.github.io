---
title: "pgmtexture(1)"
name: "pgmtexture"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtexture/"
description: "pgmtexture – calculate textural features on a portable graymap"
---

<h2 class="name">NAME</h2>
<p> pgmtexture &#8211; calculate textural features on a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtexture</code> [<code>-d</code> <i>d</i>] [<i>pgmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable graymap as input. Calculates textural features based on spatial dependence matrices at 0, 45, 90, and 135 degrees for a distance <i>d</i> (default = 1). Textural features include:</p>
<dl>
<dt>
<dd> (1) Angular Second Moment,<br />
 (2) Contrast,<br />
 (3) Correlation,<br />
 (4) Variance,<br />
 (5) Inverse Difference Moment,<br />
 (6) Sum Average,<br />
 (7) Sum Variance,<br />
 (8) Sum Entropy,<br />
 (9) Entropy,<br />
 (10) Difference Variance,<br />
 (11) Difference Entropy,<br />
 (12, 13) Information Measures of Correlation, and<br />
 (14) Maximal Correlation Coefficient.</dl>
<p> Algorithm taken from:<br />
 Haralick, R.M., K. Shanmugam, and I. Dinstein. 1973. Textural features for image classification. <i>IEEE Transactions on Systems, Man, </i> <i>and Cybertinetics,</i> <a href="/docs/linux/man/6-smc-3/">SMC-3</a>(6):610-621.</p>
<h2>BUGS</h2>
<p> The program can run incredibly slow for large images (larger than 64 x 64) and command line options are limited. The method for finding (14) the maximal correlation coefficient, which requires finding the second largest eigenvalue of a matrix Q, does not always converge.</p>
<h2>REFERENCES</h2>
<p> <i>IEEE Transactions on Systems, Man, </i> <i>and Cybertinetics,</i> <a href="/docs/linux/man/6-smc-3/">SMC-3</a>(6):610-621.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/1-pnmcut/">pnmcut</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Texas Agricultural Experiment Station, employer for hire of James Darrell McCauley. </p>
<h2>Index</h2>
