---
title: "pfb2t1c(1)"
name: "pfb2t1c"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfb2t1c/"
description: "pfb2t1c – convert from binary PostScript Type1 into compressible .t1c t1c2pfb – convert from compressible .t1c to binary PostScript Type1"
---

<h2>NAME</h2>
<p> pfb2t1c &#8211; convert from binary PostScript Type1 into compressible .t1c t1c2pfb &#8211; convert from compressible .t1c to binary PostScript Type1 </p>
<h2>SYNOPSIS</h2>
<p> <code>pfb2t1c</code> &quot;pfb file&quot; </p>
<p> <code>t1c2pfb</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>pfb2t1c</code> reads a pfb file and converts it into the t1c format. The resulting single file (written to stdout) is not much smaller than the original pfb but more compressible. The file name of the pfb file(s) is/are noted in a pseudo header inside the t1c, hence one can append the resulting t1c files to each other. </p>
<p> <code>t1c2pfb</code> extracts fonts saved in a t1c file. The program reads from stdin and creates the PostScript Type1 file(s). </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 Szab&oacute; P&eacute;ter. </p>
<p> There is NO warranty. The programs are released under GPL. See the copyright file for details.</p>
<h2>BUGS</h2>
<p> Problems with the programs should first reported into the Debian Bug Tracking system, we will forward it to upstream if necessary. </p>
<h2>AUTHOR</h2>
<p> Written by pts [at] fazekas.hu. </p>
<p> This manual page was written by Norbert Preining for the Debian GNU/Linux system (and modified by Hilmar Preusse later). It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
