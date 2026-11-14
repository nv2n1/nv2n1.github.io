---
title: "dcmcrle(1)"
name: "dcmcrle"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmcrle/"
description: "dcmcrle – Encode DICOM file to RLE transfer syntax"
---

<h2 class="name">NAME</h2>
<p> dcmcrle &#8211; Encode DICOM file to RLE transfer syntax </p>
<h2>SYNOPSIS</h2>
<pre>
dcmcrle [options] dcmfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmcrle</code> utility reads an uncompressed DICOM image (<i>dcmfile-in</i>), performs RLE compression (i.e. conversion to an encapsulated DICOM transfer syntax) and writes the converted image to an output file (<i>dcmfile-out</i>).</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in   DICOM input filename to be converted
dcmfile-out  DICOM output filename
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
<h3>encapsulated pixel data encoding options</h3>
<p>pixel data fragmentation : +ff&#8211; fragment &#8211; per &#8211; frame encode each frame as one fragment(default) + fs&#8211; fragment &#8211; size[s] ize : integer limit fragment size to s kbytes(non &#8211; standard) basic offset table encoding : +ot&#8211; offset &#8211; table &#8211; create create offset table(default) &#8211; ot&#8211; offset &#8211; table &#8211; empty leave offset table empty SOP Class UID : +cd&#8211; class &#8211; default keep SOP Class UID(default) + cs&#8211; class &#8211; sc convert to Secondary Capture Image(implies&#8211; uid &#8211; always) SOP Instance UID : +un&#8211; uid &#8211; never never assign new UID(default) + ua&#8211; uid &#8211; always always assign new UID</p>
<h3>output options</h3>
<pre><code>
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
data set trailing padding:
  -p=  --padding-retain
         do not change padding (default)
  -p   --padding-off
         no padding
  +p   --padding-create  [f]ile-pad [i]tem-pad: integer
         align file on multiple of f bytes
         and items on multiple of i bytes
</code></pre>
<h2>TRANSFER SYNTAXES</h2>
<p> <code>dcmcrle</code> supports the following transfer syntaxes for input (<i>dcmfile-in</i>): </p>
<pre>
LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax   1.2.840.10008.1.2.1.99 (*)
BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
</pre>
<p> (*) if compiled with zlib support enabled </p>
<p> <code>dcmcrle</code> supports the following transfer syntaxes for output (<i>dcmfile-out</i>): </p>
<pre>
RLELosslessTransferSyntax                      1.2.840.10008.1.2.5
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmcrle</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmdrle/">dcmdrle</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
