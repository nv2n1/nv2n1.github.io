---
title: "pct2rgb(1)"
name: "pct2rgb"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pct2rgb/"
description: "pct2rgb – pct2rgb.py Convert an 8bit paletted image to 24bit RGB"
---

<h2 class="name">NAME</h2>
<p> pct2rgb &#8211; pct2rgb.py Convert an 8bit paletted image to 24bit RGB </p>
<h2>SYNOPSIS</h2>
<pre><code>
pct2rgb.py[-of format][-b band][-rgba] source_file dest_file
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility will convert a pseudocolor band on the input file into an output RGB file of the desired format. </p>
<dl>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Format to generated (defaults to GeoTIFF).</p>
<dt><code>-b</code> <i>band</i>:</p>
<dd> Band to convert to RGB, defaults to 1.</p>
<dt><code>-rgba:</code></p>
<dd> Generate a RGBA file (instead of a RGB file by default).</p>
<dt><i>source_file</i>:</p>
<dd> The input file.</p>
<dt><i>dest_file</i>:</p>
<dd> The output RGB file that will be created.</dl>
<p> NOTE: pct2rgb.py is a Python script, and will only work if GDAL was built with Python support. </p>
<p> The new &#8216;-expand rgb|rgba&#8217; option of gdal_translate obsoletes that utility.</p>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
