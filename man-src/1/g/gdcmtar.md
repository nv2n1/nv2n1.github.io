---
title: "gdcmtar(1)"
name: "gdcmtar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmtar/"
description: "gdcmtar – .TH \"gdcmtar\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmtar &#8211; .TH &quot;gdcmtar&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmtar &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmtar [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmtar</code> is a command line tool used to tar/untar multi-frames images (including SIEMENS MOSAIC file)</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
file-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>OPTIONS</h3>
<pre>
  -M --mosaic     Split SIEMENS Mosaic image into multiple frames.
  -p --pattern    Specify trailing file pattern.
</pre>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit -
    v-- version
        print version information and exit -
    V-- verbose
        verbose
        mode(warning + error)
            .-
    W-- warning
    warning mode,
    print warning information
        - E-- error
        error mode,
    print error information
        - D-- debug
        debug mode,
    print debug information
</code></pre>
<h2>Typical usage</h2>
<h3>SIEMENS Mosaic</h3>
<pre>
 $ gdcminfo MR-sonata-3D-as-Tile.dcm
</pre>
<p>MediaStorage is 1.2.840.10008.5.1.4.1.1.4 [MR Image Storage] TransferSyntax is 1.2.840.10008.1.2.1 [Explicit VR Little Endian] NumberOfDimensions : 2 Dimensions : (384, 384, 1)&#8230;</p>
<pre>
$ gdcmtar --mosaic -i MR-sonata-3D-as-Tile.dcm -o mosaic --pattern %03d.dcm 
</pre>
<p> Will output: </p>
<p>&#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72882 2009 &#8211; 08 &#8211; 10 11:14 mosaic000.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72886 2009 &#8211; 08 &#8211; 10 11:14 mosaic001.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72886 2009 &#8211; 08 &#8211; 10 11:14 mosaic002.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72886 2009 &#8211; 08 &#8211; 10 11:14 mosaic003.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72886 2009 &#8211; 08 &#8211; 10 11:14 mosaic004.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72886 2009 &#8211; 08 &#8211; 10 11:14 mosaic005.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic006.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72882 2009 &#8211; 08 &#8211; 10 11:14 mosaic007.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic008.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic009.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic010.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic011.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic012.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic013.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72882 2009 &#8211; 08 &#8211; 10 11:14 mosaic014.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic015.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72882 2009 &#8211; 08 &#8211; 10 11:14 mosaic016.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic017.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic018.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic019.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic020.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic021.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic022.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic023.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic024.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic025.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic026.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic027.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic028.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72884 2009 &#8211; 08 &#8211; 10 11:14 mosaic029.dcm &#8211; rw &#8211; r&#8211; r&#8211; 1 mathieu mathieu 72882 2009 &#8211; 08 &#8211; 10 11:14 mosaic030.dcm</p>
<pre>
 $ gdcminfo mosaic000.dcm
</pre>
<pre><code>
MediaStorage is 1.2.840.10008.5.1.4.1.1.4 [MR Image Storage] TransferSyntax is 1.2.840.10008.1.2.1 [Explicit VR Little Endian] NumberOfDimensions : 2 Dimensions : (64, 64, 1)...
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1), <code><a href="/docs/linux/man/1-gdcminfo/">gdcminfo</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
