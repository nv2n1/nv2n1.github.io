---
title: "bggen(1)"
name: "bggen"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bggen/"
description: "bggen – generates colored backgrounds on X11 displays"
---

<h2>NAME</h2>
<p> bggen &#8211; generates colored backgrounds on X11 displays</p>
<h2>SYNTAX</h2>
<p> <code>bggen</code> [-d display] [-g geometry] [-G rptgeom] [-r rot] [-a] [-w width] [-h height] [-b bits] &lt;color-spec&gt; [&lt;color-spec&gt; &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>bggen</code> is a program that generates a rectangular 24-bit image, with a smooth vertical gradient between the listed colors. (If you only specify one color, the image will be a single solid color.) The top of the image will be in color (r1,g1,b1), and the bottom of the image will be in color (rn,gn,bn). Intermediate positions in the image are interpolated between these colors. If you specify more than 2 colors, the gradient passes through all the specified colors, in the order specified. </p>
<p> The &#8216;-d&#8217; option lets you specify what display to connect to. <code>bggen</code> only connects to the display to find out the size of the screen (and hence, the default size for the generated image). </p>
<p> The &#8216;-g&#8217; option lets you control the size of the image, as a standard X geometry specification. (ie, something like &quot;512&#215;348&quot;) </p>
<p> The &#8216;-G&#8217; option lets you control the tile size, as a standard X geometry specification. (ie, something like &quot;32&#215;32&quot;) Normally, (if you don&#8217;t give a -G option), the gradient fills the entire image. If you specify a -G option, the gradient will fill a portion of the image, and that portion will be &#8216;center-tiled&#8217; to fill the rest of the image. </p>
<p> The &#8216;-r&#8217; option lets you rotate the gradient counter-clockwise by the specified number of degrees. </p>
<p> The &#8216;-a&#8217; option lets you force bggen to generate an image in PPM &#8216;Ascii&#8217; format, rather than in PPM &#8216;raw&#8217; format. </p>
<p> The &#8216;-w&#8217; and &#8216;-h&#8217; options also let you set the size of the image. They are provided only for backward compatibility. </p>
<p> The &#8216;-b&#8217; option specifies the number of significant bits in the (output) color specifications. It must range between 1 and 8, inclusive. Use values less than 8 (the default) to limit color use by increasing the color granularity. Since XV can do this sort of thing better, this is of dubious value. </p>
<p> A &lt;color-spec&gt; can be three integers separated by spaces, forming an R,G,B triple (&quot;0 255 0&quot;). The values should be between 0 and 255. </p>
<p> A &lt;color-spec&gt; can also be a standard X color specification by name (&quot;green&quot;) or value (&quot;#00ff00&quot;). This is decidedly easier, and the &#8216;three integer&#8217; method remains mainly for backward compatibility. One note: the &#8216;#&#8217; character is treated specially by many shells, and should probably be protected by putting a &#8216;\&#8217; character in front of it, or wrapping the entire value with a pair of single-quotes. </p>
<p> <code>bggen</code> doesn&#8217;t actually affect your background directly. <code>bggen</code> merely generates a PPM (Portable Pixmap Format) datafile and dumps it to &#8216;stdout&#8217;. It&#8217;s up to some other program (such as XV) to read this file and display it. </p>
<p> To use <code>bggen</code>, you should pipe its output into an XV command, such as: &quot;xv -root -quit -&quot;</p>
<h2>TRY THESE</h2>
<pre>
Light Blue to Dark Blue
        bggen 100 100 255  0 0 100  | xv -root -quit  -
RGB Rainbow
        bggen red green blue | xv -root -quit -
Green Cylinders
        bggen black green black -h 128 | xv -root -quit -
Blue to Magenta
        bggen blue magenta | xv -root -quit -
Full Rainbow
        bggen black red yellow green blue purple black | xv -root -quit  -
Repeating Rainbow
        bggen red yellow green blue purple red -h 256 | xv -root -quit -
Green Tiles
        bggen green black  -r 30 -g 32x32 | xv -root -quit -
Red Balls
        bggen red black -r 45 -g 32x32 | xv -root -quit -rmode 3 -
Red+Yellow Diamonds
        bggen red yellow  -r 45 -g 32x32 | xv -root -quit -rmode 3 -
</pre>
<h2>AUTHOR</h2>
<p> John Bradley &#8211; bradley [at] dccs.upenn.edu </p>
<h2>Index</h2>
