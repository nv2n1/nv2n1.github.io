---

title: "dcm2xml(1)"
name: "dcm2xml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcm2xml/"
description: "dcm2xml – Convert DICOM file and data set to XML"
---

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
<p> The &#8216;file-format&#8217; and &#8216;meta-header&#8217; tags are absent for DICOM data sets.  </p>
<h3>Character Encoding</h3>
<p> The XML encoding is determined automatically from the DICOM attribute (0008,0005) &#8216;Specific Character Set&#8217; (if present) using the following mapping: </p>
<pre><code>ASCII &quot;ISO_IR 6&quot; =&gt; &quot;UTF-8&quot;
UTF-8 &quot;ISO_IR 192&quot; =&gt; &quot;UTF-8&quot;
ISO Latin 1 &quot;ISO_IR 100&quot; =&gt; &quot;ISO-8859-1&quot;
ISO Latin 2 &quot;ISO_IR 101&quot; =&gt; &quot;ISO-8859-2&quot;
ISO Latin 3 &quot;ISO_IR 109&quot; =&gt; &quot;ISO-8859-3&quot;
ISO Latin 4 &quot;ISO_IR 110&quot; =&gt; &quot;ISO-8859-4&quot;
ISO Latin 5 &quot;ISO_IR 148&quot; =&gt; &quot;ISO-8859-9&quot;
Cyrillic &quot;ISO_IR 144&quot; =&gt; &quot;ISO-8859-5&quot;
Arabic &quot;ISO_IR 127&quot; =&gt; &quot;ISO-8859-6&quot;
Greek &quot;ISO_IR 126&quot; =&gt; &quot;ISO-8859-7&quot;
Hebrew &quot;ISO_IR 138&quot; =&gt; &quot;ISO-8859-8&quot;
</code></pre>
<p> Multiple character sets are not supported (only the first attribute value is mapped in case of value multiplicity).  </p>
<h3>XML Encoding</h3>
<p> Attributes with very large value fields (e.g. pixel data) are not loaded by default. They can be identified by the additional attribute &#8216;loaded&#8217; with a value of &#8216;no&#8217; (see example above). The command line option <i>--load-all</i> forces to load all value fields including the very long ones. </p>
<p> Furthermore, binary information of OB and OW attributes are not written to the XML output file by default. These elements can be identified by the additional attribute &#8216;binary&#8217; with a value of &#8216;hidden&#8217; (default is &#8216;no&#8217;). The command line option <i>--write-binary-data</i> causes also binary value fields to be printed (attribute value is &#8216;yes&#8217; or &#8216;base64&#8217;). But, be careful when using this option together with <i>--load-all</i> because of the large amounts of pixel data that might be printed to the output. </p>
<p> Multiple values (i.e. where the DICOM value multiplicity is greater than 1) are separated by a backslash &#8216;\&#8216; (except for Base64 encoded data). The &#8216;len&#8217; attribute indicates the number of bytes for the particular value field as stored in the DICOM data set, i.e. it might deviate from the XML encoded value length e.g. because of non-significant padding that has been removed. If this attribute is missing in &#8216;sequence&#8217; or &#8216;item&#8217; start tags, the corresponding DICOM element has been stored with undefined length.  </p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>--verbose</i> also informational messages like processing details are reported. Option <i>--debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>--log-level</i>. In <i>--quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>--log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).  </p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8216; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8216; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).  </p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcm2xml</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8216;) separates entries. On Windows systems, a semicolon (&#8216;;&#8216;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.  </p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/dcm2xml.dtd</i> &#8211; Document Type Definition (DTD) file  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xml2dcm/">xml2dcm</a></code>(1), <code><a href="/docs/linux/man/1-dcmconv/">dcmconv</a></code>(1)  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
