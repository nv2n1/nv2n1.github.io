---
title: "dcmscale(1)"
name: "dcmscale"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmscale/"
description: "dcmscale – Scale DICOM images"
---

<h2 class="name">NAME</h2>
<p> dcmscale &#8211; Scale DICOM images </p>
<h2>SYNOPSIS</h2>
<pre>
dcmscale [options] dcmfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmscale</code> utility reads a DICOM image, scales it according to the command line settings and writes back the DICOM image. This utility only supports uncompressed and RLE compressed DICOM images.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in   DICOM input filename to be scaled
dcmfile-out  DICOM output filename to be written
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
  -lc   --log-config  [f]ilename: string
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
<h3>processing options</h3>
<p>scaling : +a&#8211; recognize &#8211; aspect recognize pixel aspect ratio(default) &#8211; a&#8211; ignore &#8211; aspect ignore pixel aspect ratio when scaling<br />
          +<br />
          i&#8211; interpolate[n] umber of algorithm : integer<br />
                                                  use interpolation when scaling(1..4, default : 1) &#8211;<br />
                                                  i&#8211; no &#8211; interpolation no interpolation when scaling<br />
                                                  &#8211;<br />
                                                  S&#8211; no &#8211; scaling no scaling,<br />
    ignore pixel aspect ratio(default) + Sxf&#8211; scale &#8211; x &#8211; factor[f] actor : float scale x axis by factor, auto &#8211; compute y axis + Syf&#8211; scale &#8211; y &#8211; factor[f] actor : float scale y axis by factor, auto &#8211; compute x axis + Sxv&#8211; scale &#8211; x &#8211; size[n] umber : integer scale x axis to n pixels, auto &#8211; compute y axis + Syv&#8211; scale &#8211; y &#8211; size[n] umber : integer scale y axis to n pixels, auto &#8211; compute x axis other transformations : +C&#8211; clip &#8211; region[l] eft[t] op[w] idth[h] eight : integer clip rectangular image region(l, t, w, h)<br />
SOP Instance UID : +ua&#8211; uid &#8211; always always assign new SOP Instance UID(default) + un&#8211; uid &#8211; never never assign new SOP Instance UID</p>
<h3>output options</h3>
<pre><code>
output file format:
  +F    --write-file
          write file format (default)
  -F    --write-dataset
          write data set without file meta information
output transfer syntax:
  +t=   --write-xfer-same
          write with same TS as input (default)
  +te   --write-xfer-little
          write with explicit VR little endian TS
  +tb   --write-xfer-big
          write with explicit VR big endian TS
  +ti   --write-xfer-implicit
          write with implicit VR little endian TS
post-1993 value representations:
  +u    --enable-new-vr
          enable support for new VRs (UN/UT) (default)
  -u    --disable-new-vr
          disable support for new VRs, convert to OB
group length encoding:
  +g=   --group-length-recalc
          recalculate group lengths if present (default)
  +g    --group-length-create
          always write with group length elements
  -g    --group-length-remove
          always write without group length elements
length encoding in sequences and items:
  +e    --length-explicit
          write with explicit lengths (default)
  -e    --length-undefined
          write with undefined lengths
data set trailing padding (not with --write-dataset):
  -p=   --padding-retain
          do not change padding
          (default if not --write-dataset)
  -p    --padding-off
          no padding (implicit if --write-dataset)
  +p    --padding-create  [f]ile-pad [i]tem-pad: integer
          align file on multiple of f bytes and items on
          multiple of i bytes
</code></pre>
<h2>NOTES</h2>
<p> The following preferred interpolation algorithms can be selected using the <i>&#8211;interpolate</i> option: </p>
<dl>
<dt>&bull;</p>
<dd> 1 = free scaling algorithm with interpolation from pbmplus toolkit</p>
<dt>&bull;</p>
<dd> 2 = free scaling algorithm with interpolation from c&#8217;t magazine</p>
<dt>&bull;</p>
<dd> 3 = magnification algorithm with bilinear interpolation from Eduard Stanescu</p>
<dt>&bull;</p>
<dd> 4 = magnification algorithm with bicubic interpolation from Eduard Stanescu</dl>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmscale</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
