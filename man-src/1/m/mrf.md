---
title: "mrf(1)"
name: "mrf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrf/"
description: "MRF – monochrome recursive format (compressed bitmaps)"
---

<h2 class="name">NAME</h2>
<p> MRF &#8211; monochrome recursive format (compressed bitmaps)</p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> MRF is a compressed format for bilevel (1-bit mono) images. It achieves better compression for some such images than either GIF or PNG. (It&#8217;s also very easy to implement (about the same difficulty as RLE, I&#8217;d say) and an MRF reader needs no tables/buffers, which may make it useful for tiny machines). </p>
<p> In case the above hasn&#8217;t made it sufficiently clear, I&#8217;ll make this next point explicitly: <i>MRF cannot represent color at all.</i> Nor can it represent grayscale. It&#8217;s a specifically mono format. (If you want to compress a color or grayscale image, my advice is to use JPEG2000). </p>
<p> First, here&#8217;s what goes where in an MRF file. I&#8217;ll explain how the compression works afterward. </p>
<dl>
<dt>Offset</p>
<dd> Description</p>
<dt>0</p>
<dd> magic number &#8211; &#8216;MRF1&#8217; (in ASCII) </p>
<dt>4</p>
<dd> width (32-bit, MSB first (i.e. big-endian)) </p>
<dt>8</p>
<dd> height (same) </p>
<dt>12</p>
<dd> reserved (single byte, must be zero) </p>
<dt>13</p>
<dd> compressed data </p>
</dl>
<p> Note that there is no end-of-file marker in the file itself &#8211; the compressed data carries on right up to EOF. </p>
<p> The way the picture is compressed is essentially very simple, but as they say, the devil is in the detail. So don&#8217;t be put off if it sounds confusing. </p>
<p> The image is treated as a number of 64&#215;64 squares, forming a grid large enough to encompass it. (If an image is (say) 129&#215;65, it&#8217;ll be treated in the same way as a 192&#215;128 one. On decompression, the extra area which was encoded (the contents of this area is undefined) should be ignored.) Each of these squares in turn (in left-to-right, top-to-bottom order) is recursively subdivided until the smallest completely black or white squares are found. Some pseudocode (eek!) for the recursive subdivision routine should make things clearer: </p>
<pre><code>
if square size &gt; 1x1 and square is all one color, output 1 bit
    if whole square is black, output a 0 bit and return
    if whole square is white, output a 1 bit and return
    output a 0 bit
    divide the square into four quarters, calling routine for
    each in this order: top-left, top-right, bottom-left, bottom-right
</code></pre>
<p> (Note that the &#8216;output a 0 bit&#8217; stage is not reached for squares of size 1&#215;1, which is what stops it recursing infinitely. I mention this as it may not be immediately obvious.) </p>
<p> The whole of the compressed data is made up of the bits output by the above routine. The bits are packed into bytes MSB first, so for example outputting the bits 1,0,0,0,0,0,0,0 would result in a 80h byte being output. Any `unused&#8217; bits in the last byte output are undefined; these are effectively after EOF and their value is unimportant. </p>
<p> If writing that sounds too much like hard work :-), you could always adapt <code>pbmtomrf</code> and/or <code>mrftopbm</code>. That&#8217;s the main reason their source code is public domain, after all. </p>
<p> Above, I said the contents of any extra area encoded (when a bitmap smaller than the grid of squares is compressed) is undefined. This is deliberate so that the MRF compressor can make these unseen areas anything it wants so as to maximize compression, rather than simply leaving it blank. <code>pbmtomrf</code> does a little in this respect but could definitely be improved upon. </p>
<p> <code>mrftopbm</code>&#8216;s <code>-1</code> option causes it to include the edges, if any, in the output PBM. This may help when debugging a compressor&#8217;s edge optimization. </p>
<p> Note that the &quot;F&quot; in the name &quot;MRF&quot; comes from &quot;format,&quot; which is redundant because it is the name of a format. That sort of makes &quot;MRF format&quot; sound as stupid as &quot;PIN number,&quot; but it&#8217;s not really that bad. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mrftopbm/">mrftopbm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtomrf/">pbmtomrf</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Russell Marks. </p>
<h2>Index</h2>
