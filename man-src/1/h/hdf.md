---
title: "hdf(1)"
name: "hdf"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hdf/"
description: "hdf – Hierarchical Data Format library"
---

<h2>NAME</h2>
<p> hdf &#8211; Hierarchical Data Format library</p>
<h2>SYNOPSIS</h2>
<p> <code> -lmfhdf -ldf -ljpeg -lz [ -lsz ] </p>
<p> {HDFLIBDIR}/libmfhdf.a {HDFLIBDIR}/libdf.a {JPEGLIBDIR}/libjpeg.a </p>
<p> {GZIPLIBDIR}/libz.a [{SZIPLIBDIR}/libsz.a] </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> HDF is a multi-object file format that facilitates the transfer of various types of scientific data between machines and operating systems. See <a rel="nofollow" href="http://www.hdfgroup.org/release4/platforms.html">http://www.hdfgroup.org/release4/platforms.html</a> for a list of platforms currently supported. </p>
<p> HDF allows self-definitions of data content and easy extensibility for future enhancements or compatibility with other standard formats. HDF includes Fortran and C calling interfaces, and utilities for manipulating, viewing, and analyzing data in HDF files. The HDF library contains interfaces for storing and retrieving compressed or uncompressed 8-bit and 24-bit raster images with palettes, n-Dimensional scientific datasets and binary tables. An interface is also included that allows arbitrary grouping of other HDF objects. </p>
<h3>HDF Raster Images</h3>
<p> HDF supports the storing of both 8-bit and 24-bit raster images. Beside storing information about the dimensions and palette of a raster image, HDF supports raster image compression. In previous versions of HDF (DF interfaces,) Run-length encoding and Imcomp compression were both supported. The currently supported compression methods include simple RLE, N-bit, Skipping huffman, Gzip, Szip, and JPEG. Although no longer support Imcomp compression, the library can read images with Imcomp compression. </p>
<h3>HDF Scientific Data Sets</h3>
<p> Scientific Data Sets (SDSs) are useful for storing n-Dimensional gridded data. The actual data in the dataset can be of any of the &quot;standard&quot; number types: 8, 16 and 32bit signed and unsigned integers and 32 and 64bit floating point values. In addition, a certain amount of meta-data can be stored with an SDS including: </p>
<pre><code>
  o The coordinate system to use when interpreting or displaying the data.
  o Scales to be used for each dimension.
  o Labels for each dimension and the dataset as a whole.
  o Units for each dimension and the data.
  o The valid max and min values for the data. 
  o Calibration information for the data.
  o Fill or missing value information. 
  o Ability of having more than one file open at a time.
  o A more general framework for meta-data within the SDS data-model
    (allowing 'name = value' style meta-data.)
  o Support for an "unlimited dimension" in the SDS data-model, making
    it possible to append planes to an array along one dimension.
</code></pre>
<h3>HDF Annotations</h3>
<p> Any object in an HDF file can have annotations associated with it. There are a number of types of annotations: </p>
<pre>
  o Labels are assumed to be short strings giving the &quot;name&quot; of a 
    data object. 
  o Descriptions are longer text segments that are useful for giving 
    more indepth information about a data object 
  o File annotations are assumed to apply to all of the objects in a 
    single file.
</pre>
<h3>HDF Vset Interfaces</h3>
<p> The Vset module provides interfaces to two basic HDF building blocks. Vgroups are generic grouping elements allowing a user to associate related objects within an HDF file. As Vgroups can contain other Vgroups, it is possible to build a hierarchical file. Vdatas are data structures made up of fields and records. Data is organized into &quot;fields&quot; within each Vdata. Each field is identified by a unique &quot;fieldname&quot;. The type of each field may be any of the basic number types that HDF supports. Fields of different types may exist within the same Vdata. </p>
<p> By combining Vdatas in Vgroups it is possible to represent higher level data constructs: mesh data, multi-variate datasets, sparse matrices, finite-element data, spreadsheets, splines, non-Cartesian coordinate data, etc. </p>
<h3>HDF and netCDF</h3>
<p> Starting with HDF version 3.3, netCDF v.2.3.2 of Unidata is supported with the SD multifile interface. SD and netCDF interfaces can read both netCDF files and multi-dimensional arrays (SDS) stored in the HDF4 files transparently. For more information, see Chapter 3, &quot;Scientific Data Sets&quot;, of the HDF User&#8217;s Guide. </p>
<p> To disable netCDF interfaces in the HDF library, configure the library using &#8211;disable-netcdf flag and rebuild it. </p>
<h3>EXAMPLES</h3>
<p> All HDF routines require the header &quot;hdf.h&quot; to be included in the C source file, unless if the SD routines are used, then the header &quot;mfhdf.h&quot; should be included instead. </p>
<p> Fortran programs should use &quot;dffunc.inc&quot; for all interfaces, &quot;mffunc.inc&quot; for the SD interfaces, and &quot;hdf.inc&quot; for non-SD interfaces. </p>
<p> To compile a program that makes HDF calls on most Unix platforms. </p>
<p>(FORTRAN):<br />
{HDFLIBDIR}/bin/h4fc myprog.f&nbsp;<wbr> </p>
<p>(C):<br />
{HDFLIBDIR}/bin/h4cc myprog.c&nbsp;<wbr> </p>
<h2>DOCUMENTATION</h2>
<p> The HDF web site is located at <a rel="nofollow" href="http://www.hdfgroup.org/.">http://www.hdfgroup.org/.</a> </p>
<p> For the vast majority of users, the &quot;HDF User&#8217;s Guide&quot; and &quot;HDF Reference Manual&quot; should be sufficient. </p>
<p> These documents can be viewed or downloaded at </p>
<p> <a rel="nofollow" href="http://www.hdfgroup.org/products/hdf4/.">http://www.hdfgroup.org/products/hdf4/.</a> </p>
<h2>VENDOR</h2>
<p> The HDF Group </p>
<p> 1800 South Oak Street, Suite 203 </p>
<p> Champaign, IL 61820 </p>
<p> USA </p>
<p> <a rel="nofollow" href="http://www.hdfgroup.org">www.hdfgroup.org</a> </p>
<h2>VERSION</h2>
<p> 4.2.11</p>
<h2>LICENSE &amp; SOURCE AVAILABILITY</h2>
<p> Copyright by The HDF Group. </p>
<p> Copyright by the Board of Trustees of the University of Illinois. </p>
<p> All rights reserved. </p>
<p> This file is part of HDF. The full HDF copyright notice, including terms governing use, modification, and redistribution, is contained in the files COPYING and Copyright.html. COPYING can be found at the root of the source code distribution tree; Copyright.html can be found at </p>
<p> <a rel="nofollow" href="http://hdfgroup.org/products/hdf4/doc/Copyright.html.">http://hdfgroup.org/products/hdf4/doc/Copyright.html.</a> If you do not have access to either file, you may request a copy from </p>
<p> help [at] hdfgroup.org. </p>
<h2>CONTACT &amp; HELP</h2>
<p> The HDF Group </p>
<p> Email: help [at] hdfgroup.org </p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/local/lib/hdf/{libmfhdf.a,libdf.a,libjpeg.a,libz.a [,libsz.a]}</code></p>
<dd> hdf libraries</p>
<dt><code>/usr/local/bin</code></p>
<dd> Location of most hdf utilities</p>
<dt><code>/usr/local/include/hdf</code></p>
<dd> Location of include file hdf.h, mfhdf.h, and others </p>
</dl>
<h2>Index</h2>
