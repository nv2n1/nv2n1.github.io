---
title: "i(1)"
name: "i"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i/"
description: "i.zc – Zero-crossing \"edge detection\" raster function for image processing."
---

<h2>NAME</h2>
<p> <i></i><code>i.zc</code> &#8211; Zero-crossing &quot;edge detection&quot; raster function for image processing.</p>
<h2>KEYWORDS</h2>
<p> imagery</p>
<h2>SYNOPSIS</h2>
<p> <code>i.zc</code><br />
 <code>i.zc help</code><br />
 <code>i.zc input</code>=<i>string</i> <code>output</code>=<i>string</i> [<code>width</code>=<i>integer</i>] [<code>threshold</code>=<i>float</i>] [<code>orientations</code>=<i>integer</i>] [&#8211;<code>overwrite</code>] [&#8211;<code>verbose</code>] [&#8211;<code>quiet</code>]</p>
<h3>Flags:</h3>
<dl>
<dt><code>&#8211;overwrite</code></p>
<dd>
 Allow output files to overwrite existing files</p>
<dt><code>&#8211;verbose</code></p>
<dd>
 Verbose module output</p>
<dt><code>&#8211;quiet</code></p>
<dd>
 Quiet module output</dl>
<h3>Parameters:</h3>
<dl>
<dt><code>input</code>=<i>string</i></p>
<dd>
 Name of input raster map</p>
<dt><code>output</code>=<i>string</i></p>
<dd>
 Zero crossing raster map</p>
<dt><code>width</code>=<i>integer</i></p>
<dd>
 x-y extent of the Gaussian filter<br />
 Default: <i>9</i></p>
<dt><code>threshold</code>=<i>float</i></p>
<dd>
 Sensitivity of Gaussian filter<br />
 Default: <i>10</i></p>
<dt><code>orientations</code>=<i>integer</i></p>
<dd>
 Number of azimuth directions categorized<br />
 Default: <i>1</i></dl>
<h2>DESCRIPTION</h2>
<p> <i>i.zc</i> is an image processing program used for edge detection. The raster map produced shows the location of dqboundaries&quot; on the input map. Boundaries tend to be found in regions of changing cell values and tend to run perpendicular to the direction of the slope. The algorithm used for edge detection is one of the &quot;zero-crossing&quot; algorithms and is discussed briefly below. </p>
<p> This program will be run interactively if the user types <code>i.zc</code> without program arguments on the command line. In this event, the program will prompt the user for parameter values using the standard interface described in the manual entry for <i>parser</i>. Alternately, the user can run the program non-interactively by specifying program parameter values on the command line.</p>
<h2>OPTIONS</h2>
<h3>Parameters:</h3>
<dl>
<dt><code>input_map=</code><i>name</i></p>
<dd>
 Name of input raster map layer.</p>
<dt><code>zc_map=</code><i>name</i></p>
<dd>
 Name of raster map layer to be used for zero-crossing values.</p>
<dt><code>width=</code><i>value</i></p>
<dd>
 This parameter determines the x-y extent of the Gaussian filter. The default value is 9; higher and lower values can be tested by the user. Increasing the width will result in finding &quot;edges&quot; representing more gradual changes in cell values.<br />
 Default: 9</p>
<dt><code>threshold=</code><i>value</i></p>
<dd>
 This parameter determines the &quot;sensitivity&quot; of the Gaussian filter. The default value is 10; higher and lower values can be tested by the user. Increasing the threshold value will result in fewer edges being found.<br />
 Default: 10</p>
<dt><code>orientations=</code><i>value</i></p>
<dd>
 This value is the number of azimuth directions the cells on the output raster map layer are categorized into (similar to the aspect raster map layer produced by the <i>r.slope.aspect</i> program). For example, a value of 16 would result in detected edges being categorized into one of 16 bins depending on the direction of the edge at that point.<br />
 Default: 1</dl>
<p> The current region definition and mask settings are respected when reading the input map.</p>
<h2>NOTES</h2>
<p> The procedure to find the &quot;edges&quot; in the image is as follows: The Fourier transform of the image is taken, The Fourier transform of the Laplacian of a two-dimensional Gaussian function is used to filter the transformed image, The result is run through an inverse Fourier transform, The resulting image is traversed in search of places where the image changes from positive to negative or from negative to positive, Each cell in the map where the value crosses zero (with a change in value greater than the threshold value) is marked as an edge and an orientation is assigned to it. The resulting raster map layer is output. </p>
<h2>SEE ALSO</h2>
<p> <i>i.fft</i>, <i>i.ifft</i>, <i>r.mapcalc</i>, <i>r.mfilter</i>, <i>r.slope.aspect</i></p>
<h2>AUTHOR</h2>
<p> David Satnik, GIS Laboratory, Central Washington University </p>
<p> <i>Last changed: $Date: 2003-04-17 16:51:33 +0200 (Thu, 17 Apr 2003) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
