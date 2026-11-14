---
title: "smp_ena_dis_zoning(8)"
name: "smp_ena_dis_zoning"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_ena_dis_zoning/"
description: "smp_ena_dis_zoning – invoke ENABLE DISABLE ZONING SMP function"
---

<p>smp_ena_dis_zoning &#8211; invoke ENABLE DISABLE ZONING SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_ena_dis_zoning</code> [<i>&#8211;disable</i>] [<i>&#8211;ena-dis=ED</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;save=SAV</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) ENABLE DISABLE ZONING function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> If neither <i>&#8211;disable</i> nor <i>&#8211;ena-dis=ED</i> options are given then enable zoning (i.e. &quot;&#8211;ena-dis=1&quot;) is assumed. </p>
<p> This function does not change the state of the current zoning enabled flag (as seen in the REPORT GENERAL response). Such a state change will occur on a subsequent invocation of the ZONE ACTIVATE function.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;disable</code></p>
<dd>set the &#8216;enable disable zoning&#8217; field in the SMP request to 2 which will disable zoning.</p>
<dt><code>-e</code>, <code>&#8211;ena-dis</code>=<i>ED</i></p>
<dd>set the &#8216;enable disable zoning&#8217; field in the SMP request. <i>ED</i> may take these values: 0 for no change, 1 for enable zoning (default) and 2 for disable zoning. If this option and the <i>&#8211;disable</i> option are both given then they cannot contradict one another.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-S</code>, <code>&#8211;save</code>=<i>SAV</i></p>
<dd>set the &#8216;save&#8217; field in the SMP request. <i>SAV</i> may take these values: 0 for updating the shadow values (default), 1 for updating the saved values, 2 for updating shadow values and if available the saved values, 3 for updating both saved and shadow values.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP ENABLE DISABLE ZONING function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_lock, smp_zone_activate, smp_zone_unlock(smp_utils)</code> </p>
