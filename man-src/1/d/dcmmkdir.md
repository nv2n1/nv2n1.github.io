---
title: "dcmmkdir(1)"
name: "dcmmkdir"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmmkdir/"
description: "dcmmkdir – Create a DICOMDIR file"
---

<h2 class="name">NAME</h2>
<p> dcmmkdir &#8211; Create a DICOMDIR file </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmmkdir[options][dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmmkdir</code> utility creates a <i>DICOMDIR</i> file from the specified referenced DICOM files according to the DICOM Part 11 Media Storage Application Profiles. </p>
<p> Currently the following profiles are supported (others might be added later): </p>
<dl>
<dt>&bull;</p>
<dd> General Purpose CD-R Interchange (STD-GEN-CD)</p>
<dt>&bull;</p>
<dd> General Purpose Interchange on DVD-RAM Media (STD-GEN-DVD-RAM)</p>
<dt>&bull;</p>
<dd> General Purpose DVD with Compression Interchange (STD-GEN-DVD-JPEG/J2K)</p>
<dt>&bull;</p>
<dd> General Purpose MIME Interchange (STD-GEN-MIME)</p>
<dt>&bull;</p>
<dd> General Purpose USB and Flash Memory with Compression Interchange (STD-GEN-USB/MMC/CF/SD-JPEG/J2K)</p>
<dt>&bull;</p>
<dd> DVD Interchange with MPEG2 MP@ML (STD-DVD-MPEG2-MPML)</p>
<dt>&bull;</p>
<dd> Basic Cardiac X-Ray Angiographic Studies on CD-R Media (STD-XABC-CD)</p>
<dt>&bull;</p>
<dd> 1024 X-Ray Angiographic Studies on CD-R Media (STD-XA1K-CD)</p>
<dt>&bull;</p>
<dd> 1024 X-Ray Angiographic Studies on DVD Media (STD-XA1K-DVD)</p>
<dt>&bull;</p>
<dd> Dental Radiograph Interchange (STD-DEN-CD)</p>
<dt>&bull;</p>
<dd> CT/MR Studies on various Media (STD-CTMR-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single Frame for Image Display (STD-US-ID-SF-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single Frame with Spatial Calibration (STD-US-SC-SF-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single Frame with Combined Calibration (STD-US-CC-SF-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single &amp; Multi-Frame for Image Display (STD-US-ID-MF-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single &amp; Multi-Frame with Spatial Calibration (STD-US-SC-MF-xxxx)</p>
<dt>&bull;</p>
<dd> Ultrasound Single &amp; Multi-Frame with Combined Calibration (STD-US-CC-MF-xxxx)</p>
<dt>&bull;</p>
<dd> 12-lead ECG Interchange on Diskette (STD-WVFM-ECG-FD)</p>
<dt>&bull;</p>
<dd> Hemodynamic Waveform Interchange on Diskette (STD-WVFM-HD-FD)</dl>
<p> This tool extends <code>dcmgpdir</code> which can only create General Purpose <i>DICOMDIR</i> files. The default behaviour of <code>dcmmkdir</code> (with <i>&#8211;general-purpose</i>) is equivalent to that of <code>dcmgpdir</code>.</p>
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
          (just warn)<br />
  -Nec  &#8211;no-encoding-check<br />
          do not reject images with non-standard pixel encoding<br />
          (just warn)<br />
  -Nrc  &#8211;no-resolution-check<br />
          do not reject images with non-standard spatial resolution<br />
          (just warn)<br />
icon images:<br />
  +X    &#8211;add-icon-image<br />
          add monochrome icon image on IMAGE level<br />
          (default for cardiac profiles)<br />
  -Xs   &#8211;icon-image-size  [s]ize: integer (1..128)<br />
          width and height of the icon image (in pixel)<br />
          (fixed: 128 for XA, 64 for CT/MR profile)<br />
  -Xi   &#8211;icon-file-prefix  [p]refix: string<br />
          use PGM image &#8216;prefix&#8217;+&#8217;dcmfile-in&#8217; as icon<br />
          (default: create icon from DICOM image)<br />
  -Xd   &#8211;default-icon  [f]ilename: string<br />
          use specified PGM image if icon cannot be<br />
          created automatically (default: black image)</p>
<h3>output options</h3>
<pre><code>
profiles:
  -Pgp  --general-purpose
          General Purpose Interchange on CD-R or
          DVD-RAM Media (STD-GEN-CD/DVD-RAM, default)
  -Pdv  --general-purpose-dvd
          General Purpose DVD with Compression Interchange
          (STD-GEN-DVD-JPEG/J2K)
  -Pmi  --general-purpose-mime
          General Purpose MIME Interchange (STD-GEN-MIME)
  -Pfl  --usb-and-flash
          General Purpose USB/Flash Memory with Compression
          Interchange (STD-GEN-USB/MMC/CF/SD-JPEG/J2K)
  -Pmp  --mpeg2-mpml-dvd
          DVD Interchange with MPEG2 Main Profile @ Main
          Level (STD-DVD-MPEG2-MPML)
  -Pbc  --basic-cardiac
          Basic Cardiac X-Ray Angiographic Studies on
          CD-R Media (STD-XABC-CD)
  -Pxa  --xray-angiographic
          1024 X-Ray Angiographic Studies on CD-R Media
          (STD-XA1K-CD)
  -Pxd  --xray-angiographic-dvd
          1024 X-Ray Angiographic Studies on DVD Media
          (STD-XA1K-DVD)
  -Pde  --dental-radiograph
          Dental Radiograph Interchange (STD-DEN-CD)
  -Pcm  --ct-and-mr
          CT/MR Studies (STD-CTMR-xxxx)
  -Pus  --ultrasound-id-sf
          Ultrasound Single Frame for Image Display
          (STD-US-ID-SF-xxxx)
        --ultrasound-sc-sf
          Ultrasound Single Frame with Spatial
          Calibration (STD-US-SC-SF-xxxx)
        --ultrasound-cc-sf
          Ultrasound Single Frame with Combined
          Calibration (STD-US-CC-SF-xxxx)
  -Pum  --ultrasound-id-mf
          Ultrasound Single &amp; Multi-Frame for Image
          Display (STD-US-ID-MF-xxxx)
        --ultrasound-sc-mf
          Ultrasound Single &amp; Multi-Frame with Spatial
          Calibration (STD-UD-SC-MF-xxxx)
        --ultrasound-cc-mf
          Ultrasound Single &amp; Multi-Frame with Combined
          Calibration (STD-UD-CC-MF-xxxx)
  -Pec  --12-lead-ecg
          12-lead ECG Interchange on Diskette
          (STD-WVFM-ECG-FD)
  -Phd  --hemodynamic-waveform
          Hemodynamic Waveform Interchange on Diskette
          (STD-WVFM-HD-FD)
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
<p> All files specified on the command line (or discovered by recursivly examining the contents of directories with the <i>+r</i> option) are first evaluated for their compatibility with the specified Media Storage Application Profile (Part 11). Only appropriate files encoded using one of the allowed Transfer Syntaxes will be accepted. Files having invalid filenames will be rejected (the rules can be relaxed via the <i>+m</i> option). Files missing required attributes will be rejected (the <i>+I</i> option can relax this behaviour). </p>
<p> A <i>DICOMDIR</i> file will only be constructed if all files have passed initial tests. </p>
<p> The <code>dcmmkdir</code> utility also allows to append new entries to and to update existing entries in a <i>DICOMDIR</i> file. Using option <i>+A</i> new entries are only appended to the DICOMDIR, i.e. existing records like the ones for PATIENT information are not updated. Using option <i>+U</i> also existing records are updated according to the information found in the referenced DICOM files. Please note that this update process might be slower than just appending new entries. However, it makes sure that additional information that is required for the selected application profile is also added to existing records. </p>
<p> The support for icon images is currently restricted to monochrome images. This might change in the future. Till then, color images are automatically converted to grayscale mode. The icon size is 128*128 pixels for the cardiac profiles (as required by the DICOM standard) and 64*64 for all others.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmmkdir</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmgpdir/">dcmgpdir</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
