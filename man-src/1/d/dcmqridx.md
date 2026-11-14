---
title: "dcmqridx(1)"
name: "dcmqridx"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmqridx/"
description: "dcmqridx – Register a DICOM image file in an image database index file"
---

<h2 class="name">NAME</h2>
<p> dcmqridx &#8211; Register a DICOM image file in an image database index file </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmqridx[options] index - out[dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmqridx</code> ulility registers DICOM image files in the database index file used by the <code>dcmqrscp</code> and <code>dcmqrti</code> applications. No image files are copied. <code>dcmqridx</code> can also list the contents of the database index file.</p>
<h2>PARAMETERS</h2>
<pre>
index-out   storage area for the index file (directory)
dcmfile-in  DICOM image file to be registered in the index file
</pre>
<h2>OPTIONS</h2>
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
  -p   --print
         list contents of database index file
  -n   --not-new
         set instance reviewed status to 'not new'
</code></pre>
<h2>NOTES</h2>
<p> <code>dcmqridx</code> attempts to add a reference to the database index file for each image-file provided on the command line. </p>
<p> <code>dcmqridx</code> disables the database back-end quota system so that no image files will be deleted.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmqridx</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmqrscp/">dcmqrscp</a></code>(1), <code><a href="/docs/linux/man/1-dcmqrti/">dcmqrti</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1993-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
