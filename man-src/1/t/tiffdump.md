---
title: "tiffdump(1)"
name: "tiffdump"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffdump/"
---

<h2>NAME</h2>

 tiffdump - print verbatim information about <font SIZE="-1">TIFF</font> files

<h2>SYNOPSIS</h2>

 <b>tiffdump</b> [ <i>options</i> ] <i>name ...</i>

<h2>DESCRIPTION</h2>

 <i>tiffdump</i> displays directory information from files created according to the Tag Image File Format, Revision 6.0. The header of each <font SIZE="-1">TIFF</font> file (magic number, version, and first directory offset) is displayed, followed by the tag contents of each directory in the file. For each tag, the name, data type, count, and value(s) is displayed. When the symbolic name for a tag or data type is known, the symbolic name is displayed followed by it's numeric (decimal) value. Tag values are displayed enclosed in ``&lt;&gt;'' characters immediately preceded by the value of the count field. For example, an <i>ImageWidth</i> tag might be displayed as ``ImageWidth (256) SHORT (3) 1&lt;800&gt;''. 

 <i>tiffdump</i> is particularly useful for investigating the contents of <font SIZE="-1">TIFF</font> files that <i>libtiff</i> does not understand.

<h2>OPTIONS</h2>

<dl>
<dt><b>-h</b>
<dd> Force numeric data to be printed in hexadecimal rather than the default decimal.
<dt><b>-m</b><i> items</i>
<dd> Change the number of indirect data items that are printed. By default, this will be 24.
<dt><b>-o</b><i> offset</i>
<dd> Dump the contents of the <font SIZE="-1">IFD</font> at the a particular file offset. The file offset may be specified using the usual C-style syntax; i.e. a leading ``0x'' for hexadecimal and a leading ``0'' for octal.</dl>

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-tiffinfo/">tiffinfo</a></b>(1), <b><a HREF="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></b>(3TIFF) 

 Libtiff library home page: <b><a rel="nofollow" HREF="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></b> 

<h2>Index</h2>


