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
<p> <code>enblend</code> [<i>options</i>] [<i>&#8211;output=IMAGE</i>] <i>INPUT</i>&#8230;</p>
<p> Blend INPUT images into a single IMAGE. </p>
<p> INPUT&#8230; are image filenames or response filenames. Response filenames start with an &quot;@&quot; character.</p>
<h3>Common options:</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-a</code></dt>
<dd> pre-assemble non-overlapping images</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print this help message and exit</dd>
<dt><code>-l</code>, <code>&#8211;levels</code>=<i>LEVELS</i></dt>
<dd> limit number of blending LEVELS to use (1 to 29); negative number of LEVELS decreases maximum; &quot;auto&quot; restores the default automatic maximization</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> write output to FILE; default: &quot;a.tif&quot;</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>LEVEL</i>]</dt>
<dd> verbosely report progress; repeat to increase verbosity or directly set to LEVEL</dd>
<dt><code>-w</code>, <code>&#8211;wrap</code>[=<i>MODE</i>]</dt>
<dd> wrap around image boundary, where MODE is &quot;none&quot;, &quot;horizontal&quot;, &quot;vertical&quot;, or &quot;both&quot;; default: none; without argument the option selects horizontal wrapping</dd>
<dt><code>-x</code></dt>
<dd> checkpoint partial results</dd>
<dt><code>&#8211;compression</code>=<i>COMPRESSION</i></dt>
<dd> set compression of output image to COMPRESSION, where COMPRESSION is: &quot;deflate&quot;, &quot;jpeg&quot;, &quot;lzw&quot;, &quot;none&quot;, &quot;packbits&quot;, for TIFF files and 0 to 100, or &quot;jpeg&quot;, &quot;jpeg-arith&quot; for JPEG files, where &quot;jpeg&quot; and &quot;jpeg-arith&quot; accept a compression level</dd>
<dt><code>&#8211;layer-selector</code>=<i>ALGORITHM</i></dt>
<dd> set the layer selector ALGORITHM; default: &quot;all-layers&quot;; available algorithms are: &quot;all-layers&quot;: select all layers in all images; &quot;first-layer&quot;: select only first layer in each multi-layer image; &quot;largest-layer&quot;: select largest layer in each multi-layer image; &quot;no-layer&quot;: do not select any layer from any image;</dd>
<dt><code>&#8211;parameter</code>=<i>KEY1[=VALUE1][</i>:KEY2[=VALUE2][:&#8230;]]</dt>
<dd> set one or more KEY-VALUE pairs</dd></dl>
<h3>Extended options:</h3>
<dl>
<dt><code>-b</code> BLOCKSIZE</dt>
<dd> image cache BLOCKSIZE in kilobytes; default: 2048KB</dd>
<dt><code>-c</code>, <code>&#8211;ciecam</code></dt>
<dd> use CIECAM02 to blend colors; disable with &quot;&#8211;no-ciecam&quot;</dd>
<dt><code>&#8211;fallback-profile</code>=<i>PROFILE-FILE</i></dt>
<dd> use the ICC profile from PROFILE-FILE instead of sRGB</dd>
<dt><code>-d</code>, <code>&#8211;depth</code>=<i>DEPTH</i></dt>
<dd> set the number of bits per channel of the output image, where DEPTH is &quot;8&quot;, &quot;16&quot;, &quot;32&quot;, &quot;r32&quot;, or &quot;r64&quot;</dd>
<dt><code>-g</code></dt>
<dd> associated-alpha hack for Gimp (before version 2) and Cinepaint</dd>
<dt><code>&#8211;gpu</code></dt>
<dd> use graphics card to accelerate seam-line optimization</dd>
<dt><code>-f</code> WIDTHxHEIGHT[+xXOFFSET+yYOFFSET]</dt>
<dd> manually set the size and position of the output image; useful for cropped and shifted input TIFF images, such as those produced by Nona</dd>
<dt><code>-m</code> CACHESIZE</dt>
<dd> set image CACHESIZE in megabytes; default: 1024MB</dd></dl>
<h3>Mask generation options:</h3>
<dl>
<dt><code>&#8211;primary-seam-generator</code>=<i>ALGORITHM</i></dt>
<dd> use main seam finder ALGORITHM, where ALGORITHM is &quot;nearest-feature-transform&quot; or &quot;graph-cut&quot;; default: &quot;nearest-feature-transform&quot;</dd>
<dt><code>&#8211;image-difference</code>=<i>ALGORITHM[</i>:LUMINANCE-WEIGHT[:CHROMINANCE-WEIGHT]]</dt>
<dd> use ALGORITHM for calculation of the difference image, where ALGORITHM is &quot;max-hue-luminance&quot; or &quot;delta-e&quot;; LUMINANCE-WEIGHT and CHROMINANCE-WEIGHT define the weights of lightness and color; default: delta-e:1: 1</dd>
<dt><code>&#8211;coarse-mask</code>[=<i>FACTOR</i>] shrink overlap regions by FACTOR to speedup mask</dt>
<dd> generation; this is the default; if omitted FACTOR defaults to 8</dd>
<dt><code>&#8211;fine-mask</code></dt>
<dd> generate mask at full image resolution; use e.g. if overlap regions are very narrow</dd>
<dt><code>&#8211;smooth-difference</code>=<i>RADIUS</i></dt>
<dd> (deprecated) smooth the difference image prior to seam-line optimization with a Gaussian blur of RADIUS; default: 0 pixels</dd>
<dt><code>&#8211;optimize</code></dt>
<dd> turn on mask optimization; this is the default</dd>
<dt><code>&#8211;no-optimize</code></dt>
<dd> turn off mask optimization</dd>
<dt><code>&#8211;optimizer-weights</code>=<i>DISTANCE-WEIGHT[</i>:MISMATCH-WEIGHT]</dt>
<dd> set the optimizer&#8217;s weigths for distance and mismatch; default: 8:1</dd>
<dt><code>&#8211;mask-vectorize</code>=<i>LENGTH</i></dt>
<dd> set LENGTH of single seam segment; append &quot;%&quot; for relative value; defaults: 4 for coarse masks and 20 for fine masks</dd>
<dt><code>&#8211;anneal</code>=<i>TAU[</i>:DELTAE-MAX[:DELTAE-MIN[:K-MAX]]]</dt>
<dd> set annealing parameters of optimizer strategy 1; defaults: 0.75:7000:5:32</dd>
<dt><code>&#8211;dijkstra</code>=<i>RADIUS</i></dt>
<dd> set search RADIUS of optimizer strategy 2; default: 25 pixels</dd>
<dt><code>&#8211;save-masks</code>[=<i>TEMPLATE</i>]</dt>
<dd> save generated masks in TEMPLATE; default: &quot;mask-%n.tif&quot;; conversion chars: &quot;%i&quot;: mask index, &quot;%n&quot;: mask number, &quot;%p&quot;: full path, &quot;%d&quot;: dirname, &quot;%b&quot;: basename, &quot;%f&quot;: filename, &quot;%e&quot;: extension; lowercase characters refer to input images uppercase to the output image</dd>
<dt><code>&#8211;load-masks</code>[=<i>TEMPLATE</i>]</dt>
<dd> use existing masks in TEMPLATE instead of generating them; same template characters as &quot;&#8211;save-masks&quot;; default: &quot;mask-%n.tif&quot;</dd>
<dt><code>&#8211;visualize</code>[=<i>TEMPLATE</i>] save results of optimizer in TEMPLATE; same template</dt>
<dd> characters as &quot;&#8211;save-masks&quot;; default: &quot;vis-%n.tif&quot;</dd></dl>
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
</dt><dd> <code>info enblend</code></dd></dl>
<p> should give you access to the complete manual. </p>
