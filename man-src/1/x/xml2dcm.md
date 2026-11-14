---
title: "xml2dcm(1)"
name: "xml2dcm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2dcm/"
description: "xml2dcm – Convert XML document to DICOM file or data set"
---

<h2 class="name">NAME</h2>
<p> xml2dcm &#8211; Convert XML document to DICOM file or data set </p>
<h2>SYNOPSIS</h2>
<pre>
xml2dcm [options] xmlfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>xml2dcm</code> utility converts the contents of an XML (Extensible Markup Language) document to DICOM file or data set. The XML document is expected to validate against the DTD (Document Type Definition) which is described in file <i>dcm2xml.dtd</i>. An appropriate XML file can be created using the <code>dcm2xml</code> tool (option <i>+Wb</i> recommended to include binary data).</p>
<h2>PARAMETERS</h2>
<pre>
xmlfile-in   XML input filename to be converted (stdin: &quot;-&quot;)
dcmfile-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit-- version
            print version information and exit-- arguments
                print expanded command line arguments -
    q-- quiet
        quiet mode,
    print no warnings and errors - v-- verbose
                                       verbose mode,
    print processing details - d-- debug
                                   debug mode,
    print debug information - ll-- log - level[l] evel:string
                                                       constant(fatal, error, warn, info, debug, trace)
         use level l for the logger
  -lc  --log-config  [f]ilename: string
         use config file f for the logger
</code></pre>
<h3>input options</h3>
<pre>
input file format:
  +f   --read-meta-info
         read meta information if present (default)
  -f   --ignore-meta-info
         ignore file meta information
</pre>
<h3>processing options</h3>
<p>validation : +Vd&#8211; validate &#8211; document validate XML document against DTD + Vn&#8211; check &#8211; namespace check XML namespace in document root unique identifiers : +Ug&#8211; generate &#8211; new &#8211; uids generate new Study / Series / SOP Instance UID &#8211; Uo&#8211; dont &#8211; overwrite &#8211; uids do not overwrite existing UIDs(default) + Uo&#8211; overwrite &#8211; uids overwrite existing UIDs</p>
<h3>output options</h3>
<pre><code>
output file format:
  +F   --write-file
         write file format (default)
  -F   --write-dataset
         write data set without file meta information
  +Fu  --update-meta-info
         update particular file meta information
output transfer syntax:
  +t=  --write-xfer-same
         write with same TS as input (default)
  +te  --write-xfer-little
         write with explicit VR little endian TS
  +tb  --write-xfer-big
         write with explicit VR big endian TS
  +ti  --write-xfer-implicit
         write with implicit VR little endian TS
  +td  --write-xfer-deflated
         write with deflated explicit VR little endian TS
post-1993 value representations:
  +u   --enable-new-vr
         enable support for new VRs (UN/UT) (default)
  -u   --disable-new-vr
         disable support for new VRs, convert to OB
group length encoding:
  +g=  --group-length-recalc
         recalculate group lengths if present (default)
  +g   --group-length-create
         always write with group length elements
  -g   --group-length-remove
         always write without group length elements
length encoding in sequences and items:
  +e   --length-explicit
         write with explicit lengths (default)
  -e   --length-undefined
         write with undefined lengths
data set trailing padding (not with --write-dataset):
  -p=  --padding-retain
         do not change padding (default if not --write-dataset)
  -p   --padding-off
         no padding (implicit if --write-dataset)
  +p   --padding-create  [f]ile-pad [i]tem-pad: integer
         align file on multiple of f bytes and items on
         multiple of i bytes
deflate compression level (only with --write-xfer-deflated):
  +cl  --compression-level  [l]evel: integer (default: 6)
         0=uncompressed, 1=fastest, 9=best compression
</code></pre>
<h2>NOTES</h2>
<p> The basic structure of the XML input expected looks like the following: </p>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;ISO-8859-1&quot;?&gt;
&lt;!DOCTYPE file-format SYSTEM &quot;dcm2xml.dtd&quot;&gt;
&lt;file-format xmlns=&quot;<a rel="nofollow" href="http://dicom.offis.de/dcmtk">http://dicom.offis.de/dcmtk</a>&quot;&gt;
  &lt;meta-header xfer=&quot;1.2.840.10008.1.2.1&quot; name=&quot;LittleEndianExplicit&quot;&gt;
    &lt;element tag=&quot;0002,0000&quot; vr=&quot;UL&quot; vm=&quot;1&quot; len=&quot;4&quot;
             name=&quot;MetaElementGroupLength&quot;&gt;
      166
    &lt;/element&gt;
    ...
    &lt;element tag=&quot;0002,0013&quot; vr=&quot;SH&quot; vm=&quot;1&quot; len=&quot;16&quot;
             name=&quot;ImplementationVersionName&quot;&gt;
      OFFIS_DCMTK_353
    &lt;/element&gt;
  &lt;/meta-header&gt;
  &lt;data-set xfer=&quot;1.2.840.10008.1.2&quot; name=&quot;LittleEndianImplicit&quot;&gt;
    &lt;element tag=&quot;0008,0005&quot; vr=&quot;CS&quot; vm=&quot;1&quot; len=&quot;10&quot;
             name=&quot;SpecificCharacterSet&quot;&gt;
      ISO_IR 100
    &lt;/element&gt;
    ...
    &lt;sequence tag=&quot;0028,3010&quot; vr=&quot;SQ&quot; card=&quot;2&quot; name=&quot;VOILUTSequence&quot;&gt;
      &lt;item card=&quot;3&quot;&gt;
        &lt;element tag=&quot;0028,3002&quot; vr=&quot;xs&quot; vm=&quot;3&quot; len=&quot;6&quot;
                 name=&quot;LUTDescriptor&quot;&gt;
          256
