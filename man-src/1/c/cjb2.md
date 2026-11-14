---
title: "cjb2(1)"
name: "cjb2"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjb2/"
description: "cjb2 – Simple DjVuBitonal encoder."
---

<h2>NAME</h2>
<p> cjb2 &#8211; Simple DjVuBitonal encoder. </p>
<h2>SYNOPSIS</h2>
<p> <code>cjb2 [</code><i>options</i><code>] </code><i>inputfile</i><i>outputdjvufile</i> </p>
<h2>DESCRIPTION</h2>
<p> This is a simple encoder for bitonal files. Argument <i>inputfile</i> is the name of a <font SIZE="-1">PBM</font> or bitonal <font SIZE="-1">TIFF</font> file containing a single document image. This program produces a DjVuBitonal file named <i>outputdjvufile</i>. </p>
<p> The default compression process is lossless: decoding the DjVuBitonal file at full resolution will produce an image exactly identical to the input file. Lossy compression is enabled by options <code>-losslevel</code>, <code>-lossy</code>, or <code>-clean</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dpi </code><i>n</i></p>
<dd> Specify the resolution information encoded into the output file expressed in dots per inch. The resolution information encoded in DjVu files determine how the decoder scales the image on a particular display. Meaningful resolutions range from 25 to 1200. The default resolution for <font SIZE="-1">TIFF</font> files is the resolution is the resolution specified by the input file. The default resolution for <font SIZE="-1">PBM</font> files is 300 dpi.</p>
<dt><code>-lossless</code></p>
<dd> Ensure that the encoded image is pixel-per-pixel equal to the initial image. This option is is equivalent to <code>-losslevel 0</code> and is the default.</p>
<dt><code>-clean</code></p>
<dd> Only remove flyspecks from the input image. This option enables a heuristic algorithm that removes very small marks. Such marks are often causes by noise and dust during the scanning process. The threshold mark size is chosen according to the resolution specified with option This option is is equivalent to <code>-losslevel 1</code>.</p>
<dt><code>-lossy</code></p>
<dd> Substitute patterns with small variations. In addition to the flyspeck removal heuristic, this option enables an algorithm that encodes certain characters by simply replicating the shape of a previously encoded character with a similar shape. This option is is equivalent to <code>-losslevel 100</code>.</p>
<dt><code>-losslevel </code><i>x</i></p>
<dd> Specify the aggressiveness of the lossy compression. Its argument ranges from 0 to 200. Higher values generate smaller files with more potential distortions. Loss level 0 corresponds to lossless encoding. Loss level 1 performs image cleaning but does not perform character substitution at all. Loss level 100 is intended to provide a good compromise. Higher loss levels provide marginally better compression at the risk of unacceptable character substitutions.</p>
<dt><code>-verbose</code></p>
<dd> Display informational messages while running. </p>
</dl>
<h2>REMARKS</h2>
<p> Lossless encoding is competitive with that of the Lizardtech commercial encoders. </p>
<p> Lossy encoding has made much progress thanks to Ilya Mezhirov from the minidjvu project. This also means that the lossy encoding performance can change from version to version. When lossy compression yields inadequate results, simply revert to only using option <code>-clean</code> or reduce the parameter of option <code>-losslevel</code>. </p>
<p> Two features are still missing:</p>
<dl>
<dt>*</p>
<dd> Half-tone detection. Collecting small marks belonging to half-tone patterns would improve compression speed.</p>
<dt>*</p>
<dd> Multi-page compression. Matching characters on several pages would improve the compression ratios for multi-page documents. </p>
</dl>
<h2>CREDITS</h2>
<p> This program was initially written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. The pattern matching algorithm for lossy compression was contributed by Ilya Mezhirov &lt;ilya [at] mezhirov.mccme.ru&gt;. TIFF input routines are inspired by the ones contributed by R. Keith Dennis &lt;dennis [at] rkd.math.cornell.edu&gt; and Paul Young. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5). </p>
<h2>Index</h2>
