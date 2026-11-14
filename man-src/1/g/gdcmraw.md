---
title: "gdcmraw(1)"
name: "gdcmraw"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmraw/"
description: "gdcmraw – .TH \"gdcmraw\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmraw &#8211; .TH &quot;gdcmraw&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmraw &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmraw [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmraw</code> tool is mostly used for development purpose. It is used to extract a specific binary field from a DICOM DataSet.</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
file-out  output filename
</pre>
<h2>OPTIONS</h2>
<h3>PARAMETERS</h3>
<pre>
  -i --input     Input filename
  -o --output    Output filename
  -t --tag       Specify tag to extract value from.
</pre>
<h3>OPTIONS</h3>
<pre>
  -S --split-frags  Split fragments into multiple files.
  -p --pattern      Specify trailing file pattern (see split-frags).
  -P --pixel-data   Pixel Data trailing 0.
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
<h3>Copy Attribute Value to file</h3>
<p> This will extract the value at Tag (0025,101b): </p>
<pre>
$ gdcmraw -i GE_MR_0025xx1bProtocolDataBlock.dcm -t 25,101b -o pdb.raw
</pre>
<h3>Extract Pixel Data</h3>
<p> If you do not specify any tag, the Pixel Data element is the default one. So for instance to grab the Pixel Data from an image: </p>
<pre>
$ gdcmraw -i test.acr -o test.raw 
</pre>
<p> You can then for example compute the md5sum of this pixel data (very useful): </p>
<pre>
$ md5sum test.raw
f845c8f283d39a0204c325654493ba53  test.raw
</pre>
<h3>Encapsulated Syntax</h3>
<p> When the Pixel Data is encapsulated, multiple fragments can be used to store a single slice image: </p>
<pre>
$ gdcmdump D_CLUNIE_CT1_J2KR.dcm
</pre>
<pre>
...
(7fe0,0010) OB                                                    # u/l,1 Pixel Data
  (fffe,e000) ?? []                           # 0,1 Item
  (fffe,e000) ?? ff\4ff\51
