---
title: "lav2mpeg(1)"
name: "lav2mpeg"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lav2mpeg/"
description: "lav2mpeg – easy conversion of lav files to mpeg"
---

<h2>NAME</h2>
<p> lav2mpeg &#8211; easy conversion of lav files to mpeg</p>
<h2>SYNOPSIS</h2>
<p> <code>lav2mpeg [ options ]</code> <i>lavfile1 [lavfile2 &#8230; lavfileN]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>lav2mpeg</code> is a shell script to ease the use of the mjpeg utilities, providing a convenient way to convert from MJPEG files to popular MPEG file formats. It supports output in VCD, medium and high rate VCD, SVCD, high rate SVCD, and generic mpeg1 and mpeg2 </p>
<p> The input files may be any combination of AVI (.avi), Quicktime (.qt) or editlist files so long as they are all lavtools- readable (e.g. MJPEG-encoded AVI/Quicktime or DV type 2 AVI).</p>
<h2>OPTIONS</h2>
<dl>
<dt>-s/S</p>
<dd> Turn stereo off/on (default auto)</p>
<dt>-k/K</p>
<dd> Turn keeping of raw files off/on (default off)</p>
<dt>-f/F</p>
<dd> Turn use of fifos off/on (default off)</p>
<dt>-l/L</p>
<dd> Turn logging of entire process off/on (default off)</p>
<dt>-n/N</p>
<dd> Turn &quot;noisy logging&quot; off/on (default off)</p>
<dt>-y/Y</p>
<dd> Turn use of yuvdenoise off/on (default off)</p>
<dt>-m</p>
<dd> one of MODES (see below) (default vcd)</p>
<dt>-e</p>
<dd> encoding quality : 0, 1, or 2 (default 2)</p>
<dt>-o</p>
<dd> output file ( defaults to firstInputFileName.mpg )</p>
<dt>-b</p>
<dd> video bitrate in kbps ( only used when -o is &quot;mpeg1&quot; or &quot;mpeg2&quot; )</p>
<dt>-a</p>
<dd> audio bitrate in kpbs ( only used when -o is not &quot;vcd*&quot; )</p>
<dt>-q</p>
<dd> quality for mpeg2enc ( only used when -o is &quot;mpeg1&quot; or &quot;mpeg2&quot; )</p>
<dt>-d</p>
<dd> dimensions XxY ( only used when -o is &quot;mpeg1&quot; or &quot;mpeg2&quot; ) defaults to same as input</dl>
<h2>MODES</h2>
<p> <code>vcd</code> &#8212; standard VCD (352&#215;240 or 352&#215;288) </p>
<p> <code>vcd_medium</code> &#8212; 1550kbps video VCD (352&#215;240 or 352&#215;288) </p>
<p> <code>vcd_high</code> &#8212; 1800kbps video VCD (352&#215;240 or 352&#215;288) </p>
<p> <code>svcd</code> &#8212; standard SVCD (480&#215;480 or 480&#215;576) </p>
<p> <code>svcd_high</code> &#8212; 3000kbps(max) vbr @qual=5 (480&#215;480 or 480&#215;576) </p>
<p> <code>mpeg1</code> &#8212; honor -a -b -q -d flags default resolution same as input </p>
<p> <code>mpeg2</code> &#8212; honor -a -b -q -d flags default resolution same as input </p>
<h2>FILES</h2>
<p> <i>~/.lav2mpegrc</i></p>
<dl>
<dt>
<dd> user configuration file. It is bash sourceable, and can modify any of the environment variables mentioned in the ENVIRONMENT section, or set the LAV2MPEG_OPTIONS variable to add default options.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>NICEVAL</p>
<dd> the nice value of each command, set using &#8216;nice -n command&#8217;</p>
<dt>YUVSCALER</p>
<dd> modify which command is called for yuvscaler</p>
<dt>LAV2WAV</p>
<dd> modify which command is called for lav2wav</p>
<dt>MPLEX</p>
<dd> modify which command is called for mplex</p>
<dt>YUVDENOISE</p>
<dd> modify which command is called for yuvdenoise</p>
<dt>MPEG2ENC</p>
<dd> modify which command is called for mpeg2enC</p>
<dt>AUDIOENC</p>
<dd> audioenc is similar to those above, however, if it is set to &#8216;mp2enc&#8217; it will use mp2enc rather than toolame, and set flags appropriotely.</p>
<dt>NOISYLOGFILE</p>
<dd> set the file used for noisy logging (-N) defaults to outputfile.log</p>
<dt>QUIETLOG</p>
<dd> set the file used for quiet logging. defaults to lav2mpeg.log if set to &quot;&quot; it will log only to screen</p>
<dt>LOGDATE</p>
<dd> defaults to 1, set to 0 to not have the date logged in log or output (see man date for more info)</p>
<dt>LOGDATESTR</p>
<dd> will pass this on to &#8216;date&#8217; to describe what time format to use. Only used if LOGDATE is not 0</p>
<dt>LOGCOMMANDS</p>
<dd> if set to non-zero, will log to the quite log the commands used. Commands are always logged to NOISYLOGFILE if used</p>
<dt>LOGONLY</p>
<dd> if set to non-zero, will only log the commands it would use but not actually run any commands</p>
<dt>LAV2MPEGRC</p>
<dd> the lav2mpegrc file. Only beneficial if set from environment variable.</p>
<dt>VCD_MEDIUM_BR</p>
<dd> video bitrate for mode=vcd_medium</p>
<dt>VCD_HIGH_BR</p>
<dd> video bitrate for mode=vcd_high</p>
<dt>SVCD_HIGH_BR</p>
<dd> video bitrate for mode=svcd_high</p>
<dt>SVCD_HIGH_QUAL</p>
<dd> quality used (-q 0-30 to mpeg2enc) for SVCD_HIGH</p>
<dt>SVCD_HIGH_BUFFSIZE</p>
<dd> buffsize (-V to mpeg2enc) used for svcd_high defaults to 100</p>
<dt>EXTRA_LAV2YUV</p>
<dd> set extra command line arguments to lav2yuv, which will be added on the end</p>
<dt>EXTRA_YUVSCALER</p>
<dd> set extra command line arguments to yuvscaler, which will be added on the end</p>
<dt>EXTRA_MPEG2ENC</p>
<dd> set extra command line arguments to mpeg2enc, which will be added on the end</p>
<dt>EXTRA_LAV2WAV</p>
<dd> set extra command line arguments to lav2wav, which will be added on the end</p>
<dt>EXTRA_AUDIOENC</p>
<dd> set extra command line arguments to mp2enc or toolame (depending on AUDIOENC), which will be added on the end</p>
<dt>EXTRA_MPLEX</p>
<dd> set extra command line arguments to mplex, which will be added on the end</p>
<dt>EXTRA_YUVDENOISE</p>
<dd> set extra command line arguments to yuvdenoise, which will be added on the end</dl>
<h2>DIAGNOSTICS</h2>
<p> To simply see the commands that lav2mpeg would have called, run &#8216;LOGONLY=1 lav2mpeg &#8230;&#8217;</p>
<h2>BUGS</h2>
<p> Possibly. Please let the author know.</p>
<h2>AUTHOR</h2>
<p> Scott Moser &lt;smoser at brickies dot net&gt;</p>
<h2>EXAMPLES</h2>
<pre>
create a VCD compliant mpeg regardless of input named file.mpg
<code>lav2mpeg file.avi
</code>
create a SVCD high rate mpeg from input named out.mpg
<code>lav2mpeg -o out.mpg -m svcd_high file.avi
</code>
use lav2yuv.new for instead of lav2yuv, and add the '-M MMX' flag to
yuvscaler:
<code>LAV2YUV=&quot;lav2yuv.new&quot; EXTRA_YUVSCALER=&quot;-M MMX&quot; lav2mpeg file.avi
</code>
Please read other examples included in documentation for .lav2mpegrc 
usage
</pre>
<h2>Index</h2>
