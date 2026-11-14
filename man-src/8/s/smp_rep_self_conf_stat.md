---
title: "smp_rep_self_conf_stat(8)"
name: "smp_rep_self_conf_stat"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_self_conf_stat/"
description: "smp_rep_self_conf_stat – invoke REPORT SELF-CONFIGURATION STATUS SMP function"
---

<p>smp_rep_self_conf_stat &#8211; invoke REPORT SELF-CONFIGURATION STATUS SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_self_conf_stat</code> [<i>&#8211;brief</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=SDI</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;last</i>] [<i>&#8211;one</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT SELF-CONFIGURATION STATUS function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>lessen the amount of header information output and compress each self confuration status descriptor to one line of output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>SDI</i></p>
<dd><i>SDI</i> is the starting self-configuration status descriptor index, an integer in the range 0 to 65535. The default value is 1 . If <i>SDI</i> is 0 then no descriptors are placed in the response plus the &quot;starting self-configuration status descriptor index&quot; and &quot;total number of self-configuration status descriptors&quot; fields in the response are both set to 0. That makes setting <i>SDI</i> to 0 a lot less useful tha it could have been. <i>SDI</i> may be decimal (default) or hexadecimal prefixed by &#8216;0x&#8217; (or &#8216;0X&#8217;) or with a &#8216;h&#8217; (or &#8216;H&#8217;) suffix.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-l</code>, <code>&#8211;last</code></p>
<dd>Sends a REPORT SELF-CONFIGURATION STATUS request to find out the contents of the &quot;last self-configuration status descriptor index&quot; field in the response. If it is different from <i>SDI</i> then it re-issues that request with the &quot;starting self-configuration status descriptor index&quot; field set to the &quot;last&quot; value. Often only the last (i.e. most recent) recorded descriptor is of interest and that is what this option should show. In cases there may be more than one descriptor starting at the last index.</p>
<dt><code>-o</code>, <code>&#8211;one</code></p>
<dd>If multiple self-configuration status descriptors are found, then only output the first one.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>The &quot;last self-configuration status descriptor index&quot; field in the response may indicate the lowest index of the last recorded (i.e. most recent) &quot;clump&quot; of status descriptors placed in the expander&#8217;s storage. </p>
<p> This utility flags the &quot;last self-configuration status descriptor index&quot; descriptor in its output with a &quot;&gt;&gt;&gt;&quot; indication. For brief output the descriptor line starts with &quot;&gt;&gt;&gt;&quot; while for normal output (i.e. when <i>&#8211;brief</i> not given) the index has &quot;&gt;&gt;&gt;&quot; placed in front of it.</p>
<h2>Conforming To</h2>
<p>The SMP REPORT SELF-CONFIGURATION STATUS function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_general, smp_discover, smp_discover_list(smp_utils)</code> </p>
