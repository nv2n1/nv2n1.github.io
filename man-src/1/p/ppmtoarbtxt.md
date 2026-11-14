---
title: "ppmtoarbtxt(1)"
name: "ppmtoarbtxt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoarbtxt/"
description: "ppmtoarbtxt – generate image in arbitrary text format from PPM image"
---

<h2 class="name">NAME</h2>
<p> ppmtoarbtxt &#8211; generate image in arbitrary text format from PPM image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoarbtxt</code> <i>bodyskl</i> [<code>-hd</code> <i>headskl</i>] [<code>-tl</code> <i>tailskl</i>] [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmtoarbtxt</code> generates simple text-based graphics formats based on format descriptions given as input. A text-based graphics format is one in which an image is represented by text (like PNM plain format, but unlike PNM raw format). </p>
<p> <code>ppmtoarbtxt</code> reads a PPM image as input. For each pixel in the image, <code>ppmtoarbtxt</code> writes the contents of the skeleton file <i>bodyskl</i>, with certain substitutions based on the value of the pixel, to stdout. The substitutions are as follows: </p>
<dl>
<dt><code>#(ired</code><i> format blackref whiteref</i><code>)</code></p>
<dd> generates an integer in the range <i>blackref</i> to <i>whiteref</i> using <i>format</i> representing the red intensity of the pixel. A red intensity of 0 becomes <i>blackref</i>; a red intensity of maxval becomes <i>whiteref</i>. </p>
<p> <code>#(ired)</code> is equivalent to <code>#(ired %d 0 255)</code>. </p>
<dt><code>#(igreen</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(ired&#8230;</code>, but for green. </p>
<dt><code>#(iblue</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(ired&#8230;</code>, but for blue. </p>
<dt><code>#(ilum</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(ired&#8230;</code>, but representing the luminance value (0.299*red + 0.587*green + 0.114*blue) of the pixel. </p>
<dt><code>#(fred</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(ired&#8230;</code>, but generates a floating point number instead of an integer. </p>
<p> <code>#(fred)</code> is equivalent to <code>#(fred %f 0.0 1.0)</code>. </p>
<dt><code>#(fgreen</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(fred&#8230;</code>, but for green. </p>
<dt><code>#(fblue</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(fred&#8230;</code>, but for blue. </p>
<dt><code>#(flum</code><i> format blackref whiteref</i><code>)</code></p>
<dd> Same as <code>#(fred&#8230;</code>, but representing the luminance value (0.299*red + 0.587*green + 0.114*blue) of the pixel. </p>
<dt><code>#(width)</code></p>
<dd> Generates the width in pixels of the image. </p>
<dt><code>#(height)</code></p>
<dd> Generates the height in pixels of the image. </p>
<dt><code>#(posx)</code></p>
<dd> Generates the horizontal position of the pixel, in pixels from the left edge of the image. </p>
<dt><code>#(posy)</code></p>
<dd> Generates the vertical position of the pixel, in pixels from the top edge of the image. </p>
</dl>
<p> If the skeleton file ends with a LF-character, <code>ppmtoarbtxt</code> ignores it &#8212; it does not include it in the output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-hd</code> <i>headskl</i></p>
<dd> This option causes <code>ppmtoarbtxt</code> to place the contents of the file named <i>headskl</i> at the beginning of the output, before the first pixel. It does the same substitutions as for <i>bodyskl</i>, except substitutions based on a pixel value are undefined. </p>
<dt><code>-tl</code> <i>tailskl</i></p>
<dd> This option causes <code>ppmtoarbtxt</code> to place the contents of the file named <i>tailskl</i> at the end of the output, after the last pixel. It is analogous to <code>-hd</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<h3>gray inversion</h3>
<p> Here we generate a PGM plain-format image with gray inversion (like <code>ppmtopgm | pnminvert</code>). </p>
<p> Contents of our head skeleton file: </p>
<pre>
P2
#(width) #(height)
255
</pre>
<p> Contents of our body skeleton file: </p>
<pre>
#(ilum %d 255 0)
</pre>
<h3>povray file</h3>
<p> Here we generate a povray file where each pixel is represented by a sphere at location (x,y,z) = (posx,height-posy,luminance). The color of the sphere is the color of the pixel. </p>
<p> Contents of our head skeleton: </p>
<pre><code>
#include 'colors.inc'
#include 'textures.inc'
camera{
    location&lt;#(width)*0.6, #(height)*0.7, 80&gt;
        look_at&lt;#(width)*0.5, #(height)*0.5, 0&gt;} light_source
{
    &lt;#(width)*0.5, #(height)*0.5, 25&gt; color White
}
</code></pre>
<p> Contents of our body skeleton: </p>
<pre><code>
sphere
{
    &lt;#(posx), #(height) - #(posy), #(ilum % d 0 10)&gt;, 0.5 texture
    {
        pigment{
            color rgb&lt;#(fred), #(fgreen), #(fblue)&gt;} finish
        {
            phong 1
        }
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtoplainpnm/">pnmtoplainpnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>ppmtoarbtxt</code> was added to Netpbm in Release 10.14 (March 2003). It existed under the name <code>ppmtotxt</code> since 1995. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1995 by Peter Kirchgessner </p>
<h2>Index</h2>
