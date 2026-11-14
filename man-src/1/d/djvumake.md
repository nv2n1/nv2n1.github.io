---
title: "djvumake(1)"
name: "djvumake"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvumake/"
description: "djvumake – Assemble DjVu image files."
---

<h2 class="name">NAME</h2>
<p> djvumake &#8211; Assemble DjVu image files.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvumake </code><i>djvufile</i><code> [</code><i>chkid</i><code>=</code><i>argument</i><code>]&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvumake</code> assembles a single-page DjVu file <i>djvufile</i> by copying or creating chunks according to the provided arguments. Supported arguments are as follows:</p>
<dl>
<dt><code>INFO=</code><i>w</i><code>,</code><i>h</i><code>,</code><i>dpi</i></p>
<dd> Create the initial information chunk. Arguments <i>w</i>, <i>h</i>, and <i>dpi</i> describe the width, height and resolution of the image. All arguments may be omitted. The default resolution is 300 dpi. The default width and height will be retrieved from the first mask chunk specified in the command line options.</p>
<dt><code>Sjbz=</code><i>jb2file</i></p>
<dd> Create a <font SIZE="-1">JB2 </font> foreground mask chunk. File <i>jb2file</i> may contain raw JB2 data, or be a DjVu file containing JB2 data such as those produced by program <code>cjb2</code>.</p>
<dt><code>Smmr=</code><i>mmrfile</i></p>
<dd> Create a <font SIZE="-1">MMR/G4 </font> foreground mask chunk. File <i>mmrfile</i> may contain raw MMR data or be a DjVu file containing MMR data.</p>
<dt><code>BG44=</code><i>iw44file</i><code>[:</code><i>n</i><code>]</code></p>
<dd> Create one or more <font SIZE="-1">IW44 </font> background chunks. File <i>iw44file </i> must contain <font SIZE="-1">IW44 </font> data. Such files can be obtained by compressing the background image with program <code>c44</code> and extracting the raw <font SIZE="-1">IW44 </font> data using program <code>djvuextract</code>. The optional argument <i>n</i> indicates the number of chunks to copy from the IW44 file. Omitting the number of chunks copies all available chunks.</p>
<dt><code>BGjp=</code><i>jpegfile</i></p>
<dd> Create a <font SIZE="-1">JPEG</font> encoded background chunk. File <i>jpegfile</i> must contain <font SIZE="-1">JPEG </font> encoded data.</p>
<dt><code>BG2k=</code><i>jpegfile</i></p>
<dd> Create a <font SIZE="-1">JPEG-2000 </font> background chunk. File <i>jpegfile</i> must contain <font SIZE="-1">JPEG-2000</font> encoded data. The DjVu decoder does not yet display files containing JPEG-2000 data.</p>
<dt><code>FGbz=(</code><i>filename</i><code>|{#</code><i>color</i><code>[:</code><i>x</i><code>,</code><i>y</i><code>,</code><i>w</i><code>,</code><i>h</i><code>]})</code></p>
<dd> Create a foreground color chunk describing one solid color for each <font SIZE="-1">JB2</font> encoded mark. The argument can be the name <i>filename</i> of a file containing the raw data. Such files are best created using program <code><a href="/docs/linux/man/1-djvuextract/">djvuextract</a></code>(1). Alternatively the argument could describe a sequence of color zones. Each color zone specifies a color name <i>color</i>, and optionally the coordinates <i>x</i>,<i>y</i>,<i>w</i>,<i>h</i> of a rectangle. Each mark receives the color of the last color zone whose rectangle intersects the bounding box of the mark. The mark is painted black if its bounding box does not intersect one of the zones. The rectangle coordinates are expressed in pixels with the origin at the bottom left corner of the page. The full page is assumed when no rectangle coordinates are specified. Color names can be specified with exactly six hexadecimal digits, e.g. <code>FGbz=#FF8080</code>, or by one of the following sixteen HTML color names defined by the W3C, e.g. <code>FGbz=#red</code>.<br />
 <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>aqua</code></td>
<td><code>black</code></td>
<td><code>blue</code></td>
<td><code>fuchsia</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>gray</code></td>
<td><code>green</code></td>
<td><code>lime</code></td>
<td><code>maroon</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>navy</code></td>
<td><code>olive</code></td>
<td><code>purple</code></td>
<td><code>red</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>silver</code></td>
<td><code>teal</code></td>
<td><code>white</code></td>
<td><code>yellow</code>
</td>
</tr>
</table>
</table>
<p></center></p>
<dt><code>FG44=</code><i>iw44file</i></p>
<dd> Create a <font SIZE="-1">IW44 </font> foreground color chunk. File <i>iw44file </i> must contain <font SIZE="-1">IW44 </font> data. Such files can be obtained by compressing the background image with command <code>c44</code> and extracting the raw <font SIZE="-1">IW44 </font> data using program <code>djvuextract</code>. Only the first chunk is copied.</p>
<dt><code>FGjp=</code><i>jpegfile</i></p>
<dd> Create a <font SIZE="-1">JPEG</font> foreground color chunk.</p>
<dt><code>FG2k=</code><i>jpegfile</i></p>
<dd> Create a <font SIZE="-1">JPEG-2000</font> foreground color chunk. The DjVu decoder does not yet display files containing JPEG-2000 data.</p>
<dt><code>INCL=</code><i>fileid</i></p>
<dd> Create a DjVu3 include chunk pointing to the component file named <i>fileid</i>. The resulting file should then be included into a multipage document using command <code>djvm</code>.</p>
<dt><code>Djbz=</code><i>jb2file</i></p>
<dd> Create a <font SIZE="-1">JB2 </font> shape dictionary. File <i>jb2file</i> must contain raw JB2 data describing a JB2 dictionary.</p>
<dt><code>PPM=</code><i>ppmfile</i></p>
<dd> Create a <font SIZE="-1">IW44</font> background chunk and a <font SIZE="-1">IW44 </font> foreground color chunk by masking and subsampling the <font SIZE="-1">PPM</font> file <i>ppmfile.</i> </p>
<p> Assume, for instance, that we have a <font SIZE="-1">PPM </font> image <code>myimage.ppm</code> and an identically sized <font SIZE="-1">PBM</font> bitonal image <code>mymask.pbm</code> whose black pixels indicate which pixels belong to the foreground. Such a bitonal file might have been obtained by thresholding or color-keying the <font SIZE="-1">PPM </font> image. We can then produce a DjVuDocument image using the following two commands:</p>
<dt>
<dd> <code>cjb2 mymask.pbm mymask.djvu</code><br />
 <code>djvumake my.djvu Sjbz=mymask.djvu PPM=myimage.ppm</code> </p>
</dl>
<p> The DjVu specification documents in the directory <code>doc</code> of the DjVuLibre distribution provide the authoritative information about the composition of a legal DjVu image file. </p>
<h2>CREDITS</h2>
<p> This program was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was then improved by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt;, Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvuextract/">djvuextract</a></code>(1), <code><a href="/docs/linux/man/1-cjb2/">cjb2</a></code>(1), <code><a href="/docs/linux/man/1-c44/">c44</a></code>(1) </p>
<h2>Index</h2>
