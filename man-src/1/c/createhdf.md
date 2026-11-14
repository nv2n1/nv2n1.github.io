---
title: "createhdf(1)"
name: "createhdf"
section: "1"
letter: "c"
url: "/docs/linux/man/1-createhdf/"
description: "createhdf – Create a blank IDE hard disk image in .hdf format"
---

<h2 class="name">NAME</h2>
<p> createhdf &#8211; Create a blank IDE hard disk image in .hdf format </p>
<h2>SYNOPSIS</h2>
<p> <code>createhdf</code> [ -c ] [ -s ] <i>cylinders heads sectors file</i></p>
<h2>DESCRIPTION</h2>
<p> createhdf creates a blank image of an IDE hard disk in .hdf format for use with Sinclair ZX Spectrum emulators.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c</i></p>
<dd> specifies that the .hdf image should be created in `compact&#8217; mode, where only the low byte of every word is stored in the image. This is useful for saving space if the hard disk image is for use with an interface which accesses only the low byte of every word.</p>
<dt><i>-s</i></p>
<dd> specifies that the .hdf image should <code>not</code> be created as a sparse file. Normally, <i>createhdf</i> will attempt to create the hard disk image as a `sparse file&#8217;, where the operating system knows that the file consists mostly of zero bytes and fills those in without using any space in the file. This option disables this. (There&#8217;s nothing `magic&#8217; about this: if data is written to the file, it will take up space just like any other data; it&#8217;s only empty space which is synthesised by the operating system).</p>
<dt><i>-v version</i></p>
<dd> specifies the version of .hdf image to be created. Valid values are `<i>1.0</i>&#8216; for a version 1.0 file and `<i>1.1</i>&#8216; for a version 1.1 file. Defaults to creating version 1.1 files.</p>
<dt><i>cylinders</i></p>
<dd> specifies the number of cylinders in the image.</p>
<dt><i>heads</i></p>
<dd> specifies the number of heads in the image.</p>
<dt><i>sectors</i></p>
<dd> specifies the number of sectors in the image.</p>
<dt><i>file</i></p>
<dd> specifies the file to which the image should be written.</dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-fuse/">fuse</a></i>(1), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) </p>
<p> The .hdf format specification, at<br />
 <i><a rel="nofollow" href="http://www.ramsoft.bbk.org/hdfform.html">http://www.ramsoft.bbk.org/hdfform.html</a></i>. </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<h2>Index</h2>
