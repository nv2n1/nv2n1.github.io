---
title: "sg_reassign(8)"
name: "sg_reassign"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_reassign/"
description: "sg_reassign – send SCSI REASSIGN BLOCKS command"
---

<p>sg_reassign &#8211; send SCSI REASSIGN BLOCKS command</p>
<h2>Synopsis</h2>
<p><code>sg_reassign</code> [<i>&#8211;address=A,A&#8230;</i>] [<i>&#8211;dummy</i>] [<i>&#8211;eight=0|1</i>] [<i>&#8211;grown</i>] [<i>&#8211;help</i>] [<i>&#8211;longlist=0|1</i>] [<i>&#8211;primary</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI REASSIGN BLOCKS command to <i>DEVICE</i>. Alternatively this utility can find the number of element in a &quot;grown&quot; or &quot;primary&quot; defect list with a SCSI READ DEFECT DATA (10) command. These SCSI commands are defined in SBC-2 for direct access devices (e.g. a disk). Reassign blocks is designed to change the physical location of a logical block that is known or suspected to be defective to another area on the media. Disks are typically formatted with blocks held in reserve for this situation. </p>
<p> If neither the <i>&#8211;grown</i> nor <i>&#8211;primary</i> option is supplied then one or more addresses need to be given. If the address (or all of the addresses) fit into 4 bytes and &#8216;&#8211;eight=1&#8217; is not given then the parameter block passed to <i>DEVICE</i> is made up of 4 byte logical block addresses. If any of the addresses need more than 4 bytes to represent (i.e. &gt;= 2**32) or &#8216;&#8211;eight=1&#8217; is given then the parameter block passed to <i>DEVICE</i> is made up of 8 byte logical block addresses.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;address</code>=<i>A,A&#8230;</i></p>
<dd>where <i>A,A&#8230;</i> is a string of comma separated numbers. Each number is interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). If multiple logical block addresses are given they must be separated by a comma or a (single) space. A string that contains any space separators needs to be quoted. At least one address must be given.</p>
<dt><code>-a</code>, <code>&#8211;address</code>=-</p>
<dd>reads one or more logical block addresses from stdin. These may be comma, space, tab or linefeed (newline) separated. If a line contains &quot;#&quot; then the remaining characters on that line are ignored. Otherwise each non separator sequence of characters should resolve to a decimal number unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or has a trailing &#8216;h&#8217;). At least one address must be given.</p>
<dt><code>-d</code>, <code>&#8211;dummy</code></p>
<dd>prepare for but do not execute the SCSI REASSIGN BLOCKS command. Since the REASSIGN BLOCKS command is essentially irreversible, paranoid users may wish to check the invocation of this utility before reassigning defective blocks on a disk. Useful with &#8216;-vv&#8217; for those who wish to view the parameter block that will accompany the command.</p>
<dt><code>-e</code>, <code>&#8211;eight</code>=0 | 1</p>
<dd>when value is 1 then it sets the &#8216;LONGLBA&#8217; flag in the command indicating that the addresses in the associated parameter block are 8 byte quantities. When value is 0 then it clears the &#8216;LONGLBA&#8217; flag in the command indicating that the addresses in the associated parameter block are 4 byte quantities. If this option is not given then 4 byte quantities are assumed unless one of the address is too large.</p>
<dt><code>-g</code>, <code>&#8211;grown</code></p>
<dd>use the SCSI READ DEFECT DATA (10) command to determine the number of elements in the &quot;grown defect list&quot;. When this option is given there is no reassignment of blocks (i.e. this utility is passive). When this option is given then the <i>&#8211;address=</i> option is not permitted. See the discussion below concerning the relationship between reassigned blocks and the grown defect list. This list is sometimes referred to as the GLIST.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-l</code>, <code>&#8211;longlist</code>=0 | 1</p>
<dd>sets the REASSIGN BLOCKS cdb field of the same name to the given value. Only 1000 addresses are permitted so there should be no need to specify a value of 1. The short list variant restricts the parameter block length to 2 ** 16 bytes (i.e. about 16000 4 byte addresses or 8000 8 byte addresses). Added for completeness.</p>
<dt><code>-p</code>, <code>&#8211;primary</code></p>
<dd>use the SCSI READ DEFECT DATA (10) command to determine the number of elements in the &quot;primary defect list&quot; which is established during the manufacturing process. When this option is given there is no reassignment of blocks (i.e. this utility is passive). When this option is given then the <i>&#8211;address=</i> option is not permitted. This list is sometimes referred to as the PLIST.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>Note that if the ARRE field (for reads) and/or the AWRE field (for writes) are set in the &quot;Read Write Error Recovery&quot; mode page then recoverable read and/or write errors cause automatic reassignment of the defective block. The PER bit in the same mode page controls whether a RECOVERED ERROR sense key is reported on not (PER=1 implies do report). Irrespective of the ARRE, AWRE or PER field settings, the error counter log pages reflect any errors (recovered or otherwise). Whenever a block is reassigned, a new entry is added in the &quot;grown&quot; defect list. Apart from doing selftests (see sg_senddiag or smartmontools) regularly, monitoring the grown defect list of a disk is a reasonable metric of its health. If the grown list starts growing quickly that is an ominous sign. The best grown defect lists are empty ones. The number of elements in the grown defect list can be viewed with the <i>&#8211;grown</i> option. The contents of the grown defect list can be viewed with the &#8216;sginfo -G&#8217; utility. </p>
<p> If an unrecoverable error is detected at a logical block address then REASSIGN BLOCKS is needed to reassign the block. Also if the ARRE and/or AWRE fields are clear and a recoverable error is detected then the logical block in question may be reassigned with this utility (otherwise the error counter log pages will continually be incremented for each recovered access). </p>
<p> The number of blocks held in reserve for the purposes of REASSIGN BLOCKS is vendor specific and may well be limited to the zone within the media where the original (defective) block lay. When this number is exhausted subsequent invocations of this utility may result in a sense key of hardware error and an additional sense of &#8216;No defect spare location available&#8217;. The next step would be to reformat the disk (or get a replacement). </p>
<p> The SBC-2 draft standard (revision 16) notes that when multiple addresses are given to the SCSI REASSIGN BLOCKS command and there is some failure at one of the later addresses then all addresses prior to that have already be reassigned. Care should be taken in such a case. Re-executing the command with the same addresses will cause the earlier addresses to be reassigned again. At some stage the disk will run out of reserved locations. So unless a large number of addresses are involved it may be safer to reassign them one address at a time.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_reassign is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_format,sginfo,sg_senddiag(all in sg3_utils), sdparm(sdparm),</code> <code>smartmontools(internet, sourceforge)</code> </p>
