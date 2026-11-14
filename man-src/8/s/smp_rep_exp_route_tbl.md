---
title: "smp_rep_exp_route_tbl(8)"
name: "smp_rep_exp_route_tbl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_exp_route_tbl/"
description: "smp_rep_exp_route_tbl – invoke REPORT EXPANDER ROUTE TABLE LIST SMP function"
---

<p>smp_rep_exp_route_tbl &#8211; invoke REPORT EXPANDER ROUTE TABLE LIST SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_exp_route_tbl</code> [<i>&#8211;brief</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT EXPANDER ROUTE TABLE LIST function request to an SMP target and decodes or outputs the response. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> There are two expander route table types: phy-based and expander-based. The expander-based route table was introduced in SAS-2 and supersedes the phy-based route tables. The REPORT EXPANDER ROUTE TABLE LIST function is associated with an expander-based route table. There is no corresponding CONFIGURE function because a expander-based route table is self-configured.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>reduce the decoded response output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>IN</i></p>
<dd><i>IN</i> is the starting routed SAS address index. The default value is 0.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>maximum number of descriptors to fetch (default is 62). Note that maximum SMP frame size is 1028 bytes (including a trailing 4 byte CRC) so 62 descriptors is the maximum number that can fit in one response.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>starting phy identifier within bitmap. <i>ID</i> should be one of 0 (the default), or a multiple of 48. Note there is only one expnder route table per expander, not one per phy.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP REPORT EXPANDER ROUTE TABLE LIST function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_route_info</code> </p>
