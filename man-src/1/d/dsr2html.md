---
title: "dsr2html(1)"
name: "dsr2html"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dsr2html/"
description: "dsr2html – Render DICOM SR file and data set to HTML/XHTML"
---

<h2 class="name">NAME</h2>
<p> dsr2html &#8211; Render DICOM SR file and data set to HTML/XHTML </p>
<h2>SYNOPSIS</h2>
<pre><code>
dsr2html[options] dsrfile - in[htmlfile - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dsr2html</code> utility renders the contents of a DICOM Structured Reporting (SR) document (file format or raw data set) to HTML (Hyper Text Markup Language) version 3.2 or 4.01 as well as to XHTML (Extensible Hyper Text Markup Language) version 1.1. </p>
<p> If <code>dsr2html</code> reads a raw data set (DICOM data without a file format meta-header) it will attempt to guess the transfer syntax by examining the first few bytes of the file. It is not always possible to correctly guess the transfer syntax and it is better to convert a data set to a file format whenever possible (using the <code>dcmconv</code> utility). It is also possible to use the <i>-f</i> and <i>-t[ieb]</i> options to force <code>dsr2html</code> to read a dataset with a particular transfer syntax.</p>
<h2>PARAMETERS</h2>
<pre>
dsrfile-in    DICOM SR input filename to be rendered
htmlfile-out  HTML/XHTML output filename (default: stdout)
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
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS</p>
<h3>parsing options</h3>
<p>additional information : -Ip&#8211; processing &#8211; details show currently processed content item error handling : -Er&#8211; unknown &#8211; relationship accept unknown / missing relationship type &#8211; Ec&#8211; ignore &#8211; constraints ignore relationship content constraints &#8211; Ee&#8211; ignore &#8211; item &#8211; errors do not abort on content item errors, just warn(e.g.missing value type specific attributes) &#8211; Ei&#8211; skip &#8211; invalid &#8211; items skip invalid content items(incl.sub &#8211; tree) character set : +Cr&#8211; charset &#8211; require require declaration of extended charset(default) + Ca&#8211; charset &#8211; assume[c] harset : string constant(latin &#8211; 1 to &#8211; 5, greek, cyrillic, arabic, hebrew)<br />
assume c if undeclared extended charset found</p>
<h3>output options</h3>
<pre><code>
HTML / XHTML compatibility : +H3-- html - 3.2 use only HTML version 3.2 compatible features + H4-- html - 4.0 allow all HTML version 4.01 features(default) + X1-- xhtml - 1.1 comply with XHTML version 1.1 specification
    + Hd-- add - document - type add reference to SGML document type definition cascading style sheet(CSS),
    not with HTML 3.2 : +Sr-- css - reference URL : string add reference to specified CSS to document
                                                    +
                                                    Sf-- css - file[f] ilename : string embed content of specified CSS into document general rendering : +Ri-- expand - inline expand short content items inline(default) - Ri-- never - expand - inline never expand content items inline + Ra-- always - expand - inline always expand content items inline + Rd-- render - full - data render full data of content items
                                                                                                                                                         +
                                                                                                                                                         Rt-- section - title - inline render section titles inline,
    not separately
        document rendering : +Dt-- document
        - type - title use document type as document title(default) + Dp-- patient - info - title use patient information as document title
        - Dh-- no - document - header do not render general document information code rendering : +Ci-- render - inline - codes render codes in continuous text blocks
                                                                                                  +
                                                                                                  Cn-- concept - name - codes render code of concept names
                                                                                                  +
                                                                                                  Cu-- numeric - unit - codes render code of numeric measurement units
                                                                                                  +
                                                                                                  Cv-- code - value - unit use code value as measurement unit(default) + Cm-- code - meaning - unit use code meaning as measurement unit
                                                                                                  +
                                                                                                  Cc-- render - all - codes render all codes(implies + Ci, +Cn and +Cu) + Ct-- code - details - tooltip render code details as a tooltip(implies + Cc)
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>dsr2html</code> utility supports the following SOP Classes: </p>
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
<p> The <code>dsr2html</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/report.css</i> &#8211; Sample Cascading Stylesheet file for HTML <i>&lt;datadir&gt;/reportx.css</i> &#8211; Sample Cascading Stylesheet file for XHTML</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmconv/">dcmconv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
