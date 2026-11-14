---
title: "pngquant(1)"
name: "pngquant"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pngquant/"
description: "pngquant – PNG converter and lossy image compressor"
---

<h2 class="name">NAME</h2>
<p> <code>pngquant</code> &#8211; PNG converter and lossy image compressor </p>
<h2>SYNOPSIS</h2>
<p> <code>pngquant</code> Aq options [ncolors] file [<i>file &#8230;</i> ]<br />
<code>pngquant</code> Aq options [ncolors] &#8211; <code>&lt; file </code> <code>&gt; file </code></p>
<h2>DESCRIPTION</h2>
<p> <code>pngquant</code> converts 32-bit RGBA PNGs to 8-bit (or smaller) RGBA-palette PNGs, optionally using Floyd-Steinberg dithering. The output filename is the same as the input name except that it ends in `-fs8.png&#8217; or `-or8.png&#8217; (unless the input is stdin, in which case the quantized image will go to stdout). The default behavior if the output file exists is to skip the conversion; use &#8211;<code>-force</code> to overwrite.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o </code><i>out.png , &#8211;</i><code>-output </code><i>out.png</i></p>
<dd> Writes converted file to the given path. When this option is used only single input file is allowed.</p>
<dt><code>&#8211;ext </code><i>new.png</i></p>
<dd> File extension (suffix) to use for output files instead of the default `-fs8.png&#8217; or `-or8.png&#8217;</p>
<dt><code>-f , &#8211;force</code></p>
<dd> Overwrite existing output files. Do &#8211;<code>-ext</code> <i>.png</i> &#8211;<code>-force</code> Dc can be used to convert files in place (which is unsafe).</p>
<dt><code>&#8211;nofs , &#8211;ordered</code></p>
<dd> Disable Floyd-Steinberg dithering.</p>
<dt><code>&#8211;floyd </code>[<i>=N</i> ]</p>
<dd> Set dithering level using fractional number between <code>0</code> (none) and <code>1</code> (full, the default).</p>
<dt><code>-s </code><i>N , &#8211;</i><code>-speed </code><i>N</i></p>
<dd> <code>1</code> (brute-force) to <code>11</code> (fastest). The default is <code>3</code> Speed <code>10</code> has 5% lower quality, but is about 8 times faster than the default. Speed 11 disables dithering and lowers compression level.</p>
<dt><code>-Q </code><i>min-max , &#8211;</i><code>-quality </code><i>min-max</i></p>
<dd> <i>min</i> and <i>max</i> are numbers in range <code>0</code> (worst) to <code>100</code> (perfect), similar to JPEG. <code>pngquant</code> will use the least amount of colors required to meet or exceed the <i>max</i> quality. If conversion results in quality below the <i>min</i> quality the image won&#8217;t be saved (or if outputting to stdin, 24-bit original will be output) and pngquant will exit with status code Er 99 .</p>
<dt><code>&#8211;skip-if-larger</code></p>
<dd> If conversion results in a file larger than the original, the image won&#8217;t be saved and pngquant will exit with status code Er 98 . Additionally, file size gain must be greater than the amount of quality lost. If quality drops by 50%, it will expect 50% file size reduction to consider it worthwhile.</p>
<dt><code>&#8211;posterize </code><i>bits</i></p>
<dd> Truncate number of least significant bits of color (per channel). Use this when image will be output on low-depth displays (e.g. 16-bit RGB). <code>pngquant</code> will make almost-opaque pixels fully opaque and will reduce amount of semi-transparent colors. When this option is enabled the default filename suffix is `-ie-fs8.png&#8217; / `-ie-or8.png&#8217;</p>
<dt><code>&#8211;strip</code></p>
<dd> Remove optional chunks (metadata) from PNG files.</p>
<dt><code>&#8211;transbug</code></p>
<dd> Workaround for readers that expect fully transparent color to be the last entry in the palette.</p>
<dt><code>-v , &#8211;verbose</code></p>
<dd> Enable verbose messages showing progress and information about input/output. Opposite is &#8211;<code>-quiet</code> Errors are output to stderr regardless of this option.</p>
<dt><code>-V , &#8211;version</code></p>
<dd> Display version on stdout and exit.</p>
<dt><code>-h , &#8211;help</code></p>
<dd> Display help and exit.</dl>
<h2>EXAMPLE</h2>
<p> Creating a new image with the number of colors reduced to 64: </p>
<blockquote><p> <code>pngquant</code> <code>64 image.png</code> </p></blockquote>
<p> The resulting image will have 64 colors and will be saved as image-fs8.png </p>
<p> Overwriting image in-place if it can be reduced without too much quality loss: </p>
<blockquote><p> <code>pngquant</code> <code>-f &#8211;ext .png &#8211;quality 70-95 image.png</code> </p></blockquote>
<h2>AUTHOR</h2>
<p> <code>pngquant</code> is developed by Kornel Lesinski Aq Mt kornel [at] pngquant.org based on code by Greg Roelofs Aq Mt newt [at] pobox.com . </p>
<p> Lk <a rel="nofollow" href="https://pngquant.org">https://pngquant.org</a> pngquant homepage . </p>
<h2>Index</h2>
