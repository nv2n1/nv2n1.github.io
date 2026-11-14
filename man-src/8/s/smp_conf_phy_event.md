---
title: "smp_conf_phy_event(8)"
name: "smp_conf_phy_event"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_conf_phy_event/"
description: "smp_conf_phy_event – invoke CONFIGURE PHY EVENT function"
---

<p>smp_conf_phy_event &#8211; invoke CONFIGURE PHY EVENT function</p>
<h2>Synopsis</h2>
<p><code>smp_conf_phy_event</code> [<i>&#8211;clear</i>] [<i>&#8211;enumerate</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;file=FILE</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;pes=PES,PES&#8230;</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;thres=THR,THR&#8230;</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) CONFIGURE PHY EVENT function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> The function request contains zero or more phy event configuration descriptors. Each descriptor is 8 byte long and contains a phy event source (one byte long) and optionally a peak value detector threshold which is 32 bits long (4 bytes). These values can either be supplied on the command line as the arguments to the <i>&#8211;pes</i> and <i>&#8211;thres</i> options, or within a <i>FILE</i> given to the <i>&#8211;file</i> option. </p>
<p> Once a phy event source has been configured by this function, its counters should be readable with the REPORT PHY EVENT or REPORT PHY EVENT LIST functions. Peak value detector thresholds should only be non-zero for phy event sources whose type is &quot;peak value detector&quot;. If the threshold value is exceeded the expander will originate a Broadcast(Expander).</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;clear</code></p>
<dd>sets the CLEAR PEAKS bit the in function request. This will cause all peak value detectors associated with this phy (i.e. <i>ID</i>) to be cleared to zero.</p>
<dt><code>-e</code>, <code>&#8211;enumerate</code></p>
<dd>enumerate all of the known Phy Event Source names, one per line preceded by its value in hex. Ignores <i>SMP_DEVICE</i> if it is given; most other options are also ignored. Exits after displaying the names.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></p>
<dd>where <i>FILE</i> is a file name containing pairs of values. The first member of each pair is a phy event source and the second member of the pair is a peak value detector threshold. Values are interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). Everything from and including a &quot;#&quot; on a line is ignored as are blank lines. Values may be comma, space and tab separated or appear on separate lines. This option cannot be present with the <i>&#8211;pes</i> option.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254 (default 0).</p>
<dt><code>-P</code>, <code>&#8211;pes</code>=<i>PES,PES&#8230;</i></p>
<dd>where <i>PES,PES&#8230;</i> is a string of comma (or space) separated values that are interpreted as phy event sources (each a value from 0 to 255). Each number is interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). An argument that contains any space separators needs to be quoted (or otherwise escaped). When this option is given then the <i>&#8211;thres</i> option may also be given and they should contain the same number of elements in their arguments.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-T</code>, <code>&#8211;thres</code>=<i>THR,THR&#8230;</i></p>
<dd>where <i>THR,THR&#8230;</i> is a string of comma (or space) separated values that are interpreted as peak value detector thresholds (each a 32 bit value). Each number is interpreted as decimal unless prefixed by &#8216;0x&#8217; or &#8216;0X&#8217; (or it has a trailing &#8216;h&#8217; or &#8216;H&#8217;). An argument that contains any space separators needs to be quoted (or otherwise escaped). When this option is given then the <i>&#8211;pes</i> option must also be given and they should contain the same number of elements in their arguments.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP CONFIGURE PHY EVENT function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_phy_event, smp_rep_phy_event_list</code> </p>
