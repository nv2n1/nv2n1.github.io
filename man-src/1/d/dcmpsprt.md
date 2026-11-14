---
title: "dcmpsprt(1)"
name: "dcmpsprt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmpsprt/"
description: "dcmpsprt – Read DICOM images and presentation states and render print job"
---

<h2 class="name">NAME</h2>
<p> dcmpsprt &#8211; Read DICOM images and presentation states and render print job </p>
<h2>SYNOPSIS</h2>
<pre>
dcmpsprt [options] dcmfile-in...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmpsprt</code> utility reads one or more DICOM images and presentation states and creates a print job. The print job consists of one Stored Print object and one or more Hardcopy Grayscale images and is written to the database specified in the configuration file. The print job can optionally be spooled to the printer. In this case, <code>dcmpsprt</code> calls the <code>dcmprscu</code> application which performs communication with the printer.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM image file(s) to be printed
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
<h3>processing options</h3>
<p>+ p&#8211; pstate[p] state file:string<br />
                               render the following image with presentation state<br />
                               p(this option can be specified multiple times) &#8211;<br />
                           c&#8211; config[f]<br />
                   ilename:string<br />
                           process using settings from configuration file f<br />
                           &#8211; p&#8211; printer[n]<br />
                       ame:string(default:1st printer in cfg file)<br />
                               select printer with identifier n from cfg file</p>
<h3>spooling options</h3>
<pre>
  -s   --spool
         spool print job to DICOM printer
       --nospool
         do not spool print job to DICOM printer (default)
</pre>
<h3>film orientation options</h3>
<pre>
       --portrait
         set portrait orientation
       --landscape
         set landscape orientation
       --default-orientation
         use printer default (default)
</pre>
<h3>trim (border) options</h3>
<pre>
       --trim
         set trim on
       --no-trim
         set trim off
       --default-trim
         use printer default (default)
</pre>
<h3>requested decimate/crop behaviour options</h3>
<p>&#8211;request &#8211; decimate request decimate&#8211; request &#8211; crop request crop&#8211; request &#8211; fail request failure&#8211; default &#8211; request use printer default(default)</p>
<h3>print presentation LUT options</h3>
<p>&#8211;default &#8211; plut do not create presentation LUT(default)&#8211; identity set IDENTITY presentation LUT shape&#8211; plut[l] ut identifier : string add LUT l to print job&#8211; inverse &#8211; plut render the inverse presentation LUT into the bitmap of the hardcopy grayscale image&#8211; illumination[v] alue : integer(0..65535) set illumination to v(in cd / m ^ 2)&#8211; reflection[v] alue : integer(0..65535) set reflected ambient light to v(in cd / m ^ 2)</p>
<h3>basic film session options (only with &#8211;spool)</h3>
<p>&#8211;copies[v] alue : integer(1..100, default : 1)<br />
                       set number of copies to v<br />
                   &#8212; medium<br />
    &#8211; type[v] alue : string<br />
                     set medium type to v<br />
                     &#8212; destination[v] alue : string<br />
                                              set film destination to v<br />
                                              &#8212; label[v] alue : string<br />
                                                                 set film session label to v<br />
                                                                 &#8212; priority[v] alue : string<br />
                                                                                       set print priority to v<br />
                                                                                       &#8212; owner[v] alue : string<br />
                                                                                                          set film session owner ID to v</p>
<h3>annotation options</h3>
<p>&#8211;no &#8211; annotation do not create annotation(default) &#8211; a&#8211; annotation[t] ext : string create annotation with text t + pd&#8211; print &#8211; date prepend date / time to annotation(default) &#8211; pd&#8211; print &#8211; no &#8211; date do not prepend date / time to annotation + pn&#8211; print &#8211; name prepend printer name to annotation(default) &#8211; pn&#8211; print &#8211; no &#8211; name do not prepend printer name to annotation + pl&#8211; print &#8211; lighting prepend illumination to annotation(default) &#8211; pl&#8211; print &#8211; no &#8211; lighting do not prepend illumination to annotation</p>
<h3>overlay options</h3>
<p>+ O&#8211; overlay[f] ilename:string, [x][y]:integer<br />
                                            load overlay data from PBM file f and display at<br />
                                            position(x, y) +<br />
                                     Og&#8211; ovl &#8211; graylevel[v]<br />
                    alue:integer(0..4095)<br />
                             use overlay gray level v(default:4095 = white)</p>
<h3>other_print_options</h3>
<pre><code>
- l-- layout[c] olumns[r] ows:integer(default:1 1)
                                  use 'STANDARD,r' image display format
                          -- filmsize[v]
                         alue:string
                         set film size ID to v
                         -- magnification[v]
                         alue:string
                         set magnification type to v
                         -- smoothing[v]
                         alue:string
                         set smoothing type to v
                         -- configinfo[v]
                         alue:string
                         set configuration information to v
                         -- resolution[v]
                         alue:string
                         set requested resolution ID to v
                         -- border[v]
                         alue:string
                              set border density to v
                              -- empty
                              - image[v]
                         alue:string
                              set empty image density to v
                              -- max
                              - density[v]
                         alue:string
                              set max density to v
                              -- min
                              - density[v]
                         alue:string
                              set min density to v
                              -- img
                              - polarity[v]
                         alue:string
                              set image box polarity to v(NORMAL or REVERSE)-- img
                              - request - size[v]
                         alue:string
                              set requested image size to v(width in mm)-- img
                              - magnification[v]
                         alue:string
                              set image box magnification type to v
                              -- img
                              - smoothing[v]
                         alue:string
                              set image box smoothing type to v
                              -- img
                              - configinfo[v]
                         alue:string
    set image box configuration information to v
</code></pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmpsprt</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;etcdir&gt;/dcmpstat.cfg</i>, <i>&lt;etcdir&gt;/printers.cfg</i> &#8211; sample configuration files</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmprscu/">dcmprscu</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
