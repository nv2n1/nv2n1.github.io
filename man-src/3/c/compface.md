---
title: "compface(3)"
name: "compface"
section: "3"
letter: "c"
url: "/docs/linux/man/3-compface/"
description: "compface, uncompface – compress and expand 48x48x1 face image files"
---

<h2>NAME</h2>
<p> compface, uncompface &#8211; compress and expand 48x48x1 face image files</p>
<h2>SYNOPSIS</h2>
<p> <code>compface (buf)</code> </p>
<p> <code>uncompface (buf)</code> </p>
<p> <code>char *buf</code></p>
<h2>DESCRIPTION</h2>
<p> <i>compface</i> is a function for generating highly compressed representations of 48x48x1 face image files. <i>uncompface</i> is an inverse function which performs an inverse transformation with no loss of data. The algorithm used is highly tuned for its purpose and achieves better than a five to one compression ratio on average. In both functions, input is via a NULL terminated string and a NULL terminated output string is written over the input string. <i>Buf</i> should therefore point to a block of 2K size or more to avoid buffer overruns during output generation. </p>
<p> The input format for <i>compface</i> (and the output format for <i>uncompface</i>) is 48 lines each of 3 sixteen bit hexadecimal integers, comma terminated in C initialiser style. The output format of <i>compface</i> (and the input format for <i>uncompface</i>) is some number of lines made up of a space followed by printable characters (in the range &#8220;!&#8221; to &#8220;~&#8221; inclusive). The first line contains 72 characters and following lines contain 79 characters except that the last line may be short. </p>
<p> This version of compface has been patched to also be able to handle normal XBM images. uncompface will produce XBM output only if the -X switch is applied. </p>
<p> The amount of compression obtained varies between face image files but the output of <i>compface</i> averages less than 200 characters. The average number of output lines is three.</p>
<h2>DIAGNOSTICS</h2>
<p> The return value is normally 0. 1 will be returned if extra input has been ignored during a compress operation. -1 is returned in the case of an invalid input format. -2 is returned if an internal buffer overrun occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-compface/">Compface</a>(1) </p>
<h2>Index</h2>
