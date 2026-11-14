---
title: "enfuse(1)"
name: "enfuse"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enfuse/"
description: "enfuse – manual page for enfuse 4.1.1"
---

<h2>NAME</h2>
<p> enfuse &#8211; manual page for enfuse 4.1.1</p>
<h2>SYNOPSIS</h2>
<p> <code>enfuse</code> [<i>options</i>] [<i>&#8211;output=IMAGE</i>] <i>INPUT</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Fuse INPUT images into a single IMAGE. </p>
<p> INPUT&#8230; are image filenames or response filenames. Response filenames start with an &quot;@&quot; character.</p>
<h3>Common options:</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
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
<dt><code>-f</code> WIDTHxHEIGHT[+xXOFFSET+yYOFFSET]</p>
<dd> manually set the size and position of the output image; useful for cropped and shifted input TIFF images, such as those produced by Nona</p>
<dt><code>-m</code> CACHESIZE</p>
<dd> set image CACHESIZE in megabytes; default: 1024MB</dl>
<h3>Fusion options:</h3>
<dl>
<dt><code>&#8211;exposure-weight</code>=<i>WEIGHT</i></p>
<dd> weight given to well-exposed pixels (0 &lt;= WEIGHT &lt;= 1); default: 1</p>
<dt><code>&#8211;saturation-weight</code>=<i>WEIGHT</i></p>
<dd> weight given to highly-saturated pixels (0 &lt;= WEIGHT &lt;= 1); default: 0.2</p>
<dt><code>&#8211;contrast-weight</code>=<i>WEIGHT</i></p>
<dd> weight given to pixels in high-contrast neighborhoods (0 &lt;= WEIGHT &lt;= 1); default: 0</p>
<dt><code>&#8211;entropy-weight</code>=<i>WEIGHT</i></p>
<dd> weight given to pixels in high entropy neighborhoods (0 &lt;= WEIGHT &lt;= 1); default: 0</p>
<dt><code>&#8211;exposure-mu</code>=<i>MEAN</i></p>
<dd> center also known as MEAN of Gaussian weighting function (0 &lt;= MEAN &lt;= 1); default: 0.5</p>
<dt><code>&#8211;exposure-sigma</code>=<i>SIGMA</i></p>
<dd> standard deviation of Gaussian weighting function (SIGMA &gt; 0); default: 0.2</p>
<dt><code>&#8211;soft-mask</code></p>
<dd> average over all masks; this is the default</p>
<dt><code>&#8211;hard-mask</code></p>
<dd> force hard blend masks and no averaging on finest scale; this is especially useful for focus stacks with thin and high contrast features, but leads to increased noise</dl>
<h3>Expert options:</h3>
<dl>
<dt><code>&#8211;exposure-cutoff</code>=<i>LOWERCUTOFF[</i>:UPPERCUTOFF[:LOWERPROJECTOR[:UPPERPROJECTOR]]]</p>
<dd> LOWERCUTOFF and UPPERCUTOFF are the values below or above of which pixels are weighted with zero weight in exposure weighting; append &quot;%&quot; signs for relative values; default: 0%:100%:anti-value:value</p>
<dt><code>&#8211;contrast-window-size</code>=<i>SIZE</i></p>
<dd> set window SIZE for local-contrast analysis (SIZE &gt;= 3); default: 5</p>
<dt><code>&#8211;gray-projector</code>=<i>PROJECTOR</i></p>
<dd> apply gray-scale PROJECTOR in exposure or contrast weighing, where PROJECTOR is one of &quot;anti-value&quot;, &quot;average&quot;, &quot;l-star&quot;, &quot;lightness&quot;, &quot;luminance&quot;, &quot;pl-star&quot;, &quot;value&quot;, or &quot;channel-mixer:RED-WEIGHT:GREEN-WEIGHT:BLUE-WEIGHT&quot;; default: &quot;average&quot;</p>
<dt><code>&#8211;contrast-edge-scale</code>=<i>EDGESCALE[</i>:LCESCALE[:LCEFACTOR]]</p>
<dd> set scale on which to look for edges; positive LCESCALE switches on local contrast enhancement by LCEFACTOR (EDGESCALE, LCESCALE, LCEFACTOR &gt;= 0); append &quot;%&quot; to LCESCALE for values relative to EDGESCALE; append &quot;%&quot; to LCEFACTOR for relative value; default: 0:0:0</p>
<dt><code>&#8211;contrast-min-curvature</code>=<i>CURVATURE</i></p>
<dd> minimum CURVATURE for an edge to qualify; append &quot;%&quot; for relative values; default: 0</p>
<dt><code>&#8211;entropy-window-size</code>=<i>SIZE</i></p>
<dd> set window SIZE for local entropy analysis (SIZE &gt;= 3); default: 3</p>
<dt><code>&#8211;entropy-cutoff</code>=<i>LOWERCUTOFF[</i>:UPPERCUTOFF]</p>
<dd> LOWERCUTOFF is the value below of which pixels are treated as black and UPPERCUTOFF is the value above of which pixels are treated as white in the entropy weighting; append &quot;%&quot; signs for relative values; default: 0%:100%</p>
<dt><code>&#8211;save-masks[</code>=<i>SOFT-TEMPLATE[</i>:HARD-TEMPLATE]]</p>
<dd> save weight masks in SOFT-TEMPLATE and HARD-TEMPLATE; conversion chars: &quot;%i&quot;: mask index, &quot;%n&quot;: mask number, &quot;%p&quot;: full path, &quot;%d&quot;: dirname, &quot;%b&quot;: basename, &quot;%f&quot;: filename, &quot;%e&quot;: extension; lowercase characters refer to input images uppercase to the output image default: &quot;softmask-%n.tif&quot;:&quot;hardmask-%n.tif&quot;</p>
<dt><code>&#8211;load-masks[</code>=<i>SOFT-TEMPLATE[</i>:HARD-TEMPLATE]]</p>
<dd> skip calculation of weight maps and use the ones in the files matching the templates instead. These can be either hard or soft masks. For template syntax see &quot;&#8211;save-masks&quot;; default: &quot;softmask-%n.tif&quot;:&quot;hardmask-%n.tif&quot;</dl>
<p> Enfuse accepts arguments to any option in uppercase as well as in lowercase letters.</p>
<h2>AUTHOR</h2>
<p> Written by Andrew Mihal and others. + cleanup_output</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://bugs.launchpad.net/enblend">https://bugs.launchpad.net/enblend</a>&gt;. + cleanup_output</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2012 Andrew Mihal. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>enfuse</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>enfuse</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info enfuse</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
