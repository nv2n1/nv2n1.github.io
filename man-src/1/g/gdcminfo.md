---
title: "gdcminfo(1)"
name: "gdcminfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcminfo/"
description: "gdcminfo – .TH \"gdcminfo\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcminfo &#8211; .TH &quot;gdcminfo&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcminfo &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcminfo [options] file-in
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcminfo</code> command line program takes as input a DICOM file, or a directory and process it to extract meta- information about the DICOM file processed.</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
</pre>
<h2>OPTIONS</h2>
<h3>OPTIONS</h3>
<pre><code>
- r-- recursive recursive.- d-- check - deflated check if file is proper deflated syntax.--resources - path Resources path.--md5sum Compute md5sum of Pixel Data attribute value.--check - compression check the encapsulated stream compression(lossless / lossy).
</code></pre>
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
<h3>environment variable</h3>
<p> GDCM_RESOURCES_PATH path pointing to resources files (Part3.xml, &#8230;)</p>
<h2>Simple usage</h2>
<h3>gdcmData</h3>
<p> Using data from gdcmData: </p>
<pre>
$ gdcminfo gdcmData/012345.002.050.dcm
</pre>
<pre>
MediaStorage is 1.2.840.10008.5.1.4.1.1.4 [MR Image Storage]
NumberOfDimensions: 2
Dimensions: (256,256)
Origin: (-85,21.6,108.7)
Spacing: (0.664062,0.664062,1.5)
DirectionCosines: (1,0,0,0,0,-1)
Rescale Intercept/Slope: (0,1)
SamplesPerPixel    :1
BitsAllocated      :16
BitsStored         :16
HighBit            :15
PixelRepresentation:1
Orientation Label: CORONAL
</pre>
<h3>Davie Clunie datasets:</h3>
<p> Using data from David Clunie datasets: </p>
<pre>
$ gdcminfo BRTUM001.dcm
</pre>
<pre>
MediaStorage is 1.2.840.10008.5.1.4.1.1.4.1 [Enhanced MR Image Storage]
NumberOfDimensions: 3
Dimensions: (256,256,15)
Origin: (40,-105,105)
Spacing: (0.820312,0.820312,6)
DirectionCosines: (0,1,0,0,0,-1)
Rescale Intercept/Slope: (0,1)
SamplesPerPixel    :1
BitsAllocated      :16
BitsStored         :16
HighBit            :15
PixelRepresentation:1
Orientation Label: SAGITTAL
</pre>
<h3>Checking the md5sum of the Pixel Data</h3>
<p> After compressing a DICOM file (see gdcmconv) using a lossless compression algorithm, it is fairly easy to compare the two files for differences at DICOM attribute level. However one operation is slightly easier to do: how to make sure the compression was actually lossless ? In this case one could use the &#8211;md5sum operation. </p>
<p> Take an uncompressed DICOM image file: </p>
<pre>
$ gdcminfo --md5sum SIEMENS_ImageLocationUN.dcm
</pre>
<p> The tool return: 0621954acd5815e0b4f7b65fcc6506b1 </p>
<p> Now compress this file: </p>
<pre>
$ gdcmconv --jpegls SIEMENS_ImageLocationUN.dcm lossless_compressed.dcm
</pre>
<p> and then check again the md5sum: </p>
<pre>
$ gdcminfo --md5sum lossless_compressed.dcm
</pre>
<p> The tool return: 0621954acd5815e0b4f7b65fcc6506b1</p>
<h3>Checking if Pixel Data is lossless</h3>
<p> In come environment one wish to check whether or not the DICOM file is lossless or not. It is fairly easy to do that in most cases. Only in two occasion this is not clear from the sole DICOM Attribute. When the Transfer Syntax is JPEG 2000 Image Compression (1.2.840.10008.1.2.4.91) and when the Transfer Syntax is JPEG-LS Lossy (Near-Lossless) Image Compression (1.2.840.10008.1.2.4.81). </p>
<p> In this case, the only solution is to open the Pixel Data element, read the specific JPEG header and check whether or not the JPEG transformation was lossless or not: </p>
<pre>
$ gdcminfo --check-compression gdcmData/MAROTECH_CT_JP2Lossy.dcm
</pre>
<p> The tool returns: &#8216;Encapsulated Stream was found to be: lossy&#8217;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1), <code><a href="/docs/linux/man/1-gdcmconv/">gdcmconv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
