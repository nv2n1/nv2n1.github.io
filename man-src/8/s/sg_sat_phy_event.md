---
title: "sg_sat_phy_event(8)"
name: "sg_sat_phy_event"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_sat_phy_event/"
description: "sg_sat_phy_event – use ATA READ LOG EXT via a SAT pass-through to fetch SATA phy event counters"
---

<p>sg_sat_phy_event &#8211; use ATA READ LOG EXT via a SAT pass-through to fetch SATA phy event counters</p>
<h2>Synopsis</h2>
<p><code>sg_sat_phy_event</code> [<i>&#8211;ck_cond</i>] [<i>&#8211;extend</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;ignore</i>] [<i>&#8211;len=</i>{16|12}] [<i>&#8211;raw</i>] [<i>&#8211;reset</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends an ATA READ LOG EXT with the log page (&quot;address&quot;) set to 11h to <i>DEVICE</i> and outputs the response. Log page 11h is defined in the SATA 2.5 standard and contains phy event counters. Rather than send this command directly to the <i>DEVICE</i>, are sent via a SCSI transport which is assumed to contain a SCSI to ATA Translation (SAT) Layer (SATL). The SATL may be in an operating system driver, in host bus adapter firmware or in some external enclosure. </p>
<p> The SAT standard (SAT ANSI INCITS 431-2007, prior draft: sat-r09.pdf at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>) defines two SCSI &quot;ATA PASS-THROUGH&quot; commands: one using a 16 byte &quot;cdb&quot; and the other with a 12 byte cdb. This utility defaults to using the 16 byte cdb variant. SAT-2 is also a standard: SAT-2 ANSI INCITS 465-2010 and the draft prior to that is sat2r09.pdf . The SAT-3 project has started and the most recent draft is sat3r01.pdf .</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;ck_cond</code></p>
<dd>sets the CK_COND bit in the ATA PASS-THROUGH SCSI cdb. The default setting is clear (i.e. 0). When set the SATL should yield a sense buffer containing a ATA Result descriptor irrespective of whether the command succeeded or failed. When clear the SATL should only yield a sense buffer containing a ATA Result descriptor if the command failed.</p>
<dt><code>-e</code>, <code>&#8211;extend</code></p>
<dd>sets the EXTEND bit in the ATA PASS-THROUGH SCSI cdb. The default setting is clear (i.e. 0). When set a 48 bit LBA command is sent to the device. This option has no effect when <i>&#8211;len=12</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>outputs the usage message summarizing command line options then exits. Ignores <i>DEVICE</i> if given.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>outputs the ATA READ LOG EXT response in hex. The default action (i.e. without any &#8216;-H&#8217; options) is to output the response in hex, grouped in 16 bit words (i.e. the ATA standard&#8217;s preference). When given once, the response is output in ASCII hex bytes (i.e. the SCSI standard&#8217;s preference). When given twice (i.e. &#8216;-HH&#8217;) the output is in hex, grouped in 16 bit words, the same as the default but without a header.</p>
<dt><code>-i</code>, <code>&#8211;ignore</code></p>
<dd>usually the phy counter identifier names are decoded. When this option is given, the numeric value of the identifier is output, the vendor flag, the data length (in bytes) and the corresponding value.</p>
<dt><code>-l</code>, <code>&#8211;len</code>={16|12}</p>
<dd>this is the length of the SCSI cdb used for the ATA PASS-THROUGH commands. The argument can either be 16 or 12. The default is 16. The larger cdb size is needed for 48 bit LBA addressing of ATA devices. On the other hand some SCSI transports cannot convey SCSI commands longer than 12 bytes.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the ATA READ LOG EXT response in binary. The output should be piped to a file or another utility when this option is used. The binary is sent to stdout, and errors are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;reset</code></p>
<dd>reset the counters after the current values are returned, decoded and displayed.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increases the level or verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string</dl>
<h2>Notes</h2>
<p>The SCSI ATA PASS-THROUGH (12) command&#8217;s opcode is 0xa1 and it clashes with the MMC set&#8217;s BLANK command used by cd/dvd writers. So a SATL in front of an ATAPI device that uses MMC (i.e. has peripheral device type 5) probably should treat opcode 0xa1 as a BLANK command and send it through to the cd/dvd drive. The ATA PASS-THROUGH (16) command&#8217;s opcode (0x85) does not clash with anything so it is a better choice. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. disks and ATAPI DVDs) can also be specified. For example &quot;sg_inq /dev/sda&quot; will work in the 2.6 series kernels. From lk 2.6.6 other SCSI &quot;char&quot; device names may be used as well (e.g. &quot;/dev/st0m&quot;). Prior to lk 2.6.29 USB mass storage limited sense data to 18 bytes which made the <code>&#8211;ck_cond</code> option yield strange (truncated) results.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_sat_identify is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_sat_identify(sg3_utils), smp_rep_phy_err_log(smp_utils),</code> <code>sdparm(sdparm), hdparm(hdparm)</code> </p>
