---
title: "dcmcjpls(1)"
name: "dcmcjpls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmcjpls/"
description: "dcmcjpls – Encode DICOM file to JPEG-LS transfer syntax"
---

<h2 class="name">NAME</h2>
<p> dcmcjpls &#8211; Encode DICOM file to JPEG-LS transfer syntax </p>
<h2>SYNOPSIS</h2>
<pre>
dcmcjpls [options] dcmfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmcjpls</code> utility reads an uncompressed DICOM image (<i>dcmfile-in</i>), performs a JPEG-LS compression (i. e. conversion to an encapsulated DICOM transfer syntax) and writes the converted image to an output file (<i>dcmfile-out</i>).</p>
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
<h3>JPEG-LS encoding options</h3>
<p>JPEG-LS process:<br />
  +el  &#8211;encode-lossless<br />
         encode JPEG-LS lossless only TS (default)<br />
#This options selects the JPEG &#8211; LS lossless only transfer syntax<br />
#and performs a lossless compression.<br />
  +en  &#8211;encode-nearlossless<br />
         encode JPEG-LS near-lossless TS (NEAR: 2)<br />
#This options selects the JPEG &#8211; LS lossy transfer syntax<br />
#and performs a near &#8211; lossless compression.<br />
JPEG-LS bit rate (near-lossless only):<br />
  +md  &#8211;max-deviation  [d]eviation: integer (default: 2)<br />
         defines maximum deviation for an encoded pixel<br />
#This option specifies the maximum deviation for a single pixel from<br />
#the original pixel value.<br />
lossless compression:<br />
  +pr  &#8211;prefer-raw<br />
         prefer raw encoder mode (default)<br />
#This option enables the raw encoder.The raw encoder encodes the<br />
#complete pixel cell as it was read from the source image without<br />
#performing any modifications.<br />
  +pc  &#8211;prefer-cooked<br />
         prefer cooked encoder mode<br />
#This option enables the cooked encoder.The cooked encoder moves<br />
#overlay data to separate tags(60xx, 3000) and only encodes the<br />
#stored bits in each pixel.<br />
JPEG-LS compression:<br />
  +t1  &#8211;threshold1  [t]hreshhold: integer (default for 8 bpp: 3)<br />
         set JPEG-LS encoding parameter threshold 1<br />
  +t2  &#8211;threshold2  [t]hreshhold: integer (default for 8 bpp: 7)<br />
         set JPEG-LS encoding parameter threshold 2<br />
  +t3  &#8211;threshold3  [t]hreshhold: integer (default for 8 bpp: 21)<br />
         set JPEG-LS encoding parameter threshold 3<br />
  +rs  &#8211;reset  [r]eset: integer (default: 64)<br />
         set JPEG-LS encoding parameter reset<br />
  +lm  &#8211;limit  [l]imit: integer (default: 0)<br />
         set JPEG-LS encoding parameter limit<br />
JPEG-LS interleave:<br />
  +il  &#8211;interleave-line<br />
         force line-interleaved JPEG-LS images (default)<br />
#This flag forces line &#8211; interleaved mode for the resulting image.<br />
#In line &#8211; interleave mode each line from the source image is<br />
#compressed separately for each component and then the next line<br />
#is encoded.<br />
  +is  &#8211;interleave-sample<br />
         force sample-interleaved JPEG-LS images<br />
#This flag forces sample &#8211; interleaved mode for the resulting image.<br />
#In sample &#8211; interleave mode each pixel&#8217;s components are encoded before<br />
#the next pixe is encoded.<br />
  +in  &#8211;interleave-none<br />
         force uninterleaved JPEG-LS images<br />
#This flag forces uninterleaved mode for the resulting image.<br />
#In this mode, each of the image&#8217;s components are completely encoded<br />
#before the next component is handled.<br />
  +iv  &#8211;interleave-default<br />
         use the fastest possible interleave mode<br />
#This flag selects an interleave mode based on the source image&#8217;s mode.<br />
#If possible, the image is not converted to a different interleave mode.</p>
<h3>encapsulated pixel data encoding options</h3>
<p>encapsulated pixel data fragmentation : +ff&#8211; fragment &#8211; per &#8211; frame encode each frame as one fragment(default)<br />
#This option causes the creation of one compressed fragment for each<br />
#frame(recommended).<br />
                                        +<br />
                                        fs&#8211; fragment &#8211; size[s] ize : integer limit fragment size to s kbytes<br />
#This option limits the fragment size which may cause the creation of<br />
#multiple fragments per frame.<br />
                                                                      basic offset table encoding : +ot&#8211; offset<br />
                                                                                                    &#8211;<br />
                                                                                                    table &#8211; create create offset table(default)<br />
#This option causes the creation of a valid offset table for the<br />
#compressed JPEG fragments.<br />
                                                                                                    &#8211;<br />
                                                                                                    ot&#8211; offset &#8211; table &#8211; empty leave offset table empty<br />
#This option causes the creation of an empty offset table<br />
#for the compressed JPEG fragments.<br />
                                                                                                    SOP Class UID : +cd&#8211; class<br />
                                                                                                                    &#8211;<br />
                                                                                                                    default keep SOP Class UID(default)<br />
#Keep the SOP Class UID of the source image.<br />
                                                                                                                    +<br />
                                                                                                                    cs&#8211; class &#8211; sc convert to Secondary Capture Image(implies&#8211; uid &#8211; always)<br />
#Convert the image to Secondary Capture.In addition to the SOP Class<br />
#UID, all attributes required for a valid secondary capture image are<br />
#added.A new SOP instance UID is always assigned.<br />
                                                                                                                                     SOP Instance UID : +ud&#8211; uid<br />
                                                                                                                                                        &#8211;<br />
                                                                                                                                                        default assign new UID if lossy compression(default)<br />
#Assigns a new SOP instance UID if the compression is lossy JPEG.<br />
                                                                                                                                                        +<br />
                                                                                                                                                        ua&#8211; uid &#8211; always always assign new UID<br />
#Unconditionally assigns a new SOP instance UID.<br />
                                                                                                                                                        +<br />
                                                                                                                                                        un&#8211; uid &#8211; never never assign new UID<br />
#Never assigns a new SOP instance UID.</p>
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
<h2>NOTES</h2>
<p> The <code>dcmcjpls</code> utility compresses DICOM images of all SOP classes. However, <code>dcmcjpls</code> does not attempt to ensure that the compressed image still complies with all restrictions of the object&#8217;s IOD. </p>
<p> The user is responsible for making sure that the compressed images he creates are compliant with the DICOM standard. If in question, the <code>dcmcjpls</code> utility allows to convert an image to secondary capture &#8211; this SOP class does not pose restrictions as the ones mentioned above.</p>
<h2>TRANSFER SYNTAXES</h2>
<p> <code>dcmcjpls</code> supports the following transfer syntaxes for input (<i>dcmfile-in</i>): </p>
<pre>
LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax   1.2.840.10008.1.2.1.99 (*)
BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
</pre>
<p> (*) if compiled with zlib support enabled </p>
<p> <code>dcmcjpls</code> supports the following transfer syntaxes for output (<i>dcmfile-out</i>): </p>
<pre>
JPEGLSLosslessTransferSyntax                   1.2.840.10008.1.2.4.80
JPEGLSLossyTransferSyntax                      1.2.840.10008.1.2.4.81
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmcjpls</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmdjpls/">dcmdjpls</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
