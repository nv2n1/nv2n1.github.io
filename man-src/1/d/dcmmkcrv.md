---
title: "dcmmkcrv(1)"
name: "dcmmkcrv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmmkcrv/"
description: "dcmmkcrv – Add 2D curve data to image"
---

<h2 class="name">NAME</h2>
<p> dcmmkcrv &#8211; Add 2D curve data to image </p>
<h2>SYNOPSIS</h2>
<pre>
dcmmkcrv [options] dcmfile-in curvedata-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmmkcrv</code> utility allows to create DICOM images containing curve data. Since curve data is hardly used by vendors today, this is intended as a means to test implementations that can read curve data. The utility reads an existing DICOM image and a text file containing the curve data in textual form. A DICOM curve data repeating group is created according to the options specified on the command line, added to the existing image and written back to file. The output file is encoded with the same transfer syntax used for the input file. This utility only supports the creation of two-dimensional curves.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in    DICOM input image file
curvedata-in  curve data input file (text)
dcmfile-out   DICOM output filename
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
<h3>curve creation options</h3>
<pre><code>
curve type : -r-- poly
                 create as POLY curve(default) +
             r-- roi
             create as ROI curve
             curve value representation : +v-- data
                                          -
                                          vr[n] umber : integer 0..4(default : 4)
                                                            select curve data VR : 0 = US,
                                                                                   1 = SS, 2 = FL, 3 = FD, 4 = SL - c-- curve - vr[n] umber : integer 0..2(default : 0)select VR with which the Curve Data element is written 0 = VR according to-- data - vr, 1 = OB, 2 = OW repeating group : -g-- group[n] umber : integer 0..15(default : 0)select repeating group : 0 = 0x5000, 1 = 0x5002 etc.curve description : -l-- label s : string set Curve Label to s(default
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   : absent) +
                                                                                                                                                                                                                                                                                                                                                                                         d-- description s : string set Curve Description to s(default
                                                                                                                                                                                                                                                                                                                                                                                                                                               : absent) -
                                                                                                                                                                                                                                                                                                                                                                                                             a-- axis x : string,
                                                                                   y : string
                                                                                       set Axis Units to xy(default
                                                                                                            : absent)
</code></pre>
<h2>NOTES</h2>
<h3>Syntax of the Curve Data File</h3>
<p> The curve data file is expected to be a plain ASCII text file containing numbers (integer or floating point) comprising the values of the point coordinates. Numbers must be separated by whitespace. No checking of the value range or value range conversion is performed. Example: </p>
<pre>
 256.451947    1.000000
 477.689863  128.822080
 128.822080  477.689863
  35.310137  128.822080
 256.451947    1.000000
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmmkcrv</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
