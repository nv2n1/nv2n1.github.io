---
title: "gdcmimg(1)"
name: "gdcmimg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmimg/"
description: "gdcmimg – .TH \"gdcmimg\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmimg &#8211; .TH &quot;gdcmimg&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmimg &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmimg [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmimg</code> command line tool can be used in two fashions: </p>
<dl>
<dt>*</p>
<dd> 1. Converting a recognized file format into its encapsulated DICOM counterpart,</p>
<dt>*</p>
<dd> 2. Anonymizing a rectangular portion of a DICOM file.</dl>
<h2>PARAMETERS</h2>
<pre>
file-in   input filename
file-out  output filename
</pre>
<h2>OPTIONS</h2>
<h3>PARAMETERS</h3>
<pre>
  -i --input     Input filename
  -o --output    Output filename
</pre>
<h3>OPTIONS</h3>
<pre><code>
--endian % s Endianness(LSB / MSB).- d-- depth % d Depth(8 / 16 / 32).--sign % s Pixel sign(0 / 1).- s-- size % d, % d Size.- C-- sop - class - uid SOP Class UID(name or value).- T-- study - uid Study UID.- S-- series - uid Series UID.--root - uid Root UID.
</code></pre>
<h3>fill options</h3>
<pre>
  -R --region %d,%d    Region.
  -F --fill %d         Fill with pixel value specified.
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
<h3>environment variable</h3>
<pre>
  GDCM_ROOT_UID Root UID
</pre>
<h2>Supported File Format (appropriate file extension)</h2>
<p> gdcmimg will base it&#8217;s conversion process based on the file extension. Follows the list of recognized file extension. When no extension is found, DICOM file is assumed. </p>
<p> input format </p>
<pre>
  * RAW       (raw)
  * RLE       (rle)
  * PNM       (pgm, pnm, ppm)
  * JPEG-LS   (jls)
  * JPEG 2000 (jp2, j2k, j2c, jpc)
  * JPEG      (jpg, jpeg, ljpg, ljpeg)
  * DICOM     ()
</pre>
<p> output format: </p>
<pre>
  * PGM       (pgm, pnm, ppm)
  * DICOM     ()
</pre>
<p> For RAW file format, you should take special care of the &#8211;endian option. For the (old) JPEG file format, both the lossy and lossless format are supported, user should pay attention to the &#8211;sign option. For file format such as RLE or RAW, user is expected to fill in information required to find the dimension and type of input data as there is no other way to find this information. For all other file format, the properties are derived from the file format itself. PNM file are supposed to be big endian.</p>
<h2>Typical usage</h2>
<h3>Remove a rectangular part of the image</h3>
<p> To fill the region [0,100]x[0,100] of a DICOM image simply do: </p>
<pre>
$ gdcmimg --fill 0 --region 0,100,0,100 -i input.dcm -o output_black.dcm
</pre>
<p> Warning: if the Pixel Data is compressed, the image is first decompressed so that pixel can be set to 0, but it is not recompressed.</p>
<h3>Convert RAW to DICOM</h3>
<p> Recognized extension is .raw (case insensitive) </p>
<pre>
$ gdcmimg --size 512,512 --depth 16 -i input.raw -o output.dcm
</pre>
<p> the image will be a Secondary Capture </p>
<p> You can use the <code>dd</code> cmd line to skip any header you would like to discard, for instance, if you would like to skip the first 108 bytes, simply do: </p>
<pre>
$ dd skip=108 bs=1 if=input.raw of=output.raw
</pre>
<h3>Convert PGM/PNM/PPM to DICOM</h3>
<p> Recognized extensions are .pgm, .pnm, .ppm (case insensitive) </p>
<pre>
$ gdcmimg -i input.pgm -o output.dcm
</pre>
<p> the image will be a Secondary Capture</p>
<h3>Convert RLE to DICOM</h3>
<p> Recognized extension is .rle (case insensitive) </p>
<pre>
$ gdcmimg --size 512,512 --depth 16 -i input.rle -o output.dcm
</pre>
<p> the image will be a Secondary Capture</p>
<h3>Convert JPEG to DICOM</h3>
<p> Recognized extensions are .jpg, .jpeg, .ljpg, .ljpeg (case insensitive) </p>
<pre>
$ gdcmimg -i input.ljpeg -o output.dcm
</pre>
<p> the image will be a Secondary Capture</p>
<h3>Convert J2K to DICOM</h3>
<p> Recognized extensions are .j2k, .jp2, .jpc (case insensitive) </p>
<pre>
$ gdcmimg -i input.j2k -o output.dcm
</pre>
<p> the image will be a Secondary Capture</p>
<h3>Specifying a SOP Class UID</h3>
<p> Instead of the default Secondary Capture Image Storage, one may want to specify, say VL Photographic Image Storage. </p>
<pre>
$ gdcmimg --sop-class-uid 1.2.840.10008.5.1.4.1.1.77.1.4 input.jpg output.dcm
</pre>
<h2>Multiple Files</h2>
<p> gdcmimg handle nicely a set of files (for instance jpeg): </p>
<pre>
$ gdcmimg 1.jpg 2.jpg 3.jpg 4.jpg output.dcm
</pre>
<h2>Warning</h2>
<p> There are a couple of issues with gdcmimg implementation: For JFIF file and JP2 file (with header) the header is copied into the Pixel Data element which is illegal for JP2. Use gdcmconv to properly re-encode a JP2/JFIF file into J2K/JPG. </p>
<pre>
$ gdcmimg input.jp2 output_jp2.dcm
$ gdcmconv --j2k --force output_jp2.dcm output_j2k.dcm
</pre>
<p> For RLE file, no check is done for crossing the row boundary. It is recommended to use gdcmconv &#8211;rle to re-encode into a proper RLE file in case of doubt. </p>
<p> Of course if the compression is not ok with your setup, you can always de-encapsulated the DICOM file (typically JPEG) to a non-encapsulated form, using gdcmconv: </p>
<pre>
$ gdcmconv --raw input_jpeg.dcm output_raw.dcm
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1), <code><a href="/docs/linux/man/1-convert/">convert</a></code>(1), <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
