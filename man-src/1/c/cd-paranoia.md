---

title: "cd-paranoia(1)"
name: "cd-paranoia"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-paranoia/"
description: "cd-paranoia – 9.8 (Paranoia release III via libcdio) – an audio CD reading utility which includes extra data verification features"
---

<h2>NAME</h2>
<p> cd-paranoia &#8211; 9.8 (Paranoia release III via libcdio) &#8211; an audio CD reading utility which includes extra data verification features</p>
<p> <code>cd-paranoia</code> [<code>options</code>] <code>span </code> [<code>outfile</code>]</p>
<p> <code>cd-paranoia</code> retrieves audio tracks from CDDA capable CD-ROM drives. The data can be saved to a file or directed to standard output in WAV, AIFF, AIFF-C or raw format. Most ATAPI, SCSI and several proprietary CD-ROM drive makes are supported; <code>cd-paranoia</code> can determine if the target drive is CDDA capable. </p>
<p> In addition to simple reading, <code>cd-paranoia</code> adds extra-robust data verification, synchronization, error handling and scratch reconstruction capability. </p>
<p> This version uses the libcdio library for interaction with a CD-ROM drive. The jitter and error correction however are the same as used in Xiph&#8217;s cdparanoia.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v &#8211;verbose</code></dt>
<dd> Be absurdly verbose about the autosensing and reading process. Good for setup and debugging. </dd>
<dt><code>-q &#8211;quiet</code></dt>
<dd> Do not print any progress or error information during the reading process. </dd>
<dt><code>-e &#8211;stderr-progress</code></dt>
<dd> Force output of progress information to stderr (for wrapper scripts). </dd>
<dt><code>-V &#8211;version</code></dt>
<dd> Print the program version and quit. </dd>
<dt><code>-Q &#8211;query</code></dt>
<dd> Perform CD-ROM drive autosense, query and print the CD-ROM table of contents, then quit. </dd>
<dt><code>-s &#8211;search-for-drive</code></dt>
<dd> Forces a complete search for a cdrom drive, even if the /dev/cdrom link exists. </dd>
<dt><code>-h &#8211;help</code></dt>
<dd> Print a brief synopsis of <code>cd-paranoia </code> usage and options. </dd>
<dt><code>-l &#8211;log-summary </code><i>file</i></dt>
<dd> Save result summary to file. </dd>
<dt><code>-p &#8211;output-raw</code></dt>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in host byte order. To force little or big endian byte order, use <code>-r </code> or <code>-R</code> as described below. </dd>
<dt><code>-r &#8211;output-raw-little-endian</code></dt>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in LSB first byte order. </dd>
<dt><code>-R &#8211;output-raw-big-endian</code></dt>
<dd> Output headerless data as raw 16 bit PCM data with interleaved samples in MSB first byte order. </dd>
<dt><code>-w &#8211;output-wav</code></dt>
<dd> Output data in Micro$oft RIFF WAV format (note that WAV data is always LSB first byte order). </dd>
<dt><code>-f &#8211;output-aiff</code></dt>
<dd> Output data in Apple AIFF format (note that AIFC data is always in MSB first byte order). </dd>
<dt><code>-a &#8211;output-aifc</code></dt>
<dd> Output data in uncompressed Apple AIFF-C format (note that AIFF-C data is always in MSB first byte order). </dd>
<dt><code>-B &#8211;batch </code></dt>
<dd>
<p> Cdda2wav-style batch output flag; cd-paranoia will split the output into multiple files at track boundaries. Output file names are prepended with &#8216;track#.&#8217; </p>
</dd><dt><code>-c &#8211;force-cdrom-little-endian</code></dt>
<dd> Some CD-ROM drives misreport their endianness (or do not report it at all); it&#8217;s possible that cd-paranoia will guess wrong. Use <code>-c</code> to force cd-paranoia to treat the drive as a little endian device. </dd>
<dt><code>-C &#8211;force-cdrom-big-endian</code></dt>
<dd> As above but force cd-paranoia to treat the drive as a big endian device. </dd>
<dt><code>-n &#8211;force-default-sectors </code><i>n</i></dt>
<dd> Force the interface backend to do atomic reads of <code>n</code> sectors per read. This number can be misleading; the kernel will often split read requests into multiple atomic reads (the automated Paranoia code is aware of this) or allow reads only wihin a restricted size range. <code>This option should generally not be used.</code> </dd>
<dt><code>-d &#8211;force-cdrom-device </code><i>device</i></dt>
<dd> Force the interface backend to read from <code>device</code> rather than the first readable CD-ROM drive it finds containing a CD-DA disc. This can be used to specify devices of any valid interface type (ATAPI, SCSI or proprietary). </dd>
<dt><code>-g &#8211;force-generic-device </code><i>device</i></dt>
<dd> This option is an alias for <code>-d</code> and is retained for compatibility. </dd>
<dt><code>-S &#8211;force-read-speed </code><i>number</i></dt>
<dd> Use this option explicitly to set the read rate of the CD drive (where supported). This can reduce underruns on machines with slow disks, or which are low on memory. </dd>
<dt><code>-t &#8211;toc-offset </code><i>number</i></dt>
<dd> Use this option to force the entire disc LBA addressing to shift by the given amount; the value is added to the beginning offsets in the TOC. This can be used to shift track boundaries for the whole disc manually on sector granularity. The next option does something similar&#8230; </dd>
<dt><code>-T &#8211;toc-bias </code></dt>
<dd> Some drives (usually random Toshibas) report the actual track beginning offset values in the TOC, but then treat the beginning of track 1 index 1 as sector 0 for all read operations. This results in every track seeming to start too late (losing a bit of the beginning and catching a bit of the next track). -T accounts for this behavior. Note that this option will cause cd-paranoia to attempt to read sectors before or past the known user data area of the disc, resulting in read errors at disc edges on most drives and possibly even hard lockups on some buggy hardware. </dd>
<dt><code>-O &#8211;sample-offset </code><i>number</i></dt>
<dd> Some CD-ROM/CD-R drives will add an offset to the position on reading audio data. This is usually around 500-700 audio samples (ca. 1/75 second) on reading. So when cd-paranoia queries a specific sector, it might not receive exactly that sector, but shifted by some amount.</dd></dl>
<p> Use this option to force the entire disc to shift sample position output by the given amount; This can be used to shift track boundaries for the whole disc manually on sample granularity. Note that if you are ripping something including the ending of the CD (e.g. the entire disk), this option will cause cd-paranoia to attempt to read partial sectors before or past the known user data area, probably causing read errors on most drives and possibly even hard lockups on some buggy hardware. </p>
<dl>
<dt><code>-Z &#8211;disable-paranoia</code></dt>
<dd> Disable <code>all</code> data verification and correction features. When using -Z, cd-paranoia reads data exactly as would cdda2wav with an overlap setting of zero. This option implies that <code>-Y</code> is active. </dd>
<dt><code>-z &#8211;never-skip[=max_retries]</code></dt>
<dd> Do not accept any skips; retry forever if needed. An optional maximum number of retries can be specified; for comparison, default without -z is currently 20. </dd>
<dt><code>-Y &#8211;disable-extra-paranoia</code></dt>
<dd> Disables intra-read data verification; only overlap checking at read boundaries is performed. It can wedge if errors occur in the attempted overlap area. Not recommended. </dd>
<dt><code>-X &#8211;abort-on-skip</code></dt>
<dd> If the read skips due to imperfect data, a scratch, whatever, abort reading this track. If output is to a file, delete the partially completed file. </dd>
<dt><code>-x &#8211;test-flags mask</code></dt>
<dd> Simulate CD-reading errors. This is used in regression testing, but other uses might be to see how well a CD-ROM performs under (simulated) CD degradation. mask specifies the artificial kinds of errors to introduced; &quot;or&quot;-ing values from the selection below will simulate the kind of specified failure.</dd></dl>
<p>&nbsp;<wbr>&nbsp;<wbr>0x10&nbsp;<wbr>&nbsp;<wbr>&#8211; Simulate under-run reading</p>
<dl>
</dl>
<h2>OUTPUT SMILIES</h2>
<dl>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Normal operation, low/no jitter</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Normal operation, considerable jitter</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Read drift</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Unreported loss of streaming in atomic read operation</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>8-|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Finding read problems at same point during reread; hard to correct</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> SCSI/ATAPI transport error</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:-(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Scratch detected</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>;-(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Gave up trying to perform a correction</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>8-X</code></dt>
<dd> Aborted read due to known, uncorrectable error</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>:^D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Finished extracting </dd>
</dl>
<h2>PROGRESS BAR SYMBOLS</h2>
<dl>
<dt><code>&lt;space&gt; </code></dt>
<dd> No corrections needed</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Jitter correction required</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Unreported loss of streaming/other error in read</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>!&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Errors found after stage 1 correction; the drive is making the same error through multiple re-reads, and cd-paranoia is having trouble detecting them.</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> SCSI/ATAPI transport error (corrected)</dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code></dt>
<dd> Uncorrected error/skip </dd>
</dl>
<h2>SPAN ARGUMENT</h2>
<p> The span argument specifies which track, tracks or subsections of tracks to read. This argument is required. <code>NOTE:</code> Unless the span is a simple number, it&#8217;s generally a good idea to quote the span argument to protect it from the shell. </p>
<p> The span argument may be a simple track number or an offset/span specification. The syntax of an offset/span takes the rough form: </p>
<p> 1[ww:xx:yy.zz]-2[aa:bb:cc.dd] </p>
<p> Here, 1 and 2 are track numbers; the numbers in brackets provide a finer grained offset within a particular track. [aa:bb:cc.dd] is in hours/minutes/seconds/sectors format. Zero fields need not be specified: [::20], [:20], [20], [20.], etc, would be interpreted as twenty seconds, [10:] would be ten minutes, [.30] would be thirty sectors (75 sectors per second). </p>
<p> When only a single offset is supplied, it is interpreted as a starting offset and ripping will continue to the end of the track. If a single offset is preceeded or followed by a hyphen, the implicit missing offset is taken to be the start or end of the disc, respectively. Thus: </p>
<dl>
<dt><code>1:[20.35] </code></dt>
<dd> Specifies ripping from track 1, second 20, sector 35 to the end of track 1.</dd>
<dt><code>1:[20.35]- </code></dt>
<dd> Specifies ripping from 1[20.35] to the end of the disc</dd>
<dt><code>-2 </code></dt>
<dd> Specifies ripping from the beginning of the disc up to (and including) track 2</dd>
<dt><code>-2:[30.35] </code></dt>
<dd> Specifies ripping from the beginning of the disc up to 2:[30.35]</dd>
<dt><code>2-4 </code></dt>
<dd> Specifies ripping from the beginning of track 2 to the end of track 4.</dd></dl>
<p> Again, don&#8217;t forget to protect square brackets and preceeding hyphens from the shell. </p>
<h2>EXAMPLES</h2>
<p> A few examples, protected from the shell:</p>
<dl>
<dt>Query only with exhaustive search for a drive and full reporting of autosense:</dt>
<dd></dd></dl>
<p>&nbsp;<wbr>cd-paranoia -vsQ</p>
<dl>
<dt>Extract an entire disc, putting each track in a seperate file:</dt>
<dd></dd></dl>
<p>&nbsp;<wbr>cd-paranoia -B&nbsp;<wbr></p>
<dl>
<dt>Extract from track 1, time 0:30.12 to 1:10.00:</dt>
<dd></dd></dl>
<p>&nbsp;<wbr>cd-paranoia&nbsp;<wbr>&quot;1[:30.12]-1[1:10]&quot;</p>
<dl>
<dt>Extract from the beginning of the disc up to track 3:</dt>
<dd></dd></dl>
<p>&nbsp;<wbr>cd-paranoia &#8212;&nbsp;<wbr>&quot;-3&quot;</p>
<dl>
<dt>The &quot;&#8211;&quot; above is to distinguish &quot;-3&quot; from an option flag.</dt>
<dd></dd></dl>
<h2>OUTPUT</h2>
<p> The output file argument is optional; if it is not specified, cd-paranoia will output samples to one of <code>cdda.wav</code>, <code>cdda.aifc</code>, or <code>cdda.raw</code> depending on whether <code>-w</code>, <code>-a</code>, <code>-r</code> or <code>-R</code> is used (<code>-w</code> is the implicit default). The output file argument of <code>&#8211;</code> specifies standard output; all data formats may be piped. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> cd-paranoia sprang from and once drew heavily from the interface of Heiko Eissfeldt&#8217;s (heiko [at] colossus.escape.de) &#8216;cdda2wav&#8217; package. cd-paranoia would not have happened without it. </p>
<p> Joerg Schilling has also contributed SCSI expertise through his generic SCSI transport library. </p>
<h2>AUTHOR</h2>
<p> Monty &lt;monty [at] xiph.org&gt; </p>
<p> Cdparanoia&#8217;s homepage may be found at: <a rel="nofollow" href="http://www.xiph.org/paranoia/">http://www.xiph.org/paranoia/</a> </p>
<p> Revised for use with libcdio by Rocky &lt;rocky [at] gnu.org&gt; </p>
<p> The libcdio homepage may be found at: <a rel="nofollow" href="http://www.gnu.org/software/libcdio">http://www.gnu.org/software/libcdio</a> </p>
