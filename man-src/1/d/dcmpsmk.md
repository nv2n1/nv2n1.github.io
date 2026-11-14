---
title: "dcmpsmk(1)"
name: "dcmpsmk"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmpsmk/"
description: "dcmpsmk – Create DICOM grayscale softcopy presentation state"
---

<h2 class="name">NAME</h2>
<p> dcmpsmk &#8211; Create DICOM grayscale softcopy presentation state </p>
<h2>SYNOPSIS</h2>
<pre>
dcmpsmk [options] dcmfile-in dcmfile-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmpsmk</code> utility reads a DICOM image file and creates a grayscale softcopy presentation state object according to Supplement 33. The presentation state object is written back to file. A number of command line options allow to specify how certain constructs that might be present in the image file should be referenced or activated in the presentation state. The newly created presentation state references the source image and contains values that should allow for a &#8216;reasonable&#8217; display of the image when rendered under control of the presentation state.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in   DICOM image file to be read
dcmfile-out  DICOM presentation state file to be created
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
<h3>processing options</h3>
<p>VOI transform handling:<br />
  +Vl  &#8211;voi-lut<br />
         use first VOI LUT if present (default)<br />
  +Vw  &#8211;voi-window<br />
         use first window center/width if present<br />
  -V   &#8211;voi-ignore<br />
         ignore VOI LUT and window center/width<br />
curve handling:<br />
  +c   &#8211;curve-activate<br />
         activate curve data if present (default)<br />
  -c   &#8211;curve-ignore<br />
         ignore curve data<br />
overlay handling:<br />
  +oc  &#8211;overlay-copy<br />
         copy overlays if not embedded, activate otherwise (default)<br />
  +oa  &#8211;overlay-activate<br />
         activate overlays<br />
  -o   &#8211;overlay-ignore<br />
         ignore overlays<br />
shutter handling:<br />
  +s   &#8211;shutter-activate<br />
         use shutter if present in image (default)<br />
  -s   &#8211;shutter-ignore<br />
         ignore shutter<br />
presentation LUT shape handling:<br />
  +p   &#8211;plut-activate<br />
         use presentation LUT shape if present (default)<br />
  -p   &#8211;plut-ignore<br />
         ignore presentation LUT shape<br />
layering:<br />
  +l1  &#8211;layer-single<br />
         all curves and overlays are in one layer<br />
  +l2  &#8211;layer-double<br />
         one layer for curves, one for overlays (default)<br />
  +ls  &#8211;layer-separate<br />
         separate layers for each curve and overlay<br />
location of referenced image:<br />
  -lx  &#8211;location-none<br />
         image reference without location (default)<br />
  -ln  &#8211;location-network  [a]etitle: string<br />
         image located at application entity a<br />
  -lm  &#8211;location-media  [f]ilesetID, fileset[UID]: string<br />
         image located on storage medium</p>
<h3>output options</h3>
<pre><code>
output transfer syntax : +t = --write - xfer - same write with same TS as image file(default) + te-- write - xfer - little write with explicit VR little endian TS + tb-- write - xfer - big write with explicit VR big endian TS + ti-- write - xfer - implicit write with implicit VR little endian TS
</code></pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmpsmk</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
