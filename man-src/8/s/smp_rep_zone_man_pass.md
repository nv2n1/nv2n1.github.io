---
title: "smp_rep_zone_man_pass(8)"
name: "smp_rep_zone_man_pass"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_zone_man_pass/"
description: "smp_rep_zone_man_pass – invoke REPORT ZONE MANAGER PASSWORD function"
---

<p>smp_rep_zone_man_pass &#8211; invoke REPORT ZONE MANAGER PASSWORD function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_zone_man_pass</code> [<i>&#8211;fpass=FP</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;phex</i>] [<i>&#8211;raw</i>] [<i>&#8211;report=RT</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT ZONE MANAGER PASSWORD function requests to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-F</code>, <code>&#8211;fpass</code>=<i>FP</i></p>
<dd>where <i>FP</i> is the name of a file which the password will be written to. The default action (in the absence of this option) is to write the password to stdout.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal. To only see the password in hexadecimal use the <i>&#8211;phex</i> option.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-p</code>, <code>&#8211;phex</code></p>
<dd>Output the password in comma separated hexadecimal bytes. In the absence of this option the password is output in ASCII surrounded by single quotes. Note the hexadecimal bytes are output with a hex indication (i.e. there is nos leading &quot;0x&quot; nor trailing &quot;h&quot;).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;report</code>=<i>RT</i></p>
<dd>set the &#8216;report type&#8217; field in the SMP request. <i>RT</i> may take these values: 0 for report the current zone manager password (default); 1 is reserved; 2 for report the saved zone manager password; 3 for report the default zone manager password.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP REPORT ZONE MANAGER PASSWORD function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_conf_zone_man_pass, smp_zone_lock(smp_utils)</code> </p>
