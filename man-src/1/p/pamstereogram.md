---
title: "pamstereogram(1)"
name: "pamstereogram"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamstereogram/"
description: "pamstereogram – create a single-image stereogram from a PAM depth map"
---

<p>Updated:30 December 2012 </p>
<h2 class="name">NAME</h2>
<p> pamstereogram &#8211; create a single-image stereogram from a PAM depth map</p>
<h2>SYNOPSIS</h2>
<p> <code>pamstereogram</code> [<code>-help</code>] [<code>-verbose</code>] [<code>-blackandwhite</code> | <code>-grayscale</code> | <code>-color</code>] [<code>-maxval=</code><i>value</i>] [<code>-patfile=</code><i>pamfile</i>] [<code>-texfile=</code><i>pamfile</i>] [<code>-bgcolor=</code><i>color</i>] [<code>-smoothing=</code><i>pixels</i>] [<code>-xshift=</code><i>pixels</i>] [<code>-yshift=</code><i>pixels</i>] [<code>-magnifypat=</code><i>scale</i>] [<code>-guidetop</code>] [<code>-guidebottom</code>] [<code>-guidesize=</code><i>pixels</i>] [<code>-dpi=</code><i>resolution</i>] [<code>-crosseyed</code>] [<code>-makemask</code>] [<code>-eyesep=</code><i>inches</i>] [<code>-depth=</code><i>fraction</i>] [<code>-planes=</code><i>near_pixels</i>,<i>far_pixels</i>] [<code>-randomseed=</code><i>integer</i>] [<i>infile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamstereogram</code> inputs a depth map (a map of the distances from your eye of the points in a scene) and outputs a single-image stereogram (SIS). A SIS is a 2-D image specially designed to appear three dimensional when viewed with relaxed, slightly unfocused eyes. What&#8217;s exciting about single-image stereograms is that they don&#8217;t require special glasses to view, although it does require a bit of practice to train your eyes to unfocus properly. The <code>pamstereogram</code> program provides a wealth of control over how the stereogram is generated, including the following: </p>
<dl>
<dt>&bull;</p>
<dd> black and white, grayscale, or color output </p>
<dt>&bull;</p>
<dd> single-image random-dot stereograms (SIRDS), single-image stereograms (SIS) using a tiled image, or mapped-texture stereograms (MTS) </p>
<dt>&bull;</p>
<dd> images targeting a given device resolution and eye separation </p>
<dt>&bull;</p>
<dd> optional guide boxes to assist in focusing </p>
<dt>&bull;</p>
<dd> the ability to trade off depth levels for easier viewing </p>
<dt>&bull;</p>
<dd> choice of wall-eyed or cross-eyed stereograms </p>
</dl>
<p> The output is a PAM image on standard output. Options control the exact format of the PAM. If you want a PNM (PBM, PGM, or PPM) image, use <code>pamtopnm</code> on the output. There is no need to convert if you will use the image as input to a current Netpbm program, but many other programs don&#8217;t know what a PAM is. </p>
<p> To make a red/green type of stereogram (that you view with 3-D glasses) instead, see <code>ppm3d</code>. </p>
<h2>OPTIONS</h2>
<p> You may use either single or double hyphens to denote options. You may use either whitespace or an equals sign to separate an option name from its value. </p>
<dl>
<dt><code>-verbose</code></p>
<dd> Display messages about image sizes and formats and properties of the stereogram being generated. </p>
<dt><code>-blackandwhite</code></p>
<dd> Produce a single-image random-dot black-and-white stereogram. This is the default. </p>
<dt><code>-grayscale</code></p>
<dd> Produce a single-image random-dot grayscale stereogram. </p>
<dt><code>-color</code></p>
<dd> Produce a single-image random-dot color stereogram. </p>
<dt><code>-maxval=</code><i>value</i></p>
<dd> Designate the maximum value of each gray/color component, i.e. the color resolution. Smaller values make the output image have smaller numbers of unique grays/colors. If you don&#8217;t specify <code>-maxval</code>, <code>pamstereogram</code> uses the maxval of the input image. This option has no effect with <code>-blackandwhite</code>. </p>
<dt><code>-patfile=</code><i>pamfile</i></p>
<dd> Specify an image to use as a repeated background pattern for the stereogram instead of a random-dot pattern. Intricate images generally produce a crisper 3-D effect that simpler images. The output file will have the same maxval and format (black and white, grayscale or color) as the pattern file. You cannot specify the <code>-patfile</code> option along with <code>-blackandwhite</code>, <code>-grayscale</code>, <code>-color</code>, or <code>-maxval</code>. </p>
<dt><code>-texfile=</code><i>pamfile</i></p>
<dd> Specify an image to use as the texture for a mapped-texture stereogram. The idea is that the depth-map image provides the depth values of the 3-D object/scene while the texture image provides the true-color values. Consequently, the texture image should align with the depth-map image. (Note that it&#8217;s required to have the same dimensions.) The texture image&#8217;s background color is ignored when blending colors. </p>
<p> This option was new in Netpbm 10.53 (December 2010). </p>
<dt><code>-bgcolor=</code><i>color</i></p>
<dd> Use <i>color</i> as the texture image&#8217;s background color instead of letting <code>pamstereogram</code> determine it automatically. Specify the color as described for the argument of the ppm_parsecolor() library routine . The <code>-bgcolor</code> option is meaningful only in conjunction with <code>-texfile</code>. </p>
<p> This option was new in Netpbm 10.53 (December 2010). </p>
<dt><code>-smoothing=</code><i>pixels</i></p>
<dd> When used without <code>-texfile</code>, attempt to eliminate artifacts introduced by edges in the depth map if <i>pixels</i> is greater than zero. </p>
<p> When used with <code>-texfile</code>, horizontally blur non-background colors into background pixels up to a distance of <i>pixels</i> pixels. This helps smooth over distracting glitches introduced by the stereogram&#8217;s color constraints when producing a mapped-texture stereogram. In this case, the <code>-smoothing</code> option is helpful when the texture image includes smooth color transitions (as in a photograph) but makes crisp texture images (as in a line drawing) appear blurry. </p>
<p> This option was new in Netpbm 10.53 (December 2010). Before Netpbm 10.61 (December 2012), it has no effect without <code>-texfile</code>. </p>
<dt><code>-xshift=</code><i>pixels</i></p>
<dd> Shift the pattern image (designated by <code>-patfile</code>) to the right by <i>pixels</i> pixels (default: 0). </p>
<p> This option is valid only along with <code>-patfile</code>. </p>
<dt><code>-yshift</code> <i>pixels</i></p>
<dd> Shift the pattern image (designated by <code>-patfile</code>) downwards by <i>pixels</i> pixels (default: 0). This option is valid only along with <code>-patfile</code>. </p>
<dt><code>-magnifypat=</code><i>scale</i></p>
<dd> Magnify each pixel in the pattern file or each random dot by integral scaling factor <i>scale</i>. Note that <code>pamstereogram</code> applies the pattern magnification <i>after</i> pattern shifting (<code>-xshift</code> and <code>-yshift</code>). </p>
<dt><code>-guidebottom</code></p>
<dd> Draw a pair of black squares on a white background underneath the stereogram proper. These squares help you guide your eyes into proper focus to view the 3-D image. The trick is to focus your eyes some distance behind the image, causing you to see four black squares, then continue altering your focus distance until the middle two black squares fuse into a single black square. At that point, a crisp, 3-D image will appear. </p>
<p> This option was new in Netpbm 10.61 (December 2012). Before that, the presence of <code>-guidesize</code>, with a positive value, has the same effect. </p>
<dt><code>-guidetop</code></p>
<dd> Same as <code>-guidebottom</code>, except the guides go at the top of the image. </p>
<p> This option was new in Netpbm 10.61 (December 2012). Before that, the presence of <code>-guidesize</code>, with a negative value, has the same effect. </p>
<dt><code>-guidesize=</code><i>pixels</i></p>
<dd> The size (width and height) of each guide box. </p>
<p> This is valid only with <code>-guidetop</code> or <code>-guidebottom</code>. </p>
<p> Default is 20. </p>
<p> Before Netpbm 10.61 (December 2012), if you don&#8217;t specify this option, <code>pamstereogram</code> draws no guides. If you specify it with a positive value, <code>pamstereogram</code> behaves as if you specified <code>-guidebottom</code> too, and if you specify it with a negative value, it behaves as if you specified <code>-guidetop</code> and specified <code>guidesize</code> with the absolute value of that negative value. </p>
<dt><code>-dpi=</code><i>resolution</i></p>
<dd> Specify the resolution of the output device in dots per inch. The default is 100 DPI, which represents a fairly crisp screen resolution. </p>
<p> Before Netpbm 10.53 (December 2010), the default was 96 DPI. </p>
<dt><code>-crosseyed</code></p>
<dd> Invert the gray levels in the depth map (input image) so that the 3-D image pops out of the page where it would otherwise sink into the page and vice versa. Some people are unable to diverge their eyes and can only cross them. The <code>-crosseyed</code> option enables such people to see the 3-D image as intended. You can also specify the <code>-crosseyed</code> option if you prefer using depth maps in which darker colors are closer to the eye and lighter colors are farther from the eye. </p>
<p> Before Netpbm 10.53 (December 2010), <code>pamstereogram</code> used higher (lighter) numbers for things closer to the eye <i>without</i> <code>-crosseyed</code> and vice versa. </p>
<dt><code>-makemask</code></p>
<dd> Instead of a stereogram, output a PAM mask image showing coloring constraints. New pixels will be taken from the pattern file where the mask is black. Copies of existing pixels will be taken from the pattern file where the mask is white. The <code>-makemask</code> option can be used to help create more sophisticated pattern files (to use with <code>-patfile</code>) Note that <code>-makemask</code> ignores <code>-magnifypat</code>; it always produces masks that assume a pattern magnification of 1. </p>
<dt><code>-eyesep=</code><i>inches</i></p>
<dd> Specify the separation in inches between your eyes. The default, 2.5 inches (6.4 cm), should be sufficient for most people and probably doesn&#8217;t need to be changed. </p>
<dt><code>-depth=</code><i>fraction</i></p>
<dd> Specify the output image&#8217;s depth of field. That is, <i>fraction</i> represents the fractional distance of the near plane from the far plane. Smaller numbers make the 3-D image easier to perceive but flatter. Larger numbers make the 3-D image more difficult to perceive but deeper. The default, 0.3333, generally works fairly well. </p>
<dt><code>-planes=</code><i>near_pixels</i>,<i>far_pixels</i></p>
<dd> Explicitly specify the distance between repeated pixels in the near plane and in the far plane. This is an alternative to <code>-eyesep</code> and <code>-depth</code>. The following equalities hold: </p>
<dt>&bull;</p>
<dd> <i>eyesep</i> = 2 * <i>far</i></p>
<dt>&bull;</p>
<dd> <i>depth</i> = 2 * (<i>far</i> &amp;minus; <i>near</i>) /<br />
(2&nbsp;<wbr>*&nbsp;<wbr><i>far</i>&nbsp;<wbr>&amp;minus;&nbsp;<wbr><i>near</i>) </p>
<p> The number of distinct 3-D depths is <i>far</i> &amp;minus; <i>near</i> + 1. One might say that <code>-eyesep</code> and <code>-depth</code> are a more human-friendly way to specify stereoscopic parameters (distance between eyes and tradeoff between perceptibility and depth) while <code>-planes</code> is a more computer-centric way (pixel distances in the resulting stereogram). </p>
<p> This option was new in Netpbm 10.59 (June 2012). </p>
<dt><code>-randomseed=</code><i>integer</i></p>
<dd> Specify a seed to be used for the random number generator. The default is to use a seed based on the time of day, to one second granularity. </p>
<p> It is useful to specify the seed if you want to create reproducible results. With the same random seed, you should get identical results every time you run <code>pamstereogram</code>. </p>
<p> This is irrelevant if you use a pattern file (<code>-patfile</code> option), because there is no random element to <code>pamstereogram</code>&#8216;s behavior. </p>
<p> This option was new in Netpbm 10.32 (February 2006). </p>
</dl>
<h2>PARAMETERS</h2>
<p> The only parameter, <i>infile</i>, is the name of an input file that is a depth map image. If you don&#8217;t specify <i>infile</i>, the input is from standard input. </p>
<p> The input is a PAM image of depth 1. Each sample represents the distance from the eye that the 3-D image at that location should be. Lower (darker) numbers mean further from the eye. </p>
<h2>NOTES</h2>
<h3>Input Images</h3>
<p> <code>pamstereogram</code> pays no attention the image&#8217;s tuple type and ignores all planes other than plane 0. </p>
<p> Like any Netpbm program, <code>pamstereogram</code> will accept PNM input as if it were the PAM equivalent. </p>
<h3>Mapped-texture Stereograms</h3>
<p> In a <i>mapped-texture stereogram</i> (MTS), the 3-D image can be drawn with true colors. Unlike a SIRDS or tiled-image SIS, however, the image portrayed by an MTS is apparent in normal 2-D viewing. It appears repeated multiple times and overlapped with itself, but it is not hidden. </p>
<p> You create an MTS with <code>pamstereogram</code> by passing the filename of a PAM &lt;q&gt;texture image&lt;/q&gt; with a <code>-texfile</code> option. A texture image portrays the same 3-D object as the depth-map image but indicates the colors that the program should apply to the object. </p>
<p> <code>pamstereogram</code> ignores the texture image&#8217;s background color when it overlaps copies of the 3-D object. This prevents, for example, a bright-red object on a black background from being drawn as a dark-red object (a blend of 50% bright red and 50% black); instead, the program ignores the black and the object remains bright red. A consequence of this feature is that an MTS looks best when the objects in the texture image have a crisp outline. Smooth transitions to the background color result in unwanted color artifacts around edges because the program ignores only <i>exact</i> matches with the background color. </p>
<p> You should specify a larger-than-normal value for <code>-eyesep</code> (and/or <code>-dpi</code>) when producing an MTS. Otherwise, the 3-D object will repeat so many times that most colored pixels will overlap other colored pixels, reducing the number of true-colored pixels that remain. </p>
<p> An MTS can employ a background pattern (<code>-patfile</code>). In this case, <code>pamstereogram</code> replaces background pixels with pattern pixels in the final step of generating the image. </p>
<h3>Miscellaneous</h3>
<p> A good initial test is to input an image consisting of a solid shape of distance 0 within a large field of maximum distance (e.g., a white square on a black background). </p>
<p> With the default values for <code>-dpi</code> and <code>-eyesep</code>, pattern images that are 128 pixels wide can tile seamlessly. </p>
<h2>EXAMPLES</h2>
<p> Generate a SIRDS out of small, brightly colored squares and prepare it for display on an 87 DPI monitor: </p>
<pre>
    pamstereogram depthmap.pam \
        -dpi 87 -verbose -color -maxval 1 -magnifypat 3 \
        &gt;3d.pam
</pre>
<p> Generate a SIS by tiling a PPM file (a prior run with <code>-verbose</code> indicates how wide the pattern file should be for seamless tiling, although any width is acceptable for producing SISes): </p>
<pre>
    pamstereogram depthmap.pam -patfile mypattern.ppm &gt;3d.pam
</pre>
<p> Generate an MTS by associating colors with a depth-mapped object (using a large eye separation to reduce the number of repetitions of the texture image) and twice smoothing over background-colored speckles: </p>
<pre>
    pamstereogram depthmap.pam \
        -texfile colormap.pam -smoothing 2 -eyesep 3.5 \
        &gt;3d.pam
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamsistoaglyph/">pamsistoaglyph</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppm3d/">ppm3d</a></code>(1) </p>
<dt>&bull;</p>
<dd> Harold W. Thimbleby, Stuart Inglis, and Ian H. Witten. <i>Displaying 3D Images: Algorithms for Single Image Random Dot Stereograms</i>. In IEEE Computer, <code>27</code>(10):38-48, October 1994. DOI 10.1109/2.318576 . </p>
</dl>
<h2>HISTORY</h2>
<p> <code>pamstereogram</code> was new in Netpbm 10.22 (April 2004), but probably broken beyond usability until Netpbm 10.32 (February 2006) and Netpbm 10.26.23 (January 2006). </p>
<p> A backward incompatible change to the way you request guide boxes (<code>-guidetop</code>, <code>-guidebottom</code>, <code>-guidesize</code> happened in Netpbm 10.61 (December 2012). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2006, 2010 Scott Pakin, <i>scott+pbm [at] pakin.org</i>. </p>
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
<p> OPTIONS</p>
<dt>&bull;</p>
<dd>
<p> PARAMETERS</p>
<dt>&bull;</p>
<dd>
<p> NOTES </p>
<dt>&bull;</p>
<dd>
<p> Input Images</p>
<dt>&bull;</p>
<dd>
<p> Mapped-texture Stereograms</p>
<dt>&bull;</p>
<dd>
<p> Miscellaneous<br />
&nbsp;<wbr>&nbsp;<wbr> </p>
<dt>&bull;</p>
<dd>
<p> EXAMPLES</p>
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
