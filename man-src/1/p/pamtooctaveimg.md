---
title: "pamtooctaveimg(1)"
name: "pamtooctaveimg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtooctaveimg/"
description: "pamtooctaveimg – convert a Netpbm image to a GNU Octave image"
---

<p>&quot; &quot;netpbm documentation&quot; </p>
<h2 class="name">NAME</h2>
<p> pamtooctaveimg &#8211; convert a Netpbm image to a GNU Octave image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtooctaveimg</code> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtooctaveimg</code> reads a Netpbm image as input and produces a GNU Octave image file as output. </p>
<p> An Octave image file (called &#8216;Octave&#8217;s image format&#8217; in Octave documentation) is a particular kind of Octave data file. It describes two matrices: </p>
<dl>
<dt>&bull;</p>
<dd> the image itself as a list of indexes into a colormap, and</p>
<dt>&bull;</p>
<dd> the corresponding colormap as a list of {red, green, blue} triplets. </p>
</dl>
<p> An Octave data file is an ASCII text file that you use to import data to Octave. </p>
<p> See the<br />
&nbsp;<wbr>Image Processing chapter of the GNU Octave manual for details. </p>
<p> <code>pamtooctaveimg</code> writes the output Octave image to Standard Output. </p>
<h2>Arguments</h2>
<p> <i>netpbmfile</i> is the name of the file containing the input PNM or PAM image, or <code>&#8211;</code> to indicate Standard Input. If you don&#8217;t specify <i>netpbmfile</i>, the input is from Standard Input. <code>pamtooctaveimg</code> converts only the first image in the input stream. </p>
<h2>Examples</h2>
<pre><code>

% pamtooctaveimg myimage.ppm &gt; myimage.img % octave &gt; [ img, map ] = loadimage("myimage.img");
#(At this point, img is an X by Y matrix and map is a 3 by M matrix.)
&gt; imshow(img, map);
#Displays img with colormap map&gt;[r, g, b] = ind2rgb(img, map);
#(r, g, and b are now each X by Y matrices of color levels[0 to 1].)
&gt; [ newimg, newmap ] = rgb2ind(r, b, g);
#Swap the blue and green channels.&gt; saveimage("newimage.ppm", newimg, "ppm", newmap);
#Save as a PPM file.
</code></pre>
<h2>NOTES</h2>
<p> There is no <code>octavetopam</code> program. However, GNU Octave&#8217;s <code>saveimage</code> command can save images in PPM format. </p>
<h2>HISTORY</h2>
<p> <code>pamtooctaveimg</code> was new in Netpbm 10.39 (June 2007). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2007 Scott Pakin, <i>scott+pbm [at] pakin.org</i>. </p>
<h2>Index</h2>
