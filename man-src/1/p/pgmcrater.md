---
title: "pgmcrater(1)"
name: "pgmcrater"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmcrater/"
description: "pgmcrater – create cratered terrain by fractal forgery"
---

<h2 class="name">NAME</h2>
<p> pgmcrater &#8211; create cratered terrain by fractal forgery </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmcrater</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<code>-number</code> <i>n</i>] [<code>-height</code>|<code>-ysize</code> <i>s</i>] [<code>-width</code>|<code>-xsize</code> <i>s</i>] [<code>-gamma</code> <i>g</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> <code>pgmcrater</code> creates a PGM image which mimics cratered terrain. The PGM image is created by simulating the impact of a given number of craters with random position and size, then rendering the resulting terrain elevations based on a light source shining from one side of the screen. The size distribution of the craters is based on a power law which results in many more small craters than large ones. The number of craters of a given size varies as the reciprocal of the area as described on pages 31 and 32 of Peitgen and Saupe[1]; cratered bodies in the Solar System are observed to obey this relationship. The formula used to obtain crater radii governed by this law from a uniformly distributed pseudorandom sequence was developed by Rudy Rucker. </p>
<p> High resolution images with large numbers of craters often benefit from being piped through <code>pnmsmooth</code>. The averaging performed by this process eliminates some of the jagged pixels and lends a mellow &#8220;telescopic image&#8221; feel to the overall picture. </p>
<p> <code>pgmcrater</code> simulates only small craters, which are hemispherical in shape (regardless of the incidence angle of the impacting body, as long as the velocity is sufficiently high). Large craters, such as Copernicus and Tycho on the Moon, have a &#8220;walled plain&#8221; shape with a cross-section more like: </p>
<pre>
                /\                            /\
<br>
          _____/  \____________/\____________/  \_____
</pre>
<p> Larger craters should really use this profile, including the central peak, and totally obliterate the pre-existing terrain. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-number</code><i> n</i></p>
<dd> Causes <i>n</i> craters to be generated. If no <code>-number</code> specification is given, 50000 craters will be generated. Don&#8217;t expect to see them all! For every large crater there are many, many more tiny ones which tend simply to erode the landscape. In general, the more craters you specify the more realistic the result; ideally you want the entire terrain to have been extensively turned over again and again by cratering. High resolution images containing five to ten million craters are stunning but take quite a while to create.</p>
<dt><code>-height</code><i> height</i></p>
<dd> Sets the height of the generated image to <i>height</i> pixels. The default height is 256 pixels.</p>
<dt><code>-width</code><i> width</i></p>
<dd> Sets the width of the generated image to <i>width</i> pixels. The default width is 256 pixels.</p>
<dt><code>-xsize</code><i> width</i></p>
<dd> Sets the width of the generated image to <i>width</i> pixels. The default width is 256 pixels.</p>
<dt><code>-ysize</code><i> height</i></p>
<dd> Sets the height of the generated image to <i>height</i> pixels. The default height is 256 pixels.</p>
<dt><code>-gamma</code><i> factor</i></p>
<dd> The specified <i>factor</i> is used to gamma adjust the image in the same manner as performed by <code>pnmgamma</code>. The default value is 1.0, which results in a medium contrast image. Values larger than 1 lighten the image and reduce contrast, while values less than 1 darken the image, increasing contrast. </p>
<p> Note that this is separate from the gamma correction that is part of the definition of the PGM format. The image <code>pnmgamma</code> generates is a genuine, gamma-corrected PGM image in any case. This option simply changes the contrast and may compensate for a display device that does not correctly render PGM images. </p>
</dl>
<h2>DESIGN NOTES</h2>
<p> The <code>-gamma</code> option isn&#8217;t really necessary since you can achieve the same effect by piping the output from <code>pgmcrater</code> through <code>pnmgamma</code>. However, <code>pgmcrater</code> performs an internal gamma map anyway in the process of rendering the elevation array into the PGM format, so there&#8217;s no additional overhead in allowing an additional gamma adjustment. </p>
<p> Real craters have two distinct morphologies. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/1-pnmgamma/">pnmgamma</a></code>(1), <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1)</p>
<dl>
<dt>[1]</p>
<dd> Peitgen, H.-O., and Saupe, D. eds., The Science Of Fractal Images, New York: Springer Verlag, 1988.</dl>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd>
<pre>
John Walker
Autodesk SA
Avenue des Champs-Montants 14b
CH-2074 MARIN
Suisse/Schweiz/Svizzera/Svizra/Switzerland
<dl>
<dt>Usenet:<dd>kelvin [at] Autodesk.com
<dt>Fax:<dd>038/33 88 15
<dt>Voice:<dd>038/33 76 33
</pre>
</dl>
</dl>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<p> <code>PLUGWARE!</code> If you like this kind of stuff, you may also enjoy &#8220;James Gleick&#8217;s Chaos&#8211;The Software&#8221; for MS-DOS, available for $59.95 from your local software store or directly from Autodesk, Inc., Attn: Science Series, 2320 Marinship Way, Sausalito, CA 94965, USA. Telephone: (800) 688-2344 toll-free or, outside the U.S. (415) 332-2344 Ext 4886. Fax: (415) 289-4718. &#8220;Chaos&#8211;The Software&#8221; includes a more comprehensive fractal forgery generator which creates three-dimensional landscapes as well as clouds and planets, plus five more modules which explore other aspects of Chaos. The user guide of more than 200 pages includes an introduction by James Gleick and detailed explanations by Rudy Rucker of the mathematics and algorithms used by each program. </p>
<h2>Index</h2>
