---
title: "pamtogif(1)"
name: "pamtogif"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtogif/"
description: "pamtogif – convert a Netpbm image to a GIF image"
---

<h2 class="name">NAME</h2>
<p> pamtogif &#8211; convert a Netpbm image to a GIF image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtogif</code> </p>
<p> [<code>-interlace</code>] </p>
<p> [<code>-sort</code>] </p>
<p> [<code>-mapfile=</code><i>mapfile</i>] [<code>-transparent=</code>[<code>=</code>]<i>color</i>] </p>
<p> [<code>-alphacolor=</code><i>color</i>] </p>
<p> [<code>-comment=</code><i>text</i>] </p>
<p> [<code>-nolzw</code>] </p>
<p> [<code>-aspect=</code><i>fraction</i>] </p>
<p> [<code>-verbose</code>] [<i>netpbmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtogif</code> reads a Netpbm image as input and produces a GIF file as output. </p>
<p> This program creates only individual GIF images. To combine multiple GIF images into an animated GIF, use <code>gifsicle</code> (not part of the Netpbm package). </p>
<p> <code>pamtogif</code> creates either an original GIF87 format GIF file or the newer GIF89 format. It creates GIF89 when you request features that were new with GIF89, to wit the <code>-transparent</code> or <code>-comment</code> options. Otherwise, it creates GIF87. Really old GIF readers conceivably could not recognize GIF89. </p>
<p> The GIF format is not capable of representing an image with more than 256 colors in it (it contains a color map with a maximum size of 256). If the image you want to convert has more colors than that (<code>ppmhist</code> can tell you), you can use <code>pnmquant</code> to reduce it to 256. </p>
<p> If your input image is a PAM with transparency information, <code>ppmtogif</code> uses one entry in the GIF colormap specifically for the transparent pixels, so you can have at most 255 opaque colors. In contrast, if you use the <code>-transparent</code> option, one of the colors from the input becomes transparent, so the limit is still 256. </p>
<p> <code>pamtogif</code> was new in Netpbm 10.37 (December 2006). In older Netpbm, use <code>ppmtogif</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-interlace</code></p>
<dd> Produce an interlaced GIF file. </p>
<dt><code>-sort</code></p>
<dd> Produce a GIF file with a color map sorted in a predictable order. </p>
<p> This does <i>not</i> produce the sorted color map which is part of the GIF format. That kind of sorted color map is one where the colors are sorted according to how important they are, and the GIF header tells the viewer that it is sorted that way. Its purpose is to allow the viewer to use fewer colors than are in the color map if it is not capable of displaying all the colors. </p>
<p> What this option produces is a color map sorted by red value, then green, then blue. That can be useful in analyzing GIF images, particularly those made with two versions of the program, because it removes some of the variability. </p>
<dt><code>-mapfile=</code><i>mapfile</i></p>
<dd>
<p> Use the colors found in the file <i>mapfile</i> to create the colormap in the GIF file, instead of the colors from <i>netpbmfile</i>. <i>mapfile</i> can be any PPM file; all that matters is the colors in it. If the colors in <i>netpbmfile</i> do not match those in <i>mapfile</i>, <code>pamtogif</code> matches them to a &#8216;best match.&#8217; You can obtain a much better result by using <code>pnmremap</code> to change the colors in the input to those in the map file. </p>
<p> The <i>mapfile</i> file is not a palette file, just an image whose colors you want to use. The order of colors in the GIF palette have nothing to do with where they appear in the <i>mapfile</i> image, and duplication of colors in the image is irrelevant. </p>
<p> The map file&#8217;s depth must match the number of color components in the input (which is not necessarily the same as the input&#8217;s depth &#8212; the input might have an alpha plane in addition). If your map file does not, or it <i>might</i> not, run your input through <code>pnmremap</code> using the same map file so that it does. </p>
<dt><code>-transparent=</code><i>color</i></p>
<dd> <code>pamtogif</code> marks the specified color as transparent in the GIF image. </p>
<p> If you don&#8217;t specify <code>-transparent</code>, <code>pamtogif</code> does not mark any color transparent (except as indicated by the transparency information in the input file). </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> If the color you specify is not present in the image, <code>pamtogif</code> selects instead the color in the image that is closest to the one you specify. Closeness is measured as a Cartesian distance between colors in RGB space. If multiple colors are equidistant, <code>pamtogif</code> chooses one of them arbitrarily. </p>
<p> However, if you prefix your color specification with &#8216;=&#8217;, e.g. <code>-transparent==red</code>, only the exact color you specify will be transparent. If that color does not appear in the image, there will be no transparency. <code>pamtogif</code> issues an information message when this is the case. </p>
<p> When you specify <code>-transparent</code>, <code>pamtogif</code> ignores explicit transparency information (the &#8216;alpha channel&#8217;) in the input image. </p>
<dt><code>-alpha=</code><i>pgmfile</i></p>
<dd> There is no <code>-alpha</code> option. <code>pamtogif</code>&#8216;s predecessor had such an option because it was not capable of taking PAM input that contains a transparency (alpha) plane, so one used this option to supply a transparency plane as a separate PGM file. </p>
<p>&nbsp;<wbr>This option names a PGM file that contains an alpha mask for the image. <code>pamtogif</code> creates fully transparent pixels wherever the alpha mask indicates transparency greater than 50%. The color of those pixels is that specified by the <code>-alphacolor</code> option, or black by default. </p>
<p> To do this, <code>pamtogif</code> creates an entry in the GIF colormap in addition to the entries for colors that are actually in the image. It marks that colormap entry as transparent and uses that colormap index in the output image to create a transparent pixel. </p>
<p>&nbsp;<wbr>The alpha image must be the same dimensions as the input image, but may have any maxval. White means opaque and black means transparent. </p>
<p>&nbsp;<wbr>You cannot specify both&nbsp;<wbr><code>-transparent</code>&nbsp;<wbr>and&nbsp;<wbr><code>-alpha</code>.&nbsp;<wbr>&nbsp;<wbr> </p>
<dt><code>-alphacolor=</code><i>color</i></p>
<dd> This specifies the foreground color for transparent pixels. A viewer may use the foreground color for a transparent pixel if it chooses not to have another color &#8216;show through.&#8217;. The default is black. </p>
<p> This applies only to pixels that are transparent in the GIF because they are transparent in the Netpbm input. If a GIF pixel is transparent because of the <code>-transparent</code> option, the foreground color is the color indicated by that option. </p>
<p> Note that in GIF, all transparent pixels have the same foreground color. (There is only one entry in the GIF colormap for transparent pixels). </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<dt><code>-comment=</code><i>text</i></p>
<dd> Include a comment in the GIF output with comment text <i>text</i>. </p>
<p> Without this option, there are no comments in the output. </p>
<p> Note that in a command shell, you&#8217;ll have to use quotation marks around <i>text</i> if it contains characters (e.g. space) that would make the shell think it is multiple arguments: </p>
<pre>
$ pamtogif -comment &quot;this is a comment&quot; &lt;xxx.ppm &gt;xxx.gif
</pre>
<dt><code>-nolzw</code></p>
<dd>
<p> This option is mainly of historical interest &#8212; it involves use of a patent that is now expired. </p>
<p> This option causes the GIF output, and thus <code>pamtogif</code>, not to use LZW (Lempel-Ziv) compression. As a result, the image file is larger and, before the patent expired, no royalties would be owed to the holder of the patent on LZW. See the section LICENSE below. </p>
<p> LZW is a method for combining the information from multiple pixels into a single GIF code. With the <code>-nolzw</code> option, <code>pamtogif</code> creates one GIF code per pixel, so it is not doing any compression and not using LZW. However, any GIF decoder, whether it uses an LZW decompressor or not, will correctly decode this uncompressed format. An LZW decompressor would see this as a particular case of LZW compression. </p>
<p> Note that if someone uses an LZW decompressor such as the one in <code>giftopnm</code> or pretty much any graphics display program to process the output of <code>pamtogif -nolzw </code>, he is then using the LZW patent. But the patent holder expressed far less interest in enforcing the patent on decoding than on encoding. </p>
<dt><code>-aspect=</code><i>fraction</i></p>
<dd> This is the aspect ratio of the pixels of the image. Its only effect is to record that information in the GIF for use by whatever interprets the GIF. Note that this feature of GIF is hardly ever used and most GIF decoders ignore this information and assume pixels are square. </p>
<p> Pixels in a Netpbm image do not have aspect ratios; there is always a one-one correspondence between GIF pixels and Netpbm pixels. </p>
<p> The aspect ratio is the quotient of width divided by height. GIF allows aspect ratios from 0.25 (1:4) to 4 (4:1) in increments of 1/64. <code>pamtogif</code> implements a natural extension of GIF that allows an aspect ratio up to 4 14/64. If you specify anything outside this range, <code>pamtogif</code> fails. <code>pamtogif</code> rounds <i>fraction</i> to the nearest 1/64. </p>
<p> The default is square (1.0). </p>
<p> This option was new in Netpbm 10.38 (March 2007). Before that, the pixels are always square. </p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pamtogif</code> to display information about the conversion process and the image it produces. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-giftopnm/">giftopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtogif/">ppmtogif</a></code>(1) , </p>
<p> <code>gifsicle</code> <a rel="nofollow" href="http://www.lcdf.org/gifsicle">http://www.lcdf.org/gifsicle</a> , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtogif</code> was new in Netpbm 10.37 (December 2006). It replaced <code>ppmtogif</code>, which created GIF images for Pbmplus/Netpbm users since 1989. </p>
<p> The main outward change in the conversion from <code>ppmtogif</code> to <code>pamtogif</code> was that <code>pamtogif</code> was able to use transparency information (&#8216;alpha channel&#8217;) in PAM input, whereas with <code>ppmtogif</code>, one had to supply the transparency mask in a separate pseudo-PGM image (via the <code>-alpha</code> option). </p>
<p> Jef Poskanzer wrote <code>ppmtogif</code> in 1989, and it has always been a cornerstone of Pbmplus/Netpbm because GIF is such a popular image format. Jef based the LZW encoding on GIFENCOD by David Rowley &lt;<i>mgardi [at] watdcsu.waterloo.edu</i>&gt;. Jef included GIFENCOD&#8217;s GIFCOMPR.C file pretty much whole. Rowley, in turn, adapted the LZW compression code from classic Unix <code>compress</code>, which used techniques described in IEEE Computer, June 1984. </p>
<p> Jef&#8217;s <code>ppmtogif</code> notably lacked the ability to use a transparency mask with it. You could create transparent pixels in a GIF, but only with the <code>-transparent</code> option, which allowed one to specify that all pixels of a certain color in the input were to be transparent. Bryan Henderson added the <code>-alpha</code> option in July 2001 so you could supply a mask image that indicates exactly which pixels are to be transparent, and those pixels could have the same color as other opaque ones. </p>
<p> Bryan Henderson added another significant piece of code and function in October 2001: the ability to generate a GIF without using the LZW patent &#8212; an uncompressed GIF. This was very important to many people at the time because the GIF patent was still in force, and this allowed them to make an image that any GIF viewer could display, royalty-free. Bryan adapted code from the Independent JPEG Group&#8217;s <code>djpeg</code> for that. </p>
<p> There is no code in <code>pamtogif</code> from Jef&#8217;s original, but Jef may still hold copyright over it due to the way in which it evolved. Virtually all of the code in <code>pamtogif</code> was written by Bryan Henderson and contributed to the public domain. </p>
<h2>LICENSE</h2>
<p> If you use <code>pamtogif</code> without the <code>-nolzw</code> option, you are using a patent on the LZW compression method which is owned by Unisys. The patent has expired (in 2003 in the US and in 2004 elsewhere), so it doesn&#8217;t matter. While the patent was in force, most people who used <code>pamtogif</code> and similar programs did so without a license from Unisys to do so. Unisys typically asked $5000 for a license for trivial use of the patent. Unisys never enforced the patent against trivial users. </p>
<p> Rumor has it that IBM also owns or owned a patent covering <code>pamtogif</code>. </p>
<p> A replacement for the GIF format that never required any patents to use is the PNG format. </p>
<h2>Index</h2>
