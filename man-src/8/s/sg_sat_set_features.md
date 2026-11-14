---
title: "sg_sat_set_features(8)"
name: "sg_sat_set_features"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_sat_set_features/"
description: "sg_sat_set_features – use ATA SET FEATURES command via a SCSI to ATA Translation (SAT) layer"
---

<p>sg_sat_set_features &#8211; use ATA SET FEATURES command via a SCSI to ATA Translation (SAT) layer</p>
<h2>Synopsis</h2>
<p><code>sg_sat_set_features</code> [<i>&#8211;count=CO</i>] [<i>&#8211;ck_cond</i>] [<i>&#8211;feature=FEA</i>] [<i>&#8211;help</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;len=</i>{16|12}] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends an ATA SET FEATURES command to the <i>DEVICE</i>. This command is used to change settings of ATA non-packet (i.e. disks) and packet devices (e.g. cd/dvd drives). Rather than send the SET FEATURES command directly to the device it is sent via a SCSI transport which is assumed to contain a SCSI to ATA Translation (SAT) Layer (SATL). The SATL may be in an operating system driver, in host bus adapter firmware or in some external enclosure. </p>
<p> The SAT standard (SAT ANSI INCITS 431-2007, prior draft: sat-r09.pdf at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>) defines two SCSI &quot;ATA PASS-THROUGH&quot; commands: one using a 16 byte &quot;cdb&quot; and the other with a 12 byte cdb. This utility defaults to using the 16 byte cdb variant. SAT-2 is also a standard: SAT-2 ANSI INCITS 465-2010 and the draft prior to that is sat2r09.pdf . The SAT-3 project has started and the most recent draft is sat3r01.pdf . </p>
<p> The features can be read using the sg_sat_identify utility which uses either the ATA IDENTIFY DEVICE (for non-packet devices) or the IDENTIFY PACKET DEVICE (for packet devices) command.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;count</code>=<i>CO</i></p>
<dd>the number <i>CO</i> is placed in the &quot;count&quot; field in the ATA SET FEATURES command. Only some subcommands (a term used for the value placed in the &quot;feature&quot; field) require the count field to be set. The default value placed in the &quot;count&quot; field is 0.</p>
<dt><code>-C</code>, <code>&#8211;ck_cond</code></p>
<dd>sets the CK_COND bit in the ATA PASS-THROUGH SCSI cdb. The default setting is clear (i.e. 0). When set the SATL should yield a sense buffer containing a ATA Result descriptor irrespective of whether the ATA command succeeded or failed. When clear the SATL should only yield a sense buffer containing a ATA Result descriptor if the ATA command failed.</p>
<dt><code>-f</code>, <code>&#8211;feature</code>=<i>FEA</i></p>
<dd>the value <i>FEA</i> is placed in the &quot;feature&quot; field in the ATA SET FEATURES command. The term &quot;subcommand&quot; is sometimes used for this value. The default value placed in the &quot;feature&quot; field is 0 which is reserved and hence should not change anything. Two common examples are 2h to enable the write cache and 82h to disable it.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>outputs the usage message summarizing command line options then exits. Ignores <i>DEVICE</i> if given.</p>
<dt><code>-L</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>the number <i>LBA</i> is placed in the &quot;lba&quot; field of the ATA SET FEATURES command. Only some sub-commands (a term used for the value placed in the &quot;feature&quot; field) require the lba field to be set. This value is typically not a &quot;logical block address&quot; as the acronym might imply. The default value placed in the &quot;lba&quot; field is 0. The maximum value allowed for <i>LBA</i> is 0xfffffffe (or 0xffffff if <i>&#8211;len=</i>12).</p>
<dt><code>-l</code>, <code>&#8211;len</code>={16|12}</p>
<dd>this is the length of the SCSI cdb used for the ATA PASS-THROUGH commands. The argument can either be 16 or 12. The default is 16. Some SCSI transports cannot convey SCSI commands longer than 12 bytes.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increases the level or verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string</dl>
<h2>Notes</h2>
<p>In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 and 3 series block devices (e.g. disks and ATAPI DVDs) can also be specified. For example &quot;sg_inq /dev/sda&quot; will work in the 2.6 series kernels. From lk 2.6.6 other SCSI &quot;char&quot; device names may be used as well (e.g. &quot;/dev/st0m&quot;). Prior to lk 2.6.29 USB mass storage limited sense data to 18 bytes which made the <code>&#8211;ck_cond</code> option yield strange (truncated) results.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_sat_set_features is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_sat_identify(sg3_utils), sg_inq(sg3_utils), sdparm(sdparm),</code> <code>hdparm(hdparm)</code> </p>
