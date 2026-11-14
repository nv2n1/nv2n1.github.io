---
title: "jxrencapp(1)"
name: "jxrencapp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jxrencapp/"
description: "JxrEncApp – JPEG XR Encoder Utility"
---

<p>JxrEncApp &#8211; JPEG XR Encoder Utility </p>
<h2>Description</h2>
<p>JPEG XR Encoder Utility Copyright 2013 Microsoft Corporation &#8211; All Rights Reserved </p>
<p> ./debian/tmp/usr/bin/JxrEncApp [options]&#8230; </p>
<dl>
<dt><code>-i</code> input.bmp/pnm/tif/hdr</p>
<dd>Input image file name bmp: &lt;=8bpc, BGR pnm: &gt;=8bpc, RGB tif: &gt;=8bpc, RGB hdr: 32bppRGBE only</dl>
<dl>
<dt><code>-o</code> output.jxr</p>
<dd>Output JPEG XR file name</dl>
<dl>
<dt><code>-q</code> quality</p>
<dd>[0.0 &#8211; 1.0) Default = 1.0, lossless</p>
<dt>or quantization</p>
<dd>[1 &#8211; 255] Default = 1, lossless</dl>
<dl>
<dt><code>-c</code> format</p>
<dd>Required to define uncompressed source pixel format 0: 24bppBGR 1: 1bppBlackWhite 2: 8bppGray 3: 16bppGray 4: 16bppGrayFixedPoint 5: 16bppGrayHalf 7: 32bppGrayFixedPoint 8: 32bppGrayFloat 9: 24bppRGB</p>
<dt>10: 48bppRGB</p>
<dd>11: 48bppRGBFixedPoint 12: 48bppRGBHalf 14: 96bppRGBFixedPoint 15: 128bppRGBFloat 16: 32bppRGBE 17: 32bppCMYK 18: 64bppCMYK 22: 32bppBGRA 23: 64bppRGBA 24: 64bppRGBAFixedPoint 25: 64bppRGBAHalf 27: 128bppRGBAFixedPoint 28: 128bppRGBAFloat 29: 16bppBGR555 30: 16bppBGR565 31: 32bppBGR101010 32: 40bppCMYKA 33: 80bppCMYKA 34: 32bppBGR</dl>
<dl>
<dt><code>-d</code> chroma sub-sampling</p>
<dd>0: Y-only 1: YCoCg 4:2:0 2: YCoCg 4:2:2 3: YCoCg 4:4:4 (default)</p>
<dd>(if not set is 4:4:4 for quality &gt;= 0.5 or 4:2:0 for quality &lt; 0.5)</dl>
<dl>
<dt><code>-l</code> overlapping</p>
<dd>0: No overlapping 1: One level overlapping (default) 2: Two level overlapping</p>
<dd>(if not set is One for quality &gt;= 0.5 or Two for quality &lt; 0.5)</dl>
<dl>
<dt><code>-f</code></p>
<dd>Turn off frequency order bit stream (to spatial)</dl>
<dl>
<dt><code>-p</code></p>
<dd>Turn off progressive mode (to sequential)</dl>
<dl>
<dt><code>-t</code></p>
<dd>Display timing information</dl>
<dl>
<dt><code>-v</code></p>
<dd>Display verbose encoder information</dl>
<dl>
<dt><code>-V</code> tile_wd0 [tile_wd1 &#8230; ]</p>
<dd>Macro block columns per tile</dl>
<dl>
<dt><code>-H</code> tile_ht0 [tile_ht1 &#8230; ]</p>
<dd>Macro block rows per tile</dl>
<dl>
<dt><code>-U</code> num_v_tiles num_h_tiles</p>
<dd>Vertical &amp; horizontal tile count for uniform tiling</dl>
<dl>
<dt><code>-b</code> Black/White</p>
<dd>Applies to 1bpp black/white images 0: 0 = black (default) 1: 0 = white</dl>
<dl>
<dt><code>-a</code> alpha channel format</p>
<dd>Required for any pixel format with an alpha channel 2: Planar alpha (default) 3: Interleaved alpha Other: Reserved, do not use</dl>
<dl>
<dt><code>-Q</code> quantization for alpha</p>
<dd>[1 &#8211; 255] Default = 1, lossless</dl>
<dl>
<dt><code>-F</code> trimmed flexbits</p>
<dd>[0 &#8211; 15] 0: no trimming (default) 15: trim all</dl>
<dl>
<dt><code>-s</code> skip subbands</p>
<dd>0: All subbands included (default) 1: Skip flexbits 2: Skip highpass 3: Skip highpass &amp; lowpass (DC only)</dl>
<p> Eg: ./debian/tmp/usr/bin/JxrEncApp <code>-i</code> input.bmp <code>-o</code> output.jxr <code>-q</code> 0.9</p>
<h2>Author</h2>
<p>This manual page was written by Mathieu Malaterre &lt;malat [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
