---
title: "sg_opcodes(8)"
name: "sg_opcodes"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_opcodes/"
description: "sg_opcodes – report supported SCSI commands or task management functions"
---

<p>sg_opcodes &#8211; report supported SCSI commands or task management functions</p>
<h2>Synopsis</h2>
<p><code>sg_opcodes</code> [<i>&#8211;alpha</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;no-inquiry</i>] [<i>&#8211;opcode=OP</i>] [<i>&#8211;raw</i>] [<i>&#8211;rctd</i>] [<i>&#8211;repd</i>] [<i>&#8211;sa=SA</i>] [<i>&#8211;tmf</i>] [<i>&#8211;unsorted</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_opcodes</code> [<i>-a</i>] [<i>-n</i>] [<i>-o=OP</i>] [<i>-q</i>] [<i>-R</i>] [<i>-s=SA</i>] [<i>-t</i>] [<i>-u</i>] [<i>-v</i>] [<i>-V</i>] [<i>-?</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends a SCSI REPORT SUPPORTED OPERATION CODES or a REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command to the <i>DEVICE</i> and then outputs the response. The default action is to report supported operation codes. In this mode it will either list all supported commands or give detailed information on a specific command identified by the <i>&#8211;opcode=OP</i> option (perhaps with additional information from the <i>&#8211;sa=SA</i> option). </p>
<p> The name of a SCSI command depends on its peripheral device type (e.g. a disk). The REPORT SUPPORTED OPERATION CODES and REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS commands are not supported in the MMC command set for CD and DVD devices. This utility does an INQUIRY to obtain the peripheral device type and prints out the vendor, product and revision strings. </p>
<p> A similar facility to query supported operation codes previously was available via the CmdDt bit in the SCSI INQUIRY command (see <a href="/docs/linux/man/8-sg_inq/">sg_inq</a>(8)). However that facility was made obsolete and replaced by the REPORT SUPPORTED OPERATION CODES command in SPC-3 (revision 4) during February 2002. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;alpha</code></p>
<dd>when all supported commands are being listed there is no requirement for the device server (i.e. the <i>DEVICE</i>) to sort the list of commands. When this option is given the list of supported commands is sorted by name (alphabetically). When this option and the <code>&#8211;unsorted</code> option are both _not_ given then the list of supported commands is sorted numerically (first by operation code and then by service action).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>outputs the usage message summarizing command line options then exits. Ignores <i>DEVICE</i> if given.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>outputs the response in ASCII hexadecimal to stdout.</p>
<dt><code>-n</code>, <code>&#8211;no-inquiry</code></p>
<dd>Prior to calling a SCSI REPORT SUPPORTED OPERATION CODES or a REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command, a SCSI INQUIRY command is performed. The reason is to determine the peripheral device type (pdt) of the <i>DEVICE</i> as this is helpful in translating operation codes to the command names. By default this utility prints a summary of INQUIRY command response on stdout. If this option (or the <i>&#8211;raw</i> option) is given then that summary is not printed on stdout.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-o</code>, <code>&#8211;opcode</code>=<i>OP</i></p>
<dd>the <i>DEVICE</i> will be queried for the given operation code ( i.e. the <i>OP</i> value) which is the first byte of a SCSI command. <i>OP</i> is decimal unless prefixed by &quot;0x&quot; or it has a trailing &quot;h&quot;. <i>OP</i> should be in the range 0 to 255 (0xff) inclusive. When this option is not given then all available SCSI commands supported by the <i>DEVICE</i> are listed.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the response in binary to stdout. Error messages and warnings, if any, are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;rctd</code></p>
<dd>set report command timeout descriptor (RCTD) bit in the cdb. The response may or may not contain command timeout descriptors. If available they are output. If supported there are two values: a nominal command timeout and a recommended command timeout. Both have units of seconds. A value of zero means that no timeout is indicated and this is shown in the corresponding decoded output as &quot;-&quot;.</p>
<dt><code>-q</code>, <code>&#8211;repd</code></p>
<dd>set read extended parameter data (REPD) bit in the report task management functions cdb. 16 bytes rather than the default 4 bytes expected in the response. This was added in SPC-4 (revision 26).</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SA</i></p>
<dd>the <i>DEVICE</i> will be queried for a command with the given service action (i.e. the <i>SA</i> value). Used in conjunction with the <i>&#8211;opcode=OP</i> option. If this option is not given, <i>&#8211;opcode=OP</i> is given and the command in question does have a service action then a value of 0 will be assumed. <i>SA</i> is decimal and expected to be in the range 0 to 65535 (0xffff) inclusive.</p>
<dt><code>-t</code>, <code>&#8211;tmf</code></p>
<dd>list supported task management functions. This is done with the SCSI REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command. When this option is chosen the <i>&#8211;alpha</i>, <i>&#8211;opcode=OP</i>, <i>&#8211;rctd</i>, <i>&#8211;sa=SA</i> and <i>&#8211;unsorted</i> options are ignored.</p>
<dt><code>-u</code>, <code>&#8211;unsorted</code></p>
<dd>when all supported commands are being listed there is no requirement for the device server (i.e. the <i>DEVICE</i>) to sort the list of commands. When this option is given the list of supported commands is in the order given by the <i>DEVICE</i>. When this option is not given the supported commands are sorted numerically (first by operation code and then by service action).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>As of SPC-4 revision 7a the recognized task management functions are: abort set, abort task set, clear ACA, clear task set, I_T nexus reset, logical unit reset, query task, target reset and wakeup. As of SPC-4 revision 26 target reset and wakeup have been made obsolete while query task set and query asynchronous event notification have been added. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_opcodes /dev/sda&quot; will work in the 2.6 series kernels.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_opcodes is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option.</p>
<dl>
<dt><code>-a</code></p>
<dd>sort command alphabetically. Equivalent to <i>&#8211;alpha</i> in main description.</p>
<dt><code>-n</code></p>
<dd>don&#8217;t print a summary of the SCSI INQUIRY response on stdout.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-o</code>=<i>OP</i></p>
<dd>the <i>DEVICE</i> will be queried for the given operation code (i.e. <i>OP</i>) which is the first byte of a SCSI command. <i>OP</i> is hexadecimal and expected to be in the range 0 to ff inclusive. When this option is not given then all available SCSI commands supported by the <i>DEVICE</i> are listed.</p>
<dt><code>-q</code></p>
<dd>set the read extended parameter data (REPD) bit in report TMF cdb. Equivalent to <i>&#8211;repd</i> in main description.</p>
<dt><code>-R</code></p>
<dd>set the report command timeout descriptor (RCTD) bit in cdb. Equivalent to <i>&#8211;rctd</i> in main description.</p>
<dt><code>-s</code>=<i>SA</i></p>
<dd>the <i>DEVICE</i> will be queried for a command with the given service action (i.e. <i>SA</i>). Used in conjunction with the <i>-o=OP</i> option. If this option is not given, <i>-o=OP</i> is given and the command in question does have a service action then a value of 0 will be assumed. <i>SA</i> is hexadecimal and expected to be in the range 0 to ffff inclusive.</p>
<dt><code>-t</code></p>
<dd>list supported task management functions. Equivalent to <i>&#8211;tmf</i> in the main description.</p>
<dt><code>-u</code></p>
<dd>output all supported commands in the order given by <i>DEVICE</i>. Equivalent to <i>&#8211;unsorted</i> in main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</p>
<dt><code>-?</code></p>
<dd>output usage message. Ignore all other parameters.</dl>
<h2>Examples</h2>
<p>The examples in this page use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. To see the information about a specific command give its operation code to the &#8216;&#8211;op=&#8217; option. A command line invocation is shown first followed by a typical response: </p>
<pre><code># sg_opcodes --op=93h /dev/sdb
Opcode=0x93

Command_name: Write same(16)

Command supported [conforming to SCSI standard]

Usage data: 93 e2 00 00 00 00 ff ff ff ff 00 00 ff ff 00 00</code></pre>
<p> The next example shows the supported task management functions:<br />
#&nbsp;<wbr>sg_opcodes &#8211;tmf -n&nbsp;<wbr>/dev/sdb Task Management Functions supported by device: </p>
<p>&nbsp;<wbr>Abort task </p>
<p>&nbsp;<wbr>Abort task set </p>
<p>&nbsp;<wbr>Clear ACA </p>
<p>&nbsp;<wbr>Clear task set </p>
<p>&nbsp;<wbr>Logical unit reset </p>
<p>&nbsp;<wbr>Query task</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq(sg3_utils)</code> </p>
