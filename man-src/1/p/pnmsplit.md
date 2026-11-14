---
title: "pnmsplit(1)"
name: "pnmsplit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmsplit/"
description: "pnmsplit – split a multi-image portable anymap into multiple single-image files"
---

<h2 class="name">NAME</h2>
<p> pnmsplit &#8211; split a multi-image portable anymap into multiple single-image files </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmsplit</code> [<i>pnmfile</i>[<i> output_file_pattern</i>]] </p>
<h2>DESCRIPTION</h2>
<p> Reads a Netpbm file as input. Copies each image in the input into a separate file, in the same format. </p>
<p> <i>pnmfile</i> is the file specification of the input file, or <code>&#8211;</code> to indicate Standard Input. The default is Standard Input. </p>
<p> <i>output_file_pattern</i> tells how to name the output files. It is the file specification of the output file, except that the first occurence of &quot;%d&quot; in it is replaced by the image sequence number in unpadded ASCII decimal, with the sequence starting at 0. If there is no &quot;%d&quot; in the pattern, <code>pnmsplit</code> fails. </p>
<p> The default output file pattern is &quot;image%d&quot;. </p>
<p> Note that to do the reverse operation (combining multiple single-image PNM files into a multi-image one), there is no special Netpbm program. Just use <code>cat</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Written by Bryan Henderson </p>
<h2>Index</h2>
