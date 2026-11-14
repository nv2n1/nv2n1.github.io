---
title: "smp_conf_general(8)"
name: "smp_conf_general"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_conf_general/"
description: "smp_conf_general – invoke CONFIGURE GENERAL SMP function"
---

<p>smp_conf_general &#8211; invoke CONFIGURE GENERAL SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_conf_general</code> [<i>&#8211;connect=CO</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;inactivity=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;nexus=NE</i>] [<i>&#8211;open=OP</i>] [<i>&#8211;power=PD</i>] [<i>&#8211;raw</i>] [<i>&#8211;reduced=RE</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) CONFIGURE GENERAL function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;connect</code>=<i>CO</i></p>
<dd>sets the &quot;update STP maximum connect time limit&quot; flag and the corresponding &quot;STP maximum connect time limit&quot; field to <i>CO</i>. Unit of <i>CO</i> is 100 microseconds. A <i>CO</i> of zero is taken to mean no maximum connection time limit.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;inactivity</code>=<i>IN</i></p>
<dd>sets the &quot;update STP bus inactivity time limit&quot; flag and the corresponding &quot;STP bus inactivity time limit&quot; field to <i>IN</i>. Unit of <i>IN</i> is 100 microseconds. A <i>IN</i> of zero is taken to mean no bus inactivity time limit.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-n</code>, <code>&#8211;nexus</code>=<i>NE</i></p>
<dd>sets the &quot;update STP SMP I_T nexus loss time&quot; flag and the corresponding &quot;STP SMP I_T nexus loss time&quot; field to <i>NE</i>. Unit of <i>NE</i> is one millisecond. A <i>NE</i> of zero is taken to mean a vendor specific amount of time; a <i>NE</i> of 65535 means the port shall never recognize an I_T nexus loss.</p>
<dt><code>-o</code>, <code>&#8211;open</code>=<i>OP</i></p>
<dd>sets the &quot;update STP reject to open limit&quot; flag and the corresponding &quot;STP reject to open limit&quot; field to <i>OP</i>. Unit of <i>OP</i> is 10 microseconds.</p>
<dt><code>-p</code>, <code>&#8211;power</code>=<i>PD</i></p>
<dd>sets the &quot;update power done timeout&quot; flag and the corresponding &quot;power doen timeout&quot; field to <i>PD</i>. Unit of <i>PD</i> is 1 second. A <i>PD</i> value of 0 is interpreted as don&#8217;t change the current value. The maximum value of <i>PD</i> is 255 and means the time limit is vendor specific.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;reduced</code>=<i>RE</i></p>
<dd>sets the &quot;update Initial time to reduced functionality&quot; flag and the corresponding &quot;Initial time to reduced functionality&quot; field to <i>RE</i>. Unit of <i>RE</i> is 100 milliseconds. The maximum permitted <i>RE</i> value is 255 which corresponds to 25.5 seconds.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP CONFIGURE GENERAL function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_rep_general(smp_utils)</code> </p>
