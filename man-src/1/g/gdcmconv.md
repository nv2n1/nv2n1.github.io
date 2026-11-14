---
title: "gdcmconv(1)"
name: "gdcmconv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmconv/"
description: "gdcmconv – .TH \"gdcmconv\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmconv &#8211; .TH &quot;gdcmconv&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmconv &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcmconv [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmconv</code> command line program takes as input a DICOM file (file-in) and process it to generate an output DICOM file (file-out). The command line option dictate the type of operation(s) gdcmconv will use to generate the output file.</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
file-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>PARAMETERS</h3>
<pre>
  -i --input      DICOM filename
  -o --output     DICOM filename
</pre>
<h3>OPTIONS</h3>
<pre><code>
  -X --explicit            Change Transfer Syntax to explicit.
  -M --implicit            Change Transfer Syntax to implicit.
  -U --use-dict            Use dict for VR (only public by default).
     --with-private-dict   Use private dict for VR (advanced user only).
  -C --check-meta          Check File Meta Information (advanced user only).
     --root-uid            Root UID.
     --remove-gl           Remove group length (deprecated in DICOM 2008).
     --remove-private-tags Remove private tags.
     --remove-retired      Remove retired tags.
</code></pre>
<h3>image options</h3>
<p>&#8211; l&#8211; apply &#8211; lut Apply LUT(non &#8211; standard, advanced user only).- P&#8211; photometric &#8211; interpretation % s Change Photometric Interpretation(when possible).- w&#8211; raw Decompress image.- d&#8211; deflated Compress using deflated(gzip).- J&#8211; jpeg Compress image in jpeg.- K&#8211; j2k Compress image in j2k.- L&#8211; jpegls Compress image in jpeg &#8211; ls.- R&#8211; rle Compress image in rle(lossless only).- F&#8211; force Force decompression / merging before recompression / splitting.&#8211;compress &#8211; icon Decide whether icon follows main TransferSyntax or remains uncompressed.&#8211;planar &#8211; configuration[01] Change planar configuration.- Y&#8211; lossy Use the lossy(if possible)compressor.- S&#8211; split % d Write 2D image with multiple fragments(using max size)</p>
<h3>JPEG options</h3>
<pre>
  -q --quality %*f           set quality.
</pre>
<h3>JPEG-LS options</h3>
<pre>
  -e --lossy-error %*i       set error.
</pre>
<h3>J2K options</h3>
<p>&#8211; r&#8211; rate % *f set rate.- q&#8211; quality % *f set quality.- t&#8211; tile % d, % d set tile size.- n&#8211; number &#8211; resolution % d set number of resolution.&#8211;irreversible set irreversible.</p>
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
<h3>special options</h3>
<pre>
  -I --ignore-errors   convert even if file is corrupted (advanced users only, see disclaimers).
</pre>
<h3>environment variable</h3>
<pre>
  GDCM_ROOT_UID Root UID
