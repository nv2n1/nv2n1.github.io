---
title: "pamrubber(1)"
name: "pamrubber"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamrubber/"
description: "pamrubber – a rubber-sheeting utility that stretches an image based on control points"
---

<h2>NAME</h2>
<p> pamrubber &#8211; a rubber-sheeting utility that stretches an image based on control points </p>
<h2>SYNOPSIS</h2>
<p> <code>pamrubber</code> {<code>-tri | -quad</code>} [<code>-linear</code>] [<code>-frame</code>] [<code>-randomseed=</code><i>N</i>] <i>cp1x cp1y</i> [<i>cp2x cp2y</i> [<i>cp3x cp3y</i> [<i>cp4x cp4y</i>]]] <i>cp1x cp1y</i> [<i>cp2x cp2y</i> [<i>cp3x cp3y</i> [<i>cp4x cp4y</i>]]] [<i>filename</i>] </p>
<p> Minimum unique abbreviation of options is acceptable. You may use double hyphens instead of single hyphen to denote options. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> The <code>pamrubber</code> utility converts a pam image into a new image with the contents moved around. The transformation is often called &#8216;rubber sheeting&#8217;: you identify control points (CP) on the source image and specify new positions for those points in the new image. <code>pamrubber</code> moves all the pixels around, stretching and compressing as necessary, as if the original image were on a sheet of rubber and you pulled on the sheet to make the control points move to their new locations. </p>
<p> The new image has the same dimensions and format as the original. </p>
<p> The transformation can happen in two very different ways, called &#8216;quad&#8217; and &#8216;tri.&#8217; With the former, you must specify four control points (for both source and target). These are the corners of two quadrilaterals that will act as the coordinate system for both source and target images. Consider them as non-orthogonal (0,0), (0,1), (1,0) and (1,1) points. This transformation comes close to the one <code>pamperspective</code> does, however that program does other corrections as well. </p>
<p> When you specify less than four control points, the program adds control points in the following way. With three control points, <code>pamrubber</code> chooses the fourth one such that the four points form a parallelogram. With two points, <code>pamrubber</code> considers them the opposite corners of a rectangle. When you specify only one control point, <code>pamrubber</code> uses a rectangle from the top left corner of the image to the single control point. </p>
<p> In &#8216;tri&#8217; mode, <code>pamrubber</code> conceptually cuts up the source and target image into triangles. It Transforms within each corresponding pair of triangles in a stretching fashion. It&#8217;s like pulling on the three corners of the triangle. In this mode, each pixel in the source image gets mapped to a position in the target image. No pixels are lost. </p>
<p> When, in &#8216;tri&#8217; mode, you specify only a single control point in the source and target image, <code>pamrubber</code> creates four triangles from this point to the four corners of the image. With two points, the program creates six triangles from the two endpoints of the line connecting the two points, again to the four corners of the image. Three control points is in a way the core of this utility in &#8216;tri&#8217; mode. Between the three edges of the central triangle and the four edges of the image, <code>pamrubber</code> constructs another seven triangles. Four control points define two central connected triangles. In total this results in cutting the source and target image up into ten triangles. </p>
<p> In this case clearly a picture says more than a thousand words. There is a graphical illustration of these various modes at<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.schaik.com">www.schaik.com</a>/netpbm/rubber . An example of how to use this type of rubber sheeting in cartography is in the article<br />
&nbsp;<wbr>Visualizing the Landscape of Old-Time Tokyo . </p>
<h2>PARAMETERS</h2>
<p> The parameters are control points (<i>cp</i>) in pairs of <i>x</i> and <i>y</i>. The source and target image must have the same number of control points. The minimum number of values specified here is 4 for a single control point in the source and target image. The maximum is 16 for four control points in each image. </p>
<p> <i>filename</i> is the name of the input file. If you don&#8217;t specify this, <code>pamrubber</code> reads the image from Standard Input. </p>
<h2>OPTIONS</h2>
<p> &lt;dl compact=&quot;compact&quot;&gt; </p>
<dl>
<dt><code>-tri</code> | <code>-quad</code></p>
<dd>
<p> This selects the type of rubber sheeting done. You must specify exactly one of these options. </p>
<dt><code>-linear</code></p>
<dd>
<p> This determines whether <code>pamrubber</code> uses nearest neighbor interpolation or bilinear interpolation of four source pixels. </p>
<dt><code>-frame</code></p>
<dd>
<p> This option causes <code>pamrubber</code> to overlay the target image with the edges of the quadrilaterals, respectively the triangles used for the rubber sheeting. To get the same overlay for the source image, use a <code>pamrubber</code> transformation with identical control points for source and target. </p>
<dt><code>-randomseed=</code><i>N</i></p>
<dd>
<p> <code>pamrubber</code> randomizes some of its output. So that you can produce repeatable results, you can choose the seed of the random number generator with this option. If you use the same input image and the same random number generator seed, you should always get the exact same output. By default, <code>pamrubber</code> uses the time of day as the seed, so you get slightly different output when you run the program twice on the same input. </p>
<p> Before Netpbm 10.61 (December 2012), this was called <code>-randseed</code>, and that still works. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-pamperspective/">pamperspective</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamrubber</code> was new in Netpbm 10.54 (March 2011). </p>
<h2>AUTHORS</h2>
<p> <i>Willem van Schaik</i> wrote this program in February 2011 and contributed it to Netpbm. </p>
<h2>Index</h2>
