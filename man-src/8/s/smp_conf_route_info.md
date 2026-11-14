---
title: "smp_conf_route_info(8)"
name: "smp_conf_route_info"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_conf_route_info/"
description: "smp_conf_route_info – invoke CONFIGURE ROUTE INFORMATION SMP function"
---

<p>smp_conf_route_info &#8211; invoke CONFIGURE ROUTE INFORMATION SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_conf_route_info</code> [<i>&#8211;disable</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;routed=R_SAS_ADDR</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) CONFIGURE ROUTE INFORMATION function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> There are two expander route table types: phy-based and expander-based. The expander-based route table was introduced in SAS-2 and supersedes the phy-based route tables. The CONFIGURE ROUTE INFORMATION function is associated with a phy-based route table. The REPORT ROUTE INFORMATION function is provided to report phy-based route table entries. </p>
<p> Each phy in a SAS expander that has an associated routing attribute of &quot;table&quot; has a router table. The number of rows (or entries) in each router table is given by the &quot;expander route indexes&quot; field in the response of the REPORT GENERAL function.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;disable</code></p>
<dd>set the &quot;disable expander route entry&quot; flag in a row of the router table associated with <i>&#8211;phy=ID</i> of the given SMP target (e.g. an expander). Within the router table the row that is disabled is identified by the expander route index given by <i>&#8211;index=IN</i>.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>IN</i></p>
<dd>expander route index. <i>IN</i> is a value between 0 and 65535. Default is 0. More precisely the maximum index value is (expander_route_indexes &#8211; 1).</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. Default is 0.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;routed</code>=<i>R_SAS_ADDR</i></p>
<dd>specifies the SAS address to be placed in a row (given by <i>&#8211;index=IN</i>) of the router table associated with <i>&#8211;phy=ID</i>. Default value is 0. The <i>R_SAS_ADDR</i> is in decimal but most SAS addresses are given in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP CONFIGURE ROUTE INFORMATION function was introduced in SAS-1 . The &quot;Expander change count&quot; field was added in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_general, smp_rep_route_info(smp_utils)</code> </p>