</pre>
<h2>Simple usage</h2>
<p> <code>gdcmconv</code> is a great tool to convert broken DICOM implementation into properly parsable DICOM file. Usage is simply: </p>
<pre>
gdcmconv input.dcm output.dcm
</pre>
<p> or if you prefer being explicit: </p>
<pre>
gdcmconv -i input.dcm -o output.dcm
</pre>
<p> Eventhough gdcmconv can overwrite directly on the same file (input.dcm = output.dcm), it is recommended that user should first convert into a different file to make sure the bug is properly handled by GDCM. </p>
<p> Typical cases where you would want to use gdcmconv in its simple form: </p>
<dl>
<dt>*</p>
<dd> convert non-cp246 conforming file into conforming cp246,</p>
<dt>*</p>
<dd> convert implicit little endian transfer syntax file meta header into proper explicit little endian transfer syntax,</p>
<dt>*</p>
<dd> convert the GE-13 bytes bug,</p>
<dt>*</p>
<dd> convert dual syntax file: implicit/explicit,</p>
<dt>*</p>
<dd> convert Philips dual Little Endian/Big Endian file,</p>
<dt>*</p>
<dd> convert GDCM 1.2.0 broken UN-2-bytes fields,</p>
<dt>*</p>
<dd> &amp;&#8230;</p>
<dt>*</p>
<dd> All other broken files listed in the supported section.</dl>
<p> When no option other is used, only the dataset is inspected. So encapsulated Pixel Data, for instance, is not inspected for well known bugs. </p>
<p> When doing this kind of work, this is usually a good idea to perform some kind of quality control, see gdcmconv Quality Control section (down below).</p>
<h2>Typical usage</h2>
<h3>File Meta Header</h3>
<p> Running </p>
<p> gdcmconv input.dcm output.dcm </p>
<p> Is not enough to recompute file meta header, when input file is buggy. You may want to use: &#8211;check-meta </p>
<pre>
$ gdcmconv --check-meta input.dcm output.dcm
</pre>
<p> See typical cases such as: GE_DLX-8-MONO2-PrivateSyntax.dcm or PICKER-16-MONO2-No_DicomV3_Preamble.dcm from gdcmData.</p>
<h3>Conversion to Explicit Transfer Syntax</h3>
<p> To convert a file that was written using Implicit Transfer Syntax into Explicit Transfer Syntax simply use: </p>
<pre>
$ gdcmconv --explicit uncompressed.dcm compressed.dcm
</pre>
<h3>Compressing to lossless JPEG</h3>
<p> To compress an uncompressed DICOM file to a JPEG Lossless encapsulated format: </p>
<pre>
$ gdcmconv --jpeg uncompressed.dcm compressed.dcm
</pre>
<h3>Compressing to lossy JPEG</h3>
<p> To compress an uncompressed DICOM file to a JPEG Lossy encapsulated format: </p>
<pre>
$ gdcmconv --lossy --jpeg -q 90 uncompressed.dcm compressed.dcm
</pre>
<p> Note: </p>
<p> -q is just one of the many way to specify lossy quality, you need to inspect the other cmd line flag to specify lossyness properties.</p>
<h3>Compressing to lossless JPEG-LS</h3>
<p> To compress an uncompressed DICOM file to a JPEG-LS Lossless encapsulated format: </p>
<pre>
$ gdcmconv --jpegls uncompressed.dcm compressed.dcm
</pre>
<h3>Compressing to lossy JPEG-LS</h3>
<p> To compress an uncompressed DICOM file to a JPEG-LS Lossy encapsulated format: </p>
<pre>
$ gdcmconv --lossy --jpegls -e 2 uncompressed.dcm lossy_compressed.dcm
</pre>
<p> Note: </p>
<p> -e (or &#8211;lossy-error) means that the maximum tolerate error is 2 for each pixel value</p>
<h3>Compressing to lossless J2K</h3>
<p> To compress an uncompressed DICOM file to a JPEG-2000 Lossless encapsulated format: </p>
<pre>
$ gdcmconv --j2k uncompressed.dcm compressed.dcm
</pre>
<h3>Compressing to lossy J2K</h3>
<p> To compress an uncompressed DICOM file to a JPEG-2000 Lossy encapsulated format: </p>
<pre>
$ gdcmconv --lossy -q 55,50,45 --j2k uncompressed.dcm lossy_compressed.dcm
</pre>
<p> Note: </p>
<p> -q is just one of the many way to specify lossy quality, you need to inspect the other cmd line flag to specify lossyness properties.</p>
<h3>Compressing to lossless RLE</h3>
<p> To compress an uncompressed DICOM file to a RLE Lossless encapsulated format: </p>
<pre>
$ gdcmconv --rle uncompressed.dcm compressed.dcm
</pre>
<p> There is no such thing as lossy RLE compression.</p>
<h3>Forcing (re)compression</h3>
<p> Sometime it is necessary to use the &#8211;force option. By default when user specify &#8211;j2k and input file is already in JPEG 2000 encapsulated DICOM format then no operation takes places. By using &#8211;force you make sure that (re)compression operation takes places. </p>
<p> Real life example of why you would use &#8211;force: </p>
<dl>
<dt>*</p>
<dd> When Pixel Data is missing data / is padded with junk</p>
<dt>*</p>
<dd> When you would like to make sure GDCM can handle decompression &amp; recompression cycle</dl>
<h3>Decompressing a Compressed DICOM</h3>
<pre>
$ gdcmconv --raw compressed.dcm uncompressed.dcm
</pre>
<h3>Changing the planar Configuration</h3>
<p> Often RLE files are compressed using a different Planar Comnfiguration (RRR &#8230; GGG&#8230; BBB&#8230;) instead of the usual triplet (RGB &#8230; RGB &#8230; RGB ). So upon decompression the Planar Configuration is 1. This is perfectly legal in DICOM, however this is unconventional, and thus it may be a good idea to also change the planar configuration and set it to the default : </p>
<pre>
$ gdcmconv --raw --planar-configuration 0 compressed.dcm uncompressed1.dcm
</pre>
<p> To reinvert the planar configuration of file &#8216;uncompressed1.dcm&#8217;, simply do: </p>
<pre>
$ gdcmconv --raw --planar-configuration 1 uncompressed1.dcm uncompressed2.dcm
</pre>
<h2>Lossless Conversion</h2>
<p> When talking about lossless conversion, there is an ambiguity that need to be understood. To achieve higher compression ratio, the RGB color space is usually not used, in favor of a YBR one. Changing from one color space to the other is (bit level) not lossless. </p>
<p> For more detail, see what are the true lossless transformations as described: </p>
<p> <a rel="nofollow" href="http://sourceforge.net/apps/mediawiki/gdcm/index.php?title=Color_Space_Transformations">http://sourceforge.net/apps/mediawiki/gdcm/index.php?title=Color_Space_Transformations</a></p>
<h2>Quality Control</h2>
<p> One important part when using gdcmconv it to have a way to quality control the output. </p>
<p> You can use 3rd party tool to check the output of gdcmconv is correct.</p>
<h3>DCMTK / dicom3tools</h3>
<p> Using another DICOM implementation such as the one from DCMTK or dicom3tools can be a good process to check the output of gdcmconv. </p>
<dl>
<dt>*</p>
<dd> For DCMTK use: dcmdump</p>
<dt>*</p>
<dd> For dicom3tools use: dcdump</dl>
<p> For reference, gdcmconv &#8211;raw will act as dcmdjpeg +cn +px, since it never tries to convert color space.</p>
<h3>VIM: vimdiff</h3>
<p> You can setup your favorite editor to compare the output, for instance in vim: </p>
<pre>
autocmd BufReadPre *.dcm set ro
autocmd BufReadPost *.dcm silent %!dcmdump -M +uc '%'
</pre>
<p> then simply do: </p>
<pre>
$ vimdiff input.dcm output.dcm
</pre>
<h3>vbindiff</h3>
<p> On unix you can visually compare binary file using the vbindiff command: </p>
<pre>
$ vbindiff input.dcm output.dcm
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1), <code><a href="/docs/linux/man/1-gdcminfo/">gdcminfo</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
