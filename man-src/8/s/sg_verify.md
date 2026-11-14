---
title: "sg_verify(8)"
name: "sg_verify"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_verify/"
description: "sg_verify – invoke SCSI VERIFY command(s) on a block device"
---

<p>sg_verify &#8211; invoke SCSI VERIFY command(s) on a block device</p>
<h2>Synopsis</h2>
<p><code>sg_verify</code> [<i>&#8211;16</i>] [<i>&#8211;bpc=BPC</i>] [<i>&#8211;count=COUNT</i>] [<i>&#8211;dpo</i>] [<i>&#8211;ebytchk=BCH</i>] [<i>&#8211;group=GN</i>] [<i>&#8211;help</i>] [<i>&#8211;in=IF</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;ndo=NDO</i>] [<i>&#8211;quiet</i>] [<i>&#8211;readonly</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;vrprotect=VRP</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Sends one or more SCSI VERIFY (10 or 16) commands to <i>DEVICE</i>. These SCSI commands are defined in the SBC-2 (draft) standard at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> and SBC-3 drafts. </p>
<p> When <i>&#8211;ndo=NDO</i> is not given then the verify starts at the logical block address given by the <i>&#8211;lba=LBA</i> option and continues for <i>&#8211;count=COUNT</i> blocks. No more than <i>&#8211;bpc=BPC</i> blocks are verified by each VERIFY command so if necessary multiple VERIFY commands are sent. Medium verification operations are performed by the <i>DEVICE</i> (e.g. assuming each block has additional EEC data, check this against the logical block contents). No news is good news (i.e. if there are no verify errors detected then no messages are sent to stderr and the Unix exit status is 0). </p>
<p> When <i>&#8211;ndo=NDO</i> is given then the <i>&#8211;bpc=BPC</i> option is ignored. A single VERIFY command is issued and a comparison starts at the logical block address given by the <i>&#8211;lba=LBA</i> option and continues for <i>&#8211;count=COUNT</i> blocks. The VERIFY command has an associated data-out buffer that is <i>NDO</i> bytes long. The contents of the data-out buffer are obtained from the <i>FN</i> file (if <i>&#8211;in=FN</i> is given) or from stdin. A comparison takes place between data-out buffer and the logical blocks on the <i>DEVICE</i>. If the comparison is good then no messages are sent to stderr and the Unix exit status is 0. If the comparison fails then a sense buffer with a sense key of MISCOMPARE is returned; in this case the Unix exit status will be 14. Messages will be sent to stderr associated with MISCOMPARE sense buffer unless the <i>&#8211;quiet</i> option is given. </p>
<p> In SBC-3 revision 34 the BYTCHK field in all SCSI VERIFY commands was expanded from one to two bits. That required some changes in the options of this utility, see the section below on OPTION CHANGES.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-S</code>, <code>&#8211;16</code></p>
<dd>uses a VERIFY(16) command (default VERIFY(10)). Even without this option, using an <i>&#8211;lba=LBA</i> which is too large, will cause the utility to issue a VERIFY(16) command.</p>
<dt><code>-b</code>, <code>&#8211;bpc</code>=<i>BPC</i></p>
<dd>this option is ignored if <i>&#8211;ndo=NDO</i> is given. Otherwise <i>BPC</i> specifies the maximum number of blocks that will be verified by a single SCSI VERIFY command. The default value is 128 blocks which equates to 64 KB for a disk with 512 byte blocks. If <i>BPC</i> is less than <i>COUNT</i> then multiple SCSI VERIFY commands are sent to the <i>DEVICE</i>. For the default VERIFY(10) <i>BPC</i> cannot exceed 0xffff (65,535) while for VERIFY(16) <i>BPC</i> cannot exceed 0x7fffffff (2,147,483,647). For recent block devices (disks) this value may be constrained by the maximum transfer length field in the block limits VPD page.</p>
<dt><code>-c</code>, <code>&#8211;count</code>=<i>COUNT</i></p>
<dd>where <i>COUNT</i> specifies the number of blocks to verify. The default value is 1 . If <i>COUNT</i> is greater than <i>BPC</i> (or its default value of 128) and <i>NDO</i> is not given, 0 or less then multiple SCSI VERIFY commands are sent to the device. Otherwise <i>COUNT</i> becomes the contents of the verification length field of the SCSI VERIFY command issued. The <code>sg_readcap</code> utility can be used to find the maximum number of blocks that a block device (e.g. a disk) has.</p>
<dt><code>-d</code>, <code>&#8211;dpo</code></p>
<dd>disable page out changes the cache retention priority of blocks read on the device&#8217;s cache to the lowest priority. This means that blocks read by other commands are more likely to remain in the device&#8217;s cache.</p>
<dt><code>-E</code>, <code>&#8211;ebytchk</code>=<i>BCH</i></p>
<dd>sets the BYTCHK field to <i>BCH</i> overriding the value (1) set by the <i>&#8211;ndo=NDO</i> option. Values of 1, 2 or 3 are accepted for <i>BCH</i> however sbc3r34 reserves the value 2. If this option is given then <i>&#8211;ndo=NDO</i> must also be given. If <i>BCH</i> is 3 then <i>COUNT</i> must be 1 and <i>NDO</i> should be the size of one logical block (plus the size of some or all of the protection infomation if <i>VRP</i> is greater than 0).</p>
<dt><code>-g</code>, <code>&#8211;group</code>=<i>GN</i></p>
<dd>where <i>GN</i> becomes the contents of the group number field in the SCSI VERIFY(16) command. The default value for <i>GN</i> is 0. Note that this option is ignored for the SCSI VERIFY(10) command.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;in</code>=<i>IF</i></p>
<dd>where <i>IF</i> is the name of a file from which <i>NDO</i> bytes will be read and placed in the data-out buffer. This is only done when the <i>&#8211;ndo=NDO</i> option is given. If this option is not given then stdin is read. If <i>IF</i> is &quot;-&quot; then stdin is also used.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> specifies the logical block address of the first block to start the verify operation. <i>LBA</i> is assumed to be decimal unless prefixed by &#8216;0x&#8217; or a trailing &#8216;h&#8217; (see below). The default value is 0 (i.e. the start of the device).</p>
<dt><code>-n</code>, <code>&#8211;ndo</code>=<i>NDO</i></p>
<dd><i>NDO</i> is the number of bytes to obtain from the <i>FN</i> file (if <i>&#8211;in=FN</i> is given) or from stdin. Those bytes are placed in the data-out buffer associated with the SCSI VERIFY command and <i>NDO</i> is placed in the verification length field in the cdb. The default value for <i>NDO</i> is 0 and the maximum value is dependant on the OS. If the <i>&#8211;ebytchk=BCH</i> option is not given then the BYTCHK field in the cdb is set to 1.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>suppress the sense buffer messages associated with a MISCOMPARE sense key that would otherwise be sent to stderr. Still set the exit status to 14 which is the sense key value indicating a MISCOMPARE .</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd>opens the DEVICE read-only rather than read-write which is the default. The Linux sg driver needs read-write access for the SCSI VERIFY command but other access methods may require read-only access.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-P</code>, <code>&#8211;vrprotect</code>=<i>VRP</i></p>
<dd>where <i>VRP</i> is the value in the vrprotect field in the VERIFY command cdb. It must be a value between 0 and 7 inclusive. The default value is zero.</dl>
<h2>Bytchk</h2>
<p>BYTCHK is the name of a field (two bits wide) in the VERIFY(10) and VERIFY(16) commands. When set to 1 or 3 (sbc3r34 reserves the value 2) it indicates that associated with the SCSI VERIFY command, a data-out buffer will be sent for the device (disk) to check. Using the <i>&#8211;ndo=NDO</i> option sets the BYTCHK field to 1 and <i>NDO</i> is the number of bytes placed in the data-out buffer. Those bytes are obtained from stdin or <i>IF</i> (from the <i>&#8211;in=FN</i> option). The <i>&#8211;ebytchk=BCH</i> option may be used to override the BYTCHK field value of 1 with <i>BCH</i>. </p>
<p> The calculation of <i>NDO</i> is left up to the user. Its value depends on the logical block size (which can be found with the sg_readcap utility), the <i>COUNT</i> and the <i>VRP</i> values. If the <i>VRP</i> is greater than 0 then each logical block will contain an extra 8 bytes (at least) of protection information. </p>
<p> When the BYTCHK field is 0 then the verification process done by the device (disk) is vendor specific. It typically involves checking each block on the disk against its error correction codes (ECC) which is additional data also held on the disk. </p>
<p> Many Operating Systems put limits on the maximum size of the data-out (and data-in) buffer. For Linux at one time the limit was less than 1 MB but has been increased somewhat.</p>
<h2>Option Changes</h2>
<p>Earlier versions of this utility had a <i>&#8211;bytchk=NDO</i> option which set the BYTCHK bit and set the cdb verification length field to <i>NDO</i>. The shorter form of that option was <i>-B NDO</i>. For backward compatibility that option is still present but not documented. In its place is the <i>&#8211;ndo=NDO</i> whose shorter form of <i>-n NDO</i>. <i>&#8211;ndo=NDO</i> sets the BYTCHK field to 1 unless that is overridden by the <i>&#8211;ebytchk=BCH</i>.</p>
<h2>Notes</h2>
<p>Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> The amount of error correction and the number of retries attempted before a block is considered defective are controlled in part by the Verify Error Recovery mode page. A note in the SBC-3 draft (rev 29 section 6.4.9 on the Verify Error Recovery mode page) advises that to minimize the number of checks (and hence have the most &quot;sensitive&quot; verify check) do the following in that mode page: set the EER bit to 0, the PER bit to 1, the DTE bit to 1, the DCR bit to 1, the verify retry count to 0 and the verify recovery time limit to 0. Mode pages can be modified with the <code>sdparm</code> utility. </p>
<p> The SCSI <a href="/docs/linux/man/6-verify/">VERIFY</a>(6) command defined in the SSC-2 standard and later (i.e. for tape drive systems) is not supported by this utility.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_verify is 0 when it is successful. When <i>BCH</i> is other than 0 then a comparison takes place and if it fails then the exit status is 14 which happens to be the sense key value of MISCOMPARE. Otherwise see the EXIT STATUS section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> Earlier versions of this utility set an exit status of 98 when there was a MISCOMPARE.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sdparm(sdparm), sg_modes(sg3_utils), sg_readcap(sg3_utils),</code> <code>sg_inq(sg3_utils)</code> </p>
