---
title: "miff(4)"
name: "miff"
section: "4"
letter: "m"
url: "/docs/linux/man/4-miff/"
description: "MIFF – Magick Image File Format"
---

<p>MIFF &#8211; Magick Image File Format</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;image.h&gt;</code></pre>
<h2>Description</h2>
<p>The Magick Image File Format (MIFF) is a platform-independent format for storing bitmap images. MIFF is a part of the ImageMagick toolkit of image manipulation utilities for the X Window System. ImageMagick is capable of converting many different image file formats to and from MIFF (e.g. JPEG, XPM, TIFF, etc.). A MIFF image file consist of two sections. The first section is a header composed of keys describing the image in text form. The next section is the binary image data. The header is separated from the image data by a <code>:</code> character immediately followed by a <code>newline</code>. The MIFF header is composed entirely of LATIN-1 characters. The fields in the header are key and value combination in the <i>key=value</i> format, with each key and value separated by an equal sign (=). Each <i>key=value</i> combination is delimited by at least one control or whitespace character. Comments may appear in the header section and are always delimited by braces. The MIFF header always ends with a colon (:) character, followed by a <code>ctrl-Z</code> character. It is also common to proceed the colon with a <code>formfeed</code> and a <code>newline</code> character. The <code>formfeed</code> prevents the listing of binary data when using <code><a href="/docs/linux/man/1-more/">more</a>(1)</code> under Unix where the <code>ctrl-Z</code> has the same effect with the <code>type</code> command on the Win32 command line. The following is a list of <i>key=value</i> combinations that may be found in a MIFF file:</p>
<dl>
<dt><code>background-color=</code><i>color</i></p>
<dd><code>border-color=</code><i>color</i> <code>matte-color=</code><i>color</i> these optional keys reflects the image background, border, and matte colors respectively. A color can be a name (e.g. white) or a hex value (e.g. #ccc).</p>
<dt><code>class=</code><i>DirectClass</i></p>
<dd><code>class=PseudoClass</code> the type of binary image data stored in the MIFF file. If this key is not present, <code>DirectClass</code> image data is assumed.</p>
<dt><code>colors=</code><i>value</i></p>
<dd>the number of colors in a <code>DirectClass</code> image. For a <code>PseudoClass</code> image, this key specifies the size of the colormap. If this key is not present in the header, and the image is <code>PseudoClass</code>, a linear 256 color grayscale colormap is used with the image data. The maximum number of colormap entries is 65535. <code>colorspace=CMYK</code> the colorspace of the pixel data. The default is RGB.</p>
<dt><code>columns=</code><i>value</i></p>
<dd>the width of the image in pixels. This is a required key and has no default.</p>
<dt><code>compression=BZip</code></p>
<dd><code>compression=Fax</code> <code>compression=JPEG</code> <code>compression=LZW</code> <code>compression=RLE</code> <code>compression=Zip</code> the type of algorithm used to compress the image data. If this key is not present, the image data is assumed to be uncompressed.</p>
<dt><code>delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd>the interframe delay in an image sequence. The maximum delay is 65535.</p>
<dt><code>depth=8</code></p>
<dd><code>depth=16</code> the depth of a single color value representing values from 0 to 255 (depth 8) or 65535 (depth 16). If this key is absent, a depth of 8 is assumed.</p>
<dt><code>dispose </code><i>value</i></p>
<dd>GIF disposal method. Here are the valid methods: </p>
<pre> 0 No disposal specified.
 1 Do not dispose between frames.
 2 Overwrite frame with background color from header.
 3 Overwrite with previous frame.</pre>
<dt><code>gamma=</code><i>value</i></p>
<dd>the gamma of the image. If it is not specified, a gamma of 1.0 (linear brightness response) is assumed,</p>
<dt><code>id=ImageMagick</code></p>
<dd>identifies the file as a MIFF-format image file. This key is required and has no default. Although this key can appear anywhere in the header, it should start as the first key of the header in column 1. This will allow programs like <code><a href="/docs/linux/man/1-file/">file</a></code>(1) to easily identify the file as MIFF.</p>
<dt><code>iterations </code><i>value</i></p>
<dd>the number of times an image sequence loops before stopping.</p>
<dt><code>label=</code><i>{value}</i></p>
<dd>defines a short title or caption for the image. If any whitespace appears in the label, it must be enclosed within braces.</p>
<dt><code>matte=True</code></p>
<dd><code>matte=False</code> specifies whether a <code>DirectClass</code> image has matte data. Matte data is generally useful for image compositing. This key has no meaning for pseudo-color images.</p>
<dt><code>montage=</code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x offset&gt;{+-}&lt;y offset&gt;</i></p>
<dd>size and location of the individual tiles of a composite image. See <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> for details about the geometry specification. Use this key when the image is a composite of a number of different tiles. A tile consists of an image and optionally a border and a label. <i>&lt;width&gt;</i> is the size in pixels of each individual tile in the horizontal direction and <i>&lt;height&gt;</i> is the size in the vertical direction. Each tile must have an equal number of pixels in width and equal in height. However, the width can differ from the height. <i>&lt;x offset&gt;</i> is the offset in number of pixels from the vertical edge of the composite image where the first tile of a row begins and <i>&lt;y offset&gt;</i> is the offset from the horizontal edge where the first tile of a column begins. If this key is specified, a directory of tile names must follow the image header. The format of the directory is explained below.</p>
<dt><code>page=</code><i>value</i></p>
<dd>preferred size and location of an image canvas.</p>
<dt><code>profile-icc=</code><i>value</i></p>
<dd>the number of bytes in the International Color Consortium color profile. The profile is defined by the ICC profile specification located at <a href="ftp://sgigate.sgi.com/pub/icc/icc34.ps.">ftp://sgigate.sgi.com/pub/icc/icc34.ps.</a></p>
<dt><code>colorspace=RGB</code></p>
<dd>
<dt><code>red-primary=</code><i>x,y</i></p>
<dd><code>green-primary=</code><i>x,y</i> <code>blue-primary=</code><i>x,y</i> <code>white-point=</code><i>x,y</i> this optional key reflects the chromaticity primaries and white point.</p>
<dt><code>rendering-intent=saturation</code></p>
<dd><code>rendering-intent=perceptual</code> <code>rendering-intent=absolute</code> <code>rendering-intent=relative</code> Rendering intent is the CSS-1 property that has been defined by the International Color Consortium (<a rel="nofollow" href="http://www.color.org">http://www.color.org</a>).</p>
<dt><code>resolution=</code><i>&lt;x-resolution&gt;x&lt;y-resolution&gt;</i></p>
<dd>vertical and horizontal resolution of the image. See <code>units</code> for the specific resolution units (e.g. pixels per inch).</p>
<dt><code>rows=</code><i>value</i></p>
<dd>the height of the image in pixels. This is a required key and has no default.</p>
<dt><code>scene=</code><i>value</i></p>
<dd>the sequence number for this MIFF image file. This optional key is used when a MIFF image file is one in a sequence of files used in an animation.</p>
<dt><code>signature=</code><i>value</i></p>
<dd>this optional key contains a string that uniquely identifies the image pixel contents. NIST&#8217;s SHA-256 message digest algorithm is recommended.</p>
<dt><code>units=pixels-per-inch</code></p>
<dd><code>units=pixels-per-centimeter</code> image resolution units. Other key value pairs are permitted. If a value contains whitespace it must be enclosed with braces as illustrated here: </p>
<pre><code>id=ImageMagick

class=PseudoClass  colors=256

compression=RunlengthEncoded  packets=27601

columns=1280  rows=1024

signature=d79e1c308aa5bbcdeea8ed63df412da9

copyright={Copyright (c) 2001 ImageMagick Studio}

&lt;FF&gt;

:
</code></pre>
<p> Note that <i>key=value</i> combinations may be separated by newlines or spaces and may occur in any order within the header. Comments (within braces) may appear anywhere before the colon. If you specify the <code>montage</code> key in the header, follow the header with a directory of image tiles. This directory consists of a name for each tile of the composite image separated by a <code>newline</code> character. The list is terminated with a NULL character. If you specify the <code>color-profile</code> key in the header, follow the header (or montage directory if the <code>montage</code> key is in the header) with the binary color profile. Next comes the binary image data itself. How the image data is formatted depends upon the class of the image as specified (or not specified) by the value of the <code>class</code> key in the header. DirectClass images (class=DirectClass) are continuous-tone, images stored as RGB (red, green, blue), RGBA (red, green, blue, alpha), or CMYK (cyan, yellow, magenta, black) intensity values as defined by the colorspace key. Each intensity value is one byte in length for images of depth 8 (0..255), whereas, images of depth 16 (0..65535) require two bytes in most significant byte first order. PseudoClass images (class=PseudoClass) are colormapped RGB images. The colormap is stored as a series of red, green, and blue pixel values, each value being a byte in size. If the image depth is 16, each colormap entry consumes two bytes with the most significant byte being first. The number of colormap entries is defined by the colors key. The colormap data occurs immediately following the header (or image directory if the montage key is in the header). PseudoClass image data is an array of index values into the color map. If there are 256 or fewer colors in the image, each byte of image data contains an index value. If the image contains more than 256 colors or the image depth is 16, the index value is stored as two contiguous bytes with the most significant byte being first. If matte is true, each colormap index is followed by a 1 or 2-byte alpha value. The image data in a MIFF file may be uncompressed, runlength encoded, Zip compressed, or BZip compressed. The compression key in the header defines how the image data is compressed. Uncompressed pixels are just stored one scanline at a time in row order. Runlength encoded compression counts runs of identical adjacent pixels and stores the pixels followed by a length byte (the number of identical pixels minus 1). Zip and BZip compression compresses each row of an image and preceeds the compressed row with the length of compressed pixel bytes as a word in most significant byte first order. MIFF files may contain more than one image. Simply concatenate each individual image (composed of a header and image data) into one file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-display/">display</a>(1), <a href="/docs/linux/man/1-animate/">animate</a>(1), <a href="/docs/linux/man/1-import/">import</a>(1), <a href="/docs/linux/man/1-montage/">montage</a>(1), <a href="/docs/linux/man/1-mogrify/">mogrify</a>(1), <a href="/docs/linux/man/1-convert/">convert</a>(1), <a href="/docs/linux/man/1-more/">more</a>(1), <a href="/docs/linux/man/1-compress/">compress</a>(1)</code></p>
<h2>Copyright</h2>
<p>Copyright (C) 2000 ImageMagick Studio, a non-profit organization dedicated to making software imaging solutions freely available. </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (&quot;ImageMagick&quot;), to deal in ImageMagick without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of ImageMagick, and to permit persons to whom the ImageMagick is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of ImageMagick. </p>
<p> The software is provided &quot;as is&quot;, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall ImageMagick Studio be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with ImageMagick or the use or other dealings in ImageMagick. </p>
<p> Except as contained in this notice, the name of the ImageMagick Studio shall not be used in advertising or otherwise to promote the sale, use or other dealings in ImageMagick without prior written authorization from the ImageMagick Studio.</p>
<h2>Authors</h2>
<p>John Cristy, ImageMagick Studio</p>
