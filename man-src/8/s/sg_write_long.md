---
title: "sg_write_long(8)"
name: "sg_write_long"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_write_long/"
description: "sg_write_long – send SCSI WRITE LONG command"
---

<p>sg_write_long &#8211; send SCSI WRITE LONG command</p>
<h2>Synopsis</h2>
<p><code>sg_write_long</code> [<i>&#8211;16</i>] [<i>&#8211;cor_dis</i>] [<i>&#8211;help</i>] [<i>&#8211;in=IF</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;pblock</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;wr_uncor</i>] [<i>&#8211;xfer_len=BTL</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send the SCSI WRITE LONG (10 or 16 byte) command to <i>DEVICE</i>. The buffer to be written to the <i>DEVICE</i> is filled with <code>0xff</code> bytes or read from the <i>IF</i> file. This buffer includes the logical data (e.g. 512 bytes) and the ECC bytes. </p>
<p> This utility can be used to generate a MEDIUM ERROR at a specific logical block address. This can be useful for testing error handling. Prior to such a test, the <code>sg_dd</code> utility could be used to copy the original contents of the logical block address to some safe location. After the test the <code>sg_dd</code> utility could be used to write back the original contents of the logical block address. An alternate strategy would be to read the &quot;long&quot; contents of the logical block address with <code>sg_read_long</code> utility prior to testing and restore it with this utility after testing. </p>
<p> <code>Take care:</code> If recoverable errors are being injected (e.g. only one or a few bits changed so that the ECC is able to correct the data) then care should be taken with the settings in the &quot;read write error recovery&quot; mode page. Specifically if the ARRE (for reads) and/or AWRE (for writes) are set then recovered errors will cause the lba to be reassigned (and the old location to be added to the grown defect list (PLIST)). This is not easily reversed and uses (one of the finite number of) the spare sectors set aside for this purpose. If in doubt it is probably safest to clear the ARRE and AWRE bits. These bits can be checked and modified with the sdparm utility. For example: &quot;sdparm -c AWRE,ARRE /dev/sda&quot; will clear the bits until the disk is power cycled.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-S</code>, <code>&#8211;16</code></p>
<dd>send a SCSI WRITE LONG (16) command to <i>DEVICE</i>. The default action (in the absence of this option) is to send a SCSI WRITE LONG (10) command.</p>
<dt><code>-c</code>, <code>&#8211;cor_dis</code></p>
<dd>sets the correction disabled (i.e &#8216;COR_DIS&#8217;) bit. This inhibits various other mechanisms such as automatic block reallocation, error recovery and various informational exception conditions being triggered. This bit is relatively new in SBC-3 .</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;in</code>=<i>IF</i></p>
<dd>read data (binary) from file named <i>IF</i> and use it for the SCSI WRITE LONG command. If <i>IF</i> is &quot;-&quot; then stdin is read. If this option is not given then 0xff bytes are used as fill.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the logical block address of the sector to overwrite. Defaults to lba 0 which is a dangerous block to overwrite on a disk that is in use. Assumed to be in decimal unless prefixed with &#8216;0x&#8217; or has a trailing &#8216;h&#8217;. If <i>LBA</i> is larger than can fit in 32 bits then the <i>&#8211;16</i> option should be used.</p>
<dt><code>-p</code>, <code>&#8211;pblock</code></p>
<dd>sets the physical block (i.e &#8216;PBLOCK&#8217;) bit. This instructs <i>DEVICE</i> to use the given data (unless <i>&#8211;wr_uncor</i> is also given) to write to the physical block specified by <i>LBA</i>. The default action is to write to the logical block corresponding to the given lba. This bit is relatively new in SBC-3 .</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the degree of verbosity (debug messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>output version string then exit.</p>
<dt><code>-w</code>, <code>&#8211;wr_uncor</code></p>
<dd>sets the &quot;write uncorrected&quot; (i.e &#8216;WR_UNCOR&#8217;) bit. This instructs the <i>DEVICE</i> to flag the given lba (or the physical block that contains it if <i>&#8211;pblock</i> is also given) as having an unrecoverable error associated with it. Note: no data is transferred to <i>DEVICE</i>, other than the command (i.e. the cdb). In the absence of this option, the default action is to use the provided data or 0xff bytes (<i>&#8211;xfer_len=BTL</i> in length) and write it to <i>DEVICE</i>. This bit is relatively new in SBC-3 .</p>
<dt><code>-x</code>, <code>&#8211;xfer_len</code>=<i>BTL</i></p>
<dd>where <i>BTL</i> is the byte transfer length (default to 520). If the given value (or the default) does not match the &quot;long&quot; block size of the device, nothing is written to <i>DEVICE</i> and the appropriate xfer_len value may be deduced from the error response which is printed (to stderr).</dl>
<h2>Notes</h2>
<p>Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> The 10 byte SCSI WRITE LONG command limits the logical block address to a 32 bit quantity. For larger LBAs use the <i>&#8211;16</i> option for the SCSI WRITE LONG (16) command.</p>
<h2>Examples</h2>
<p>This section outlines setting up a block with corrupted data, checking the error condition, then restoring useful contents to that sector. First, if the data in a sector is important, save it with the sg_read_long utility: </p>
<pre><code>sg_read_long --lba=0x1234 --out=0x1234_1.img -x BTL /dev/sda</code></pre>
<p> This utility may need to be executed several time in order to determine what the correct value for <i>BTL</i> is. Next use this utility to &quot;corrupt&quot; that sector. That might be done with: sg_write_long &#8211;lba=0x1234 -x BTL /dev/sda This will write a sector (and ECC data) of 0xff bytes. Some disks may reject this (at least one of the author&#8217;s does). Another approach is to copy the 0x1234_1.img file (to 0x1234_2.img in this example) and change some values with a hex editor. Then write the changed image with: sg_write_long &#8211;lba=0x1234 &#8211;in=0x1234_2.img -x BTL /dev/sda Yet another approach is to use the <i>&#8211;wr_uncor</i> option, if supported: sg_write_long &#8211;lba=0x1234 &#8211;wr_uncor /dev/sda Next we use the sg_dd utility to check that the sector is corrupted. Here is an example: sg_dd if=/dev/sda blk_sgio=1 skip=0x1234 of=. bs=512 count=1 verbose=4 Notice that the &quot;blk_sgio=1&quot; option is given. This is to make sure that the sector is read (and no others) and the error is fully reported. The &quot;blk_sgio=1&quot; option causes the SG_IO ioctl to be used by sg_dd rather than the block subsystem. Finally we should restore sector 0x1234 to a non-corrupted state. A sector full of zeros could be written with: sg_dd if=/dev/zero of=/dev/sda blk_sgio=1 seek=0x1234 bs=512 count=1 This will result in a sector (block) with 512 bytes of 0x0 without a MEDIUM ERROR since the ECC and associated data will be regenerated and thus well formed. The &#8216;blk_sgio=1&#8217; option is even more important in this case as it may stop the block subsystem doing a read before write (since the read will most likely fail). Another approach is to write back the original contents: </p>
<pre><code>sg_write_long --lba=0x1234 --in=0x1234_1.img -x BTL /dev/sda
</code></pre>
<h2>Exit Status</h2>
<p>The exit status of sg_write_long is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Saeed Bishara. Further work by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_read_long, sg_dd (both in sg3_utils), sdparm(sdparm)</code> </p>
