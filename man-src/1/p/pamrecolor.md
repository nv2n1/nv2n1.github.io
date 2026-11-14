---
title: "pamrecolor(1)"
name: "pamrecolor"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamrecolor/"
description: "pamrecolor – alter colors without affecting luminance"
---

<h2 class="name">NAME</h2>
<p> pamrecolor &#8211; alter colors without affecting luminance</p>
<h2>SYNOPSIS</h2>
<p> <code>pamrecolor</code> [<code>&#8211;colorspace</code>=<i>name</i>] [<code>&#8211;rmult</code>=<i>fraction</i>] [<code>&#8211;gmult</code>=<i>fraction</i>] [<code>&#8211;bmult</code>=<i>fraction</i>] [<code>&#8211;targetcolor</code>=<i>color</i>] [<code>&#8211;colorfile</code>=<i>file</i>] [<code>-randomseed=</code><i>integer</i>] </p>
<p> [<i>infile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamrecolor</code> changes an image&#8217;s colors to be as close as possible to given target colors but with the constraint that the luminance not be modified. That is, the original image and the target image will look identical if both are converted to grayscale (e.g. with <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) ). You can have <code>pamrecolor</code> select target colors randomly, specify a single hue for the entire image, or take the target colors from a target image. </p>
<p> <code>pamrecolor</code> works on pseudo-Netpbm images based on arbitrary color spaces. You can define the color space explicitly or choose on of many that <code>pamrecolor</code> knows by name. </p>
<p> The output is a PAM image on standard output. Options control the exact format of the PAM. If you want a PNM (PBM, PGM, or PPM) image, use <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1)<br />
&nbsp;<wbr>on the output.&nbsp;<wbr>&nbsp;<wbr>There is no need to convert if you will use the image as input to a current Netpbm program, but many other programs don&#8217;t know what a PAM is. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;colorspace</code>=<i>name</i></p>
<dd> Designate the color space to use for determining the contribution to luminance of each of the red, green, and blue color channels. For example, in the SMPTE-C color space an RGB color is converted to grayscale by multiplying the red channel by 0.2124132, the green channel by 0.7010437, and the blue channel by 0.0865432 and summing the resulting three products. </p>
<p> When you use this option, the input and output images are not true Netpbm images, because the Netpbm image format specifies a particular color space. Instead, you are using a variation on the format in which the sample values in the raster have different meaning. Many programs that ostensibly use Netpbm images actually use a variation with a different color space, For example, GIMP uses sRGB internally and if you have GIMP generate a Netpbm image file, it really generates a variation of the format that uses sRGB. </p>
<p> <code>pamrecolor</code> knows the following color spaces (<i>name</i> values): </p>
<dt>adobe</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Adobe RGB (1998) with a D65 reference white </p>
<dt>apple</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Apple RGB with a D65 reference white </p>
<dt>cie</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> CIE with an Illuminant E reference white </p>
<dt>ntsc</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> NTSC RGB with an Illuminant C reference white </p>
<dt>pal</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> PAL/SECAM with a D65 reference white </p>
<dt>smpte-c</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> SMPTE-C with a D65 reference white </p>
<dt>srgb</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> sRGB with a D65 reference white </p>
<dt>wide</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Wide-gamut RGB with a D50 reference white </p>
<p> The default is &lt;q&gt;ntsc&lt;/q&gt; because this is the color space that the Netpbm format of Netpbm and many other graphics utilities. As a counterexample, GIMP uses sRGB as its native color space. </p>
<p> The luminance values <code>pamrecolor</code> uses for each of the above come from Bruce Lindbloom&#8217;s Computing RGB-to-XYZ and XYZ-to-RGB matrices (1)<br />
&nbsp;<wbr>page. </p>
<dt><code>&#8211;rmult</code>=<i>fraction</i></p>
<dd>
<dt><code>&#8211;gmult</code>=<i>fraction</i></p>
<dd>
<dt><code>&#8211;bmult</code>=<i>fraction</i></p>
<dd> Instead of selecting a color space by name, you can specify explicitly the contribution of each color channel to the overall luminance as red, green, and blue multipliers. These three options must be used together, and the three <i>fraction</i> values must sum to 1.0. For example, you can specify the ProPhoto (ROMM) RGB color space with &lt;q&gt;<code>&#8211;rmult</code>=0.2880402 <code>&#8211;gmult</code>=0.7118741 <code>&#8211;bmult</code>=0.0000857&lt;/q&gt;. </p>
<dt><code>&#8211;targetcolor</code>=<i>color</i></p>
<dd> Designate <i>color</i> as the target color for the image. <code>pamrecolor</code> will make each pixel as close as possible to <i>color</i> subject to the constraint that the luminance must stay the same as in the original image. Specify <i>color</i> as in the argument of the <code>ppm_parsecolor()</code> library routine (e.g.,&nbsp;<wbr>&lt;q&gt;hotpink&lt;/q&gt; or &lt;q&gt;#ff69b4&lt;/q&gt;). </p>
<p> If you specify neither <code>&#8211;targetcolor</code> nor <code>&#8211;colorfile</code>, <code>pamrecolor</code> will randomly select a target color for each pixel of the input image. </p>
<p> You may not specify both <code>-targetcolor</code> and <code>-colorfile</code>. </p>
<dt><code>&#8211;colorfile</code>=<i>file</i></p>
<dd> Take per-pixel target colors from Netpbm file <i>file</i> instead of using a single target color for the entire image. <i>file</i> should be a PPM or color PAM image. If the image in the file wider or taller than the input image, <code>pamrecolor</code> uses only the left and top part of it. If the image is narrower or shorter, <code>pamrecolor</code> considers the image to be repeated in a tile pattern. </p>
<p> If you specify neither <code>&#8211;targetcolor</code> nor <code>&#8211;colorfile</code>, <code>pamrecolor</code> will randomly select a target color for each pixel of the input image. </p>
<p> You may not specify both <code>-targetcolor</code> and <code>-colorfile</code>. </p>
<dt><code>-randomseed=</code><i>integer</i></p>
<dd> This is the seed for the random number generator that generates the pixels. </p>
<p> Use this to ensure you get the same image on separate invocations. </p>
<p> By default, <code>pamrecolor</code> uses a seed derived from the time of day and process ID, which gives you fairly uncorrelated results in multiple invocations. </p>
<p> This option was new in Netpbm 10.61 (December 2012). </p>
</dl>
<h2>EXAMPLES</h2>
<p> This command tints an image yellow: </p>
<pre>
    pamrecolor --targetcolor=yellow colorpic.pam &gt; yellowpic.pam
</pre>
<p> This command takes the colors from <code>colorpicture.ppm</code> and applies them to <code>graypicture.pgm</code>: </p>
<pre>
    pamrecolor --colorfile=colorpic.ppm graypic.pgm &gt; colorizedpic.pam
</pre>
<p> The grayscale version of <code>colorizedpic.pam</code> will look just like graypic.pgm. Note that if you use a non-Netpbm tool to do the conversion to grayscale, you may additionally need to specify an appropriate <code>&#8211;colorspace</code> value for your conversion tool. </p>
<h2>NOTES</h2>
<p> Here are a couple of fun special effects you can produce with <code>pamrecolor</code>: </p>
<dl>
<dt>&bull;</p>
<dd> Specify a color file that is identical to the input image but with some large, colored text added to it. The text will &lt;q&gt;magically&lt;/q&gt; vanish when the image is converted to grayscale. </p>
<dt>&bull;</p>
<dd> Provide a low-contrast grayscale image &amp;mdash; perhaps a secret message written in similar shades of gray &amp;mdash; as the input file and a colorful but completely different image as the color file. If done carefully, the grayscale image can be hidden by the colorful image. Only people who know to convert the result to grayscale can recover the original grayscale image. </p>
<dt>&bull;</p>
<dd> Use <code>&#8211;targetcolor</code>=tan to make an image look like an old-timey photograph (or, more precisely, a sepia-toned photograph of the late 1800s). </p>
</dl>
<h2>HISTORY</h2>
<p> Scott Pakin wrote <code>pamrecolor</code> in July 2010. </p>
<p> <code>pamrecolor</code> was new in Netpbm 10.52 (September 2010). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2010 Scott Pakin, <i>scott+pbm [at] pakin.org.</i> </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmchange/">ppmchange</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1) </p>
</dl>
<h2>Index</h2>
