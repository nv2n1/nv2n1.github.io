---
title: "dsrdump(1)"
name: "dsrdump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dsrdump/"
description: "dsrdump – Dump DICOM SR file and data set"
---

<h2 class="name">NAME</h2>
<p> dsrdump &#8211; Dump DICOM SR file and data set </p>
<h2>SYNOPSIS</h2>
<pre>
dsrdump [options] dsrfile-in...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dsrdump</code> utility dumps the contents of a DICOM Structured Reporting (SR) document (file format or raw data set) to stdout in textual form. The output of the document content follows the format proposed in David Clunie&#8217;s book &#8216;DICOM Structured Reporting&#8217; (PixelMed Publishing, 2000). </p>
<p> If <code>dsrdump</code> reads a raw data set (DICOM data without a file format meta-header) it will attempt to guess the transfer syntax by examining the first few bytes of the file. It is not always possible to correctly guess the transfer syntax and it is better to convert a data set to a file format whenever possible (using the <code>dcmconv</code> utility). It is also possible to use the <i>-f</i> and <i>-t[ieb]</i> options to force <code>dsrdump</code> to read a dataset with a particular transfer syntax.</p>
<h2>PARAMETERS</h2>
<pre>
dsrfile-in  DICOM SR input filename to be dumped
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
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS</p>
<h3>parsing options</h3>
<p>additional information : -Ip&#8211; processing &#8211; details show currently processed content item error handling : -Er&#8211; unknown &#8211; relationship accept unknown / missing relationship type &#8211; Ec&#8211; ignore &#8211; constraints ignore relationship content constraints &#8211; Ee&#8211; ignore &#8211; item &#8211; errors do not abort on content item errors, just warn(e.g.missing value type specific attributes) &#8211; Ei&#8211; skip &#8211; invalid &#8211; items skip invalid content items(incl.sub &#8211; tree)</p>
<h3>output options</h3>
<pre><code>
printing:
  +Pf  --print-filename
         print header with filename for each document
  -Ph  --no-document-header
         do not print general document information
  +Pn  --number-nested-items
         print position string in front of each line
  -Pn  --indent-nested-items
         indent nested items by spaces (default)
  +Pl  --print-long-values
         print long item values completely
  -Pl  --shorten-long-values
         print long item values shortened (default)
  +Pu  --print-instance-uid
         print SOP instance UID of referenced objects
  +Pc  --print-all-codes
         print all codes (incl. concept name codes)
  +Pt  --print-template-id
         print template identification information
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>dsrdump</code> utility supports the following SOP Classes: </p>
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
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dsrdump</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmconv/">dcmconv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
