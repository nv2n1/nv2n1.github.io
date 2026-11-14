---
title: "sg_rtpg(8)"
name: "sg_rtpg"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_rtpg/"
description: "sg_rtpg – send SCSI REPORT TARGET PORT GROUPS command"
---

<p>sg_rtpg &#8211; send SCSI REPORT TARGET PORT GROUPS command</p>
<h2>Synopsis</h2>
<p><code>sg_rtpg</code> [<i>&#8211;decode</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI REPORT TARGET PORT GROUPS command to <i>DEVICE</i> and outputs the response. </p>
<p> Target port group access is described in SPC-3 found at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> in section 5.8 (in rev 21c dated 2005/1/15). The Report Target Port Groups command is also described in that document.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;decode</code></p>
<dd>decodes the status code and asymmetric access state from each target port group descriptor returned. The default action is not to decode these values.</p>
<dt><code>-e</code>, <code>&#8211;extended</code></p>
<dd>use extended header format for parameter data.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output response in hex (rather than partially or fully decode it).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output response in binary to stdout.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>The Report Target Port Groups command should be supported whenever the TPGS bits in a standard INQUIRY response are greater than zero. [View with sg_inq utility.]</p>
<h2>Exit Status</h2>
<p>The exit status of sg_rtpg is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Christophe Varoqui and Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq(sg3_utils)</code> </p>
