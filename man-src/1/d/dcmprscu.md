---
title: "dcmprscu(1)"
name: "dcmprscu"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmprscu/"
description: "dcmprscu – Print spooler for presentation state viewer"
---

<h2 class="name">NAME</h2>
<p> dcmprscu &#8211; Print spooler for presentation state viewer </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmprscu[options][dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmprscu</code> utility implements the DICOM Basic Grayscale Print Management Service Class as SCU. It also supports the optional Basic Annotation Box and Presentation LUT SOP Classes. The utility is intended for use within the DICOMscope viewer. </p>
<p> The <code>dcmprscu</code> utility takes complete print jobs consisting of a Stored Print object and one or more Hardcopy Grayscale objects and spools them to the printer. No attempt is made to check whether the attributes defined in the Stored Print object are supported by the Print SCP. However, the print spooler will not attempt to use the optional Annotation or Presentation LUT services if they are not successfully negotiated with the Print SCP. </p>
<p> The <code>dcmprscu</code> utility reads the characteristics of the printer to communicate with from the configuration file. Depending on the printer&#8217;s support for Presentation LUT, any Presentation LUT present in the print job will be rendered into the hardcopy images before they are spooled to the printer if necessary. If the printer does not support image transmission with 12 bits/pixel (as per the configuration file), the grayscale hardcopy images are down-sampled to 8 bits/pixel before transmission to the printer. </p>
<p> The <code>dcmprscu</code> utility can be run either in &#8216;printer mode&#8217;, in which case the file name of a Stored Print object must be passed, or in &#8216;spool mode&#8217;, in which case commands are read periodically from a spool directory.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  stored print file(s) to be spooled
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
<h3>print options</h3>
<pre>
       --noprint
         do not create print-out (no n-action-rq)
       --session-print
         send film session n-action-rq (instead of film box)
       --monochrome1
         transmit basic grayscale images in MONOCHROME1
</pre>
<h3>mode options</h3>
<p>+ p&#8211; print<br />
    printer mode,<br />
    print file(s)and terminate(default) + s&#8211; spool[n] ame:string<br />
                                                           spooler mode,<br />
                                                           use job prefix n</p>
<h3>processing options</h3>
<p>&#8211; c&#8211; config[f] ilename:string<br />
                            process using settings from configuration file &#8211;<br />
                        p&#8211; printer[n]<br />
                    ame:string(default:1st printer in cfg file)<br />
                            select printer with identifier n from cfg file<br />
                        + d&#8211; dump<br />
                        dump all DIMSE messages</p>
<h3>spooler options (only with &#8211;spool)</h3>
<pre>
       --sleep  [d]elay: integer (default: 1)
         sleep d seconds between spooler checks
</pre>
<h3>basic film session options (not with &#8211;spool):</h3>
<pre><code>
--copies[v] alue : integer(1..100, default : 1)
                       set number of copies to v
                   -- medium
    - type[v] alue : string
                     set medium type to v
                     -- destination[v] alue : string
                                              set film destination to v
                                              -- label[v] alue : string
                                                                 set film session label to v
                                                                 -- priority[v] alue : string
                                                                                       set print priority to v
                                                                                       -- owner[v] alue : string
                                                                                                          set film session owner ID to v
</code></pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmprscu</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;etcdir&gt;/dcmpstat.cfg</i>, <i>&lt;etcdir&gt;/printers.cfg</i> &#8211; sample configuration files</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmprscp/">dcmprscp</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
