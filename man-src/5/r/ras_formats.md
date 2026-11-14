---
title: "ras_formats(5)"
name: "ras_formats"
section: "5"
letter: "r"
url: "/docs/linux/man/5-ras_formats/"
---

ras_formats - Information on raster formats supported by NCAR Graphics and NCAR View.

<h2>Synopsis</h2>

Abekas A60, AVS, Generic Binary, HDF, HPPCL, NRIF, Sun, SGI, and XWD.

<h2>Description</h2>

NCAR Graphics and NCAR View applications are built upon a common library that provides read and write access to raster imagery. The table below summarizes the support that is provided for all the different formats. Note that a format may be writeable but not readable, and that a compressed image may be readable but not writeable. By default, a raster image is written as compressed if possible. For those applications that key upon the filename to determine the raster format, or allow a <i>-ifmt</i> or <i>-ofmt</i>, the <i>extension</i>, as listed below, should be used without the &quot;.&quot; in front (e.g. use &quot;hdf&quot;, not &quot;.hdf&quot;). <table> <tr VALIGN=top><td>Format(extensions)</td><td>Encoding</td><td>Input</td><td>Output</td><td>Compression
</td></tr><tr VALIGN=top><td COLSPAN=5><hr></td></tr><tr VALIGN=top><td>Abekas A60(.a60)</td><td>RGB24</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>None
</td></tr><tr VALIGN=top><td>AVS(.avs)</td><td>RGB24</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>None
</td></tr><tr VALIGN=top><td>HDF(.hdf)</td><td>Indexed-8</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In/Out
</td></tr><tr VALIGN=top><td>HDF(.hdf)</td><td>Direct-24</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In/Out
</td></tr><tr VALIGN=top><td>HPPCL(.hppcl)</td><td>Indexed-8</td><td ALIGN=center>No</td><td ALIGN=center>Yes</td><td ALIGN=center>Out
</td></tr><tr VALIGN=top><td>NRIF(.nrif)</td><td>Bilevel</td><td ALIGN=center>No</td><td ALIGN=center>No</td><td ALIGN=center>None
</td></tr><tr VALIGN=top><td>NRIF(.nrif)</td><td>Indexed-8</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In/Out
</td></tr><tr VALIGN=top><td>NRIF(.nrif)</td><td>Direct-24</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In/Out
</td></tr><tr VALIGN=top><td>Sun(.sun)</td><td>Indexed-8</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In
</td></tr><tr VALIGN=top><td>Sun(.sun)</td><td>Direct-24</td><td ALIGN=center>Yes</td><td ALIGN=center>No</td><td ALIGN=center>In
</td></tr><tr VALIGN=top><td>SGI(.sgi,.rgb)</td><td>Direct-24</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>In
</td></tr><tr VALIGN=top><td>XWD(.xwd)</td><td>Indexed-8</td><td ALIGN=center>Yes</td><td ALIGN=center>Yes</td><td ALIGN=center>None
</td></tr><tr VALIGN=top><td COLSPAN=5><hr></td></tr> </table> 

<h2>Caveats</h2>

Not all formats and encodings that are supported for output are supported for input; the software has separate input and output drivers for format/encoding pair. 

 For all the formats listed below, only 8-bit pixels and 8-bit run-lengths (where applicable) are supported. 

 Experience with HDF's &quot;advanced&quot; compression option indicates that you should use it only if you consider random pixels an advanced-appearing image.

<h2>See Also</h2>

rasview(1NCARG), rasls(1NCARG), rascat(1NCARG), rasgetpal(1NCARG), rassplit(1NCARG) 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
