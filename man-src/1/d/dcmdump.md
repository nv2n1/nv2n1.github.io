---
title: "dcmdump(1)"
name: "dcmdump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmdump/"
description: "dcmdump – Dump DICOM file and data set"
---

<h2 class="name">NAME</h2>
<p> dcmdump &#8211; Dump DICOM file and data set </p>
<h2>SYNOPSIS</h2>
<pre>
dcmdump [options] dcmfile-in...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmdump</code> utility dumps the contents of a DICOM file (file format or raw data set) to stdout in textual form. Attributes with very large value fields (e.g. pixel data) can be described as &#8216;(not loaded)&#8217;. String value fields will be delimited with square brackets ([]). Known UIDs will be displayed by their names prefixed by an equals sign (e.g. &#8216;=MRImageStorage&#8217;) unless this mapping would be explicitly switched off. Empty value fields are described as &#8216;(no value available)&#8217;. </p>
<p> If <code>dcmdump</code> reads a raw data set (DICOM data without a file format meta-header) it will attempt to guess the transfer syntax by examining the first few bytes of the file. It is not always possible to correctly guess the transfer syntax and it is better to convert a data set to a file format whenever possible (using the <code>dcmconv</code> utility). It is also possible to use the <i>-f</i> and <i>-t[ieb]</i> options to force <code>dcmdump</code> to read a dataset with a particular transfer syntax.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM input file or directory to be dumped
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
input files:<br />
  +sd  &#8211;scan-directories<br />
         scan directories for input files (dcmfile-in)<br />
  +sp  &#8211;scan-pattern  [p]attern: string (only with &#8211;scan-directories)<br />
         pattern for filename matching (wildcards)<br />
#possibly not available on all systems<br />
  -r   &#8211;no-recurse<br />
         do not recurse within directories (default)<br />
  +r   &#8211;recurse<br />
         recurse within specified directories<br />
parsing of file meta information:<br />
  +ml  &#8211;use-meta-length<br />
         use file meta information group length (default)<br />
  -ml  &#8211;ignore-meta-length<br />
         ignore file meta information group length<br />
parsing of odd-length attributes:<br />
  +ao  &#8211;accept-odd-length<br />
         accept odd length attributes (default)<br />
  +ae  &#8211;assume-even-length<br />
         assume real length is one byte larger<br />
handling of non-standard VR:<br />
  +vr  &#8211;treat-as-unknown<br />
         treat non-standard VR as unknown (default)<br />
  -vr  &#8211;assume-implicit<br />
         try to read with implicit VR little endian TS<br />
handling of undefined length UN elements:<br />
  +ui  &#8211;enable-cp246<br />
         read undefined len UN as implicit VR (default)<br />
  -ui  &#8211;disable-cp246<br />
         read undefined len UN as explicit VR<br />
handling of defined length UN elements:<br />
  -uc  &#8211;retain-un<br />
         retain elements as UN (default)<br />
  +uc  &#8211;convert-un<br />
         convert to real VR if known<br />
handling of private max-length elements (implicit VR):<br />
  -sq  &#8211;maxlength-dict<br />
         read as defined in dictionary (default)<br />
  +sq  &#8211;maxlength-seq<br />
         read as sequence with undefined length<br />
automatic data correction:<br />
  +dc  &#8211;enable-correction<br />
         enable automatic data correction (default)<br />
  -dc  &#8211;disable-correction<br />
         disable automatic data correction<br />
general handling of parser errors:<br />
  +Ep  &#8211;ignore-parse-errors<br />
         try to recover from parse errors<br />
  -Ep  &#8211;handle-parse-errors<br />
         handle parse errors and stop parsing (default)<br />
other parsing options:<br />
  +st  &#8211;stop-after-elem  [t]ag: &#8220;gggg,eeee&#8221; or dictionary name<br />
         stop parsing after element specified by t<br />
bitstream format of deflated input:<br />
  +bd  &#8211;bitstream-deflated<br />
         expect deflated bitstream (default)<br />
  +bz  &#8211;bitstream-zlib<br />
         expect deflated zlib bitstream</p>
<h3>output options</h3>
<pre><code>
loading:
  +M   --load-all
         load very long tag values (default)
  -M   --load-short
         do not load very long values (e.g. pixel data)
  +R   --max-read-length  [k]bytes: integer (4..4194302, default: 4)
         set threshold for long values to k kbytes
printing:
  +L   --print-all
         print long tag values completely
  -L   --print-short
         print long tag values shortened (default)
  +T   --print-tree
         print hierarchical structure as a simple tree
  -T   --print-indented
         print hierarchical structure indented (default)
  +F   --print-filename
         print header with filename for each input file
  +Fs  --print-file-search
         print header with filename only for those input files
         that contain one of the searched tags
  +Un  --map-uid-names
         map well-known UID numbers to names (default)
  -Un  --no-uid-names
         do not map well-known UID numbers to names
  +Qn  --quote-nonascii
         quote non-ASCII and control chars as XML markup
  -Qn  --print-nonascii
         print non-ASCII and control chars (default)
  +C   --print-color
         use ANSI escape codes for colored output
#not available on Windows systems
error handling:
  -E   --stop-on-error
         do not print if file is damaged (default)
  +E   --ignore-errors
         attempt to print even if file is damaged
searching:
  +P   --search  [t]ag: "gggg,eeee" or dictionary name
         print the value of tag t this option can be specified
         multiple times (default: the complete file is printed)
  +s   --search-all
         print all instances of searched tags (default)
  -s   --search-first
         only print first instance of searched tags
  +p   --prepend
         prepend sequence hierarchy to printed tag,
         denoted by: (gggg,eeee).(gggg,eeee).*
         (only with --search-all or --search-first)
  -p   --no-prepend
         do not prepend hierarchy to tag (default)
writing:
  +W   --write-pixel  [d]irectory: string
         write pixel data to a .raw file stored in d
         (little endian, filename created automatically)
</code></pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmdump</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dump2dcm/">dump2dcm</a></code>(1), <code><a href="/docs/linux/man/1-dcmconv/">dcmconv</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1994-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
