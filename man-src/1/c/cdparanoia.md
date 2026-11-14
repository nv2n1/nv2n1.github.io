---
title: "cdparanoia(1)"
name: "cdparanoia"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdparanoia/"
description: "cdparanoia 10.2 (Paranoia release III) – an audio CD reading utility which includes extra data verification features"
---

<h2>NAME</h2>
<p> cdparanoia 10.2 (Paranoia release III) &#8211; an audio CD reading utility which includes extra data verification features</p>
<h2>SYNOPSIS</h2>
<p> <code>cdparanoia</code> [<code>options</code>] <code>span </code> [<code>outfile</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>cdparanoia</code> retrieves audio tracks from CDDA capable CDROM drives. The data can be saved to a file or directed to standard output in WAV, AIFF, AIFF-C or raw format. Most ATAPI, SCSI and several proprietary CDROM drive makes are supported; <code>cdparanoia</code> can determine if the target drive is CDDA capable. </p>
<p> In addition to simple reading, <code>cdparanoia</code> adds extra-robust data verification, synchronization, error handling and scratch reconstruction capability.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A &#8211;analyze-drive</code></p>
<dd> Run and log a complete analysis of drive caching, timing and reading behavior; verifies that cdparanoia is correctly modelling a sprcific drive&#8217;s cache and read behavior. Implies -vQL. </p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Be absurdly verbose about the autosensing and reading process. Good for setup and debugging. </p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Do not print any progress or error information during the reading process. </p>
<dt><code>-e &#8211;stderr-progress</code></p>
<dd> Force output of progress information to stderr (for wrapper scripts). </p>
<dt><code>-l &#8211;log-summary [file]</code></p>
<dd> Save result summary to file, default filename cdparanoia.log. </p>
<dt><code>-L &#8211;log-debug [file]</code></p>
<dd> Save detailed device autosense and debugging output to a file, default filename cdparanoia.log. </p>
<dt><code>-V &#8211;version</code></p>
<dd> Print the program version and quit. </p>
<dt><code>-Q &#8211;query</code></p>
<dd> Perform CDROM drive autosense, query and print the CDROM table of contents, then quit. </p>
<dt><code>-s &#8211;search-for-drive</code></p>
<dd> Forces a complete search for a cdrom drive, even if the /dev/cdrom link exists. </p>
<dt><code>-h &#8211;help</code></p>
<dd> Print a brief synopsis of <code>cdparanoia </code> usage and options. </p>
<dt><code>-p &#8211;output-raw</code></p>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in host byte order. To force little or big endian byte order, use <code>-r </code> or <code>-R</code> as described below. </p>
<dt><code>-r &#8211;output-raw-little-endian</code></p>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in LSB first byte order. </p>
<dt><code>-R &#8211;output-raw-big-endian</code></p>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in MSB first byte order. </p>
<dt><code>-w &#8211;output-wav</code></p>
<dd> Output data in Micro$oft RIFF WAV format (note that WAV data is always LSB first byte order). </p>
<dt><code>-f &#8211;output-aiff</code></p>
<dd> Output data in Apple AIFF format (note that AIFC data is always in MSB first byte order). </p>
<dt><code>-a &#8211;output-aifc</code></p>
<dd> Output data in uncompressed Apple AIFF-C format (note that AIFF-C data is always in MSB first byte order). </p>
<dt><code>-B &#8211;batch </code></p>
<dd>
<p> Cdda2wav-style batch output flag; cdparanoia will split the output into multiple files at track boundaries. Output file names are prepended with &#8216;track#.&#8217; </p>
<dt><code>-c &#8211;force-cdrom-little-endian</code></p>
<dd> Some CDROM drives misreport their endianness (or do not report it at all); it&#8217;s possible that cdparanoia will guess wrong. Use <code>-c</code> to force cdparanoia to treat the drive as a little endian device. </p>
<dt><code>-C &#8211;force-cdrom-big-endian</code></p>
<dd> As above but force cdparanoia to treat the drive as a big endian device. </p>
<dt><code>-n &#8211;force-default-sectors </code><i>n</i></p>
<dd> Force the interface backend to do atomic reads of <code>n</code> sectors per read. This number can be misleading; the kernel will often split read requests into multiple atomic reads (the automated Paranoia code is aware of this) or allow reads only wihin a restricted size range. <code>This option should generally not be used.</code> </p>
<dt><code>-d &#8211;force-cdrom-device </code><i>device</i></p>
<dd> Force the interface backend to read from <code>device</code> rather than the first readable CDROM drive it finds. This can be used to specify devices of any valid interface type (ATAPI, SCSI or proprietary). </p>
<dt><code>-k &#8211;force-cooked-device </code><i>device</i></p>
<dd> This option forces use of the old &#8216;cooked ioctl&#8217; kernel interface with the specified cdrom device. The cooked ioctl interface is obsolete in Linux 2.6 if it is present at all. <code>-k </code> cannot be used with <code>-d </code> or <code>-g</code>. </p>
<dt><code>-g &#8211;force-generic-device </code><i>device</i></p>
<dd> This option forces use of the old &#8216;generic scsi&#8217; (sg) kernel interface with the specified generic scsi device. <code>-g </code> cannot be used with <code>-k</code>. <code>-g</code> may be used with <code>-d</code> to explicitly set both the SCSI cdrom and generic (sg) devices seperately. This option is only useful on obsolete SCSI setups and when using the generic scsi (sg) driver. </p>
<dt><code>-S &#8211;force-read-speed </code><i>number</i></p>
<dd> Use this option explicitly to set the read rate of the CD drive (where supported). This can reduce underruns on machines with slow disks, or which are low on memory. </p>
<dt><code>-t &#8211;toc-offset </code><i>number</i></p>
<dd> Use this option to force the entire disc LBA addressing to shift by the given amount; the value is added to the beginning offsets in the TOC. This can be used to shift track boundaries for the whole disc manually on sector granularity. The next option does something similar&#8230; </p>
<dt><code>-T &#8211;toc-bias </code></p>
<dd> Some drives (usually random Toshibas) report the actual track beginning offset values in the TOC, but then treat the beginning of track 1 index 1 as sector 0 for all read operations. This results in every track seeming to start too late (losing a bit of the beginning and catching a bit of the next track). <code>-T</code> accounts for this behavior. Note that this option will cause cdparanoia to attempt to read sectors before or past the known user data area of the disc, resulting in read errors at disc edges on most drives and possibly even hard lockups on some buggy hardware. </p>
<dt><code>-O &#8211;sample-offset </code><i>number</i></p>
<dd> Use this option to force the entire disc to shift sample position output by the given amount; This can be used to shift track boundaries for the whole disc manually on sample granularity. Note that this will cause cdparanoia to attempt to read partial sectors before or past the known user data area of the disc, probably causing read errors on most drives and possibly even hard lockups on some buggy hardware. </p>
<dt><code>-Z &#8211;disable-paranoia</code></p>
<dd> Disable <code>all</code> data verification and correction features. When using -Z, cdparanoia reads data exactly as would cdda2wav with an overlap setting of zero. This option implies that <code>-Y</code> is active. </p>
<dt><code>-z &#8211;never-skip[=max_retries]</code></p>
<dd> Do not accept any skips; retry forever if needed. An optional maximum number of retries can be specified; for comparison, default without -z is currently 20. </p>
<dt><code>-Y &#8211;disable-extra-paranoia</code></p>
<dd> Disables intra-read data verification; only overlap checking at read boundaries is performed. It can wedge if errors occur in the attempted overlap area. Not recommended. </p>
<dt><code>-X &#8211;abort-on-skip</code></p>
<dd> If the read skips due to imperfect data, a scratch, whatever, abort reading this track. If output is to a file, delete the partially completed file. </p>
</dl>
<h2>OUTPUT SMILIES</h2>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Normal operation, low/no jitter</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Normal operation, considerable jitter</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Read drift</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Unreported loss of streaming in atomic read operation</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>8-|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Finding read problems at same point during reread; hard to correct</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> SCSI/ATAPI transport error</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Scratch detected</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>;-(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Gave up trying to perform a correction</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>8-X</code></p>
<dd> Aborted read due to known, uncorrectable error</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:^D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Finished extracting </p>
</dl>
<h2>PROGRESS BAR SYMBOLS</h2>
<dl>
<dt><code>&lt;space&gt; </code></p>
<dd> No corrections needed</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Jitter correction required</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Unreported loss of streaming/other error in read</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>!&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Errors found after stage 1 correction; the drive is making the same error through multiple re-reads, and cdparanoia is having trouble detecting them.</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> SCSI/ATAPI transport error (corrected)</p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></p>
<dd> Uncorrected error/skip </p>
</dl>
<h2>SPAN ARGUMENT</h2>
<p> The span argument specifies which track, tracks or subsections of tracks to read. This argument is required. <code>NOTE:</code> Unless the span is a simple number, it&#8217;s generally a good idea to quote the span argument to protect it from the shell. </p>
<p> The span argument may be a simple track number or an offset/span specification. The syntax of an offset/span takes the rough form: </p>
<p> 1[ww:xx:yy.zz]-2[aa:bb:cc.dd] </p>
<p> Here, 1 and 2 are track numbers; the numbers in brackets provide a finer grained offset within a particular track. [aa:bb:cc.dd] is in hours/minutes/seconds/sectors format. Zero fields need not be specified: [::20], [:20], [20], [20.], etc, would be interpreted as twenty seconds, [10:] would be ten minutes, [.30] would be thirty sectors (75 sectors per second). </p>
<p> When only a single offset is supplied, it is interpreted as a starting offset and ripping will continue to the end of the track. If a single offset is preceeded or followed by a hyphen, the implicit missing offset is taken to be the start or end of the disc, respectively. Thus: </p>
<dl>
<dt><code>1:[20.35] </code></p>
<dd> Specifies ripping from track 1, second 20, sector 35 to the end of track 1.</p>
<dt><code>1:[20.35]- </code></p>
<dd> Specifies ripping from 1[20.35] to the end of the disc</p>
<dt><code>-2 </code></p>
<dd> Specifies ripping from the beginning of the disc up to (and including) track 2</p>
<dt><code>-2:[30.35] </code></p>
<dd> Specifies ripping from the beginning of the disc up to 2:[30.35]</p>
<dt><code>2-4 </code></p>
<dd> Specifies ripping from the beginning of track 2 to the end of track 4.</dl>
<p> Again, don&#8217;t forget to protect square brackets and preceeding hyphens from the shell. </p>
<h2>EXAMPLES</h2>
<p> A few examples, protected from the shell:</p>
<dl>
<dt>Query only with exhaustive search for a drive and full reporting of autosense:</p>
<dd></dl>
<p>&nbsp;<wbr>cdparanoia -vsQ</p>
<dl>
<dt>Extract an entire disc, putting each track in a seperate file:</p>
<dd></dl>
<p>&nbsp;<wbr>cdparanoia -B&nbsp;<wbr></p>
<dl>
<dt>Extract from track 1, time 0:30.12 to 1:10.00:</p>
<dd></dl>
<p>&nbsp;<wbr>cdparanoia&nbsp;<wbr>&quot;1[:30.12]-1[1:10]&quot;</p>
<dl>
<dt>Extract from the beginning of the disc up to track 3:</p>
<dd></dl>
<p>&nbsp;<wbr>cdparanoia &#8212;&nbsp;<wbr>&quot;-3&quot;</p>
<dl>
<dt>The &quot;&#8211;&quot; above is to distinguish &quot;-3&quot; from an option flag.</p>
<dd></dl>
<h2>OUTPUT</h2>
<p> The output file argument is optional; if it is not specified, cdparanoia will output samples to one of <code>cdda.wav</code>, <code>cdda.aifc</code>, or <code>cdda.raw</code> depending on whether <code>-w</code>, <code>-a</code>, <code>-r</code> or <code>-R</code> is used (<code>-w</code> is the implicit default). The output file argument of <code>&#8211;</code> specifies standard output; all data formats may be piped. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Cdparanoia sprang from and once drew heavily from the interface of Heiko Eissfeldt&#8217;s (heiko [at] colossus.escape.de) &#8216;cdda2wav&#8217; package. Cdparanoia would not have happened without it. </p>
<p> Joerg Schilling has also contributed SCSI expertise through his generic SCSI transport library. </p>
<h2>AUTHOR</h2>
<p> Monty &lt;monty [at] xiph.org&gt; </p>
<p> Cdparanoia&#8217;s homepage may be found at: <a rel="nofollow" href="http://www.xiph.org/paranoia/">http://www.xiph.org/paranoia/</a> </p>
<h2>Index</h2>
