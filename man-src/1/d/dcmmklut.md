---
title: "dcmmklut(1)"
name: "dcmmklut"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmmklut/"
description: "dcmmklut – Create DICOM look-up tables"
---

<h2 class="name">NAME</h2>
<p> dcmmklut &#8211; Create DICOM look-up tables </p>
<h2>SYNOPSIS</h2>
<pre>
dcmmklut [options] dcmimg-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmmklut</code> utility allows to create a variety of DICOM Modality, Presentation and VOI look-up tables (LUT) and is intended for the creation of test images. The utility is able to read an existing DICOM image file, create a look up table according to the command line options, and write the new object back to file. It is also possible to create a new object containing the specified LUT without reading an existing DICOM image file. This is e.g. useful to simply store different look-up tables in a DICOM-like structure. As a default the output file is encoded with the same transfer syntax used for the input file, but the transfer syntax can also be specified as a command line option. </p>
<p> The LUT data can be derived from the shape of a gamma curve (default for the gamma factor is 1) or imported from a file (currently the MAP format from Ulead&#8217;s PhotoImpact and a simple text format are supported). The input and output width of the LUT can also be specified in the range allowed by the DICOM standard. The interpolation of the input range is done by a polynomial curve fitting algorithm. </p>
<p> In addition to the DICOM output file the LUT data can also be exported to a tabbed text file which allows the easy visualization of the curves with a common spread sheet application (e.g. Microsoft Excel).</p>
<h2>PARAMETERS</h2>
<pre>
dcmimg-out  DICOM output filename
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
<h3>LUT creation options</h3>
<p>LUT type:<br />
  +Tm  &#8211;modality<br />
         create as Modality LUT<br />
  +Tp  &#8211;presentation<br />
         create as Presentation LUT<br />
  +Tv  &#8211;voi<br />
         create as VOI LUT (default)<br />
LUT placement:<br />
  +Pa  &#8211;add<br />
         add to existing transform<br />
         (default for and only with &#8211;voi)<br />
  +Pr  &#8211;replace<br />
         replace existing transform<br />
         (default for &#8211;modality and &#8211;presentation)<br />
LUT content:<br />
  +Cg  &#8211;gamma  [g]amma: float<br />
         use gamma value (default: 1.0)<br />
  +Cm  &#8211;map-file  [f]ilename: string<br />
         read input data from MAP file<br />
  +Ct  &#8211;text-file  [f]ilename: string<br />
         read input data from text file<br />
LUT options:<br />
  +Og  &#8211;inverse-gsdf<br />
         apply inverse GSDF (print presentation LUT in OD)<br />
       &#8211;min-density  [v]alue: integer (0..65535, default: 20)<br />
         set min density to v (in hundreds of OD)<br />
       &#8211;max-density  [v]alue: integer (0..65535, default: 300)<br />
         set max density to v (in hundreds of OD)<br />
  +Oi  &#8211;illumination  [v]alue: integer (0..65535, default: 2000)<br />
         set illumination to v (in cd/m^2)<br />
  +Or  &#8211;reflection  [v]alue: integer (0..65535, default: 10)<br />
         set reflected ambient light to v (in cd/m^2)<br />
LUT structure:<br />
  -b   &#8211;bits  [n]umber: integer<br />
         create LUT with n bit values (8..16, default: 16)<br />
  -e   &#8211;entries  [n]umber: integer<br />
         create LUT with n entries (1..65536, default: 256)<br />
  -f   &#8211;first-mapped  [n]umber: integer<br />
         first input value mapped (-31768..65535, default: 0)<br />
  -r   &#8211;random  [n]umber: unsigned integer<br />
         perform n randomly selected permutations on the LUT<br />
  -rs  &#8211;random-seed  [n]umber: unsigned integer<br />
         initialize the random-number generator with n<br />
         (default: 0, for reproducible results)<br />
  -o   &#8211;order  [n]umber: integer<br />
         use polynomial curve fitting algorithm with order n<br />
         (0..99, default: 5)<br />
  -E   &#8211;explanation  [n]ame: string<br />
         LUT explanation (default: automatically created)<br />
LUT data alignment:<br />
  -a   &#8211;byte-align<br />
         create byte-aligned LUT<br />
         (default for and only with 8 bit values)<br />
  +a   &#8211;word-align<br />
         create word-aligned LUT<br />
         (default for 9-16 bit values)<br />
LUT data VR:<br />
  +Dw  &#8211;data-ow<br />
         write LUT Data as OW (default)<br />
  +Du  &#8211;data-us<br />
         write LUT Data as US<br />
  +Ds  &#8211;data-ss<br />
         write LUT Data as SS (minimal support)</p>
<h3>file options</h3>
<pre><code>
+ Fi-- dicom - input[f] ilename:string
                                    read dataset from DICOM file f +
                                Fo-- text - output[f]
                        ilename:string
                                    write LUT data to tabbed text file f
</code></pre>
<h2>NOTES</h2>
<p> Please check the DICOM standard for further restrictions on the look-up table structure. Especially the number of bits per table entry might be restricted in particular IODs.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmmklut</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/philips.lut</i> &#8211; sample LUT in text format</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
