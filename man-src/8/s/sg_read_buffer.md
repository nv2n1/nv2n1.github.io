---
title: "sg_read_buffer(8)"
name: "sg_read_buffer"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_read_buffer/"
description: "sg_read_buffer – send SCSI READ BUFFER command"
---

<p>sg_read_buffer &#8211; send SCSI READ BUFFER command</p>
<h2>Synopsis</h2>
<p><code>sg_read_buffer</code> [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;id=ID</i>] [<i>&#8211;length=LEN</i>] [<i>&#8211;mode=MO</i>] [<i>&#8211;offset=OFF</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Sends a SCSI READ BUFFER command to the <i>DEVICE</i>, and if there is a response either decodes it, prints it in hexadecimal or sends it in binary to stdout. If a response is received for a &quot;descriptor&quot; mode then, in the absence of <i>&#8211;hex</i> and <i>&#8211;raw</i>, it is decoded. Response for non-descriptor modes are output in hexadecimal unless the <i>&#8211;raw</i> option is given.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>output the usage message then exit. If used multiple times also prints the mode names and their acronyms.</dd>
<dt><code>-H</code>, <code>&#8211;hex</code></dt>
<dd>output the response in hexadecimal. When given twice the response is output in hex with the corresponding representation in ASCII to the right of each line.</dd>
<dt><code>-i</code>, <code>&#8211;id</code>=<i>ID</i></dt>
<dd>this option sets the buffer id field in the cdb. <i>ID</i> is a value between 0 (default) and 255 inclusive.</dd>
<dt><code>-l</code>, <code>&#8211;length</code>=<i>LEN</i></dt>
<dd>where <i>LEN</i> is the length, in bytes, that is placed in the &quot;allocation length&quot; field in the cdb. The default value is 4 (bytes). The device may respond with less bytes.</dd>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>MO</i></dt>
<dd>this option sets the mode field in the cdb. <i>MO</i> is a value between 0 (default) and 31 inclusive. Alternatively an abbreviation can be given. To list the available mode abbreviations use an invalid one (e.g. &#8216;&#8211;mode=xxx&#8217;). As an example, to fetch the read buffer descriptor give &#8216;&#8211;mode=desc&#8217; .</dd>
<dt><code>-o</code>, <code>&#8211;offset</code>=<i>OFF</i></dt>
<dd>this option sets the buffer offset field in the cdb. <i>OFF</i> is a value between 0 (default) and 2**24-1 . It is a byte offset.</dd>
<dt><code>-r</code>, <code>&#8211;raw</code></dt>
<dd>if a response is received then it is sent in binary to stdout.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>increase the level of verbosity, (i.e. debug output).</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>print the version string and then exit.</dd></dl>
<h2>Notes</h2>
<p>All numbers given with options are assumed to be decimal. Alternatively numerical values can be given in hexadecimal preceded by either &quot;0x&quot; or &quot;0X&quot; (or has a trailing &quot;h&quot; or &quot;H&quot;).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_read_buffer is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Luben Tuikov and Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2012 Luben Tuikov and Douglas Gilbert<br/>
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_write_buffer(sg3_utils)</code> </p>
