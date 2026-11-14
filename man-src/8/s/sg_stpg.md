---
title: "sg_stpg(8)"
name: "sg_stpg"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_stpg/"
description: "sg_stpg – send SCSI SET TARGET PORT GROUPS command"
---

<p>sg_stpg &#8211; send SCSI SET TARGET PORT GROUPS command</p>
<h2>Synopsis</h2>
<p><code>sg_stpg</code> [<i>&#8211;active</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;offline</i>] [<i>&#8211;optimized</i>] [<i>&#8211;raw</i>] [<i>&#8211;standby</i>] [<i>&#8211;state=S,S&#8230;</i>] [<i>&#8211;tp=P,P&#8230;</i>] [<i>&#8211;unavailable</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI SET TARGET PORT GROUPS command to <i>DEVICE</i>. This utility has different modes depending on whether the <i>&#8211;tp=</i> option is given. If <i>&#8211;tp=</i> is given then the SET TARGET PORT GROUPS command parameter block is built with a descriptor for each element in the list given to <i>&#8211;tp=</i>. The corresponding asymmetric access state value is either taken from the <i>&#8211;state=</i> list or, if that is not given, from one of the explicit state options (e.g. <i>&#8211;unavailable</i>), used repeatedly if required. If <i>&#8211;tp=</i> is not given then a sequence of SCSI commands are sent to the <i>DEVICE</i> leading up to the SET TARGET PORT GROUPS command. First an INQUIRY is sent to fetch the device identification VPD page to find the (primary) target port group associated with <i>DEVICE</i>. Then a REPORT TARGET PORT GROUPS command is issued to find the current state and whether a transition to the requested state is supported. If so the SET TARGET PORT GROUPS command is sent. Target port group access is described in SPC-4 found at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> in sections 5.8 and 5.16 (in rev 36e dated 2012/8/24). The SET TARGET PORT GROUPS command is also described in section 6.45 of that document. </p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;active</code></p>
<dd>set active/non-optimized state.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output response to the REPORT TARGET PORT GROUPS command in hex then exit.</p>
<dt><code>-O</code>, <code>-l</code>, <code>&#8211;offline</code></p>
<dd>set offline state. This is the appropriate state to set a target port to prior to removing the device. Note that a relative target port identifier should be given with this state (rather than a target port group identifier that all other states take).</p>
<dt><code>-o</code>, <code>&#8211;optimized</code></p>
<dd>set active/optimized state. If no other state options or <i>&#8211;tp=</i> option are given then active/optimized is the default state.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output response to the REPORT TARGET PORT GROUPS command in binary to stdout then exit.</p>
<dt><code>-s</code>, <code>&#8211;standby</code></p>
<dd>set standby state. Port group shall accept those commands listed for &quot;unavailable&quot; state plus LOG SELECT/SENSE, MODE SELECT/SENSE, RECEIVE DIAGNOSTIC RESULTS, SEND DIAGNOSTIC, PERSISTENT RESERVE IN/OUT commands.</p>
<dt><code>-S</code>, <code>&#8211;state</code>=<i>S,S&#8230;</i></p>
<dd>specifies a comma separated list (one element of more) of states. Either a number or an abbreviation can be given. A number is assumed to be a decimal number unless it is prefixed by &quot;0x&quot; or has a trailing &quot;h&quot; in which case a hexadecimal value is assumed. Only the values 0, 1, 2, 3 or 14 are accepted. The accepted abbreviations are &quot;an&quot;, &quot;ao&quot;, &quot;o&quot;, &quot;s&quot; or &quot;u&quot;; which represent active/<a href="/docs/linux/man/1-non-optimized/">non-optimized</a>(1), active/optimized(0), offline(14), <a href="/docs/linux/man/2-standby/">standby</a>(2) or <a href="/docs/linux/man/3-unavailable/">unavailable</a>(3) respectively.</p>
<dt><code>-t</code>, <code>&#8211;tp</code>=<i>P,P&#8230;</i></p>
<dd>specifies a comma separated list (one element of more). Each elements is either a target port group identifier (when the corresponding state is other than &quot;offline&quot;) or a relative target port identifier (when the corresponding state is &quot;offline&quot;). Each element is assumed to be a decimal number unless it is prefixed by &quot;0x&quot; or has a trailing &quot;h&quot; in which case a hexadecimal value is assumed.</p>
<dt><code>-u</code>, <code>&#8211;unavailable</code></p>
<dd>set unavailable state. Port group shall only accept INQUIRY, REPORT LUNS, REPORT/SET TARGET PORT GROUPS, REQUEST SENSE and READ/WRITE BUFFER commands.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>The SET TARGET PORT GROUPS command should be supported whenever the TPGS value in a standard INQUIRY response is 2 or 3. [View with sg_inq utility.] </p>
<p> Notice that the offline state is termed as a &quot;secondary target port asymmetric access state&quot; and takes a relative target port identifier (i.e. acts on a single target port). All the other states are termed as &quot;primary target port asymmetric access states&quot; and each takes a target port group identifier (i.e. acts on one or more target ports). </p>
<p> When <i>&#8211;tp=</i> is given then the same number of elements should be given to the <i>&#8211;state=</i> option. If more than one list element is given to <i>&#8211;tp=</i> and an equal number of elements is _not_ given to the <i>&#8211;state=</i> option, then if only one state is specified then it is repeated.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_stpg is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2012 Hannes Reinecke, Christophe Varoqui and Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq, sg_rtpg (sg3_utils)</code> </p>
