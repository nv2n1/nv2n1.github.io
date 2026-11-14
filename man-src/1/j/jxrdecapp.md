---
title: "jxrdecapp(1)"
name: "jxrdecapp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jxrdecapp/"
description: "JxrDecApp – JPEG XR Decoder Utility"
---

<p>JxrDecApp &#8211; JPEG XR Decoder Utility </p>
<h2>Description</h2>
<p>JPEG XR Decoder Utility Copyright 2013 Microsoft Corporation &#8211; All Rights Reserved </p>
<p> ./debian/tmp/usr/bin/JxrDecApp [options]&#8230; </p>
<dl>
<dt><code>-i</code> input.jxr/wdp</p>
<dd>Input JPEG XR/HD Photo file name</dl>
<dl>
<dt><code>-o</code> output.bmp/pnm/tif/jxr</p>
<dd>Output image file name bmp: &lt;=8bpc, BGR pnm: &gt;=8bpc, RGB tif: &gt;=8bpc, RGB jxr: for compressed domain transcode</dl>
<dl>
<dt><code>-c</code> format</p>
<dd>Specifies the uncompressed output format 0: 24bppBGR 1: 1bppBlackWhite 2: 8bppGray 3: 16bppGray 4: 16bppGrayFixedPoint 5: 16bppGrayHalf 7: 32bppGrayFixedPoint 8: 32bppGrayFloat 9: 24bppRGB</p>
<dt>10: 48bppRGB</p>
<dd>11: 48bppRGBFixedPoint 12: 48bppRGBHalf 14: 96bppRGBFixedPoint 15: 128bppRGBFloat 16: 32bppRGBE 17: 32bppCMYK 18: 64bppCMYK 22: 32bppBGRA 23: 64bppRGBA 24: 64bppRGBAFixedPoint 25: 64bppRGBAHalf 27: 128bppRGBAFixedPoint 28: 128bppRGBAFloat 29: 16bppBGR555 30: 16bppBGR565 31: 32bppBGR101010 32: 40bppCMYKA 33: 80bppCMYKA 34: 32bppBGR</dl>
<dl>
<dt><code>-r</code> top left height width</p>
<dd>Specifies the rectangle for region decode</dl>
<dl>
<dt><code>-T</code> m</p>
<dd>Reduced resolution (mipmap) decode 0: Full resolution (default) 1: 1/2 res (down-sampled from full res) 2: 1/4 res (native decode) 3: 1/8 res (down-sampled from 1/4 res) 4: 1/16 res (native decode)</p>
<dd>&gt;4: 1/(2^m) res (down-sampled from 1/16 res)</dl>
<dl>
<dt><code>-O</code> orientation</p>
<dd>0: No transformation (default) 1: Flip vertically 2: Flip horizontally 3: Flip vertically &amp; horizontally 4: Rotate 90 degrees CW 5: Rotate 90 degrees CW &amp; flip vertically 6: Rotate 90 degrees CW &amp; flip horizontally 7: Rotate 90 degrees CW &amp; flip vert &amp; horiz</dl>
<dl>
<dt><code>-s</code> skip subbands</p>
<dd>Used for compressed domain transcoding 0: All subbands included (default) 1: Skip flexbits 2: Skip highpass 3: Skip highpass &amp; lowpass (DC only)</dl>
<dl>
<dt><code>-a</code> alpha decode</p>
<dd>0: Decode without alpha channel 1: Decode only alpha channel 2: Decode image &amp; alpha (default)</dl>
<dl>
<dt><code>-p</code> strength</p>
<dd>Post processing filter strength 0: None (default) 1: Light 2: Medium 3: Strong 4: Very strong</dl>
<dl>
<dt><code>-C</code></p>
<dd>Suppress overlapping boundary macro blocks (Used for compressed domain tile extraction)</dl>
<dl>
<dt><code>-t</code></p>
<dd>Display timing information</dl>
<dl>
<dt><code>-v</code></p>
<dd>Display verbose decoder information</dl>
<p> Eg: ./debian/tmp/usr/bin/JxrDecApp <code>-i</code> input.jxr <code>-o</code> output.bmp <code>-c</code> 0</p>
<h2>Author</h2>
<p>This manual page was written by Mathieu Malaterre &lt;malat [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
