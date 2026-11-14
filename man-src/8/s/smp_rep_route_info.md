---
title: "smp_rep_route_info(8)"
name: "smp_rep_route_info"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_route_info/"
description: "smp_rep_route_info – invoke REPORT ROUTE INFORMATION SMP function"
---

<p>smp_rep_route_info &#8211; invoke REPORT ROUTE INFORMATION SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_route_info</code> [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;multiple</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;zero</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT ROUTE INFORMATION function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> There are two expander route table types: phy-based and expander-based. The expander-based route table was introduced in SAS-2 and supersedes the phy-based route tables. The REPORT ROUTE INFORMATION function is associated with a phy-based route table. The CONFIGURE ROUTE INFORMATION function is provided to manually set up a phy-based route table. </p>
<p> Each phy in a SAS expander that has an associated routing attribute of &quot;table&quot; has a router table. The number of rows (or entries) in each router table is given by the &quot;expander route indexes&quot; field in the response of the REPORT GENERAL function. </p>
<p> When the <i>&#8211;multiple</i> option is given, the REPORT ROUTE INFORMATION function is called multiple times. The index value increments on each iteration, starting from <i>&#8211;index=IN</i> (default 0). If <i>&#8211;num=NUM</i> is given and <i>NUM</i> is greater than zero then that is the maximum number of iterations performed. If <i>&#8211;num=NUM</i> is not given (or <i>NUM</i> is zero) then iterations continue until there are 4 adjacent disabled route entries (or some error is detected).</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>IN</i></p>
<dd>expander route index. <i>IN</i> is a value between 0 and 65535. Default is 0. More precisely the maximum index value is (expander_route_indexes &#8211; 1).</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-m</code>, <code>&#8211;multiple</code></p>
<dd>call the REPORT ROUTE INFORMATION function multiple times, starting at <i>&#8211;index=IN</i>, incrementing the index value on each iteration for a maximum of <i>&#8211;num=NUM</i> iterations. For each enabled route table entry, one line is output. If <i>&#8211;num=NUM</i> is not given (or <i>NUM</i> is zero) then iterations continue until 4 adjacent disabled entries are found (or some error occurs).</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>used with <i>&#8211;multiple</i> option to specify the maximum number of iterations.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. Default is 0.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd>zero the Allocated Response Length field in the request. This option also zeros the Request Length field in the request. This is required for strict SAS-1.1 compliance. However this option should not be given in SAS-2 and later; if it is given an abridged response may result.</dl>
<h2>Conforming To</h2>
<p>The SMP REPORT ROUTE INFORMATION function was introduced in SAS-1 . The &quot;Expander change count&quot; field was added in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_general(smp_utils)</code> </p>
