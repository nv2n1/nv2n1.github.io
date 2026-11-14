---
title: "pamtopnm(1)"
name: "pamtopnm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtopnm/"
description: "pamtopnm – convert PAM image to PBM, PGM, or PPM"
---

<h2 class="name">NAME</h2>
<p> pamtopnm &#8211; convert PAM image to PBM, PGM, or PPM</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtopnm</code> </p>
<p> [<code>-assume</code>] </p>
<p> [<i>pnmfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtopnm</code> reads a PAM image as input and produces an equivalent PBM, PGM, or PPM (i.e. PNM) image, whichever is most appropriate, as output. </p>
<p> <code>pamtopnm</code> assumes the PAM image represents the information required for a PBM, PGM, or PPM image if its tuple type is &#8216;BLACKANDWHITE&#8217;, &#8216;GRAYSCALE&#8217;, or &#8216;RGB&#8217; and its depth and maxval are appropriate. If this is not the case, <code>pamtopnm</code> fails. </p>
<p> However, you can override the tuple type requirement with the <code>-assume</code> option. </p>
<p> <code>pamtopnm</code> produces a PPM image if the input PAM has depth 3 or 4; it produces PGM or PBM if the input PAM has depth 1 or 2. Whether it produced PGM or PBM depends upon the maxval: PBM for 1, PGM for anything higher. The tuple type does not play a role in determining the output type. You can use Netpbm programs such as <code>pgmtopgm</code> to generate a different PNM output, but remember that Netpbm program that expects PGM input will take PBM and so on. </p>
<p> As with any Netpbm program that reads PAM images, <code>pamtopnm</code> also reads PNM images as if they were PAM. In that case, <code>pamtopnm</code>&#8216;s functions reduces to simply copying the input to the output. But this can be useful in a program that doesn&#8217;t know whether its input is PAM or PNM but needs to feed it to a program that only recognizes PNM. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-assume</code></p>
<dd> When you specify <code>-assume</code>, you tell <code>pamtopnm</code> that you personally vouch for the fact that the tuples contain the same data as belongs in the channels of a PBM, PGM, or PPM file. The depth must still conform, though, so to truly force a conversion, you may have to run the input through <code>pamchannel</code> first. But be careful with <code>-assume</code>. When you -assume, you make an -ass of u and me. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtopgm/">pbmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pamditherbw/">pamditherbw</a></code>(1) , <code><a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtopnm</code> was new, along with the PAM format, in Netpbm 9.7 (August 2000). </p>
<h2>Index</h2>
