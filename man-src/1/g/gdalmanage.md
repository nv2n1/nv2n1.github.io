---
title: "gdalmanage(1)"
name: "gdalmanage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalmanage/"
description: "gdalmanage – gdalmanage Identify, delete, rename and copy raster data files"
---

<h2 class="name">NAME</h2>
<p> gdalmanage &#8211; gdalmanage Identify, delete, rename and copy raster data files </p>
<h2>SYNOPSIS</h2>
<pre><code>
Usage : gdalmanage mode[-r][-u][-f format] datasetname[newdatasetname]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdalmanage program can perform various operations on raster data files, depending on the chosen <i>mode</i>. This includes identifying raster data types and deleting, renaming or copying the files. </p>
<dl>
<dt><i>mode</i>:</p>
<dd> Mode of operation</p>
<dt><code>identify</code> <i>datasetname</i>:</p>
<dd> List data format of file.</p>
<dt><code>copy</code> <i>datasetname newdatasetname</i>:</p>
<dd> Create a copy of the raster file with a new name.</p>
<dt><code>rename</code> <i>datasetname newdatasetname</i>:</p>
<dd> Change the name of the raster file.</p>
<dt><code>delete</code> <i>datasetname</i>:</p>
<dd> Delete raster file.</dl>
<dl>
<dt><code>-r</code>:</p>
<dd> Recursively scan files/folders for raster files.</p>
<dt><code>-u</code>:</p>
<dd> Report failures if file type is unidentified.</p>
<dt><code>-f</code> <i>format</i>:</p>
<dd> Specify format of raster file if unknown by the application. Uses short data format name (e.g. <i>GTiff</i>).</dl>
<dl>
<dt><i>datasetname</i>:</p>
<dd> Raster file to operate on.</p>
<dt><i>newdatasetname</i>:</p>
<dd> For copy and rename modes, you provide a <i>source</i> filename and a <i>target</i> filename, just like copy and move commands in an operating system.</dl>
<h2>EXAMPLES</h2>
<h3>Using identify mode</h3>
<p> Report the data format of the raster file by using the <i>identify</i> mode and specifying a data file name: </p>
<pre>
$ gdalmanage identify NE1_50M_SR_W.tif
NE1_50M_SR_W.tif: GTiff
</pre>
<p> Recursive mode will scan subfolders and report the data format: </p>
<pre>
$ gdalmanage identify -r 50m_raster/
NE1_50M_SR_W/ne1_50m.jpg: JPEG
NE1_50M_SR_W/ne1_50m.png: PNG
NE1_50M_SR_W/ne1_50m_20pct.tif: GTiff
NE1_50M_SR_W/ne1_50m_band1.tif: GTiff
NE1_50M_SR_W/ne1_50m_print.png: PNG
NE1_50M_SR_W/NE1_50M_SR_W.aux: HFA
NE1_50M_SR_W/NE1_50M_SR_W.tif: GTiff
NE1_50M_SR_W/ne1_50m_sub.tif: GTiff
NE1_50M_SR_W/ne1_50m_sub2.tif: GTiff.fi
 
</pre>
<h3>Using copy mode</h3>
<p> Copy the raster data: </p>
<pre>
$ gdalmanage copy NE1_50M_SR_W.tif ne1_copy.tif
</pre>
<h3>Using rename mode</h3>
<p> Rename raster data: </p>
<pre>
$ gdalmanage rename NE1_50M_SR_W.tif ne1_rename.tif
</pre>
<h3>Using delete mode</h3>
<p> Delete the raster data: </p>
<pre>
gdalmanage delete NE1_50M_SR_W.tif
</pre>
<h2>AUTHORS</h2>
<p> Tyler Mitchell spatialguru [at] shaw.ca </p>
<h2>Index</h2>
