---
title: "sg_read_block_limits(8)"
name: "sg_read_block_limits"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_read_block_limits/"
description: "sg_read_block_limits – send SCSI READ BLOCK LIMITS command"
---

<p>sg_read_block_limits &#8211; send SCSI READ BLOCK LIMITS command</p>
<h2>Synopsis</h2>
<p><code>sg_read_block_limits</code> [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI READ BLOCK LIMITS command to <i>DEVICE</i> and outputs the response. This command is defined for tape (drives) and its description is found in the SSC documents at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> .</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output response in hex (rather than decode it).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output response in binary to stdout.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Exit Status</h2>
<p>The exit status of sg_read_block_limits is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Examples</h2>
<p>It is usually okay to use no options. Here is an invocation (on the first line following the &quot;#&quot; command prompt) followed by some typical output: </p>
<p>#&nbsp;<wbr>sg_read_block_limits&nbsp;<wbr>/dev/st0<br />
 Read Block Limits results: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Minimum block size: 1 byte(s) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Maximum block size: 16777215 byte(s), 16383 KB, 15 MB</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg3_utils(sg3_utils)</code> </p>
