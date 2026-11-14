---
title: "pammosaicknit(1)"
name: "pammosaicknit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pammosaicknit/"
description: "pammosaicknit – validate a mosaic knitting pattern"
---

<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd</a>&quot;&gt; </p>
<p> Table Of Contents </p>
<h2 class="name">NAME</h2>
<p> pammosaicknit &#8211; validate a mosaic knitting pattern </p>
<h2>SYNOPSIS</h2>
<p> <code>pammosaicknit</code> [<i>in_netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pammosaicknit</code> helps the user create mosaic knitting patterns . The program inputs a black-and-white Netpbm image that describes a mosaic knitting pattern and outputs a color Netpbm image of the same pattern but with invalid runs shown in red. </p>
<p> A valid knitting pattern starts with a &lt;q&gt;black&lt;/q&gt; row on the bottom and alternates &lt;q&gt;white&lt;/q&gt; and &lt;q&gt;black&lt;/q&gt; rows. A &lt;q&gt;black&lt;/q&gt; row can contain any arrangement of black pixels but no more than three consecutive white pixels. A &lt;q&gt;white&lt;/q&gt; row can contain any arrangement of white pixels but no more than three consecutive black pixels. Columns wrap horizontally, so a &lt;q&gt;white&lt;/q&gt; row that both begins and ends with two black pixels is deemed to contain four consecutive black pixels. Because this is an invalid number for a &lt;q&gt;white&lt;/q&gt; row, those four pixels will be recolored red in the output image. </p>
<p> For clarity, there are two shades of red in the output image. Dark red pixels indicate pixels that were black in the input image but which must contain one or more white pixels. Light red pixels indicate pixels that were white in the input image but which must contain one or more black pixels. </p>
<p> If the output image contains no red pixels, then the input image represents a valid mosaic knitting pattern. </p>
<h2>ARGUMENTS</h2>
<p> <code>pammosaicknit</code>&#8216;s only argument, <i>in_netpbmfile</i>, is the name of an image file that represents a mosaic knitting pattern. If you don&#8217;t specify <i>in_netpbmfile</i>, the program reads the image from Standard Input. </p>
<h2>NOTES</h2>
<p> If the input image is not a black-and-white image, <code>pammosaicknit</code> converts it internally to black and white by thresholding each pixel&#8217;s luminosity. The output image is always a color image containing at most four colors (black, white, dark red, light red). </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
</dl>
<h2>HISTORY</h2>
<p> pammosaicknit was new in Netpbm 10.53 (December 2010). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2010 Scott Pakin, <i>scott+pbm [at] pakin.org.</i> </p>
<h2>Table Of Contents</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> SYNOPSIS</p>
<dt>&bull;</p>
<dd>
<p> DESCRIPTION</p>
<dt>&bull;</p>
<dd>
<p> ARGUMENTS</p>
<dt>&bull;</p>
<dd>
<p> NOTES</p>
<dt>&bull;</p>
<dd>
<p> SEE ALSO</p>
<dt>&bull;</p>
<dd>
<p> HISTORY</p>
<dt>&bull;</p>
<dd>
<p> AUTHOR </p>
</dl>
<h2>Index</h2>
