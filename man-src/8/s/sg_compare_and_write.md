---
title: "sg_compare_and_write(8)"
name: "sg_compare_and_write"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_compare_and_write/"
description: "sg_compare_and_write – send the SCSI COMPARE AND WRITE command"
---

<p>sg_compare_and_write &#8211; send the SCSI COMPARE AND WRITE command</p>
<h2>Synopsis</h2>
<p><code>sg_compare_and_write</code> [<i>&#8211;dpo</i>] [<i>&#8211;fua</i>] [<i>&#8211;fua_nv</i>] [<i>&#8211;help</i>] <i>&#8211;in=IF</i> [<i>&#8211;inw=WF</i>] <i>&#8211;lba=LBA</i> [<i>&#8211;num=NUM</i>] [<i>&#8211;quiet</i>] [<i>&#8211;timeout=TO</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;wrprotect=WP</i>] [<i>&#8211;xferlen=LEN</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send the SCSI COMPARE AND WRITE command to <i>DEVICE</i>. This utility reads a compare buffer and a write buffer from either one or two files. If the <i>&#8211;inw=WF</i> option is not given then the concatenated compare and write buffers are read from the file indicated by the <i>&#8211;in=IF</i> option. If the <i>&#8211;inw=WF</i> option is given then the compare buffer is read from the file indicated by the <i>&#8211;in=IF</i> while the write buffer is read from the file indicated by the <i>&#8211;inw=WF</i>. </p>
<p> Those buffers are expected to each contain <i>NUM</i> blocks of data. The compare starts at at logical block address <i>LBA</i> on the <i>DEVICE</i> and if the comparison fails (i.e. the provided compare buffer does not equal at <i>LBA</i> on the <i>DEVICE</i>) then the COMPARE AND WRITE command finishes with a sense key of MISCOMPARE. In this case this utility will completes and set an exit status of 14 (which happens to be the sense key value of MISCOMPARE). </p>
<p> If the comparison succeeds then the provided write buffer is written to starting at <i>LBA</i> for <i>NUM</i> blocks on the <i>DEVICE</i>. </p>
<p> The actual number of bytes transferred in the data-out buffer of the COMPARE AND WRITE command may need to be given by the user with the <i>&#8211;xferlen=LEN</i> option. <i>LEN</i> defaults to (2* <i>NUM</i> * 512) which is 1024 for the default <i>NUM</i> of 1. If the block size is other than 512 then the user will need to use <i>&#8211;xferlen=LEN</i> option. If protection information is given (indicated by a value of <i>WP</i> other than 0 (the default)) then for a <i>NUM</i> of 1 <i>LEN</i> should be 1040 . Note that the SCSI READ CAPACITY command is not checked by this utility (e.g. to find the block size). </p>
<p> The definition of the SCSI COMPARE AND WRITE command requires that the <i>DEVICE</i> implement the compare and optional write as an uninterrupted series of actions. Depending on some other <i>DEVICE</i> settings a verify operation may occur prior to the compare. </p>
<p> When a mismatch occurs between the compare buffer and the blocks starting at <i>LBA</i> read from the <i>DEVICE</i> the sense buffer containing the MISCOMPARE sense key causes several messages to be sent to stderr (including the offset of the first byte mismatch). To suppress these messages use the <i>&#8211;quiet</i> option. With or without the <i>&#8211;quiet</i> option the exit status will be set to 14. </p>
<p> This command is defined in SBC-3 whose most recent revision is 35f. SBC-3 and other SCSI documents can be found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> .</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;dpo</code></p>
<dd>Set the DPO bit in the COMPARE AND WRITE CDB</p>
<dt><code>-f</code>, <code>&#8211;fua</code></p>
<dd>Set the FUA bit in the COMPARE AND WRITE CDB</p>
<dt><code>-F</code>, <code>&#8211;fua_nv</code></p>
<dd>Set the FUA_NV bit in the COMPARE AND WRITE CDB. This bit was removed in SBC-3 revision 35d and its position marked as &quot;reserved&quot;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;in</code>=<i>IF</i></p>
<dd>read data (binary) from file named <i>IF</i>. This will either be the combined compare and write buffers (when the <i>&#8211;inw=WF</i> option is not given) or just the compare buffer (when the <i>&#8211;inw=WF</i> option is given). If <i>IF</i> is &#8216;-&#8216; then stdin (e.g. a pipe) is read.</p>
<dt><code>-D</code>, <code>&#8211;inw</code>=<i>WF</i></p>
<dd>read data (binary) from file named <i>WF</i>. This will the write buffer that will become the second half of the data-out buffer sent to the <i>DEVICE</i> associated with the COMPARE AND WRITE command. Note that when this option is given then the <i>&#8211;in=IF</i> is expected to hold the associated compare buffer.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the logical block address to start the COMPARE AND WRITE command. Assumed to be in decimal unless prefixed with &#8216;0x&#8217; or has a trailing &#8216;h&#8217;.</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>where <i>NUM</i> is the number of blocks, starting at <i>LBA</i>, to read and compare with the verify instance. And given a match, the <i>NUM</i> of blocks to write starting <i>LBA</i>. The default value for <i>NUM</i> is 1.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>suppress the sense buffer messages associated with a MISCOMPARE sense key that would otherwise be sent to stderr. Still set the exit status to 14 which is the sense key value indicating a MISCOMPARE.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>TO</i></p>
<dd>where <i>TO</i> is the command timeout value in seconds. The default value is 60 seconds. If <i>NUM</i> is large (or zero) a WRITE SAME command may require considerably more time than 60 seconds to complete.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the degree of verbosity (debug messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>output version string then exit.</p>
<dt><code>-w</code>, <code>&#8211;wrprotect</code>=<i>WP</i></p>
<dd>set the WRPROTECT field in the cdb to <i>WP</i>. The default value is 0 which implies no protection information is sent (along with the user data) by this utility.</p>
<dt><code>-x</code>, <code>&#8211;xferlen</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the data out buffer length in byte. It defaults to (2 * <i>NUM</i> * 512) bytes. If the <i>DEVICE</i> block size is other than 512 bytes or <i>WP</i> is non-zero (implying additional protection information) then this default will be incorrect; the use must supply the correct value for <i>LEN</i></dl>
<h2>Notes</h2>
<p>Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_compare_and_write is 0 when it is successful. If the compare step fails then the exit status is 14. For other exit status values see the EXIT STATUS section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> Earlier versions of this utility set an exit status of 98 when there was a MISCOMPARE.</p>
<h2>Authors</h2>
<p>Written by Shahar Salzman. Maintained by Douglas Gilbert. Additions by Eric Seppanen.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to shahar.salzman [at] kaminario.com or dgilbert [at] interlog.com</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012-2013 Kaminario Technologies LTD </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:<br />
 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.<br />
 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.<br />
 * Neither the name of the &lt;organization&gt; nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission. </p>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Kaminario Technologies LTD BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>See Also</h2>
<p><code>sg_xcopy, sg_receive_copy_results(sg3_utils)</code> </p>
