---
title: "gdal-config(1)"
name: "gdal-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdal-config/"
description: "gdal-config – gdal-config determines various information about a GDAL installation"
---

<h2 class="name">NAME</h2>
<p> gdal-config &#8211; gdal-config determines various information about a GDAL installation </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdal - config[OPTIONS] Options : [--prefix[= DIR]]
                                     [--libs]
                                     [--cflags]
                                     [--version]
                                     [--ogr - enabled]
                                     [--formats]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This utility script (available on Unix systems) can be used to determine various information about a GDAL installation. It is normally just used by configure scripts for applications using GDAL but can be queried by an end user. </p>
<dl>
<dt><code>&#8211;prefix</code>:</dt>
<dd> the top level directory for the GDAL installation.</dd>
<dt><code>&#8211;libs</code>:</dt>
<dd> The libraries and link directives required to use GDAL.</dd>
<dt><code>&#8211;cflags</code>:</dt>
<dd> The include and macro definition required to compiled modules using GDAL.</dd>
<dt><code>&#8211;version</code>:</dt>
<dd> Reports the GDAL version.</dd>
<dt><code>&#8211;ogr-enabled</code>:</dt>
<dd> Reports &#8216;yes&#8217; or &#8216;no&#8217; to standard output depending on whether OGR is built into GDAL.</dd>
<dt><code>&#8211;formats</code>:</dt>
<dd> Reports which formats are configured into GDAL to stdout.</dd></dl>
