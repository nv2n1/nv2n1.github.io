---
title: "gdalcompare(1)"
name: "gdalcompare"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdalcompare/"
description: "gdalcompare – gdalcompare.py compare two images"
---

<h2 class="name">NAME</h2>
<p> gdalcompare &#8211; gdalcompare.py compare two images </p>
<h2>SYNOPSIS</h2>
<pre>
gdalcompare.py [-sds] golden_file new_file
</pre>
<h2>DESCRIPTION</h2>
<p> The gdalcompare.py script compares two GDAL supported datasets and reports the differences. In addition to reporting differences to the standard out the script will also return the difference count in it&#8217;s exit value. </p>
<p> Image pixels, and various metadata are checked. There is also a byte by byte comparison done which will count as one difference. So if it is only important that the GDAL visible data is identical a difference count of 1 (the binary difference) should be considered acceptable. </p>
<dl>
<dt><code>-sds</code>:</p>
<dd> If this flag is passed the script will compare all subdatasets that are part of the dataset, otherwise subdatasets are ignored.</dl>
<dl>
<dt><i>golden_file</i>:</p>
<dd> The file that is considered correct, referred to as the golden file.</dl>
<dl>
<dt><i>new_file</i>:</p>
<dd> The file being compared to the golden file, referred to as the new file.</dl>
<p> Note that the gdalcompare.py script can also be called as a library from python code though it is not typically in the python path for including. The primary entry point is gdalcompare.compare() which takes a golden gdal.Dataset and a new gdal.Dataset as arguments and returns a difference count (excluding the binary comparison). The gdalcompare.compare_sds() entry point can be used to compare subdatasets.</p>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com </p>
<h2>Index</h2>
