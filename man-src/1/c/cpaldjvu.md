---
title: "cpaldjvu(1)"
name: "cpaldjvu"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpaldjvu/"
description: "cpaldjvu – DjVuDocument encoder for low-color images."
---

<h2>NAME</h2>
<p> cpaldjvu &#8211; DjVuDocument encoder for low-color images. </p>
<h2>SYNOPSIS</h2>
<p> <code>cpaldjvu [</code><i>options</i><code>] </code><i>inputppmfile</i><i>outputdjvufile</i> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>cpaldjvu</code> is a DjVuDocument encoder for images containing few colors. It performs best on images containing large solid color areas such as screen dumps. Compression ratios on such images can be much higher than those achieved by <font SIZE="-1">GIF</font> or <font SIZE="-1">PNG</font> compression. </p>
<p> This program works by first reducing the number of distinct colors to a small specified value using a simple color quantization algorithm. The dominant color is encoded into the background layer. The other colors are encoded into the foreground layer. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dpi </code><i>n</i></p>
<dd> Specify the resolution information encoded into the output file expressed in dots per inch. The resolution information encoded in DjVu files determine how the decoder scales the image on a particular display. Meaningful resolutions range from 25 to 6000. The default value is 300 dpi.</p>
<dt><code>-colors </code><i>n</i></p>
<dd> Specify a maximum number of distinct colors for the color quantization algorithm. process. The default value is 256. Smaller values can produce much smaller files.</p>
<dt><code>-bgwhite</code></p>
<dd> Cause the background layer to use the lightest quantified color instead of the dominant color.</p>
<dt><code>-verbose</code></p>
<dd> Display informational messages while running. </p>
</dl>
<h2>REMARKS</h2>
<p> The color quantization might introduce severe degradation if the image contains photographic areas with a large number of very similar colors. Color quantization problems might be solved by pre-processing the input file with a different quantization program such as <code>ppmquant</code>. Avoid using the error diffusion dithering algorithm. This algorithm generates random dithering patterns that might be very costly to encode. </p>
<h2>BUGS</h2>
<p> This program should be rewritten as a pre-processor for <code>csepdjvu</code>. </p>
<h2>CREDITS</h2>
<p> This program was initially written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/1-pnmtogif/">pnmtogif</a></code>(1), <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1) </p>
<h2>Index</h2>
