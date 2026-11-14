---
title: "dcmp2pgm(1)"
name: "dcmp2pgm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmp2pgm/"
description: "dcmp2pgm – Read DICOM image and presentation state and render bitmap"
---

<h2 class="name">NAME</h2>
<p> dcmp2pgm &#8211; Read DICOM image and presentation state and render bitmap </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmp2pgm[options] dcmimage - in[bitmap - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmp2pgm</code> utility renders a monochrome DICOM image under the control of a grayscale softcopy presentation state object into a monochrome bitmap with 8 bits/pixel. The bitmap is stored either as &#8216;Portable Gray Map&#8217; (PGM) or as a DICOM secondary capture image object. If no presentation state is read from file, a default presentation state is created. The utility allows to read a configuration file of the Softcopy Presentation State Viewer upon startup. In this case, the settings from the configuration file affecting the rendering of the presentation state are used, e.g. a correction of the gray scale range according to Barten&#8217;s model (DICOM part 14) can be performed if the characteristic curve of the display system is available and defined in the configuration file.</p>
<h2>PARAMETERS</h2>
<pre>
dcmimage-in  input DICOM image
bitmap-out   output DICOM image or PGM bitmap
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
<pre><code>
- p-- pstate[f] ilename:string
                            process using presentation state file -
                        c-- config[f]
                ilename:string
                            process using settings from configuration file -
                        f-- frame[f]
                   rame:integer
                            process using image frame f(default:1)
</code></pre>
<h3>output format</h3>
<pre>
  -D   --pgm
         save image as PGM (default)
  +D   --dicom
         save image as DICOM secondary capture
</pre>
<h3>output options</h3>
<pre>
  +S   --save-pstate  [f]ilename: string
         save presentation state to file
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmp2pgm</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;etcdir&gt;/dcmpstat.cfg</i> &#8211; sample configuration file</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
