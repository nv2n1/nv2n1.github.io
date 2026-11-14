---
title: "raw2hdf(1)"
name: "raw2hdf"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raw2hdf/"
description: "raw2hdf – Create an .hdf hard disk image from a raw data file"
---

<h2 class="name">NAME</h2>
<p> raw2hdf &#8211; Create an .hdf hard disk image from a raw data file </p>
<h2>SYNOPSIS</h2>
<p> <code>raw2hdf</code> <i>rawfile hdffile</i></p>
<h2>DESCRIPTION</h2>
<p> raw2hdf converts a binary dump of a hard disk&#8217;s data into an IDE disk image in .hdf format for use with Sinclair ZX Spectrum emulators.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-v version</i></p>
<dd> specifies the version of .hdf image to be created. Valid values are `<i>1.0</i>&#8216; for a version 1.0 file and `<i>1.1</i>&#8216; for a version 1.1 file. Defaults to creating version 1.1 files.</p>
<dt><i>rawfile</i></p>
<dd> specifies a raw data file (or block device corresponding to an actual disk) to be converted.</p>
<dt><i>hdffile</i></p>
<dd> specifies the .hdf file to create.</dl>
<h2>NOTES</h2>
<p> Since raw2hdf has no knowledge of the geometry of the disk from which the original image was taken (indeed, the input file need not originate from a real IDE disk at all), there is no guarantee that the information contained in the .hdf file header accurately represents the original disk. However, it will attempt to construct a header that is consistent with the size of the image, to produce an .hdf file which is functionally equivalent.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) </p>
<p> The .hdf format specification, at<br />
 <i><a rel="nofollow" href="http://www.ramsoft.bbk.org/hdfform.html">http://www.ramsoft.bbk.org/hdfform.html</a></i>. </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Matthew Westcott (matthew [at] west.co.tt). </p>
<h2>Index</h2>
