---
title: "rgb2pct(1)"
name: "rgb2pct"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rgb2pct/"
description: "rgb2pct – rgb2pct.py Convert a 24bit RGB image to 8bit paletted"
---

<h2 class="name">NAME</h2>
<p> rgb2pct &#8211; rgb2pct.py Convert a 24bit RGB image to 8bit paletted </p>
<h2>SYNOPSIS</h2>
<pre><code>
rgb2pct.py[-n colors | -pct palette_file][-of format] source_file dest_file
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility will compute an optimal pseudo-color table for a given RGB image using a median cut algorithm on a downsampled RGB histogram. Then it converts the image into a pseudo-colored image using the color table. This conversion utilizes Floyd-Steinberg dithering (error diffusion) to maximize output image visual quality. </p>
<dl>
<dt><code>-n</code> <i>colors</i>:</p>
<dd> Select the number of colors in the generated color table. Defaults to 256. Must be between 2 and 256.</p>
<dt><code>-pct</code> <i>palette_file</i>:</p>
<dd> Extract the color table from <i>palette_file</i> instead of computing it. Can be used to have a consistent color table for multiple files. The <i>palette_file</i> must be a raster file in a GDAL supported format with a palette.</p>
<dt><code>-of</code> <i>format</i>:</p>
<dd> Format to generated (defaults to GeoTIFF). Same semantics as the <code>-of</code> flag for gdal_translate. Only output formats supporting pseudocolor tables should be used.</p>
<dt><i>source_file</i>:</p>
<dd> The input RGB file.</p>
<dt><i>dest_file</i>:</p>
<dd> The output pseudo-colored file that will be created.</dl>
<p> NOTE: rgb2pct.py is a Python script, and will only work if GDAL was built with Python support.</p>
<h2>EXAMPLE</h2>
<p> If it is desired to hand create the palette, likely the simplest text format is the GDAL VRT format. In the following example a VRT was created in a text editor with a small 4 color palette with the RGBA colors 238/238/238/255, 237/237/237/255, 236/236/236/255 and 229/229/229/255. </p>
<pre>
% rgb2pct.py -pct palette.vrt rgb.tif pseudo-colored.tif
% more &lt; palette.vrt
&lt;VRTDataset rasterXSize=&quot;226&quot; rasterYSize=&quot;271&quot;&gt;
  &lt;VRTRasterBand dataType=&quot;Byte&quot; band=&quot;1&quot;&gt;
    &lt;ColorInterp&gt;Palette&lt;/ColorInterp&gt;
    &lt;ColorTable&gt;
      &lt;Entry c1=&quot;238&quot; c2=&quot;238&quot; c3=&quot;238&quot; c4=&quot;255&quot;/&gt;
      &lt;Entry c1=&quot;237&quot; c2=&quot;237&quot; c3=&quot;237&quot; c4=&quot;255&quot;/&gt;
      &lt;Entry c1=&quot;236&quot; c2=&quot;236&quot; c3=&quot;236&quot; c4=&quot;255&quot;/&gt;
      &lt;Entry c1=&quot;229&quot; c2=&quot;229&quot; c3=&quot;229&quot; c4=&quot;255&quot;/&gt;
    &lt;/ColorTable&gt;
  &lt;/VRTRasterBand&gt;
&lt;/VRTDataset&gt; 
</pre>
<h2>AUTHOR</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
