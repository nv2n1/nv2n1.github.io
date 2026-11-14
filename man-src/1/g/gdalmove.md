---
title: "gdalmove(1)"
name: "gdalmove"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalmove/"
description: "gdalmove – gdalmove.py Transform georeferencing of raster file in place"
---

<h2 class="name">NAME</h2>
<p> gdalmove &#8211; gdalmove.py Transform georeferencing of raster file in place </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdalmove.py[-s_srs&lt;srs_defn&gt;] - t_srs&lt;srs_defn&gt;[-et&lt;max_pixel_err&gt;] target_file
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdalmove.py script transforms the bounds of a raster file from one coordinate system to another, and then updates the coordinate system and geotransform of the file. This is done without altering pixel values at all. It is loosely similar to using gdalwarp to transform an image but avoiding the resampling step in order to avoid image damage. It is generally only suitable for transformations that are effectively linear in the area of the file. </p>
<p> If no error threshold value (-et) is provided then the file is not actually updated, but the errors that would be incurred are reported. If -et is provided then the file is only modify if the apparent error being introduced is less than the indicate threshold (in pixels). </p>
<p> Currently the transformed geotransform is computed based on the transformation of the top left, top right, and bottom left corners. A reduced overall error could be produced using a least squares fit of at least all four corner points. </p>
<dl>
<dt><code>-s_srs</code> <i>srs_defn</i>:</p>
<dd></dl>
<p> Override the coordinate system of the file with the indicated coordinate system definition. Optional. If not provided the source coordinate system is read from the source file. </p>
<dl>
<dt><code>-t_srs</code> <i>srs_defn</i>:</p>
<dd></dl>
<p> Defines the target coordinate system. This coordinate system will be written to the file after an update. </p>
<dl>
<dt><code>-et</code> <i>max_pixel_err</i>:</p>
<dd></dl>
<p> The error threshold (in pixels) beyond which the file will not be updated. If not provided no update will be applied to the file, but errors will be reported. </p>
<dl>
<dt><i>target_file</i></p>
<dd> The file to be operated on. To update this must be a file format that supports in place updates of the geotransform and SRS.</dl>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
