---
title: "dsr2xml(1)"
name: "dsr2xml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dsr2xml/"
description: "dsr2xml – Convert DICOM SR file and data set to XML"
---

<h2 class="name">NAME</h2>
<p> dsr2xml &#8211; Convert DICOM SR file and data set to XML </p>
<h2>SYNOPSIS</h2>
<pre><code>
dsr2xml[options] dsrfile - in[xmlfile - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dsr2xml</code> utility converts the contents of a DICOM Structured Reporting (SR) document (file format or raw data set) to XML (Extensible Markup Language). The XML Schema <i>dsr2xml.xsd</i> does not yet follow any standard format. However, the <code>dsr2xml</code> application might be enhanced in this aspect in the future (e.g. by supporting HL7/CDA &#8211; Clinical Document Architecture). </p>
<p> If <code>dsr2xml</code> reads a raw data set (DICOM data without a file format meta-header) it will attempt to guess the transfer syntax by examining the first few bytes of the file. It is not always possible to correctly guess the transfer syntax and it is better to convert a data set to a file format whenever possible (using the <code>dcmconv</code> utility). It is also possible to use the <i>-f</i> and <i>-t[ieb]</i> options to force <code>dsr2xml</code> to read a dataset with a particular transfer syntax.</p>
<h2>PARAMETERS</h2>
<pre>
dsrfile-in   DICOM SR input filename to be converted
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
<h3>processing options</h3>
<p>character set : +Cr&#8211; charset &#8211; require require declaration of extended charset(default) + Ca&#8211; charset &#8211; assume[c] harset : string constant(latin &#8211; 1 to &#8211; 5, greek, cyrillic, arabic, hebrew)<br />
assume charset c if no extended charset found + Cc&#8211; charset &#8211; check &#8211; all check all data elements with string values(default<br />
                                                                                                                      : only PN, LO, LT, SH, ST and UT)</p>
<h3>input options</h3>
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS</p>
<h3>output options</h3>
<pre><code>
encoding:
  +Ea  --attr-all
         encode everything as XML attribute
         (shortcut for +Ec, +Er, +Ev and +Et)
  +Ec  --attr-code
         encode code value, coding scheme designator
         and coding scheme version as XML attribute
  +Er  --attr-relationship
         encode relationship type as XML attribute
  +Ev  --attr-value-type
         encode value type as XML attribute
  +Et  --attr-template-id
         encode template id as XML attribute
  +Ee  --template-envelope
         template element encloses content items
         (requires +Wt, implies +Et)
XML structure:
  +Xs  --add-schema-reference
         add reference to XML Schema "dsr2xml.xsd"
         (not with +Ea, +Ec, +Er, +Ev, +Et, +Ee, +We)
  +Xn  --use-xml-namespace
         add XML namespace declaration to root element
writing:
  +We  --write-empty-tags
         write all tags even if their value is empty
  +Wi  --write-item-id
         always write item identifier
  +Wt  --write-template-id
         write template identification information
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>dsr2xml</code> utility supports the following SOP Classes: </p>
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
<p> The <code>dsr2xml</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/dsr2xml.xsd</i> &#8211; XML Schema file</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xml2dsr/">xml2dsr</a></code>(1), <code><a href="/docs/linux/man/1-dcmconv/">dcmconv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
