---
title: "pnmhisteq(1)"
name: "pnmhisteq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmhisteq/"
description: "pnmhisteq – histogram equalise a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmhisteq &#8211; histogram equalise a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmhisteq</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-gray</code>] [<code>-rmap</code> <i>pgmfile</i>] [<code>-wmap</code> <i>pgmfile</i>] [<code>-verbose</code>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pnmhisteq</code> increases the contrast of a portable graymap or pixmap through the technique of <i>histogram equalisation</i>[1]. A histogram of the luminance of pixels in the map is computed, from which a transfer function is calculated which spreads out intensity levels around histogram peaks and compresses them at troughs. This has the effect of using the available levels of intensity more efficiently and thereby increases the detail visible in the image. </p>
<p> Mathematically, if <i>N[i]</i> is the number of pixels of luminosity <i>i</i> in the image and <i>T</i> is the total number of pixels, luminosity <i>j</i> is replaced by: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;N[i]&nbsp;/&nbsp;T<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i=0 </p>
<p> If you&#8217;re processing a related set of images, for example frames of an animation, it&#8217;s generally best to apply the same intensity map to every frame, since otherwise you&#8217;ll get distracting frame-to-frame changes in the brightness of objects. <code>pnmhisteq</code>&#8216;s <code>-wmap</code> option allows you to save, as a portable graymap, the luminosity map computed from an image (usually a composite of the images you intend to process created with <code>pnmcat</code>). Then, you can subsequently process each of the individual images using the luminosity map saved in the file, supplied with the <code>-rmap</code> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-gray</code></p>
<dd> When processing a pixmap, only gray pixels (those with identical red, green, and blue values) are included in the histogram and modified in the output image. This is a special purpose option intended for images where the actual data are gray scale, with colour annotations you don&#8217;t want modified. Weather satellite images that show continent outlines in colour are best processed using this option. The option has no effect when the input is a graymap.</p>
<dt><code>-rmap</code><i> mapfile</i></p>
<dd> Process the image using the luminosity map specified by the portable graymap <i>mapfile.</i> The graymap, usually created by an earlier run of <code>pnmhisteq</code> with the <code>-wmap</code> option, contains a single row with number of columns equal to the <i>maxval</i> (greatest intensity) of the image. Each pixel in the image is transformed by looking up its luminosity in the corresponding column in the map file and changing it to the value given by that column.</p>
<dt><code>-wmap</code><i> mapfile</i></p>
<dd> Creates a portable graymap, <i>mapfile,</i> containing the luminosity map computed from the histogram of the input image. This map file can be read on subsequent runs of <code>pnmhisteq</code> with the <code>-rmap</code> option, allowing a group of images to be processed with an identical map.</p>
<dt><code>-verbose</code></p>
<dd> Prints the histogram and luminosity map on standard error.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>BUGS</h2>
<p> Histogram equalisation is effective for increasing the visible detail in scientific imagery and in some continuous-tone pictures. It is often too drastic, however, for scanned halftone images, where it does an excellent job of making halftone artifacts apparent. You might want to experiment with <code>pgnnorm</code>, <code>ppmnorm</code>, and <code>pnmgamma</code> for more subtle contrast enhancement. </p>
<p> The luminosity map file supplied by the <code>-rmap</code> option must have the same <i>maxval</i> as the input image. This is always the case when the map file was created by the <code>-wmap</code> option of <code>pnmhisteq</code>. If this restriction causes a problem, simply adjust the <i>maxval</i> of the map with <code>pnmdepth</code> to agree with the input image. </p>
<p> If the input is a PBM file (on which histogram equalisation is an identity operation), the only effect of passing the file through <code>pnmhisteq</code> will be the passage of time.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmnorm/">pgmnorm</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1), <code><a href="/docs/linux/man/1-pnmnorm/">pnmnorm</a></code>(1)</p>
<dl>
<dt>[1]</p>
<dd> Russ, John C. The Image Processing Handbook. Boca Raton: CRC Press, 1992. Pages 105-110.</dl>
<h2>AUTHOR</h2>
<p> <center> Copyright (C) 1995 by John Walker (kelvin [at] fourmilab.ch).<br />
 WWW home page: <a rel="nofollow" href="http://www.fourmilab.ch/">http://www.fourmilab.ch/</a><br />
 </center> </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<h2>Index</h2>
