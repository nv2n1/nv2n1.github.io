---
title: "pamlookup(1)"
name: "pamlookup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamlookup/"
description: "pamlookup – map an image to a new image by using it as indices into a table"
---

<h2 class="name">NAME</h2>
<p> pamlookup &#8211; map an image to a new image by using it as indices into a table</p>
<h2>SYNOPSIS</h2>
<p> <code>pamlookup</code> <code>-lookupfile=</code><i>lookupfile</i> <code>-missingcolor=</code><i>color</i> [<code>-fit</code>] <i>indexfile</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamlookup</code> takes a two dimensional array of indices and a lookup table as input. For each position in the index array, it looks up the index in the lookup table and places the result of the lookup in the output image. The output thus has the same width and height as the index image, and tuple types determined by the lookup table. </p>
<p> An index is either a whole number or an ordered pair of whole numbers. If the index image has a depth of one, each index in it is a whole number: the value of the one sample. If the index image has a depth greater than one, each index in it is an ordered pair of the first and second samples in the relevant tuple. </p>
<p> The lookup table is a PAM or PNM image. If the index image contains whole number indices, the lookup image is a single row and the index is a column number. The lookup result is the value of the tuple or pixel at the indicated column in the one row in the lookup table. If the index image contains ordered pair indices, the first element of the ordered pair is a row number and the second element of the ordered pair is a column number. The lookup result is the value of the tuple or pixel at the indicated row and column in the lookup table. </p>
<p> For example: Consider an index image consisting of a 3x2x1 PAM as follows: </p>
<table>
<tr VALIGN=top>
<td>0</td>
<td>1</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>2</td>
<td>2
</td>
</tr>
</table>
<p> and a lookup table consisting of a 3&#215;1 PPM image as follows: </p>
<table>
<tr VALIGN=top>
<td>red</td>
<td>yellow</td>
<td>beige
</td>
</tr>
</table>
<p> The lookup table above says Index 0 corresponds to the color red, Index 1 corresponds to yellow, and Index 2 corresponds to beige. The output of <code>pamlookup</code> is the following PPM image: </p>
<table>
<tr VALIGN=top>
<td>red</td>
<td>yellow</td>
<td>red
</td>
</tr>
<tr VALIGN=top>
<td>beige</td>
<td>beige</td>
<td>beige
</td>
</tr>
</table>
<p> Now let&#8217;s look at an example of the more complex case where the indices are ordered pairs of whole numbers instead of whole numbers. Our index image will be this 3x2x2 PAM image: </p>
<table>
<tr VALIGN=top>
<td>(0,0)</td>
<td>(0,1)</td>
<td>(0,0)
</td>
</tr>
<tr VALIGN=top>
<td>(1,1)</td>
<td>(1,0)</td>
<td>(0,0)
</td>
</tr>
</table>
<p> Our lookup table for the example will be this two dimensional PPM: </p>
<table>
<tr VALIGN=top>
<td>red</td>
<td>yellow</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>green</td>
<td>black</td>
<td>
</td>
</tr>
</table>
<p> This lookup table says Index (0,0) corresponds to the color red, Index (0,1) corresponds to yellow, Index (1,0) corresponds to green, and Index (1,1) corresponds to black. The output of <code>pamlookup</code> is the following PPM image: </p>
<table>
<tr VALIGN=top>
<td>red</td>
<td>yellow</td>
<td>red
</td>
</tr>
<tr VALIGN=top>
<td>black</td>
<td>green</td>
<td>red
</td>
</tr>
</table>
<p> If an index specifies a row or column that exceeds the dimensions of the lookup table image, <code>pamlookup</code> uses the value from the top left corner of the lookup image, or the value you specify with the <code>-missingcolor</code> option. </p>
<p> The <i>indexfile</i> argument identifies the file containing the index PAM or PNM image. <code>&#8211;</code> means Standard Input. The mandatory <code>-lookupfile</code> option identifies the file containing the lookup table image. Again, <code>&#8211;</code> means Standard Input. It won&#8217;t work if both the index image file and lookup table file are Standard Input. The output image goes to Standard Output. </p>
<p> You can use <code>ppmmake</code> and <code>pnmcat</code> to create a lookup table file. </p>
<p> If you want to use two separate 1-plane images as indices (so that your output reflects the combination of both inputs), use <code>pamstack</code> to combine the two into one two-plane image (and use a 2-dimensional lookup table image). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-lookupfile=</code><i>lookupfile</i></p>
<dd> <i>lookupfile</i> names the file that contains the PAM or PNM image that is the lookup table. This option is mandatory. </p>
<dt><code>-missingcolor=</code><i>color</i></p>
<dd> This option is meaningful only if the lookup image (and therefore the output) is a PNM image. <i>color</i> specifies the color that is to go in the output wherever the index from the input is not present in the lookup table (not present means the index exceeds the dimensions of the lookup image &#8212; e.g. index is 100 but the lookup image is a 50 x 1 PPM). </p>
<p> If you don&#8217;t specify this option of <code>-fit</code>, <code>pamlookup</code> uses the value from the top left corner of the lookup image whenever an index exceeds the dimensions of the lookup image. </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> Another way to deal with a too-small lookup image is to use the <code>-fit</code> option. </p>
<dt><code>-fit</code></p>
<dd> This option says to shrink or expand the lookup image as necessary to fit the indices present in the index image, per the index image&#8217;s maxval. For example, if your index image has a single plane and a maxval of 255 and your lookup image is 1 row of 10 columns, <code>pamlookup</code> stretches your lookup image to 255 columns before doing the lookups. <code>pamlookup</code> does the stretching (or shrinking) with the <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) </p>
<p> program. </p>
<p> When you use <code>-fit</code>, <code>pamlookup</code> never fails or warns you due to invalid lookup image dimensions, and the <code>-missingcolor</code> option has no effect. </p>
</dl>
<h2>EXAMPLES</h2>
<h3>Example: rainfall map</h3>
<p> Say you have a set of rainfall data in a single plane PAM image. The rows and columns of the PAM indicate latitude and longitude. The sample values are the annual rainfall in (whole) centimeters. The highest rainfall value in the image is 199 centimeters. The image is in the file rainfall.pam. </p>
<p> You want to produce a PPM rainfall map with green for the wettest places, red for the driest, and other colors in between. </p>
<p> First, compose a lookup table image, probably with a graphical editor and the image blown way up so you can work with individual pixels. The image must have a single row and 200 columns. Make the leftmost pixel red and the rightmost pixel green and choose appropriate colors in between. Call it colorkey.ppm. </p>
<pre>
<tt>
    pamlookup rainfall.ppm -lookupfile=colorkey.ppm &gt;rainfallmap.ppm
</tt>
</pre>
<p> Now lets say you&#8217;re too lazy to type in 200 color values and nobody really cares about the places that have more than 99 centimeters of annual rainfall. In that case, just make colorkey.ppm 100 columns wide and do this: </p>
<pre>
<tt>
    pamlookup rainfall.ppm -lookupfile=colorkey.ppm -missingcolor=black \
       &gt;rainfallmap.ppm
</tt>
</pre>
<p> Now if there are areas that get more than 100 centimeters of rainfall, they will just show up black in the output. </p>
<h3>Example: graphical diff</h3>
<p> Say you want to compare two PBM (black and white) images visually. Each consists of black foreground pixels on a white background. You want to create an image that contains background where both images contain background and foreground where both images contain foreground. But where Image 1 has a foreground pixel and Image 2 does not, you want red in the output; where Image 2 has a foreground pixel and Image 1 does not, you want green. </p>
<p> First, we create a single image that contains the information from both input PBMs: </p>
<pre>
<tt>
    pamstack image1.pbm image2.pbm &gt;bothimages.pam
</tt>
</pre>
<p> Note that this image has 1 of 4 possible tuple values at each location: (0,0), (0,1), (1,0), or (1,1). </p>
<p> Now, we create a lookup table that we can index with those 4 values: </p>
<pre>
<tt>
    ppmmake white 1 1 &gt;white.ppm
    ppmmake black 1 1 &gt;black.ppm
    ppmmake red   1 1 &gt;red.ppm
    ppmmake green 1 1 &gt;green.ppm
    pnmcat -leftright black.ppm red.ppm   &gt;blackred.ppm
    pnmcat -leftright green.ppm white.ppm &gt;greenwhite.ppm
    pnmcat -topbottom blackred.ppm greenwhite.ppm &gt;lookup.ppm
</tt>
</pre>
<p> Finally, we look up the indices from our index in our lookup table and produce the output: </p>
<pre>
<tt>
    pamlookup bothimages.ppm -lookupfile=lookup.ppm &gt;imagediff.ppm
</tt>
</pre>
<p>&nbsp;<wbr>&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1) , <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) , <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1) , <code><a href="/docs/linux/man/1-pamstack/">pamstack</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamlookup</code> was new in Netpbm 10.13 (December 2002). </p>
<h2>Index</h2>
