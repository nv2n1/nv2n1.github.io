---
title: "xml2dsr(1)"
name: "xml2dsr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2dsr/"
description: "xml2dsr – Convert DICOM SR file and data set to XML"
---

<h2 class="name">NAME</h2>
<p> xml2dsr &#8211; Convert DICOM SR file and data set to XML </p>
<h2>SYNOPSIS</h2>
<pre>
xml2dsr [options] xmlfile-in dsrfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>xml2dsr</code> utility converts the contents of an XML (Extensible Markup Language) document to DICOM Structured Reporting (SR) format (file format or raw data set). The XML Schema <i>dsr2xml.xsd</i> does not yet follow any standard format. However, the <code>xml2dsr</code> application might be enhanced in this aspect in the future (e. g. by supporting HL7/CDA &#8211; Clinical Document Architecture). </p>
<p> An appropriate XML file can be created using the <code>dsr2xml</code> tool (option <i>+Xn</i> recommended to add XML namespace declaration to the root element).</p>
<h2>PARAMETERS</h2>
<pre>
xmlfile-in   XML input filename to be converted (stdin: &quot;-&quot;)
dsrfile-out  DICOM SR output filename
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
encoding:
  +Ee  --template-envelope
         template element encloses content items
</pre>
<h3>processing options</h3>
<p>validation : +Vs&#8211; validate &#8211; schema validate XML document against Schema(not with&#8211; template &#8211; envelope) + Vn&#8211; check &#8211; namespace check XML namespace in document root unique identifiers : +Ug&#8211; generate &#8211; new &#8211; uids generate new Study / Series / SOP Instance UID<br />
                                                                                                                                                                                             &#8211;<br />
                                                                                                                                                                                             Uo&#8211; dont &#8211; overwrite &#8211; uids do not overwrite existing UIDs(default) + Uo&#8211; overwrite &#8211; uids overwrite existing UIDs</p>
<h3>output options</h3>
<pre><code>
output file format:
  +F   --write-file
         write file format (default)
  -F   --write-dataset
         write data set without file meta information
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
         align file on multiple of f bytes
         and items on multiple of i bytes
deflate compression level (only with --write-xfer-deflated):
  +cl  --compression-level  [l]evel: integer (default: 6)
         0=uncompressed, 1=fastest, 9=best compression
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>xml2dsr</code> utility supports the following SOP Classes: </p>
<pre>
SpectaclePrescriptionReportStorage          1.2.840.10008.5.1.4.1.1.78.6
MacularGridThicknessAndVolumeReportStorage  1.2.840.10008.5.1.4.1.1.79.1
BasicTextSRStorage                          1.2.840.10008.5.1.4.1.1.88.11
EnhancedSRStorage                           1.2.840.10008.5.1.4.1.1.88.22
ComprehensiveSRStorage                      1.2.840.10008.5.1.4.1.1.88.33
ProcedureLogStorage                         1.2.840.10008.5.1.4.1.1.88.40
MammographyCADSRStorage                     1.2.840.10008.5.1.4.1.1.88.50
KeyObjectSelectionDocumentStorage           1.2.840.10008.5.1.4.1.1.88.59
ChestCADSRStorage                           1.2.840.10008.5.1.4.1.1.88.65
XRayRadiationDoseSRStorage                  1.2.840.10008.5.1.4.1.1.88.67
ColonCADSRStorage                           1.2.840.10008.5.1.4.1.1.88.69
ImplantationPlanSRDocumentStorage           1.2.840.10008.5.1.4.1.1.88.70
</pre>
<p> Please note that currently only mandatory and some optional attributes are supported.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>xml2dsr</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/dsr2xml.xsd</i> &#8211; XML Schema file</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dsr2xml/">dsr2xml</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
