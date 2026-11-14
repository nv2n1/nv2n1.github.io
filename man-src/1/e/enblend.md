---
title: "enblend(1)"
name: "enblend"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enblend/"
description: "enblend – manual page for enblend 4.1.1"
---

<h2>NAME</h2>
<p> enblend &#8211; manual page for enblend 4.1.1</p>
<h2>SYNOPSIS</h2>
<p> <code>enblend</code> [<i>options</i>] [<i>&#8211;output=IMAGE</i>] <i>INPUT</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Blend INPUT images into a single IMAGE. </p>
<p> INPUT&#8230; are image filenames or response filenames. Response filenames start with an &quot;@&quot; character.</p>
<h3>Common options:</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-a</code></p>
<dd> pre-assemble non-overlapping images</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print this help message and exit</p>
<dt><code>-l</code>, <code>&#8211;levels</code>=<i>LEVELS</i></p>
<dd> limit number of blending LEVELS to use (1 to 29); negative number of LEVELS decreases maximum; &quot;auto&quot; restores the default automatic maximization</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> write output to FILE; default: &quot;a.tif&quot;</p>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>LEVEL</i>]</p>
<dd> verbosely report progress; repeat to increase verbosity or directly set to LEVEL</p>
<dt><code>-w</code>, <code>&#8211;wrap</code>[=<i>MODE</i>]</p>
<dd> wrap around image boundary, where MODE is &quot;none&quot;, &quot;horizontal&quot;, &quot;vertical&quot;, or &quot;both&quot;; default: none; without argument the option selects horizontal wrapping</p>
<dt><code>-x</code></p>
<dd> checkpoint partial results</p>
<dt><code>&#8211;compression</code>=<i>COMPRESSION</i></p>
<dd> set compression of output image to COMPRESSION, where COMPRESSION is: &quot;deflate&quot;, &quot;jpeg&quot;, &quot;lzw&quot;, &quot;none&quot;, &quot;packbits&quot;, for TIFF files and 0 to 100, or &quot;jpeg&quot;, &quot;jpeg-arith&quot; for JPEG files, where &quot;jpeg&quot; and &quot;jpeg-arith&quot; accept a compression level</p>
<dt><code>&#8211;layer-selector</code>=<i>ALGORITHM</i></p>
<dd> set the layer selector ALGORITHM; default: &quot;all-layers&quot;; available algorithms are: &quot;all-layers&quot;: select all layers in all images; &quot;first-layer&quot;: select only first layer in each multi-layer image; &quot;largest-layer&quot;: select largest layer in each multi-layer image; &quot;no-layer&quot;: do not select any layer from any image;</p>
<dt><code>&#8211;parameter</code>=<i>KEY1[=VALUE1][</i>:KEY2[=VALUE2][:&#8230;]]</p>
<dd> set one or more KEY-VALUE pairs</dl>
<h3>Extended options:</h3>
<dl>
<dt><code>-b</code> BLOCKSIZE</p>
<dd> image cache BLOCKSIZE in kilobytes; default: 2048KB</p>
<dt><code>-c</code>, <code>&#8211;ciecam</code></p>
<dd> use CIECAM02 to blend colors; disable with &quot;&#8211;no-ciecam&quot;</p>
<dt><code>&#8211;fallback-profile</code>=<i>PROFILE-FILE</i></p>
<dd> use the ICC profile from PROFILE-FILE instead of sRGB</p>
<dt><code>-d</code>, <code>&#8211;depth</code>=<i>DEPTH</i></p>
<dd> set the number of bits per channel of the output image, where DEPTH is &quot;8&quot;, &quot;16&quot;, &quot;32&quot;, &quot;r32&quot;, or &quot;r64&quot;</p>
<dt><code>-g</code></p>
<dd> associated-alpha hack for Gimp (before version 2) and Cinepaint</p>
<dt><code>&#8211;gpu</code></p>
<dd> use graphics card to accelerate seam-line optimization</p>
<dt><code>-f</code> WIDTHxHEIGHT[+xXOFFSET+yYOFFSET]</p>
<dd> manually set the size and position of the output image; useful for cropped and shifted input TIFF images, such as those produced by Nona</p>
<dt><code>-m</code> CACHESIZE</p>
<dd> set image CACHESIZE in megabytes; default: 1024MB</dl>
<h3>Mask generation options:</h3>
<dl>
<dt><code>&#8211;primary-seam-generator</code>=<i>ALGORITHM</i></p>
<dd> use main seam finder ALGORITHM, where ALGORITHM is &quot;nearest-feature-transform&quot; or &quot;graph-cut&quot;; default: &quot;nearest-feature-transform&quot;</p>
<dt><code>&#8211;image-difference</code>=<i>ALGORITHM[</i>:LUMINANCE-WEIGHT[:CHROMINANCE-WEIGHT]]</p>
<dd> use ALGORITHM for calculation of the difference image, where ALGORITHM is &quot;max-hue-luminance&quot; or &quot;delta-e&quot;; LUMINANCE-WEIGHT and CHROMINANCE-WEIGHT define the weights of lightness and color; default: delta-e:1: 1</p>
<dt><code>&#8211;coarse-mask</code>[=<i>FACTOR</i>] shrink overlap regions by FACTOR to speedup mask</p>
<dd> generation; this is the default; if omitted FACTOR defaults to 8</p>
<dt><code>&#8211;fine-mask</code></p>
<dd> generate mask at full image resolution; use e.g. if overlap regions are very narrow</p>
<dt><code>&#8211;smooth-difference</code>=<i>RADIUS</i></p>
<dd> (deprecated) smooth the difference image prior to seam-line optimization with a Gaussian blur of RADIUS; default: 0 pixels</p>
<dt><code>&#8211;optimize</code></p>
<dd> turn on mask optimization; this is the default</p>
<dt><code>&#8211;no-optimize</code></p>
<dd> turn off mask optimization</p>
<dt><code>&#8211;optimizer-weights</code>=<i>DISTANCE-WEIGHT[</i>:MISMATCH-WEIGHT]</p>
<dd> set the optimizer&#8217;s weigths for distance and mismatch; default: 8:1</p>
<dt><code>&#8211;mask-vectorize</code>=<i>LENGTH</i></p>
<dd> set LENGTH of single seam segment; append &quot;%&quot; for relative value; defaults: 4 for coarse masks and 20 for fine masks</p>
<dt><code>&#8211;anneal</code>=<i>TAU[</i>:DELTAE-MAX[:DELTAE-MIN[:K-MAX]]]</p>
<dd> set annealing parameters of optimizer strategy 1; defaults: 0.75:7000:5:32</p>
<dt><code>&#8211;dijkstra</code>=<i>RADIUS</i></p>
<dd> set search RADIUS of optimizer strategy 2; default: 25 pixels</p>
<dt><code>&#8211;save-masks</code>[=<i>TEMPLATE</i>]</p>
<dd> save generated masks in TEMPLATE; default: &quot;mask-%n.tif&quot;; conversion chars: &quot;%i&quot;: mask index, &quot;%n&quot;: mask number, &quot;%p&quot;: full path, &quot;%d&quot;: dirname, &quot;%b&quot;: basename, &quot;%f&quot;: filename, &quot;%e&quot;: extension; lowercase characters refer to input images uppercase to the output image</p>
<dt><code>&#8211;load-masks</code>[=<i>TEMPLATE</i>]</p>
<dd> use existing masks in TEMPLATE instead of generating them; same template characters as &quot;&#8211;save-masks&quot;; default: &quot;mask-%n.tif&quot;</p>
<dt><code>&#8211;visualize</code>[=<i>TEMPLATE</i>] save results of optimizer in TEMPLATE; same template</p>
<dd> characters as &quot;&#8211;save-masks&quot;; default: &quot;vis-%n.tif&quot;</dl>
<p> Enblend accepts arguments to any option in uppercase as well as in lowercase letters.</p>
<h2>AUTHOR</h2>
<p> Written by Andrew Mihal and others. + cleanup_output</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://bugs.launchpad.net/enblend">https://bugs.launchpad.net/enblend</a>&gt;. + cleanup_output</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2012 Andrew Mihal. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>enblend</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>enblend</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info enblend</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
