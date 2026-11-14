---
title: "winicontoppm(1)"
name: "winicontoppm"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winicontoppm/"
description: "winicontoppm – convert a Windows .ico file into 1 or more portable pixmap files"
---

<h2 class="name">NAME</h2>
<p> winicontoppm &#8211; convert a Windows .ico file into 1 or more portable pixmap files </p>
<h2>SYNOPSIS</h2>
<p> <code>winicontoppm</code> [<i>-writeands</i>] [<i>-allicons|-bestqual</i>] [<i>-multippm</i>] [<i>-verbose</i>] [<i>iconfile</i>] [<i>ppmdestfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Microsoft Windows .ico file, converts it to one or more ppms. </p>
<p> A Windows icon contains 1 or more images, at different resolutions and color depths. Each image has an &#8216;and&#8217; mask, which contains transparancy data. </p>
<p> By default, the output goes to Standard Output. If you specify <i>ppmdestfile</i>, output goes into one or more files named as follows. If it&#8217;s just one file (i.e. you specify the <code>-multippm </code> option or don&#8217;t specify <code>-allicons</code>), the file specification is <i>ppmdestfile</i><code>.ppm</code><i></i>. If it&#8217;s multiple files, their file specifications are <i>ppmdestfile</i><code>_1.ppm</code><i></i>, <i>ppmdestfile</i><code>_2.ppm</code><i></i>, etc. </p>
<p> When you specify the <code>-writeands</code> option, the filenames above are modified to include the string <code>xor</code> as in <i>ppmdestfile</i><code>_xor.ppm</code> or <i>ppmdestfile</i><code>_xor_1.ppm</code><i></i>. </p>
<p> <code>winicontoppm</code> can convert images with 1, 4, 8, 24 or 32 bits per pixel (bpp). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-writeands</code></p>
<dd> For each icon written, also write the &#8216;and&#8217; (transparancy) mask as a seperate PBM file. It&#8217;s name is of the form <i>ppmdestfile</i><code>_and.pbm</code> or <i>ppmdestfile</i><code>_and_1.pbm</code><i></i>.</p>
<dt><code>-allicons</code></p>
<dd> Extract all images from the .ico file.</p>
<dt><code>-bestqual</code></p>
<dd> Extract only the best quality (largest, then highest bpp) image from the .ico file.</p>
<dt><code>-multippm</code></p>
<dd> Write all ppms to a single file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtowinicon/">ppmtowinicon</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000, 2003 by Lee Benfield. </p>
<h2>Index</h2>
