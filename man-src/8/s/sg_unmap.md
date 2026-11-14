---
title: "sg_unmap(8)"
name: "sg_unmap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_unmap/"
description: "sg_unmap – send SCSI UNMAP command (known as ‘trim’ in ATA specs)"
---

<p>sg_unmap &#8211; send SCSI UNMAP command (known as &#8216;trim&#8217; in ATA specs)</p>
<h2>Synopsis</h2>
<p><code>sg_unmap</code> [<i>&#8211;anchor</i>] [<i>&#8211;grpnum=GN</i>] [<i>&#8211;help</i>] [<i>&#8211;in=FILE</i>] [<i>&#8211;lba=LBA,LBA&#8230;</i>] [<i>&#8211;num=NUM,NUM&#8230;</i>] [<i>&#8211;timeout=TO</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI UNMAP command to <i>DEVICE</i> to unmap one or more logical blocks. This command was introduced in SBC-3 revision 18 under the broad heading of &quot;logical block provisioning&quot;. Logical blocks may also be unmapped by the SCSI WRITE SAME command; see the sg_write_same utility. The unmap capability is closely related to the ATA DATA SET MANAGEMENT command with the &quot;Trim&quot; bit set. </p>
<p> Logical blocks to be unmapped can be specified in one of two ways to this utility. One way is by supplying the start LBAs to the &#8216;&#8211;lba=&#8217; option and the corresponding number(s) to unmap to the &#8216;&#8211;num=&#8217; option. The other way is by putting start LBA and number to unmap pairs in a file whose name is given to the &#8216;&#8211;in=&#8217; option. All values are assumed to be decimal unless prefixed by &quot;0x&quot; (or &quot;0X&quot;) or have a trailing &quot;h&quot; (or &quot;H&quot;) in which case they are interpreted as hexadecimal. </p>
<p> When the &#8216;&#8211;lba=&#8217; option is given then the &#8216;&#8211;num=&#8217; option must also be given. If one has a comma separated list as its argument then the other must have the same number of elements in its list. The arguments can use a single space as a separator but need to be in quotes or escaped to not be misinterpreted by the shell. </p>
<p> With the &#8216;&#8211;in=FILE&#8217; option an even number of values must be found and are interpreted as pairs: the first value in each pair is a starting LBA and the second value is the number to unmap from that LBA. Everything from and including a &quot;#&quot; on a line is ignored as are blank lines. Values may be comma, space and tab separated or appear on separate lines.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;anchor</code></p>
<dd>sets the &#8216;Anchor&#8217; bit in the command (introduced in sbc3r22).</p>
<dt><code>-g</code>, <code>&#8211;grpnum</code>=<i>GN</i></p>
<dd>sets the &#8216;Group number&#8217; field to <i>GN</i>. Defaults to a value of zero. <i>GN</i> should be a value between 0 and 31.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-I</code>, <code>&#8211;in</code>=<i>FILE</i></p>
<dd>where <i>FILE</i> is a file name containing pairs of values. The first member of each pair is a starting LBA and the second member of the pair is the number of logical blocks to unmap from and including that starting LBA. Values are interpreted as decimal unless indicated otherwise. This option cannot be present with the &#8216;&#8211;lba=&#8217; option.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA,LBA&#8230;</i></p>
<dd>where <i>LBA,LBA&#8230;</i> is a string of comma (or space) separated values that are interpreted as starting logical block addresses. Each number is interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). An argument that contains any space separators needs to be quoted (or otherwise escaped). When this option is given then the &#8216;&#8211;num=&#8217; option must also be given and they must contain the same number of elements in their arguments.</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM,NUM&#8230;</i></p>
<dd>where <i>NUM,NUM&#8230;</i> is a string of comma (or space) separated values that are interpreted as a number of logical blocks to unmap. Each number is interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). Note that 0 blocks is acceptable. An argument that contains any space separators needs to be quoted (or otherwise escaped). When this option is given then the &#8216;&#8211;lba=&#8217; option must also be given and they must contain the same number of elements in their arguments.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>TO</i></p>
<dd>where <i>TO</i> is a timeout value (in seconds) for the UNMAP command. The default value is 60 seconds.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>Some limits: an LBA can be up to 64 bits, a NUM up to 32 bits (imposed by structure of UNMAP SCSI command parameter data). The NUM is further constrained by the MAXIMUM UNMAP LBA COUNT field in the BLOCK LIMITS VPD page (0xb0). The maximum number of LBA,NUM pairs is limited to 128 by this utility and may be further constrained by the MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT field in the BLOCK LIMITS VPD page. </p>
<p> Since it is unclear how long the UNMAP command will take to execute a &#8216;&#8211;timeout=&quot; option has been provided. The default timeout period is 60 seconds. If all the logical blocks on a logical unit (e.g. a disk drive) are to be unmapped then the FORMAT UNIT SCSI command (see the sg_format utility) may be considered as an alternative. </p>
<p> Support for logical block provisioning is indicated by the LBPME bit in the response to the SCSI READ CAPACITY (16) command (see the sg_readcap utility). </p>
<p> In SBC-3 revision 25 the LBPU and ANC_SUP bits where added to the Logical Block Provisioning VPD page. When LBPU is set it indicates that the device supports the UNMAP command. When the ANC_SUP bit is set it indicates the device supports anchored LBAs.</p>
<h2>Examples</h2>
<p>In the examples directory of the sg3_utils package there is a sg_unmap_example.txt file that shows the format that the &#8216;&#8211;in=&#8217; option accepts.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_unmap is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_format,sg_get_lba_status,sg_readcap,sg_vpd,sg_write_same(sg3_utils)</code> </p>
