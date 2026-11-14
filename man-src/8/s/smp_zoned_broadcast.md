---
title: "smp_zoned_broadcast(8)"
name: "smp_zoned_broadcast"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_zoned_broadcast/"
description: "smp_zoned_broadcast – invoke ZONED BROADCAST SMP function"
---

<p>smp_zoned_broadcast &#8211; invoke ZONED BROADCAST SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_zoned_broadcast</code> [<i>&#8211;broadcast=BT</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;fszg=FS</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;szg=ZGL</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) ZONED BROADCAST function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> This function requires zoning to be enabled. To send a Broadcast (Change) in the absence of zoning, the least intrusive way seems to be to use a PHY CONTROL request to send a link reset to an expander phy. Broadcast (Change) should cause a management application client behind an SMP initiator port (e.g. a SAS HBA) to start a discover process.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;broadcast</code>=<i>BT</i></p>
<dd><i>BT</i> is the broadcast type, an integer in the range 0 (default) to 15. Broadcast (Change) corresponds to 0 and will cause SMP initiators that receive it to do their discover process. Other known broadcast types are listed in the NOTES section. <i>BT</i> may be decimal (default) or hexadecimal prefixed by &#8216;0x&#8217; (or &#8216;0X&#8217;) or with a &#8216;h&#8217; (or &#8216;H&#8217;) suffix.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response. In SPL-1 this field is marked as &quot;restricted (for expected expander change count)&quot;.</p>
<dt><code>-F</code>, <code>&#8211;fszg</code>=<i>FS</i></p>
<dd>where <i>FS</i> is the name of a file which contains one or more source zone groups to send a broadcast to. The zone groups can be given in decimal (default) or hexadecimal prefixed by &#8216;0x&#8217; (or &#8216;0X&#8217;) or with a &#8216;h&#8217; (or &#8216;H&#8217;) suffix. A zone group is a number in the range 0 to 255. Each zone group can be separated by space, tab, comma or newline. Empty lines and those starting with &quot;#&quot; are ignored.</p>
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
<dt><code>-S</code>, <code>&#8211;szg</code>=<i>ZGL</i></p>
<dd>one or more source zone groups for broadcast can appear as a comma separated list <i>ZGL</i>. The may be decimal (default) or hexadecimal prefixed by &#8216;0x&#8217; (or &#8216;0X&#8217;) or with a &#8216;h&#8217; (or &#8216;H&#8217;) suffix. A zone group is a number in the range 0 to 255. Either this option or <i>&#8211;fszg=FS</i> (but not both) should be given.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>The following is a list of broadcast types:<br />
 0 Broadcast (Change)<br />
 1 Broadcast (Reserved change 0)<br />
 2 Broadcast (Reserved change 1)<br />
 3 Broadcast (SES)<br />
 4 Broadcast (Expander)<br />
 5 Broadcast (Asynchronous event)<br />
 6 Broadcast (Reserved 3)<br />
 7 Broadcast (Reserved 4)<br />
 8 Broadcast (Zone activate) </p>
<p> The remaining zone types (9 to 15) may be issued by the ZONED BROADCAST function.</p>
<h2>Conforming To</h2>
<p>The SMP ZONED BROADCAST function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_zone_lock, smp_zone_unlock, smp_ena_dis_zoning(smp_utils)</code> </p>
