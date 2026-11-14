---
title: "gdcmviewer(1)"
name: "gdcmviewer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmviewer/"
description: "gdcmviewer – .TH \"gdcmviewer\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmviewer &#8211; .TH &quot;gdcmviewer&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmviewer &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmviewer [options] file-in
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmviewer</code> is a simple tool that show how to use <code>vtkGDCMImageReader</code>. The class that use gdcm to make a layer to VTK. <code>gdcmviewer</code> is basically only just a wrapper around GDCM. </p>
<p> This tool is meant for testing integration of GDCM in VTK. You should see it as a demo tool. It does compile with VTK ranging from 4.2 to 5.6, but only with VTK 5.2 (or above) can only play with the widgets (as described below).</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
</pre>
<h2>OPTIONS</h2>
<h3>OPTIONS</h3>
<pre>
     --force-rescale    force rescale (advanced users)
     --force-spacing    force spacing (advanced users)
  -r --recursive        Recusively descend directory
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
<h2>Simple usage</h2>
<p> For now gdcmviewer should be started from a command line prompt. The next argument should be the name of the DICOM file you wish to read. For instance: </p>
<pre>
 $ gdcmviewer -V 012345.002.050.dcm
</pre>
<p> gdcmviewer will try to read your file, and the print the vtk information associated with this file. Basically what kind of image you are looking at. </p>
<dl>
<dt>*</p>
<dd> ScalarType is the DICOM Real World Value type</p>
<dt>*</p>
<dd> Dimensions is the dimension of the image</p>
<dt>*</p>
<dd> Spacing is the spacing of the image</p>
<dt>*</p>
<dd> NumberOfScalarComponents should be 1 for grayscale &amp; PALETTE COLOR and 3 for RGB, YBR data.</dl>
<h2>Wiki Link</h2>
<p> The wiki page, will color pictures can be found at: <a rel="nofollow" href="http://sourceforge.net/apps/mediawiki/gdcm/index.php?title=Gdcmviewer">http://sourceforge.net/apps/mediawiki/gdcm/index.php?title=Gdcmviewer</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcm2vtkraw/">gdcm2vtkraw</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
