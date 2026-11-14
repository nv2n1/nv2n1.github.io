---
title: "dcmdjpls(1)"
name: "dcmdjpls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmdjpls/"
description: "dcmdjpls – Decode JPEG-LS compressed DICOM file"
---

<h2 class="name">NAME</h2>
<p> dcmdjpls &#8211; Decode JPEG-LS compressed DICOM file </p>
<h2>SYNOPSIS</h2>
<pre>
dcmdjpls [options] dcmfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmdjpls</code> utility reads a JPEG-ls compressed DICOM image (<i>dcmfile-in</i>), decompresses the JPEG-LS data (i. e. conversion to a native DICOM transfer syntax) and writes the converted image to an output file (<i>dcmfile-out</i>).</p>
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
<pre>
input file format:
  +f   --read-file
         read file format or data set (default)
  +fo  --read-file-only
         read file format only
  -f   --read-dataset
         read data set without file meta information
  # This option allows to decompress JPEG-LS compressed DICOM objects that have
  # been stored as dataset without meta-header. Such a thing should not exist
  # since the transfer syntax cannot be reliably determined without meta-header,
  # but unfortunately it does.
</pre>
<h3>processing options</h3>
<p>planar configuration : +pr&#8211; planar &#8211; restore restore original planar configuration(default)<br />
#If the compressed image is a color image, restore the planar<br />
#configuration as described in the Planar Configuration attribute.<br />
                       +<br />
                       pa&#8211; planar &#8211; auto automatically determine planar configuration from SOP class and color space<br />
#If the compressed image is a color image, store in color &#8211; by &#8211; plane<br />
#planar configuration if required by the SOP class and photometric<br />
#interpretation.Hardcopy Color images are always stored color &#8211; by &#8211;<br />
#plane, and the revised Ultrasound image objects are stored color &#8211; by &#8211;<br />
#plane if the color model is YBR_FULL.Everything else is stored<br />
#color &#8211; by &#8211; pixel.<br />
                       +<br />
                       px&#8211; color &#8211; by &#8211; pixel always store color &#8211; by &#8211; pixel<br />
#If the compressed image is a color image, store in color &#8211; by &#8211; pixel<br />
#planar configuration.<br />
                       +<br />
                       pl&#8211; color &#8211; by &#8211; plane always store color &#8211; by &#8211; plane<br />
#If the compressed image is a color image, store in color &#8211; by &#8211; plane<br />
#planar configuration.<br />
                       SOP Instance UID : +ud&#8211; uid<br />
                                          &#8211;<br />
                                          default keep same SOP Instance UID(default)<br />
#Never assigns a new SOP instance UID.<br />
                                          +<br />
                                          ua&#8211; uid &#8211; always always assign new UID<br />
#Always assigns a new SOP instance UID.<br />
                                          other processing options : +io&#8211; ignore<br />
                                                                     &#8211;<br />
                                                                     offsettable<br />
                                                                     ignore offset table when decompressing</p>
<h3>output options</h3>
<pre><code>
output file format:
  +F   --write-file
         write file format (default)
  -F   --write-dataset
         write data set without file meta information
output transfer syntax:
  +te  --write-xfer-little
         write with explicit VR little endian (default)
  +tb  --write-xfer-big
         write with explicit VR big endian TS
  +ti  --write-xfer-implicit
         write with implicit VR little endian TS
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
data set trailing padding (not with --write-dataset):
  -p=  --padding-retain
         do not change padding (default if not --write-dataset)
  -p   --padding-off
         no padding (implicit if --write-dataset)
  +p   --padding-create  [f]ile-pad [i]tem-pad: integer
         align file on multiple of f bytes
         and items on multiple of i bytes
</code></pre>
<h2>TRANSFER SYNTAXES</h2>
<p> <code>dcmdjpls</code> supports the following transfer syntaxes for input (<i>dcmfile-in</i>): </p>
<pre>
LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax   1.2.840.10008.1.2.1.99 (*)
BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
JPEGLSLosslessTransferSyntax                   1.2.840.10008.1.2.4.80
JPEGLSLossyTransferSyntax                      1.2.840.10008.1.2.4.81
</pre>
<p> (*) if compiled with zlib support enabled </p>
<p> <code>dcmdjpls</code> supports the following transfer syntaxes for output (<i>dcmfile-out</i>): </p>
<pre>
LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmdjpls</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmcjpls/">dcmcjpls</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
