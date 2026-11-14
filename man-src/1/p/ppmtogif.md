---
title: "ppmtogif(1)"
name: "ppmtogif"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtogif/"
description: "ppmtogif – convert a portable pixmap into a GIF file"
---

<h2 class="name">NAME</h2>
<p> ppmtogif &#8211; convert a portable pixmap into a GIF file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtogif</code> [<code>-interlace</code>] [<code>-sort</code>] [<code>-map</code> <i>mapfile</i>]<br />
 [<code>-transparent</code> [<code>=</code>]<i>color</i>] [<code>-alpha</code> <i>pgmfile</i>] [<code>-comment</code> <i>text</i>] [<code>-nolzw</code>]<br />
 [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a GIF file as output. </p>
<p> This program creates only individual GIF images. To combine multiple GIF images into an animated GIF, use <code>gifsicle</code> (not part of the Netpbm package). </p>
<p> <code>ppmtogif</code> creates either an original GIF87 format GIF file or the newer GIF89 format. It creates GIF89 when you request features that were new with GIF89, to wit the <code>-transparent</code> or <code>-comment</code> options. Otherwise, it creates GIF87. Really old GIF readers conceivably could not recognize GIF89. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-interlace</code></p>
<dd> Produce an interlaced GIF file.</p>
<dt><code>-sort</code></p>
<dd> Produces a GIF file with a sorted color map.</p>
<dt><code>-map </code></p>
<dd> <i>mapfile</i> </p>
<p> Uses the colors found in the <i>mapfile</i> to create the colormap in the GIF file, instead of the colors from <i>ppmfile.</i> The <i>mapfile</i> can be any <i>ppm</i> file; all that matters is the colors in it. If the colors in <i>ppmfile</i> do not match those in <i>mapfile</i> , they are matched to a &quot;best match.&quot; A (much) better result can be obtained by using the following filter in advance: </p>
<p> <i>ppmquant</i> -floyd -map <i>mapfile</i></p>
<dt><code>-transparent </code><i>color</i></p>
<dd> <code>ppmtogif</code> marks the specified color as transparent in the GIF image. </p>
<p> If you don&#8217;t specify <code>-transparent</code>, <code>ppmtogif</code> does not mark any color transparent (except as indicated by the <code>-alpha</code> option). </p>
<p> You specify the color as in <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1).<code>E.g.</code> <code>red</code> or <code>rgb:ff/00/0d</code>. If the color you specify is not present in the image, <code>ppmtogif</code> selects instead the color in the image that is closest to the one you specify. Closeness is measured as a cartesian distance between colors in RGB space. If multiple colors are equidistant, <code>ppmtogif</code> chooses one of them arbitrarily. </p>
<p> However, if you prefix your color specification with &quot;=&quot;, e.g. </p>
<p> <code>-transparent==red</code> </p>
<p> Only the exact color you specify will be transparent. If that color does not appear in the image, there will be no transparency. <code>ppmtogif</code> issues an information message when this is the case. </p>
<p> You cannot specify both <code>-transparent</code> and <code>-alpha</code>. </p>
<dt><code>-alpha= </code><i>pgmfile</i></p>
<dd> This option names a PGM file that contains an alpha mask for the image. <code>ppmtogif</code> Creates fully transparent pixels wherever the alpha mask indicates transparency greater than 50%. The color of those pixels is that specified by the <code>-alphacolor</code> option, or black by default. </p>
<p> To do this, <code>ppmtogif</code> creates an entry in the GIF colormap in addition to the entries for colors that are actually in the image. It marks that colormap entry as transparent and uses that colormap index in the output image to create a transparent pixel. </p>
<p> The alpha image must be the same dimensions as the input image, but may have any maxval. White means opaque and black means transparent. </p>
<p> You cannot specify both <code>-transparent</code> and <code>-alpha</code>. </p>
<dt><code>-alphacolor</code></p>
<dd> See <code>-alpha</code>. </p>
<dt><code>-comment </code><i>text</i></p>
<dd> Include a comment in the GIF output with comment text <i>text</i>. Without this option, there are no comments in the output. </p>
<dt><code>-nolzw </code></p>
<dd> This option causes the GIF output, and thus <code>ppmtogif</code>, not to use LZW (Lempel-Ziv) compression. As a result, the image file is larger and no royalties are owed to the holder of the patent on LZW. See the section LICENSE below. </p>
<p> LZW is a method for combining the information from multiple pixels into a single GIF code. With the <code>-nolzw</code> option, <code>ppmtogif</code> creates one GIF code per pixel, so it is not doing any compression and not using LZW. However, any GIF decoder, whether it uses an LZW decompressor or not, will correctly decode this uncompressed format. An LZW decompressor would see this as a particular case of LZW compression. </p>
<p> Note that if someone uses an LZW decompressor such as the one in <code>ppmtogif</code> or pretty much any graphics display program to process the output of <code>ppmtogif -nolzw </code> he is then using the LZW patent. But the patent holder has expressed far less interest in enforcing the patent on decoding than on encoding. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-giftopnm/">giftopnm</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/1-pngtopnm/">pngtopnm</a></code>(1), <code><a href="/docs/linux/man/1-gifsicle/">gifsicle</a></code>(1) &lt;<a rel="nofollow" href="http://www.lcdf.org/gifsicle">http://www.lcdf.org/gifsicle</a>&gt;, <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> Based on GIFENCOD by David Rowley &lt;mgardi [at] watdcsu.waterloo.edu&gt;. Lempel-Ziv compression based on &quot;compress&quot;. </p>
<p> The non-LZW format is generated by code based on <code>djpeg</code> by the Independent Jpeg Group. </p>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>LICENSE</h2>
<p> If you use <code>ppmtogif</code> without the <code>-nolzw</code> option, you are using a patent on the LZW compression method which is owned by Unisys, and in all probability you do not have a license from Unisys to do so. Unisys typically asks $5000 for a license for trivial use of the patent. Unisys has never enforced the patent against trivial users. The patent expires in 2003. </p>
<p> Rumor has it that IBM also owns a patent covering <code>ppmtogif</code>. </p>
<p> A replacement for the GIF format that does not require any patents to use is the PNG format. </p>
<h2>Index</h2>
