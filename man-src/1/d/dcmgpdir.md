---
title: "dcmgpdir(1)"
name: "dcmgpdir"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmgpdir/"
description: "dcmgpdir – Create a general purpose DICOMDIR"
---

<h2 class="name">NAME</h2>
<p> dcmgpdir &#8211; Create a general purpose DICOMDIR </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmgpdir[options][dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmgpdir</code> utility creates a <i>DICOMDIR</i> file from the specified referenced DICOM files according to the DICOM Part 11 Media Storage Application Profiles. </p>
<p> Currently, the following profiles are supported: </p>
<dl>
<dt>&bull;</p>
<dd> General Purpose CD-R Interchange (STD-GEN-CD)</p>
<dt>&bull;</p>
<dd> General Purpose Interchange on DVD-RAM Media (STD-GEN-DVD-RAM)</dl>
<p> <code>dcmmkdir</code> is an extended version of this tool which also supports other Media Storage Application Profiles than the general purpose one (e.g. both cardio profiles requiring the use of icon images).</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  referenced DICOM file
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
  -lc   &#8211;log-config  [f]ilename: string<br />
          use config file f for the logger</p>
<h3>input options</h3>
<p>DICOMDIR identifiers:<br />
  +D    &#8211;output-file  [f]ilename: string<br />
          generate specific DICOMDIR file<br />
          (default: DICOMDIR in current directory)<br />
  +F    &#8211;fileset-id  [i]d: string (default: DCMTK_MEDIA_DEMO)<br />
          use specific file set ID<br />
  +R    &#8211;descriptor  [f]ilename: string<br />
          add a file set descriptor file ID<br />
          (e.g. README, default: no descriptor)<br />
  +C    &#8211;char-set  [c]harset: string<br />
          add a specific character set for descriptor<br />
          (default: &#8220;ISO_IR 100&#8221; if descriptor present)<br />
reading:<br />
  +id   &#8211;input-directory  [d]irectory: string<br />
          read referenced DICOM files from directory d<br />
          (default for &#8211;recurse: current directory)<br />
  -m    &#8211;keep-filenames<br />
          expect filenames to be in DICOM format (default)<br />
  +m    &#8211;map-filenames<br />
          map to DICOM filenames (lowercase-&gt;uppercase,<br />
          and remove trailing period)<br />
  -r    &#8211;no-recurse<br />
          do not recurse within directories (default)<br />
  +r    &#8211;recurse<br />
          recurse within filesystem directories<br />
  +p    &#8211;pattern  [p]attern: string (only with &#8211;recurse)<br />
          pattern for filename matching (wildcards)<br />
#possibly not available on all systems</p>
<h3>processing options</h3>
<p>consistency check:<br />
  -W    &#8211;no-consistency-check<br />
          do not check files for consistency<br />
  +W    &#8211;warn-inconsist-files<br />
          warn about inconsistent files (default)<br />
  -a    &#8211;abort-inconsist-file<br />
          abort on first inconsistent file<br />
type 1 attributes:<br />
  -I    &#8211;strict<br />
          exit with error if DICOMDIR type 1 attributes<br />
          are missing in DICOM file (default)<br />
  +I    &#8211;invent<br />
          invent DICOMDIR type 1 attributes if missing in DICOM file<br />
  +Ipi  &#8211;invent-patient-id<br />
          invent new PatientID in case of inconsistent<br />
          PatientName attributes<br />
other checks:<br />
  +Nrs  &#8211;allow-retired-sop<br />
          allow retired SOP classes defined in previous editions<br />
          of the DICOM standard<br />
  -Nxc  &#8211;no-xfer-check<br />
          do not reject images with non-standard transfer syntax<br />
          (just warn)</p>
<h3>output options</h3>
<pre><code>
writing:
  -A    --replace
          replace existing DICOMDIR (default)
  +A    --append
          append to existing DICOMDIR
  +U    --update
          update existing DICOMDIR
  -w    --discard
          do not write out DICOMDIR
  -nb   --no-backup
          do not create a backup of existing DICOMDIR
post-1993 value representations:
  +u    --enable-new-vr
          enable support for new VRs (UN/UT) (default)
  -u    --disable-new-vr
          disable support for new VRs, convert to OB
group length encoding:
  -g    --group-length-remove
          write without group length elements (default)
  +g    --group-length-create
          write with group length elements
length encoding in sequences and items:
  +e    --length-explicit
          write with explicit lengths (default)
  -e    --length-undefined
          write with undefined lengths
</code></pre>
<h2>NOTES</h2>
<p> All files specified on the command line (or discovered by recursivly examining the contents of directories with the <i>+r</i> option) are first evaluated for their compatibility with the General Purpose CD-R Image Interchange Profile (Supplement 19). Only appropriate files encoded using the Explicit VR Little Endian Uncompressed Transfer Syntax will be accepted. Files having invalid filenames will be rejected (the rules can be relaxed via the <i>+m</i> option). Files missing required attributes will be rejected (the <i>+I</i> option can relax this behaviour). </p>
<p> A <i>DICOMDIR</i> file will only be constructed if all files have passed initial tests. </p>
<p> The <code>dcmgpdir</code> utility also allows to append new entries to and to update existing entries in a <i>DICOMDIR</i> file. Using option <i>+A</i> new entries are only appended to the DICOMDIR, i.e. existing records like the ones for PATIENT information are not updated. Using option <i>+U</i> also existing records are updated according to the information found in the referenced DICOM files. Please note that this update process might be slower than just appending new entries. However, it makes sure that additional information that is required for the selected application profile is also added to existing records.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmgpdir</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmmkdir/">dcmmkdir</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1996-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
