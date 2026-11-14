---
title: "dcm2xml(1)"
name: "dcm2xml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcm2xml/"
description: "dcm2xml – Convert DICOM file and data set to XML"
---

<h2 class="name">NAME</h2>
<p> dcm2xml &#8211; Convert DICOM file and data set to XML </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcm2xml[options] dcmfile - in[xmlfile - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcm2xml</code> utility converts the contents of a DICOM file (file format or raw data set) to XML (Extensible Markup Language). The DTD (Document Type Definition) is described in the file <i>dcm2xml.dtd</i>. </p>
<p> If <code>dcm2xml</code> reads a raw data set (DICOM data without a file format meta-header) it will attempt to guess the transfer syntax by examining the first few bytes of the file. It is not always possible to correctly guess the transfer syntax and it is better to convert a data set to a file format whenever possible (using the <code>dcmconv</code> utility). It is also possible to use the <i>-f</i> and <i>-t[ieb]</i> options to force <code>dcm2xml</code> to read a data set with a particular transfer syntax.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in   DICOM input filename to be converted
xmlfile-out  XML output filename (default: stdout)
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit&#8211; version<br />
            print version information and exit&#8211; arguments<br />
                print expanded command line arguments &#8211;<br />
    q&#8211; quiet<br />
        quiet mode,<br />
    print no warnings and errors &#8211; v&#8211; verbose<br />
                                       verbose mode,<br />
    print processing details &#8211; d&#8211; debug<br />
                                   debug mode,<br />
    print debug information &#8211; ll&#8211; log &#8211; level[l] evel:string<br />
                                                       constant(fatal, error, warn, info, debug, trace)<br />
         use level l for the logger<br />
  -lc  &#8211;log-config  [f]ilename: string<br />
         use config file f for the logger</p>
<h3>input options</h3>
<p>input file format:<br />
  +f   &#8211;read-file<br />
         read file format or data set (default)<br />
  +fo  &#8211;read-file-only<br />
         read file format only<br />
  -f   &#8211;read-dataset<br />
         read data set without file meta information<br />
input transfer syntax:<br />
  -t=  &#8211;read-xfer-auto<br />
         use TS recognition (default)<br />
  -td  &#8211;read-xfer-detect<br />
         ignore TS specified in the file meta header<br />
  -te  &#8211;read-xfer-little<br />
         read with explicit VR little endian TS<br />
  -tb  &#8211;read-xfer-big<br />
         read with explicit VR big endian TS<br />
  -ti  &#8211;read-xfer-implicit<br />
         read with implicit VR little endian TS<br />
long tag values:<br />
  +M   &#8211;load-all<br />
         load very long tag values (e.g. pixel data)<br />
  -M   &#8211;load-short<br />
         do not load very long values (default)<br />
  +R   &#8211;max-read-length  [k]bytes: integer (4..4194302, default: 4)<br />
         set threshold for long values to k kbytes</p>
<h3>processing options</h3>
<p>character set : +Cr&#8211; charset &#8211; require require declaration of extended charset(default) + Ca&#8211; charset &#8211; assume[c] harset : string constant(latin &#8211; 1 to &#8211; 5, cyrillic, arabic, greek, hebrew)<br />
assume charset c if no extended charset declared + Cc&#8211; charset &#8211; check &#8211; all check all data elements with string values(default<br />
                                                                                                                         : only PN, LO, LT, SH, ST and UT)</p>
<h3>output options</h3>
<pre><code>
XML structure : +Xd-- add - dtd - reference add reference to document type definition(DTD) + Xe-- embed - dtd - content embed document type definition into XML document
                +
                Xf-- use - dtd - file[f] ilename : string use specified DTD file(only with + Xe)(default
                                                                                                 : / usr / local / share / dcmtk / dcm2xml.dtd) +
                                                   Xn-- use - xml - namespace add XML namespace declaration to root element DICOM data elements : +Wn-- write - element - name write name of the DICOM data elements(default) - Wn-- no - element - name do not write name of the DICOM data elements
                                                                                                                                                  +
                                                                                                                                                  Wb-- write - binary - data write binary data of OB
    and OW elements(default
                    : off, be careful with-- load - all) +
            Eh-- encode - hex encode binary data as hex numbers(default) + Eb-- encode - base64 encode binary data as Base64(RFC 2045, MIME)
</code></pre>
<h2>NOTES</h2>
<p> The basic structure of the XML output created from a DICOM image file looks like the following: </p>
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
