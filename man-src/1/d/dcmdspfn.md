---
title: "dcmdspfn(1)"
name: "dcmdspfn"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmdspfn/"
description: "dcmdspfn – Export standard display curves to a text file"
---

<h2 class="name">NAME</h2>
<p> dcmdspfn &#8211; Export standard display curves to a text file </p>
<h2>SYNOPSIS</h2>
<pre>
dcmdspfn [options]
</pre>
<h2>DESCRIPTION</h2>
<p> Command line program converts a DCMTK monitor / camera / printer / scanner characteristics file to tabbed text file describing the characteristic curve (CC), the display function and the post-standardized curve (PSC) for an 8 bit display. The 256 values of each curve can be visualized by a common spread sheet program. Above that the display curve (without CC and PSC) can also be computed for a specified luminance/OD range (min/max) and a certain number of Device Driving Levels (DDL).</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM input filename to be dumped
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
<p>+ Im&#8211; monitor &#8211; file[f] ilename:string<br />
                                     text file describing the monitor characteristics +<br />
                                 Ic&#8211; camera &#8211; file[f]<br />
                         ilename:string<br />
                                     text file describing the camera characteristics +<br />
                                 Ip&#8211; printer &#8211; file[f]<br />
                         ilename:string<br />
                                     text file describing the printer characteristics +<br />
                                 Is&#8211; scanner &#8211; file[f]<br />
                         ilename:string<br />
                                     text file describing the scanner characteristics +<br />
                                 Il&#8211; lum &#8211; range[m] in<br />
                             max:float<br />
                                     minimum and maximum<br />
                                     luminance(cd / m ^ 2) +<br />
                                 Io&#8211; od &#8211; range[m] in<br />
                             max:float minimum and maximum optical density(OD),<br />
                                 automatically converted to luminance</p>
<h3>creation options</h3>
<p>+ Ca&#8211; ambient &#8211; light[a] mbient light:float<br />
                                           ambient light<br />
                                           value(cd / m ^ 2, default:file f) +<br />
                                       Ci&#8211; illumination[i]<br />
                           llumination:float illumination value(cd / m ^ 2, default:file f) + Dn&#8211; min &#8211; density[m] inimum optical<br />
                               density:float Dmin value(default:off, only with + Ip and +Io) + Dx&#8211; max &#8211; density[m] aximum optical<br />
                               density:float Dmax value(default:off, only with + Ip and +Io) + Cd&#8211; ddl &#8211; count[n] umber of<br />
                                  DDLs:integer<br />
                                       number of Device Driving Levels(default:256, only with&#8211; lum / od &#8211; range) +<br />
                                       Cf&#8211; curve &#8211; fitting[n]<br />
                                 umber:integer<br />
    use polynomial curve fitting algorithm with order n(0..99, default:file setting or cubic spline)</p>
<h3>output options</h3>
<pre><code>
+ Og-- gsdf[f] ilename:string
                           write GSDF curve data to file f +
                       Oc-- cielab[f]
               ilename:string
                           write CIELAB curve data to file f
</code></pre>
<h2>NOTES</h2>
<p> The output file describing the CC, GSDF or CIELAB and PSC for an 8 bit display system (monitor, camera, printer or scanner) is a simple text file. Lines starting with a &#8216;#&#8217; are treated as comments and, therefore, skipped as well as blank lines. An input file can for instance be created by the command line tool <code>dconvlum</code>. </p>
<p> The ambient light value possibly defined in the characteristics file is also used for the calculation. In this case the value is part of the file comment header as well as the number of DDL (device driving level) values, the absolute luminance range (measured in candela per square meter) and the range of the JND index (just noticable difference) in case of GSDF. Alternatively, the ambient light value can be specified as a command line option. When setting the two luminance values instead of reading a monitor characteristic file as input the luminance range is linearly divided by the number of DDLs. </p>
<p> For printers and scanners the illumination can be specified in addition to the reflected ambient light (both in the characteristics file and on the command line). The header of the output file includes the minimum and maximum Optical Density (OD) instead of the luminance range. Please note that the OD values in the input file have to be ordered in descending order (in contrast to the luminance values used for monitors and cameras). The DDL value 0 always means black (darkest value) and the maximum DDL value means white (brightest value, clear film). </p>
<p> The <i>data</i> folder contains sample characteristics file for monitors, cameras, printers and scanners. See DICOM standard part 14 for more details on display calibration and Barten&#8217;s model (including GSDF).</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/camera.lut</i> &#8211; sample characteristics file of a camera<br />
 <i>&lt;datadir&gt;/monitor.lut</i> &#8211; sample characteristics file of a monitor<br />
 <i>&lt;datadir&gt;/printer.lut</i> &#8211; sample characteristics file of a printer<br />
 <i>&lt;datadir&gt;/scanner.lut</i> &#8211; sample characteristics file of a scanner</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dconvlum/">dconvlum</a></code>(1), <code><a href="/docs/linux/man/1-dcod2lum/">dcod2lum</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
