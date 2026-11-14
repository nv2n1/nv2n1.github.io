---
title: "smp_phy_control(8)"
name: "smp_phy_control"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_phy_control/"
description: "smp_phy_control – invoke PHY CONTROL SMP function"
---

<p>smp_phy_control &#8211; invoke PHY CONTROL SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_phy_control</code> [<i>&#8211;attached=ADN</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;max=MA</i>] [<i>&#8211;min=MI</i>] [<i>&#8211;op=OP</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;pptv=TI</i>] [<i>&#8211;pwrdis=PDC</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;sas_pa=CO</i>] [<i>&#8211;sas_sl=CO</i>] [<i>&#8211;sata_pa=CO</i>] [<i>&#8211;sata_sl=CO</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) PHY CONTROL function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> The PHY CONTROL function is used to change the state of a phy within an SMP target. SMP targets are typically SAS expanders which have multiple phys. Certain operation values (e.g. &#8216;lr&#8217; (link reset) and &#8216;hr&#8217; (hard reset)) change the state of the attached phy. Sending such operation values to the phy in the SMP target that is attached to the originator (i.e. the SMP initiator) may lead to a bad response. </p>
<p> Invoking this utility with no arguments (other than <i>SMP_DEVICE</i> which might be in an environment variable and <i>&#8211;sa=SAS_ADDR</i> which might be in an environment variable or not needed) is harmless. In other words a phy&#8217;s state is only changed when either <i>&#8211;max=MA</i>, <i>&#8211;min=MI</i>, <i>&#8211;op=OP</i> or <i>&#8211;pptv=TI</i> is given with a non default value.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;attached</code>=<i>ADN</i></p>
<dd>specifies the attached device name (<i>ADN</i>). The default value is 0 . The <i>ADN</i> is in decimal but is likely to be a SAS address which is typically shown in hexadecimal. To specify a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it. This option is ignored by the expander unless the &#8216;&#8211;op=sadn&#8217; option is also given.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-M</code>, <code>&#8211;max</code>=<i>MA</i></p>
<dd>permits the programmed maximum physical link rate to be changed on the gven phy. Permitted values are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>&nbsp;<wbr>: no change </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>8</code>&nbsp;<wbr>&nbsp;<wbr>: 1.5 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>9</code>&nbsp;<wbr>&nbsp;<wbr>: 3 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>10</code>&nbsp;<wbr>: 6 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>11</code>&nbsp;<wbr>: 12 Gbps<br />
 Default value is 0.</p>
<dt><code>-m</code>, <code>&#8211;min</code>=<i>MI</i></p>
<dd>permits the programmed minimum physical link rate to be changed on the given phy. Permitted values are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>&nbsp;<wbr>: no change </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>8</code>&nbsp;<wbr>&nbsp;<wbr>: 1.5 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>9</code>&nbsp;<wbr>&nbsp;<wbr>: 3 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>10</code>&nbsp;<wbr>: 6 Gbps </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>11</code>&nbsp;<wbr>: 12 Gbps<br />
 Default value is 0.</p>
<dt><code>-o</code>, <code>&#8211;op</code>=<i>OP</i></p>
<dd>specifies the operation to be performed on the given phy. The <i>OP</i> argument can be either numeric or a string. If a number is given, it is put into the &#8216;phy operation&#8217; field of the request. Allowable strings are abbreviations of which only the first two characters need to match. Each line in the following list contains a numeric value, a string and then a brief explanation: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>:&nbsp;<wbr><code>nop</code>&nbsp;<wbr>&nbsp;<wbr>: no operation </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>1</code>&nbsp;<wbr>:&nbsp;<wbr><code>lr</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: link reset </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>2</code>&nbsp;<wbr>:&nbsp;<wbr><code>hr</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: hard reset </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>3</code>&nbsp;<wbr>:&nbsp;<wbr><code>dis</code>&nbsp;<wbr>&nbsp;<wbr>: disable phy </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>5</code>&nbsp;<wbr>:&nbsp;<wbr><code>cel</code>&nbsp;<wbr>&nbsp;<wbr>: clear error log </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>6</code>&nbsp;<wbr>:&nbsp;<wbr><code>ca</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: clear affiliation </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>7</code>&nbsp;<wbr>:&nbsp;<wbr><code>tspss</code>: transmit SATA port selection signal </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>8</code>&nbsp;<wbr>:&nbsp;<wbr><code>citnl</code>: clear STP I_T nexus loss&nbsp;<wbr>(bit) </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>9</code>&nbsp;<wbr>:&nbsp;<wbr><code>sadn</code>&nbsp;<wbr>: set attached device name<br />
 The default value is 0 (no operation).</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. Default is 0.</p>
<dt><code>-P</code>, <code>&#8211;pptv</code>=<i>TI</i></p>
<dd>partial pathway timeout value. The units are microseconds and the permitted values are between 0 and 15 inclusive. 7 microseconds is recommended by sas2r07.</p>
<dt><code>-D</code>, <code>&#8211;pwrdis</code>=<i>PDC</i></p>
<dd>where <i>PDC</i> is the power disable control value. The default value is 0 which means no change. The value of 1 is reserved; 2, if supported, instructs the management device server to negate the POWER DISABLE signal; while 3, if supported, instructs it to assert that signal. This applies to the phy given by <i>ID</i> (which defaults to 0).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-q</code>, <code>&#8211;sas_pa</code>=<i>CO</i></p>
<dd>set the Enable SAS Partial field to <i>CO</i> which is two bits wide. The defined values for <i>CO</i> are 0 for no change; 1 for manage partial phy power conditions; 2 for disable partial phy power conditions.</p>
<dt><code>-l</code>, <code>&#8211;sas_sl</code>=<i>CO</i></p>
<dd>set the Enable SAS Slumber field to <i>CO</i> which is two bits wide. The defined values for <i>CO</i> are 0 for no change; 1 for manage slumber phy power conditions; 2 for disable slumber phy power conditions.</p>
<dt><code>-Q</code>, <code>&#8211;sata_pa</code>=<i>CO</i></p>
<dd>set the Enable SATA Partial field to <i>CO</i> which is two bits wide. The defined values for <i>CO</i> are 0 for no change; 1 for manage partial phy power conditions; 2 for disable partial phy power conditions.</p>
<dt><code>-L</code>, <code>&#8211;sata_sl</code>=<i>CO</i></p>
<dd>set the Enable SATA Slumber field to <i>CO</i> which is two bits wide. The defined values for <i>CO</i> are 0 for no change; 1 for manage slumber phy power conditions; 2 for disable slumber phy power conditions.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>Once an expander phy has been disabled with <i>&#8211;op=dis</i> then it can be later re-enabled with a link reset or hard reset (e.g. <i>&#8211;op=lr</i>).</p>
<h2>Examples</h2>
<p>See &quot;Examples&quot; section in <a rel="nofollow" href="http://sg.danny.cz/sg/smp_utils.html">http://sg.danny.cz/sg/smp_utils.html</a></p>
<h2>Conforming To</h2>
<p>The SMP PHY CONTROL function was introduced in SAS-1 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_discover(smp_utils)</code> </p>
