---
title: "gsl-histogram(1)"
name: "gsl-histogram"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsl-histogram/"
description: "gsl-histogram – compute histogram of data on stdin"
---

<h2>NAME</h2>
<p> gsl-histogram &#8211; compute histogram of data on stdin</p>
<h2>SYNOPSYS</h2>
<p> <code>gsl-histogram xmin xmax [n]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gsl-histogram </code> is a demonstration program for the GNU Scientific Library. It takes three arguments, specifying the upper and lower bounds of the histogram and the number of bins. It then reads numbers from `stdin&#8217;, one line at a time, and adds them to the histogram. When there is no more data to read it prints out the accumulated histogram using gsl_histogram_fprintf. If n is unspecified then bins of integer width are used.</p>
<h2>EXAMPLE</h2>
<p> Here is an example. We generate 10000 random samples from a Cauchy distribution with a width of 30 and histogram them over the range -100 to 100, using 200 bins.<br />
&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>gsl-randist 0 10000 cauchy 30 | gsl-histogram -100 100 200&nbsp;<wbr>&gt;&nbsp;<wbr>histogram.dat<br />
&nbsp;<wbr> A plot of the resulting histogram will show the familiar shape of the Cauchy distribution with fluctuations caused by the finite sample size. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>awk&nbsp;<wbr>&#8216;{print&nbsp;<wbr>$1,&nbsp;<wbr>$3&nbsp;<wbr>;&nbsp;<wbr>print&nbsp;<wbr>$2,&nbsp;<wbr>$3}&#8217;&nbsp;<wbr>histogram.dat | graph -T X </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gsl/">gsl</a>(3)</code>, <code><a href="/docs/linux/man/1-gsl-randist/">gsl-randist</a>(1)</code>. </p>
<h2>AUTHOR</h2>
<p> <code>gsl-histogram </code> was written by Brian Gough. Copyright 1996-2000; for copying conditions see the GNU General Public Licence. </p>
<p> This manual page was added by the Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, the Debian GNU/Linux maintainer for <code>GSL</code>. </p>
<h2>Index</h2>
