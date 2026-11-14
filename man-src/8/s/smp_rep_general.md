---
title: "smp_rep_general(8)"
name: "smp_rep_general"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_general/"
description: "smp_rep_general – invoke REPORT GENERAL SMP function"
---

<p>smp_rep_general &#8211; invoke REPORT GENERAL SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_general</code> [<i>&#8211;brief</i>] [<i>&#8211;changecount</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;zero</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT GENERAL function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>reports (prints to stdout) only a few important fields from the response.</p>
<dt><code>-c</code>, <code>&#8211;changecount</code></p>
<dd>reports (prints to stdout) the value of the expander change count field from the response. The value is printed in decimal and is in the range 0 to 65535. Only expanders compliant with SAS-1.1 (and earlier) should yield 0. [Expanders compliant with SAS-2 (and later) should set the &quot;long response&quot; bit in the REPORT GENERAL response to 1.]</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd>zero the Allocated Response Length field in the request. This is required for strict SAS-1.1 compliance. However this option should not be given in SAS-2 and later; if it is given an abridged response may result.</dl>
<h2>Examples</h2>
<p>See &quot;Examples&quot; section in <a rel="nofollow" href="http://sg.danny.cz/sg/smp_utils.html">http://sg.danny.cz/sg/smp_utils.html</a></p>
<h2>Conforming To</h2>
<p>The SMP REPORT GENERAL function was introduced in SAS-1, with small additions in SAS-1.1 . There have been a large number of additions in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_discover(smp_utils)</code> </p>
