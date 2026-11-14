---
title: "pamtotiff(1)"
name: "pamtotiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtotiff/"
description: "pamtotiff – convert a Netpbm image to a TIFF file"
---

<h2 class="name">NAME</h2>
<p> pamtotiff &#8211; convert a Netpbm image to a TIFF file</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtotiff</code> </p>
<p> [<code>-none</code> | <code>-packbits</code> | <code>-lzw</code> | <code>-g3</code> | <code>-g4</code> | <code>-flate</code> | <code>-adobeflate</code>] </p>
<p> [<code>-2d</code>] </p>
<p> [<code>-fill</code>] </p>
<p> [<code>-predictor=</code><i>n</i>] </p>
<p> [<code>-msb2lsb</code>|<code>-lsb2msb</code>] </p>
<p> [<code>-rowsperstrip=</code><i>n</i>] </p>
<p> [<code>-minisblack</code>|<code>-miniswhite</code>|<code>mb</code>|<code>mw</code>] </p>
<p> [<code>-truecolor</code>] </p>
<p> [<code>-color</code>] </p>
<p> [<code>-indexbits=</code><i>bitwidthlist</i>] [<code>-xresolution=</code><i>xres</i>] </p>
<p> [<code>-yresolution=</code><i>yres</i>] [<code>-resolutionunit=</code>{<code>inch</code> | <code>centimeter</code> | <code>none</code> | <code>in</code> | <code>cm</code> | <code>no</code>}] </p>
<p> [<code>-indexbits=</code>[<code>1</code>[<code>2</code>[<code>4</code>[<code>8</code>]]]]] </p>
<p> [<code>-append</code>] </p>
<p> [<code>-tag=</code><i>taglist</i>] </p>
<p> [<i>pamfile</i>] </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtotiff</code> reads a PNM or PAM image as input and produces a TIFF file as output. </p>
<p> Actually, it handles multi-image Netpbm streams, producing multi-image TIFF streams (i.e. a TIFF stream with multiple &#8216;directories&#8217;). But before Netpbm 10.27 (March 2005), it ignored all but the first Netpbm image in the input stream. </p>
<h3>The Output File</h3>
<p> The output goes to Standard Output. <code>pamtotiff</code> approaches this output file differently from Unix and Netpbm convention. This is entirely due to <code>pamtotiff</code>&#8216;s use of the TIFF library to do all TIFF output. </p>
<dl>
<dt>&bull;</p>
<dd> The output file must be seekable. <code>pamtotiff</code> does not write it sequentially. Therefore, you can&#8217;t use a pipe; you can&#8217;t pipe the output of <code>pamtotiff</code> to some other program. But any regular file should work. </p>
<dt>&bull;</p>
<dd> If the output file descriptor is readable, you must either specify <code>-append</code> so as to add to the existing file, or make sure the file is empty. Otherwise, <code>pamtotiff</code> will fail with an unhelpful message telling you that a TIFF library function failed to open the TIFF output stream. </p>
<dt>&bull;</p>
<dd> If you are converting multiple images (your input stream contains multiple images), the output file must be both readable and writable. </p>
</dl>
<p> If you&#8217;re using a Unix command shell to run <code>pamtotiff</code>, you use facilities of your shell to set up Standard Output. In Bash, for example, you would set up a write-only Standard Output to the file /tmp/myimage.tiff like this: </p>
<pre>
<tt>
    $ pamtotiff myimage.pnm &gt;/tmp/myimage.tiff
</tt>
</pre>
<p> In Bash, you would set up a read/write Standard Output to the file /tmp/myimage.tiff like this: </p>
<pre>
<tt>
    $ pamtotiff myimage.pnm 1&lt;&gt;/tmp/myimage.tiff
</tt>
</pre>
<h3>TIFF Capability</h3>
<p> <code>pamtotiff</code> uses the Libtiff.org TIFF library (or whatever equivalent you provide) to generate the TIFF output. Details of the format it produces are therefore controlled by that library. </p>
<h2>OPTIONS</h2>
<h3>Compression</h3>
<p> By default, <code>pamtotiff</code> creates a TIFF file with no compression. This is your best bet most of the time. If you want to try another compression scheme or tweak some of the other even more obscure output options, there are a number of options which to play. </p>
<p> Before Netpbm 8.4 (April 2000), the default was to use LZW compression. But then new releases of the TIFF library started omitting the LZW compression capability due to concern about patents on LZW. So since then, the default has been no compression. The LZW patents have now expired and new TIFF libraries do LZW, but the <code>pamtotiff</code> behavior remains the same for compatibility with older TIFF libraries and applications of <code>pamtotiff</code>. </p>
<p> The <code>-none</code>, <code>-packbits</code>, <code>-lzw</code>, <code>-g3</code>, <code>-g4</code>, <code>-flate</code>, and <code>-adobeflate</code> options are used to override the default and set the compression scheme used in creating the output file. </p>
<p> The <code>-predictor</code> option is meaningful only with LZW compression: a predictor value of 2 causes each scanline of the output image to undergo horizontal differencing before it is encoded; a value of 1 forces each scanline to be encoded without differencing. By default, <code>pamtotiff</code> creates a TIFF file with msb-to-lsb fill order. The <code>-msb2lsb</code> and <code>-lsb2msb</code> options are used to override the default and set the fill order used in creating the file. </p>
<p> With some older TIFF libraries, <code>-lzw</code> doesn&#8217;t work because the TIFF library doesn&#8217;t do LZW compression. This is because of concerns about Unisys&#8217;s patent on LZW which was then in force. Actually, with very old TIFF libraries, <code>-lzw</code> works because no distributors of the TIFF library were sensitive yet to the patent issue. </p>
<p> <code>-flate</code> chooses &#8216;flate&#8217; compression, which is the patent-free compression common in the Unix world implemented by the &#8216;Z&#8217; library. It is what the PNG format uses. </p>
<p> <code>Fax Compression</code> </p>
<p> If you have bilevel data (e.g. PBM), you can generate a TIFF that uses the same compression scheme specified for use by fax machines. See the <code>Fax</code><a href="/docs/linux/man/1-format/">Format</a><code>(1)</code><br />
&nbsp;<wbr>page for more information on these compression schemes. </p>
<p> These formats all relate to ITU Group 3 and Group 4 fax machine standards. </p>
<p> The <code>-g3</code> option chooses MH or MR compression: MR with the additional option <code>-2d</code>; MH without it. <code>-g4</code> selects MMR. The option names are a little unfortunate and historical, but are consistent with the TIFF specification. </p>
<p> MMR has a better compression ratio than the other two. </p>
<p> <code>-fill</code> specifies that for MH or MR compression, each encoded scanline shall be zero-filled to a byte boundary. </p>
<p> <code>-2d</code> and <code>-fill</code> are meaningful only with <code>-g3</code>. </p>
<h3>Fill Order</h3>
<p> The <code>-msb2lsb</code> and <code>lsb2msb</code> options control the fill order. </p>
<p> The fill order is the order in which pixels are packed into a byte in the Tiff raster, in the case that there are multiple pixels per byte. msb-to-lsb means that the leftmost columns go into the most significant bits of the byte in the Tiff image. However, there is considerable confusion about the meaning of fill order. Some believe it means whether 16 bit sample values in the Tiff image are little-endian or big-endian. This is totally erroneous (The endianness of integers in a Tiff image is designated by the image&#8217;s magic number). However, ImageMagick and older Netpbm both have been known to implement that interpretation. 2001.09.06. </p>
<p> If the image does not have sub-byte pixels, these options have no effect other than to set the value of the FILLORDER tag in the Tiff image (which may be useful for those programs that misinterpret the tag with reference to 16 bit samples). </p>
<h3>Color Space</h3>
<p> <code>-color</code> tells <code>pamtotiff</code> to produce a color, as opposed to grayscale, TIFF image if the input is PPM, even if it contains only shades of gray. Without this option, <code>pamtotiff</code> produces a grayscale TIFF image if the input is PPM and contains only shades of gray, and at most 256 shades. Otherwise, it produces a color TIFF output. For PBM and PGM input, <code>pamtotiff</code> always produces grayscale TIFF output and this option has no effect. </p>
<p> The <code>-color</code> option can prevent <code>pamtotiff</code> from making two passes through the input file, thus improving speed and memory usage. See Multiple Passes . </p>
<p> <code>-truecolor</code> tells <code>pamtotiff</code> to produce the 24-bit RGB form of TIFF output if it is producing a color TIFF image. Without this option, <code>pamtotiff</code> produces a colormapped (paletted) TIFF image unless there are more than 256 colors (and in the latter case, issues a warning). </p>
<p> The <code>-truecolor</code> option can prevent <code>pamtotiff</code> from making two passes through the input file, thus improving speed and memory usage. See Multiple Passes . </p>
<p> The <code>-color</code> and <code>-truecolor</code> options did not exist before Netpbm 9.21 (December 2001). </p>
<p> If <code>pamtotiff</code> produces a grayscale TIFF image, this option has no effect. </p>
<p> The <code>-minisblack</code> and <code>-miniswhite</code> options force the output image to have a &#8216;minimum is black&#8217; or &#8216;minimum is white&#8217; photometric, respectively. If you don&#8217;t specify either, <code>pamtotiff</code> uses minimum is black except when using Group 3 or Group 4 compression, in which case <code>pamtotiff</code> follows CCITT fax standards and uses &#8216;minimum is white.&#8217; This usually results in better compression and is generally preferred for bilevel coding. </p>
<p> Before February 2001, <code>pamtotiff</code> always produced &#8216;minimum is black,&#8217; due to a bug. In either case, <code>pamtotiff</code> sets the photometric interpretation tag in the TIFF output according to which photometric is actually used. </p>
<p> The <code>-indexbits</code> option is meaningful only for a colormapped (paletted) image. In this kind of image, the raster contains values which are indexes into a table of colors, with the indexes normally taking less space that the color description in the table. <code>pamtotiff</code> can generate indexes of 1, 2, 4, or 8 bits. By default, it will use 8, because many programs that interpret TIFF images can&#8217;t handle any other width. </p>
<p> But if you have a small number of colors, you can make your image considerably smaller by allowing fewer than 8 bits per index, using the <code>-indexbits</code> option. The value is a comma-separated list of the bit widths you allow. <code>pamtotiff</code> chooses the smallest width you allow that allows it to index the entire color table. If you don&#8217;t allow any such width, <code>pamtotiff</code> fails. Normally, the only useful value for this option is <code>1,2,4,8</code>, because a program either understands the 8 bit width (default) or understands them all. </p>
<p> In a Baseline TIFF image, according to the 1992 TIFF 6.0 specification, 4 and 8 are the only valid widths. There are no formal standards that allow any other values. </p>
<p> This option was added in June 2002. Before that, only 8 bit indices were possible. </p>
<h3>Extra Tags</h3>
<p> There are lots of tag types in the TIFF format that don&#8217;t correspond to any information in the PNM format or to anything in the conversion process. For example, a TIFF_ARTIST tag names the artist who created the image. </p>
<p> You can tell <code>pamtotiff</code> explicitly to include tags such as this in its output with the <code>-tag</code> option. You identify a list of tag types and values and <code>pamtotiff</code> includes a tag in the output for each item in your list. </p>
<p> The value of <code>-tag</code> is the list of tags, like this example: </p>
<pre>
<tt>
    -tag=subfiletype=reducedimage,documentname=Fred,xposition=25
</tt>
</pre>
<p> As you see, it is a list of tag specifications separated by commas. Each tag specification is a name and a value separated by an equal sign. The name is the name of the tag type, except in arbitrary upper/lower case. One place to see the names of TIFF tag types is in the TIFF library&#8217;s <code>tiff.h</code> file, where there is a macro defined for each consisting of &#8216;TIFF_&#8217; plus the name. E.g. for the SUBFILETYPE tag type, there is a macro TIFF_SUBFILETYPE. </p>
<p> The format of the value specification for a tag (stuff after the equal sign) depends upon what kind of value the tag type has: </p>
<dl>
<dt>&bull;</p>
<dd> Integer: a decimal number </p>
<dt>&bull;</p>
<dd> Floating point number: a decimal number </p>
<dt>&bull;</p>
<dd> String: a string </p>
<dt>&bull;</p>
<dd> Enumerated (For example, a &#8216;subfiletype&#8217; tag takes an enumerated value. Its possible values are REDUCEDIMAGE, PAGE, and MASK.): The name of the value. You can see the possible value names in the TIFF library&#8217;s <code>tiff.h</code> file, where there is a macro defined for each consisting of a qualifier plus the value name. E.g. for the REDUCEDIMAGE value of a SUBFILETYPE tag, you see the macro FILETYPE_REDUCEDIMAGE. </p>
<p> The TIFF format assigns a unique number to each enumerated value and you can specify that number, in decimal, as an alternative. This is useful if you are using an extension of TIFF that <code>pamtotiff</code> doesn&#8217;t know about. </p>
</dl>
<p> If you specify a tag type with <code>-tag</code> that is not independent of the content of your PNM source image and <code>pamtotiff</code>&#8216;s conversion process (i.e. a tag type in which <code>pamtotiff</code> is interested), <code>pamtotiff</code> fails. For example, you cannot specify an IMAGEWIDTH tag with <code>-tag</code>, because <code>pamtotiff</code> generates an IMAGEWIDTH tag that gives the actual width of the image. </p>
<p> <code>-tag</code> was new in Netpbm 10.31 (December 2005). </p>
<h3>Other</h3>
<p> You can use the <code>-rowsperstrip</code> option to set the number of rows (scanlines) in each strip of data in the output file. By default, the output file has the number of rows per strip set to a value that will ensure each strip is no more than 8 kilobytes long. </p>
<p> The <code>-append</code> option tells <code>pamtotiff</code> to add images to the existing output file (a TIFF file may contain multiple images) instead of the default, which is to replace the output file. </p>
<p> <code>-append</code> was new in Netpbm 10.27 (March 2005). </p>
<h2>NOTES</h2>
<p> There are myriad variations of the TIFF format, and this program generates only a few of them. <code>pamtotiff</code> creates a grayscale TIFF file if its input is a PBM (monochrome) or PGM (grayscale) or equivalent PAM file. <code>pamtotiff</code> also creates a grayscale file if it input is PPM (color) or equivalent PAM, but there is only one color in the image. </p>
<p> If the input is a PPM (color) file and there are 256 colors or fewer, but more than 1, <code>pamtotiff</code> generates a color palette TIFF file. If there are more colors than that, <code>pamtotiff</code> generates an RGB (not RGBA) single plane TIFF file. Use <code>pnmtotiffcmyk</code> to generate the cyan-magenta-yellow-black ink color separation TIFF format. </p>
<p> The number of bits per sample in the TIFF output is determined by the maxval of the Netpbm input. If the maxval is less than 256, the bits per sample in the output is the smallest number that can encode the maxval. If the maxval is greater than or equal to 256, there are 16 bits per sample in the output. </p>
<h3>Extra Channels</h3>
<p> Like most Netpbm programs, <code>pamtotiff</code>&#8216;s function is mostly undefined if the input is PAM image with tuple type other than BLACKANDWHITE, GRAYSCALE, or RGB. Most of the statements in this manual assume the input is not such an exotic PAM. But there is a little defined processing of other PAM subformats. </p>
<p> <code>pamtotiff</code> assumes any 1 plane PAM image is BLACKANDWHITE or GRAYSCALE (and doesn&#8217;t distinguish between those two). </p>
<p> <code>pamtotiff</code> assumes a PAM with more than 1 plane is of tuple type RGB except with that number of planes instead of 3. <code>pamtotiff</code> doesn&#8217;t really understand red, green, and blue, so it has no trouble with a 2-component or 5-component color space. The TIFF format allows an arbitrary number of color components, so <code>pamtotiff</code> simply maps the PAM planes directly to TIFF color components. I don&#8217;t know if the meanings of 5 components in a TIFF image are standard at all, but the function is there if you want to use it. </p>
<p> Note that <code>pamtotiff</code> may generate either a truecolor or colormapped image with an arbitrary number of color components. In the truecolor case, the raster has that number of planes. In the colormapped case, the raster has of course 1 plane, but the color map has all the color components in it. </p>
<p> The most common reason for a PAM to have extra planes is when the tuple type is xxx_ALPHA, which means the highest numbered plane is a transparency plane (alpha channel). At least one user found that a TIFF with an extra plane for transparency was useful. </p>
<p> Note that the grayscale detection works on N-component colors, so if your planes aren&#8217;t really color components, you&#8217;ll want to disable this via the <code>-color</code> option. </p>
<h3>Multiple Passes</h3>
<p> <code>pamtotiff</code> reads the input image once if it can, and otherwise twice. It needs that second pass (which happens before the main pass, of course) to analyze the colors in the image and generate a color map (palette) and determine if the image is grayscale. So the second pass happens only when the input is PPM. And you can avoid it then by specifying both the <code>-truecolor</code> and <code>-color</code> options. </p>
<p>&nbsp;<wbr>If the input image is small enough to fit in your system&#8217;s file cache, the second pass is very fast. If not, it requires reading from disk twice, which can be slow. </p>
<p> When the input is from a file that cannot be rewound and reread, <code>pamtotiff</code> reads the entire input image into a temporary file which can, and works from that. Even if it needs only one pass. </p>
<p> Before Netpbm 9.21 (December 2001), <code>pamtotiff</code> always read the entire image into virtual memory and then did one, two, or three passes through the memory copy. The <code>-truecolor</code> and <code>-color</code> options did not exist. The passes through memory would involve page faults if the entire image did not fit into real memory. The image in memory required considerably more memory (12 bytes per pixel) than the cached file version of the image would. </p>
<h3>Resolution</h3>
<p> A Tiff image may contain information about the resolution of the image, which means how big in real dimensions (centimeters, etc.) each pixel in the raster is. That information is in the TIFF XRESOLUTION, YRESOLUTION, and RESOLUTIONUNIT tags. By default, <code>pamtotiff</code> does not include any tags of these types, but you can specify them with the <code>-tags</code> option. </p>
<p> There are also options <code>-xresolution</code>, <code>-yresolution</code>, and <code>-resolutionunit</code>, but those are obsolete. Before <code>-tags</code> existed (before Netpbm 10.31 (December 2005), they were the only way. </p>
<p> Note that the number of pixels in the image and how much information each contains is determined independently from the setting of the resolution tags. The number of pixels in the output is the same as in the input, and each pixel contains the same information. For your resolution tags to be meaningful, they have to consistent with whatever created the PNM input. E.g. if a scanner turned a 10 centimeter wide image into a 1000 pixel wide PNM image, then your horizontal resolution is 100 pixels per centimeter, and if your XRESOLUTION tag says anything else, something that prints your TIFF image won&#8217;t print the proper 10 centimeter image. </p>
<p> The value of the XRESOLUTION tag is a floating point decimal number that tells how many pixels there are per unit of distance in the horizontal direction. <code>-yresolution</code> is analogous for the vertical direction. </p>
<p> The unit of distance is given by the value of the RESOLUTIONUNIT option. That value is either INCH, CENTIMETER, or NONE. NONE means the unit is arbitrary or unspecified. This could mean that the creator and user of the image have a separate agreement as to what the unit is. But usually, it just means that the horizontal and vertical resolution values cannot be used for anything except to determine aspect ratio (because even though the unit is arbitrary or unspecified, it has to be the same for both resolution numbers). </p>
<p> If you <i>don&#8217;t</i> use a <code>-tag</code> option to specify the resolution tag and use the obsolete options instead, note the following: </p>
<dl>
<dt>&bull;</p>
<dd> If you don&#8217;t include an specify <code>-xresolution</code>, the Tiff image does not contain horizontal resolution information. Likewise for <code>-yresolution</code>. If you don&#8217;t specify <code>-resolutionunit</code>, the default is inches. </p>
<dt>&bull;</p>
<dd> Before Netpbm 10.16 (June 2003), <code>-resolutionunit</code> did not exist and the resolution unit was always inches. </p>
</dl>
<h2>HISTORY</h2>
<p> <code>pamtotiff</code> was originally <code>pnmtotiff</code> and did not handle PAM input. It was extended and renamed in Netpbm 10.30 (October 2005). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tifftopnm/">tifftopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtotiffcmyk/">pnmtotiffcmyk</a></code>(1) , <code><a href="/docs/linux/man/1-pamdepth/">pamdepth</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Derived by Jef Poskanzer from ras2tiff.c, which is Copyright (c) 1990 by Sun Microsystems, Inc. Author: Patrick J. Naughton (<i>naughton [at] wind.sun.com</i>). </p>
<h2>Index</h2>
