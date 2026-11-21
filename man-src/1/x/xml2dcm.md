---
title: "xml2dcm(1)"
name: "xml2dcm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2dcm/"
description: "xml2dcm – Convert XML document to DICOM file or data set"
---

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
          256\0\8
        &lt;/element&gt;
        ...
      &lt;/item&gt;
      ...
    &lt;/sequence&gt;
    ...
    &lt;element tag=&quot;7fe0,0010&quot; vr=&quot;OW&quot; vm=&quot;1&quot; len=&quot;262144&quot;
             name=&quot;PixelData&quot; loaded=&quot;no&quot; binary=&quot;hidden&quot;&gt;
    &lt;/element&gt;
  &lt;/data-set&gt;
&lt;/file-format&gt;
</code></pre>
<p> The &#8216;file-format&#8217; and &#8216;meta-header&#8217; tags may be absent for DICOM data sets.  </p>
<h3>Character Encoding</h3>
<p> The DICOM character encoding is determined automatically from the element with tag &#8216;0008,0005&#8217; (Specific Character Set) &#8211; if present. The following character sets are currently supported (requires <code>libxml2</code> to include <code>iconv</code> support): </p>
<pre><code>ASCII &quot;ISO_IR 6&quot; (UTF-8)
UTF-8 &quot;ISO_IR 192&quot; (UTF-8)
ISO Latin 1 &quot;ISO_IR 100&quot; (ISO-8859-1)
ISO Latin 2 &quot;ISO_IR 101&quot; (ISO-8859-2)
ISO Latin 3 &quot;ISO_IR 109&quot; (ISO-8859-3)
ISO Latin 4 &quot;ISO_IR 110&quot; (ISO-8859-4)
ISO Latin 5 &quot;ISO_IR 148&quot; (ISO-8859-9)
Cyrillic &quot;ISO_IR 144&quot; (ISO-8859-5)
Arabic &quot;ISO_IR 127&quot; (ISO-8859-6)
Greek &quot;ISO_IR 126&quot; (ISO-8859-7)
Hebrew &quot;ISO_IR 138&quot; (ISO-8859-8)
</code></pre>
<p> Multiple character sets are not supported (only the first value of the &#8216;Specific Character Set&#8217; is used for the character encoding in case of value multiplicity). </p>
<p> See <code>dcm2xml</code> documentation for more details on the XML structure.  </p>
<h3>Binary Data</h3>
<p> Binary data can be encoded either as a sequence of hex numbers separated by a backslash &#8216;\&#8216; or in Base64 format (binary=&#8216;base64&#8217;). In addition, binary data can also be read from file (binary=&#8216;file&#8217;). In this case, the filename has to be specified as the element value, e.g. </p>
<pre><code>&lt;element tag=&quot;7fe0,0010&quot; vr=&quot;OW&quot; ... binary=&quot;file&quot;&gt;subdir/pixeldata.raw&lt;/element&gt;
</code></pre>
<p> Please note that the contents of the file will be read as is. OW data is expected to be little endian ordered and will be swapped if necessary. No checks will be made to ensure that the amount of data is reasonable in terms of other attributes such as Rows or Columns.  </p>
<h3>Limitations</h3>
<p> Please note that <code>xml2dcm</code> currently does not fully support DICOMDIR files. Specifically, the value of the various offset data elements is not updated automatically by this tool.  </p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>--verbose</i> also informational messages like processing details are reported. Option <i>--debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>--log-level</i>. In <i>--quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>--log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).  </p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8216; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8216; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).  </p>
<h2>ENVIRONMENT</h2>
<p> The <code>xml2dcm</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8216;) separates entries. On Windows systems, a semicolon (&#8216;;&#8216;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.  </p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/dcm2xml.dtd</i> &#8211; Document Type Definition (DTD) file  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcm2xml/">dcm2xml</a></code>(1)  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
