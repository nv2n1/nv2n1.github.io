---
title: "sg_write_same(8)"
name: "sg_write_same"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_write_same/"
description: "sg_write_same – send SCSI WRITE SAME command"
---

<p>sg_write_same &#8211; send SCSI WRITE SAME command</p>
<h2>Synopsis</h2>
<p><code>sg_write_same</code> [<i>&#8211;10</i>] [<i>&#8211;16</i>] [<i>&#8211;32</i>] [<i>&#8211;anchor</i>] [<i>&#8211;grpnum=GN</i>] [<i>&#8211;help</i>] [<i>&#8211;in=IF</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;lbdata</i>] [<i>&#8211;pbdata</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;ndob</i>] [<i>&#8211;timeout=TO</i>] [<i>&#8211;unmap</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;wrprotect=WPR</i>] [<i>&#8211;xferlen=LEN</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send the SCSI WRITE SAME (10, 16 or 32 byte) command to <i>DEVICE</i>. This command writes the given block <i>NUM</i> times to consecutive blocks on the <i>DEVICE</i> starting at logical block address <i>LBA</i>. </p>
<p> SBC-3 revision 35d introduced a &quot;no data-out buffer&quot; (NDOB) bit which, if set, bypasses the requirement to send a single block of data to the <i>DEVICE</i> together with the command. Only WRITE SAME (16 and 32 byte) support the NDOB bit. </p>
<p> The length of the block to be written multiple times is obtained from either the <i>LEN</i> argument, or the length of the given input file <i>IF</i>, or by calling READ CAPACITY(16) on <i>DEVICE</i>. The contents of the block to be written are obtained from the input file <i>IF</i> or zeros are used. If READ CAPACITY(16) is called (which implies <i>IF</i> was not given) and the PROT_EN bit is set then an extra 8 bytes (i.e. more than the logical block size) of 0xff are sent. If READ CAPACITY(16) fails then READ CAPACITY(10) is used to determine the block size. </p>
<p> If neither <i>&#8211;10</i>, <i>&#8211;16</i> nor <i>&#8211;32</i> is given then WRITE SAME(10) is sent unless one of the following conditions is met. If <i>LBA</i> (plus <i>NUM</i>) exceeds 32 bits, <i>NUM</i> exceeds 65535, or the <i>&#8211;unmap</i> option is given then WRITE SAME(16) is sent. The <i>&#8211;10</i>, <i>&#8211;16</i> and <i>&#8211;32</i> options are mutually exclusive. </p>
<p> In SBC-3 revision 26 the UNMAP and ANCHOR bits were added to the WRITE SAME (10) command. Since the UNMAP bit has been in WRITE SAME (16) and WRITE SAME (32) since SBC-3 revision 18, the lower of the two (i.e. WRITE SAME (16)) is the default when the <i>&#8211;unmap</i> option is given. To send WRITE SAME (10) use the <i>&#8211;10</i> option. </p>
<p> <code>Take care:</code> The WRITE SAME(10, 16 and 32) commands interpret a <i>NUM</i> of zero as write to the end of <i>DEVICE</i>. This utility defaults <i>NUM</i> to 1 . The WRITE SAME commands have no IMMED bit so if <i>NUM</i> is large (or zero) then an invocation of this utility could take a long time, potentially as long as a FORMAT UNIT command. In such situations the command timeout value <i>TO</i> may need to be increased from its default value of 60 seconds. In SBC-3 revision 26 the WSNZ (write same no zero) bit was added to the Block Limits VPD page [0xB0]. If set the WRITE SAME commands will not accept a <i>NUM</i> of zero. The same SBC-3 revision added the &quot;Maximum Write Same Length&quot; field to the Block Limits VPD page. </p>
<p> The Logical Block Provisioning VPD page [0xB2] contains the LBWS and LBW10 bits. If LBWS is set then WRITE SAME (16) supports the UNMAP bit. If LBWS10 is set then WRITE SAME (10) supports the UNMAP bit. If either LBWS or LBWS10 is set and the WRITE SAME (32) is supported then WRITE SAME (32) supports the UNMAP bit. This is as of SBC-3 revision 26. </p>
<p> As a precaution against an accidental &#8216;sg_write_same /dev/sda&#8217; (for example) overwriting LBA 0 on /dev/sda with zeros, at least one of the <i>&#8211;in=IF</i>, <i>&#8211;lba=LBA</i> or <i>&#8211;num=NUM</i> options must be given. Obviously this utility can destroy a lot of user data so check the options carefully.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-R</code>, <code>&#8211;10</code></p>
<dd>send a SCSI WRITE SAME (10) command to <i>DEVICE</i>. The ability to set the <i>&#8211;unmap</i> (and <i>&#8211;anchor</i>) options to this command was added in SBC-3 revision 26.</p>
<dt><code>-S</code>, <code>&#8211;16</code></p>
<dd>send a SCSI WRITE SAME (16) command to <i>DEVICE</i>.</p>
<dt><code>-T</code>, <code>&#8211;32</code></p>
<dd>send a SCSI WRITE SAME (32) command to <i>DEVICE</i>.</p>
<dt><code>-a</code>, <code>&#8211;anchor</code></p>
<dd>sets the ANCHOR bit in the cdb. Introduced in SBC-3 revision 22. That draft requires the <i>&#8211;unmap</i> option to also be specified.</p>
<dt><code>-g</code>, <code>&#8211;grpnum</code>=<i>GN</i></p>
<dd>sets the &#8216;Group number&#8217; field to <i>GN</i>. Defaults to a value of zero. <i>GN</i> should be a value between 0 and 31.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;in</code>=<i>IF</i></p>
<dd>read data (binary) from file named <i>IF</i> and use it as the data out buffer for the SCSI WRITE SAME command. The length of the data out buffer is <i>&#8211;xferlen=LEN</i> or, if that is not given, the length of the <i>IF</i> file. If <i>IF</i> is &quot;-&quot; then stdin is read. If this option is not given then 0x00 bytes are used as fill with the length of the data out buffer obtained from <i>&#8211;xferlen=LEN</i> or by calling READ CAPACITY(16 or 10). If the response to READ CAPACITY(16) has the PROT_EN bit set then data out buffer size is modified accordingly with the last 8 bytes set to 0xff.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the logical block address to start the WRITE SAME command. Defaults to lba 0 which is a dangerous block to overwrite on a disk that is in use. Assumed to be in decimal unless prefixed with &#8216;0x&#8217; or has a trailing &#8216;h&#8217;.</p>
<dt><code>-L</code>, <code>&#8211;lbdata</code></p>
<dd>sets the LBDATA bit in the WRITE SAME cdb.</p>
<dt><code>-N</code>, <code>&#8211;ndob</code></p>
<dd>sets the NDOB bit in the WRITE SAME (16 and 32 byte) commands. Default is to clear this bit. When this option is given then <i>&#8211;in=IF</i> is not allowed and <i>&#8211;xferlen=LEN</i> can only be given if <i>LEN</i> is 0 .</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>where <i>NUM</i> is the number of blocks, starting at <i>LBA</i>, to write the data out buffer to. The default value for <i>NUM</i> is 1. The value corresponds to the &#8216;Number of logical blocks&#8217; field in the WRITE SAME cdb. Note that a value of 0 in <i>NUM</i> is interpreted as write the data out buffer on every block starting at <i>LBA</i> to the end of the <i>DEVICE</i>.</p>
<dt><code>-P</code>, <code>&#8211;pbdata</code></p>
<dd>sets the PBDATA bit in the WRITE SAME cdb.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>TO</i></p>
<dd>where <i>TO</i> is the command timeout value in seconds. The default value is 60 seconds. If <i>NUM</i> is large (or zero) a WRITE SAME command may require considerably more time than 60 seconds to complete.</p>
<dt><code>-U</code>, <code>&#8211;unmap</code></p>
<dd>sets the UNMAP bit in the WRITE SAME(10, 16 and 32) cdb. See UNMAP section below.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the degree of verbosity (debug messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>output version string then exit.</p>
<dt><code>-w</code>, <code>&#8211;wrprotect</code>=<i>WPR</i></p>
<dd>sets the &quot;Write protect&quot; field in the WRITE SAME cdb to <i>WPR</i>. The default value is zero. <i>WPR</i> should be a value between 0 and 7. When <i>WPR</i> is 1 or greater, and the disk&#8217;s protection type is 1 or greater, then 8 extra bytes of protection information are expected or generated (to place in the command&#8217;s data out buffer).</p>
<dt><code>-x</code>, <code>&#8211;xferlen</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the data out buffer length. Defaults to the length of the <i>IF</i> file or, if that is not given, then the READ CAPACITY(16 or 10) command is used to find the &#8216;Logical block length in bytes&#8217;. That figure may be increased by 8 bytes if the <i>DEVICE</i>&#8216;s protection type is 1 or greater and the WRPROTECT field (see <i>&#8211;wrprotect=WPR</i>) is 1 or greater. If both this option and the <i>IF</i> option are given and <i>LEN</i> exceeds the length of the <i>IF</i> file then <i>LEN</i> is the data out buffer length with zeros used as pad bytes.</dl>
<h2>Unmap</h2>
<p>Logical block provisioning is a new term introduced in SBC-3 revision 25 for the ability to mark blocks as unused. It is closely related to the ATA DATA SET MANAGEMENT command with the &quot;Trim&quot; bit set. For large storage arrays, it is a way to provision less physical storage than the READ CAPACITY command reports is available, potentially allocating more physical storage when WRITE commands require it. For flash memory it is a way of potentially saving power (and perhaps access time) when it is known large sections (or almost all) of the flash memory is not in use. </p>
<p> Support for logical block provisioning is indicated by the LBPME bit being set in the READ CAPACITY(16) command response (see the sg_readcap utility). That implies at least one of the UNMAP or WRITE SAME(16) commands is implemented. If the UNMAP command is implemented then the &quot;Maximum unmap LBA count&quot; and &quot;Maximum unmap block descriptor count&quot; fields in the Block Limits VPD page should both be greater than zero. The READ CAPACITY(16) command response also contains a LBPRZ bit which if set means that if unmapped blocks are read then zeros will be returned for the data (and if protection information is active, 0xff bytes are returned for that). In SBC-3 revision 27 the same LBPRZ bit was added to the Logical Block Provisioning VPD page. </p>
<p> In SBC-3 revision 25 the LBPU and ANC_SUP bits where added to the Logical Block Provisioning VPD page. When LBPU is set it indicates that the device supports the UNMAP command (see the sg_unmap utility). When the ANC_SUP bit is set it indicates the device supports anchored LBAs. </p>
<p> When the UNMAP bit is set in the cdb then the data out buffer is also sent. Additionally the data section of that data out buffer should be full of 0x0 bytes while the data protection block, 8 bytes at the end if present, should be set to 0xff bytes. If these conditions are not met and the LBPRZ bit is set then the UNMAP bit is ignored and the data out buffer is written to the <i>DEVICE</i> as if the UNMAP bit was zero. In the absence of the <i>&#8211;in=IF</i> option, this utility will attempt build a data out buffer that meets the requirements for the UNMAP bit in the cdb to be acted on by the <i>DEVICE</i>. </p>
<p> Logical blocks may also be unmapped by the SCSI UNMAP and FORMAT UNIT commands (see the sg_unmap and sg_format utilities).</p>
<h2>Notes</h2>
<p>Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> In Linux at this time the sg driver does not support cdb sizes greater than 16 bytes. Hence a device node like /dev/sg1 which is associated with the sg driver will fail with this utility if the <i>&#8211;32</i> option is given (or implied by other options). The bsg driver with device nodes like /dev/bsg/6:0:0:1 does support cdb sizes greater than 16 bytes.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_write_same is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Examples</h2>
<p>One simple usage is to write blocks of zero from (and including) a given LBA: </p>
<pre><code>sg_write_same --lba=0x1234 --num=63 /dev/sdc</code></pre>
<p> Since <i>&#8211;xferlen=LEN</i> has not been given, then this utility will call the READ CAPACITY command on /dev/sdc to determine the number of bytes in a logical block. Let us assume that is 512 bytes. Since <i>&#8211;in=IF</i> is not given a block of zeros is assumed. So 63 blocks of zeros (each block containing 512 bytes) will be written from (and including) LBA 0x1234 . Note that only one block of zeros is passed to the SCSI WRITE SAME command in the data out buffer (as required by SBC-3). A similar example follows but in this case the blocks are &quot;unmapped&quot; (&quot;trimmed&quot; in ATA speak) rather than zeroed:<br />
&nbsp;<wbr>&nbsp;<wbr>sg_write_same &#8211;unmap -L 0x1234 -n 63&nbsp;<wbr>/dev/sdc Note that if the LBPRZ bit in the READ CAPACITY(16) response is set (i.e. LPPRZ is an acronym for logical block provisioning read zeros) then these two examples do the same thing, at least seen from the point of view of subsequent reads. This utility can also be used to write protection information (PI) on disks formatted with a protection type greater than zero. PI is 8 bytes of extra data appended to the user data of a logical block: the first two bytes are a CRC (the &quot;guard&quot;), the next two bytes are the &quot;application tag&quot; and the last four bytes are the &quot;reference tag&quot;. With protection types 1 and 2 if the application tag is 0xffff then the guard should not be checked (against the user data). In this example we assume the logical block size (of the user data) is 512 bytes and the disk has been formatted with protection type 1. Since we are going to modify LBA 2468 then we take a copy of it first: dd if=/dev/sdb skip=2468 bs=512 of=2468.bin count=1 The following command line sets the user data to zeros and the PI to 8 0xFF bytes on LBA 2468: sg_write_same &#8211;lba=2468 /dev/sdb Reading back that block should be successful because the application tag is 0xffff which suppresses the guard (CRC) check (which would otherwise be wrong): dd if=/dev/sdb skip=2468 bs=512 of=/dev/null count=1 Now an attempt is made to create a binary file with zeros in the user data, 0x0000 in the application tag and 0xff bytes in the other two PI fields. It is awkward to create 0xff bytes in a file (in Unix) as the &quot;tr&quot; command below shows: dd if=/dev/zero bs=1 count=512 of=ud.bin</p>
<p>tr &quot;
