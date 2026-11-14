---
title: "sg_get_lba_status(8)"
name: "sg_get_lba_status"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_get_lba_status/"
description: "sg_get_lba_status – send SCSI GET LBA STATUS command"
---

<p>sg_get_lba_status &#8211; send SCSI GET LBA STATUS command</p>
<h2>Synopsis</h2>
<p><code>sg_get_lba_status</code> [<i>&#8211;brief</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send the SCSI GET LBA STATUS command to the <i>DEVICE</i> and outputs the response. This command was introduced in (draft) SBC-3 revision 20 and devices that support logical block provisioning should support this command. </p>
<p> The default action is to decode the response into one LBA status descriptor per line output to stdout. The descriptor LBA is output in hex (prefixed by &#8216;0x&#8217;) and the number of blocks is output in decimal followed by the provisioning status in decimal. The provisioning status can be in the range 0 to 15 of which only 0 (mapped), 1 (unmapped) and 2 (anchored) are used currently. The amount of output can be reduced by the <i>&#8211;brief</i> option.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>when use once then one LBA status descriptor per line is output to stdout. Each line has this format: &quot;0x&lt;descriptor_LBA&gt; 0x&lt;blocks&gt; &lt;provisioning_status&gt;&quot;. So the descriptor LBA and blocks are output in hex and the provisioning status in decimal. When used twice (e.g. &#8216;-bb&#8217; or &#8216;&#8211;brief &#8211;brief&#8217;) the provisioning status of the given <i>LBA</i> (or LBA 0 if the <i>&#8211;lba</i> option is not given) is output to stdout. A check is made that the given <i>LBA</i> lies on the range of the first returned LBA status descriptor (as it should according to SBC-3 revision 20) and warnings are sent to stderr if it doesn&#8217;t.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output response to this command in ASCII hex.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the starting Logical Block Address (LBA) to check the provisioning status for. Note that the <i>DEVICE</i> chooses how many following blocks that it will return provisioning status for.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the (maximum) response length in bytes. It is placed in the cdb&#8217;s &quot;allocation length&quot; field. If not given then 24 is used. 24 is enough space for the response header and one LBA status descriptor. <i>LEN</i> should be 8 plus a multiple of 16 (e.g. 24, 40, and 56 are suitable).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output response in binary (to stdout).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output). Additional output caused by this option is sent to stderr.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>In SBC-3 revision 25 the calculation associated with the Parameter Data Length field in the response was modified. Prior to that the byte offset was 8 and in revision 25 it was changed to 4. </p>
<p> For a discussion of logical block provisioning see section 4.7 of sbc3r29.pdf at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> (or the corresponding section of a later draft).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_get_lba_status is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_write_same/">sg_write_same</a>(8), <a href="/docs/linux/man/8-sg_unmap/">sg_unmap</a>(8)</code> </p>
