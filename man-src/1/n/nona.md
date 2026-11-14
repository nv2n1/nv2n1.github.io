---
title: "nona(1)"
name: "nona"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nona/"
description: "nona – Stitch a panorama image"
---

<h2 class="name">NAME</h2>
<p> nona &#8211; Stitch a panorama image </p>
<h2>SYNOPSIS</h2>
<p> <code>nona</code> [options] <code>-o</code> <i>output</i> <i>project_file</i> (image files)</p>
<h2>DESCRIPTION</h2>
<p> <code>nona</code> uses the transform function from PanoTools, the stitching itself is quite simple, no seam feathering is done. </p>
<p> Only the non-antialiasing interpolators of PanoTools are supported. </p>
<p> The following output formats (<code>n</code> option of PanoTools <code>p</code> script line) are supported:</p>
<dl>
<dt><font SIZE="-1">JPEG, TIFF, PNG :</font> Single image formats without feathered blending</p>
<dd>
<dt>TIFF_m : multiple tiff files</p>
<dd>
<dt>TIFF_multilayer : Multilayer tiff files, readable by The Gimp 2.0</p>
<dd></dl>
<h2>OPTIONS</h2>
<p> General options:</p>
<dl>
<dt><code>-c</code></p>
<dd> Create coordinate images (only TIFF_m output)</p>
<dt><code>-v</code></p>
<dd> Quiet, do not output progress indicators</p>
<dt><code>-t</code> <i>num</i></p>
<dd> Number of threads to be used (default: number of available cores)</dl>
<p> The following options can be used to override settings in the project file:</p>
<dl>
<dt><code>-i</code> <i>num</i></p>
<dd> Remap only image with number num (can be specified multiple times)</p>
<dt><code>-m</code> <i>str</i></p>
<dd> Set output file format (<font SIZE="-1">TIFF,</font> TIFF_m, TIFF_multilayer, <font SIZE="-1">EXR,</font> EXR_m)</p>
<dt><code>-r</code> <i>ldr</i>/<i>hdr</i></p>
<dd> Set output mode:</p>
<dl>
<dt>
<dd>
<dl>
<dt>ldr &#8211; keep original bit depth and response</p>
<dd>
<dt>hdr &#8211; merge to hdr</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-e</code> <i>exposure</i></p>
<dd> Set exposure for ldr mode</p>
<dt><code>-p</code> <i></i><font SIZE="-1"><i>TYPE</i></font><i></i></p>
<dd> Pixel type of the output. Can be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">UINT8 8</font> bit unsigned integer</p>
<dd>
<dt><font SIZE="-1">UINT16 16</font> bit unsigned integer</p>
<dd>
<dt><font SIZE="-1">INT16 16</font> bit signed integer</p>
<dd>
<dt><font SIZE="-1">UINT32 32</font> bit unsigned integer</p>
<dd>
<dt><font SIZE="-1">INT32 32</font> bit signed integer</p>
<dd>
<dt><font SIZE="-1">FLOAT 32</font> bit floating point</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-z</code></p>
<dd> Set compression type. Possible options for tiff output:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">NONE </font> no compression</p>
<dd>
<dt><font SIZE="-1">LZW LZW</font> compression</p>
<dd>
<dt><font SIZE="-1">DEFLATE </font> deflate compression</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
