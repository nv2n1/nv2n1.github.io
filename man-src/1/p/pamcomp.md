---
title: "pamcomp(1)"
name: "pamcomp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamcomp/"
description: "pamcomp – composite (overlay) two Netpbm images together"
---

<h2 class="name">NAME</h2>
<p> pamcomp &#8211; composite (overlay) two Netpbm images together</p>
<h2>SYNOPSIS</h2>
<p> <code>pamcomp</code> </p>
<p> [<code>-align=</code>{<code>left</code>|<code>center</code>|<code>right</code>| <code>beyondleft</code>|<code>beyondright</code>}] [<code>-valign=</code>{<code>top</code>|<code>middle</code>|<code>bottom</code>| <code>above</code>|<code>below</code>}] [<code>-xoff=</code><i>X</i>] [<code>-yoff=</code><i>Y</i>] [<code>-alpha=</code><i>alpha-pgmfile</i>] [<code>-invert</code>] [<code>-opacity=</code><i>opacity</i>] [<code>-mixtransparency</code>] [<code>-linear</code>] <i>overlay_file</i> [<i>underlying_file</i> [<i>output_file</i>]] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamcomp</code> reads two images and produces a composite image with one of the images overlayed on top of the other, possible translucently. The images need not be the same size. The input and outputs are Netpbm format image files. </p>
<p> In its simplest use, <code>pamcomp</code> simply places the image in the file <i>overlay_file</i> on top of the image in the file <i>underlying_file</i>, blocking out the part of <i>underlying_file</i> beneath it. </p>
<p> If you add the <code>-alpha</code> option, then <code>pamcomp</code> uses the image in file <i>alpha-pgmfile</i> as an alpha mask, which means it determines the level of transparency of each point in the overlay image. The alpha mask must have the same dimensions as the overlay image. In places where the alpha mask defines the overlay image to be opaque, the composite output contains only the contents of the overlay image; the underlying image is totally blocked out. In places where the alpha mask defines the overlay image to be transparent, the composite output contains none of the overlay image; the underlying image shows through completely. In places where the alpha mask shows a value in between opaque and transparent (translucence), the composite image contains a mixture of the overlay image and the underlying image and the level of translucence determines how much of each. </p>
<p> The alpha mask is a PGM file in which a white pixel represents opaqueness and a black pixel transparency. Anything in between is translucent. (Like any Netpbm program, <code>pamcomp</code> will see a PBM file as if it is PGM). </p>
<p> If the overlay image is a PAM image of tuple type RGB_ALPHA or GRAYSCALE_ALPHA, then the overlay image contains transparency information itself and <code>pamcomp</code> uses it the same way as the alpha mask described above. If you supply both an overlay image that has transparency information and an alpha mask, <code>pamcomp</code> multiplies the two opacities to get the opacity of the overlay pixel. </p>
<p> Before Netpbm 10.25 (October 2004), <code>pamcomp</code> did not recognize the transparency information in a PAM image &#8212; it just ignored it. So people had to make appropriate alpha masks in order to have a non-opaque overlay. Some Netpbm programs that convert from image formats that contain transparency information are not able to create RGB_ALPHA or GRAYSCALE_ALPHA PAM output, so you have to use the old method &#8212; extract the transparency information from the original into a separate alpha mask and use that as input to <code>pamcomp</code>. </p>
<p> The output image is always of the same dimensions as the underlying image. <code>pamcomp</code> uses only parts of the overlay image that fit within the underlying image. </p>
<p> The output image is a PAM image. Its tuples are color, grayscale, or black and white, whichever is the &#8216;highest&#8217; format between the two input images. The maxval of the output is the least common multiple of the maxvals of the input, up to the maximum possible PAM maxval, 65535. </p>
<p> The output has an opacity channel if and only if the underlying image does, and then the opacities are as described under the <code>-mixtransparency</code> option. Before Netpbm 10.56 (September 2011), the output never has an opacity channel. </p>
<p> To specify where on the underlying image to place the overlay image, use the <code>-align</code>, <code>-valign</code>, <code>-xoff</code>, and <code>-yoff</code> options. Without these options, the default horizontal position is flush left and the default vertical position is flush top. </p>
<p> The overlay image, in the position you specify, need not fit entirely within the underlying image. <code>pamcomp</code> uses only the parts of the overlay image that appear above the underlying image. It is possible to specify positioning such that <i>none</i> of the overlay image is over the underlying image &#8212; i.e. the overlay is out of frame. If you do that, <code>pamcomp</code> issues a warning. </p>
<p>&nbsp;<wbr>The overlay and underlying images may be of different formats (e.g. overlaying a PBM text image over a full color PPM image) and have different maxvals. The output image has the more general of the two input formats and a maxval that is the least common multiple the two maxvals (or the maximum maxval allowable by the format, if the LCM is more than that). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-align=</code><i>alignment</i></p>
<dd> This option selects the basic horizontal position of the overlay image with respect to the underlying image, in syntax reminiscent of HTML. <code>left</code> means flush left, <code>center</code> means centered, and <code>right</code> means flush right. </p>
<p> The <code>-xoff</code> option modifies this position. </p>
<p> <code>beyondleft</code> means just out of frame to the left &#8212; the right edge of the overlay is flush with the left edge of the underlying image. <code>beyondright</code> means just out of frame to the right. These alignments are useful only if you add a <code>-xoff</code> option. These two values were added in Netpbm 10.10 (October 2002). </p>
<p> The default is <code>left</code>. </p>
<dt><code>-valign=</code><i>alignment</i></p>
<dd> This option selects the basic vertical position of the overlay image with respect to the underlying image, in syntax reminiscent of HTML. <code>top</code> means flush top, <code>middle</code> means centered, and <code>bottom</code> means flush bottom. </p>
<p> The <code>-yoff</code> option modifies this position. </p>
<p> <code>above</code> means just out of frame to the top &#8212; the bottom edge of the overlay is flush with the top edge of the underlying image. <code>below</code> means just out of frame to the bottom. These alignments are useful only if you add a <code>-yoff</code> option. These two values were added in Netpbm 10.10 (October 2002). </p>
<p> The default is <code>top</code>. </p>
<dt><code>-xoff=</code><i>x</i></p>
<dd> This option modifies the horizontal positioning of the overlay image with respect to the underlying image as selected by the <code>-align</code> option. <code>pamcomp</code> shifts the overlay image from that basic position <i>x</i> pixels to the right. <i>x</i> can be negative to indicate shifting to the left. </p>
<p> The overlay need not fit entirely (or at all) on the underlying image. <code>pamcomp</code> uses only the parts that lie over the underlying image. </p>
<p> Before Netpbm 10.10 (October 2002), <code>-xoff</code> was mutually exclusive with <code>-align</code> and always measured from the left edge. </p>
<dt><code>-yoff=</code><i>y</i></p>
<dd> This option modifies the vertical positioning of the overlay image with respect to the underlying image as selected by the <code>-valign</code> option. <code>pamcomp</code> shifts the overlay image from that basic position <i>y</i> pixels downward. <i>y</i> can be negative to indicate shifting upward. </p>
<p> The overlay need not fit entirely (or at all) on the underlying image. <code>pamcomp</code> uses only the parts that lie over the underlying image. </p>
<p> Before Netpbm 10.10 (October 2002), <code>-xoff</code> was mutually exclusive with <code>-valign</code> and always measured from the top edge. </p>
<dt><code>-alpha=</code><i>alpha-pgmfile</i></p>
<dd> This option names a file that contains the alpha mask. If you don&#8217;t specify this option, there is no alpha mask, which is equivalent to having an alpha mask specify total opaqueness everywhere. </p>
<p> You can specify <code>&#8211;</code> as the value of this option and the alpha mask will come from Standard Input. If you do this, don&#8217;t specify Standard Input as the source of any other input image. </p>
<dt><code>-invert</code></p>
<dd> This option inverts the sense of the values in the alpha mask, which effectively switches the roles of the overlay image and the underlying image in places where the two intersect. </p>
<dt><code>-opacity=</code><i>opacity</i></p>
<dd> This option tells how opaque the overlay image is to be, i.e. how much of the composite image should be from the overlay image, as opposed to the underlying image. <i>opacity</i> is a floating point number, with 1.0 meaning the overlay image is totally opaque and 0.0 meaning it is totally transparent. The default is 1.0. </p>
<p> If you specify an alpha mask (the <code>-alpha</code> option), <code>pamcomp</code> uses the product of the opacity indicated by the alpha mask (as modified by the <code>-invert</code> option, as a fraction, and this opacity value. The <code>-invert</code> option does not apply to this opacity value. </p>
<p> As a simple opacity value, the value makes sense only if it is between 0 and 1, inclusive. However, <code>pamcomp</code> accepts all values and performs the same arithmetic computation using whatever value you provide. An opacity value less than zero means the underlay image is intensified and then the overlay image is &quot;subtracted&quot; from it. An opacity value greater than unity means the overlay image is intensified and the underlaying image subtracted from it. In either case, <code>pamcomp</code> clips the resulting color component intensities so they are nonnegative and don&#8217;t exceed the output image&#8217;s maxval. </p>
<p> This may seem like a strange thing to do, but it has uses. You can use it to brighten or darken or saturate or desaturate areas of the underlaying image. See this description (1)<br />
&nbsp;<wbr>of the technique. </p>
<p> This option was added in Netpbm 10.6 (July 2002). Before Netpbm 10.15 (April 2003), values less than zero or greater than unity were not allowed. </p>
<dt><code>-mixtransparency</code></p>
<dd> This option controls what <code>pamcomp</code> does where both the underlying and overlay image are non-opaque. </p>
<p> By default, the output image has the same transparency as the underlying image and the transparency of the underlying image has no effect on the composition of color. </p>
<p> But with this option, <code>pamcomp</code> composes the image according to a plastic transparency metaphor: the underlying and overlay images are plastic slides. The output image is the slide you get when you stack up those two slides. So the transparency of the output is a combination of the transparency of the inputs and the transparency of the underlying image affects the underlying image&#8217;s contribution to the output image&#8217;s color. </p>
<p> Unlike the metaphorical slide, a PAM pixel has a color even where it is completely transparent, so <code>pamcomp</code> departs from the metaphor in that case and makes the output color identical to the underlying image. </p>
<p> This option was new in Netpbm 10.56 (September 2011). Before that, the output is always opaque and the <code>pamcomp</code> ignores the transparency of the underlying image. </p>
<dt><code>-linear</code></p>
<dd> This option indicates that the inputs are not true Netpbm images but rather a non-gamma-adjusted variation. This is relevant only when you mix pixels, using the <code>-opacity</code> option or an alpha mask (the <code>-alpha</code> option). </p>
<p> The alpha mask and <code>-opacity</code> values indicate a fraction of the light intensity of a pixel. But the PNM and PNM-equivalent PAM image formats represent intensities with gamma-adjusted numbers that are not linearly proportional to intensity. So <code>pamcomp</code>, by default, performs a calculation on each sample read from its input and each sample written to its output to convert between these gamma-adjusted numbers and internal intensity-proportional numbers. </p>
<p> Sometimes you are not working with true PNM or PAM images, but rather a variation in which the sample values are in fact directly proportional to intensity. If so, use the <code>-linear</code> option to tell <code>pamcomp</code> this. <code>pamcomp</code> then will skip the conversions. </p>
<p> The conversion takes time. And the difference between intensity-proportional values and gamma-adjusted values may be small enough that you would barely see a difference in the result if you just pretended that the gamma-adjusted values were in fact intensity-proportional. So just to save time, at the expense of some image quality, you can specify <code>-linear</code> even when you have true PPM input and expect true PPM output. </p>
<p> For the first 13 years of Netpbm&#8217;s life, until Netpbm 10.20 (January 2004), <code>pamcomp</code>&#8216;s predecessor <code>pnmcomp</code> always treated the PPM samples as intensity-proportional even though they were not, and drew few complaints. So using <code>-linear</code> as a lie is a reasonable thing to do if speed is important to you. </p>
<p> Another technique to consider is to convert your PNM image to the linear variation with <code>pnmgamma</code>, run <code>pamcomp</code> on it and other transformations that like linear PNM, and then convert it back to true PNM with <code>pnmgamma -ungamma</code>. <code>pnmgamma</code> is often faster than <code>pamcomp</code> in doing the conversion. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmmix/">ppmmix</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a></code>(1)<br />
&nbsp;<wbr>are simpler, less general versions of the same tool. </p>
<p> <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pbmmask/">pbmmask</a></code>(1) , and <code><a href="/docs/linux/man/1-pambackground/">pambackground</a></code>(1)<br />
&nbsp;<wbr>can help with generating an alpha mask. </p>
<p> <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1)<br />
&nbsp;<wbr>is an older program that runs faster, but has less function. </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamcomp</code> was new in Netpbm 10.21 (March 2004). Its predecessor, <code>pnmcomp</code>, was one of the first programs added to Netpbm when the project went global in 1993. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992 by David Koblas (<i>koblas [at] mips.com</i>). </p>
<h2>Index</h2>
