---
title: "pamsistoaglyph(1)"
name: "pamsistoaglyph"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsistoaglyph/"
description: "pamsistoaglyph – convert a single-image stereogram to a red/cyan anaglyphic image"
---

<h2 class="name">NAME</h2>
<p> pamsistoaglyph &#8211; convert a single-image stereogram to a red/cyan anaglyphic image </p>
<h2>SYNOPSIS</h2>
<p> <code>pamsistoaglyph</code> [&#8211;<code>invert</code>] [&#8211;<code>sep</code>=<i>number</i>] [&#8211;<code>minsep</code>=<i>number</i>] [&#8211;<code>gray</code>=<i>number</i>] [<i>in_netpbmfile</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsistoaglyph</code> reads a Netpbm image as input and produces a Netpbm image as output. </p>
<p> <code>pamsistoaglyph</code> takes a single-image stereogram (SIS) such as those produced by <code><a href="/docs/linux/man/1-pamstereogram/">pamstereogram</a></code>(1) </p>
<p> and converts it to a red/cyan anaglyphic image such as those produced by <code><a href="/docs/linux/man/1-ppm3d/">ppm3d</a></code>(1) Many people have trouble tricking their eyes into focusing beyond the image in front of them and are therefore unable to perceive the 3-D shape hidden within a single-image stereogram. Anaglyphic stereograms are easier to perceive in 3-D but require a pair of red/cyan glasses such as those often used to watch 3-D movies. The goal of <code>pamsistoaglyph</code> is to help people who have trouble viewing single-image stereograms see the intriguing 3-D effect. </p>
<p> <code>pamsistoaglyph</code> can convert single-image random-dot stereograms (SIRDS), wallpaper stereograms, and even dual-image stereograms to anaglyphic images. </p>
<h2>OPTIONS</h2>
<p> For most images, no command-line options need to be specified. The following options are available, however, for unusual circumstances: </p>
<dl>
<dt><code>&#8211;invert</code></p>
<dd> Swap the left- and right-eye<br />
&nbsp;<wbr>images.&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>assumes that its input<br />
&nbsp;<wbr>represents a wall-eyed stereogram and generates the anaglyphic<br />
&nbsp;<wbr>image accordingly. If the generated image appears to recede into<br />
&nbsp;<wbr>the page where it should pop out of the page&nbsp;<wbr>(and vice versa),<br />
&nbsp;<wbr>this typically implies that the input image represents a<br />
&nbsp;<wbr>cross-eyed stereogram. Use&nbsp;<wbr><code>&#8211;invert</code>&nbsp;<wbr>to correct<br />
&nbsp;<wbr>the image depth. </p>
<dt><code>&#8211;sep</code>=<i>number</i></p>
<dd> Specify the distance in pixels between the left- and right-eye<br />
&nbsp;<wbr>images. Essentially, this corresponds to the distance between<br />
&nbsp;<wbr>repetitions of the background pattern.&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>&#8211;sep</code><br />
&nbsp;<wbr>option should rarely be necessary<br />
&nbsp;<wbr>as&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>is fairly good at determining<br />
&nbsp;<wbr>automatically the eye-separation distance. </p>
<dt><code>&#8211;minsep</code>=<i>number</i></p>
<dd> This option is similar to <code>&#8211;sep</code> but<br />
&nbsp;<wbr>constrains&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>only to<br />
&nbsp;<wbr>a&nbsp;<wbr><i>minimum</i>&nbsp;<wbr>eye-separation distance. Any distance larger<br />
&nbsp;<wbr>than&nbsp;<wbr><i>number</i>&nbsp;<wbr>is acceptable.&nbsp;<wbr>&nbsp;<wbr>The&nbsp;<wbr><code>&#8211;minsep</code><br />
&nbsp;<wbr>option should rarely be necessary<br />
&nbsp;<wbr>as&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>is fairly good at determining<br />
&nbsp;<wbr>automatically the eye-separation distance.&nbsp;<wbr>&nbsp;<wbr>The default value for<br />
&nbsp;<wbr>the minimum eye-separation distance is 10%&nbsp;<wbr>of the image width;<br />
&nbsp;<wbr>this value seems to work well in practice. </p>
<dt><code>&#8211;gray</code>=<i>number</i></p>
<dd> Limit the number of gray levels to use when searching for the<br />
&nbsp;<wbr>optimal eye-separation<br />
&nbsp;<wbr>distance.&nbsp;<wbr>&nbsp;<wbr>Because&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>looks for<br />
&nbsp;<wbr>repeated patterns, it is vulnerable to being confused by slight<br />
&nbsp;<wbr>variations in color.&nbsp;<wbr>&nbsp;<wbr>By reducing the input image to grayscale and<br />
&nbsp;<wbr>capping the number of gray levels,<br />
&nbsp;<wbr><code>pamsistoaglyph</code>&nbsp;<wbr>ameliorates the effects of<br />
&nbsp;<wbr>unintentional color variations&nbsp;<wbr>(such as those caused by conversion<br />
&nbsp;<wbr>from a low-quality JPEG image, for example). The default of 63<br />
&nbsp;<wbr>seems to work well so the&nbsp;<wbr><code>&#8211;gray</code>&nbsp;<wbr>option should<br />
&nbsp;<wbr>rarely be necessary. </p>
</dl>
<h2>NOTES</h2>
<p> The registration algorithm used by <code>pamsistoaglyph</code> was developed specifically for this program. As far as the author knows, there are no existing algorithms for converting stereograms to anaglyphs. The algorithm works as follows: </p>
<dl>
<dt>&bull;</p>
<dd> Convert the image to grayscale to increase the ability to identify<br />
&nbsp;<wbr>matches. </p>
<dt>&bull;</p>
<dd> Count the number of pixels that match <i>N</i> pixels ahead in the<br />
&nbsp;<wbr>image for all&nbsp;<wbr><i>N</i>&nbsp;<wbr>in&nbsp;<wbr>[1,&nbsp;<wbr><i>width</i>/2]. </p>
<dt>&bull;</p>
<dd> Maintain a running mean (&amp;mu;) and standard deviation (&amp;sigma;) of<br />
&nbsp;<wbr>the number of matched pixels. </p>
<dt>&bull;</p>
<dd> Store the <i>N</i> corresponding to each spike in the number of<br />
&nbsp;<wbr>matched pixels. A spike is defined as a tally that exceeds the<br />
&nbsp;<wbr>mean plus one, two, or three standard deviations. Only the first<br />
&nbsp;<wbr>spike of a given standard-deviation multiplier is stored. </p>
<dt>&bull;</p>
<dd> If a tally greater than &amp;mu;+3&amp;sigma; was encountered, return the<br />
&nbsp;<wbr>corresponding&nbsp;<wbr><i>N</i>. If not, then if a tally greater than<br />
&nbsp;<wbr>&amp;mu;+2&amp;sigma;&nbsp;<wbr>was encountered, return the<br />
&nbsp;<wbr>corresponding&nbsp;<wbr><i>N</i>. If not, then if a tally greater than<br />
&nbsp;<wbr>&amp;mu;+&amp;sigma;&nbsp;<wbr>was encountered, return the<br />
&nbsp;<wbr>corresponding&nbsp;<wbr><i>N</i>. If not, then return the&nbsp;<wbr><i>N</i>&nbsp;<wbr>that<br />
&nbsp;<wbr>produces the minimum average distance between matched pixels<br />
&nbsp;<wbr>(i.e.,&nbsp;<wbr><i>#matches</i>&nbsp;<wbr>divided by&nbsp;<wbr><i>#pixels</i>). If no<br />
&nbsp;<wbr>such&nbsp;<wbr><i>N</i>&nbsp;<wbr>exceeds the minimum allowable eye-separation value,<br />
&nbsp;<wbr>return zero to indicate failure. </p>
<dt>&bull;</p>
<dd> If the algorithm returned zero, rerun the algorithm independently<br />
&nbsp;<wbr>on each row of the input image and return the median of<br />
&nbsp;<wbr>all&nbsp;<wbr><i>N</i>&nbsp;<wbr>that exceed the minimum allowable eye-separation<br />
&nbsp;<wbr>value. If no such&nbsp;<wbr><i>N</i>&nbsp;<wbr>exists, abort with an error<br />
&nbsp;<wbr>message. </p>
</dl>
<h2>HISTORY</h2>
<p> Scott Pakin wrote <code>pamsistoaglyph</code> in April 2009. It first appeared in Netpbm in Release 10.47 (June 2009). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2009 Scott Pakin, <i>scott+pbm [at] pakin.org.</i> </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamstereogram/">pamstereogram</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppm3d/">ppm3d</a></code>(1) ,</p>
<dt>&bull;</p>
<dd>
<p> <a rel="nofollow" href="http://en.wikipedia.org/wiki/Stereogram">http://en.wikipedia.org/wiki/Stereogram</a> </p>
</dl>
<h2>Index</h2>
