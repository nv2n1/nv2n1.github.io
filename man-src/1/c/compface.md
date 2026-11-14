---
title: "compface(1)"
name: "compface"
section: "1"
letter: "c"
url: "/docs/linux/man/1-compface/"
description: "compface, uncompface – compress and expand 48x48x1 face image files"
---

<h2>NAME</h2>
<p> compface, uncompface &#8211; compress and expand 48x48x1 face image files</p>
<h2>SYNOPSIS</h2>
<p> <code>compface</code> [ <i>infile</i> [ <i>outfile</i> ] ] &#8230; </p>
<p> <code>uncompface</code> [-X] [ <i>infile</i> [ <i>outfile</i> ] ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>compface</i> is a filter for generating highly compressed representations of 48x48x1 face image files. <i>uncompface</i> is an inverse filter which performs an inverse transformation with no loss of data. The algorithm used is highly tuned for its purpose and achieves better than a five to one compression ratio on average. Arguments operate identically for both programmes. The first argument, if present, causes input to be taken from the named file instead of from standard input unless it is the string &#8220;-&#8221;. A second argument, if present, causes output to go to the named file instead of to standard output unless it is the string &#8220;-&#8221;. Subsequent pairs of arguments may be used to specify further pairs of input and output files. </p>
<p> The input format for <i>compface</i> (and the output format for <i>uncompface</i>) is 48 lines each of 3 sixteen bit hexadecimal integers, comma terminated in C initialiser style. The output format of <i>compface</i> (and the input format for <i>uncompface</i>) is some number of lines made up of a space followed by printable characters (in the range &#8220;!&#8221; to &#8220;~&#8221; inclusive). The first line contains 72 characters and following lines contain 79 characters except that the last line may be short. </p>
<p> This version of compface has been patched to also be able to handle normal XBM images. uncompface will produce XBM output only if the -X switch is applied. </p>
<p> The amount of compression obtained varies between face image files but the output of <i>compface</i> averages less than 200 characters. The average number of output lines is three.</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is normally 0. Possible errors include IO errors when opening, reading or writing files, format errors in <i>compface</i> input files and invalid arguments. Each results in an explanatory message on standard error and an exit status of 1. A warning will be produced if <i>compface</i> detects extra input data.</p>
<h2>BUGS</h2>
<p> Nominating standard input as input more than once does not work.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-compface/">Compface</a>(3) </p>
<h2>Index</h2>
