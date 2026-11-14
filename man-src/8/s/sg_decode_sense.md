---
title: "sg_decode_sense(8)"
name: "sg_decode_sense"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_decode_sense/"
description: "sg_decode_sense – decode SCSI sense data"
---

<p>sg_decode_sense &#8211; decode SCSI sense data</p>
<h2>Synopsis</h2>
<p><code>sg_decode_sense</code> [<i>&#8211;binary=FN</i>] [<i>&#8211;file=FN</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;nospace</i>] [<i>&#8211;status=SS</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;write=WFN</i>] [H1 H2 H3 &#8230;]</p>
<h2>Description</h2>
<p>This utility takes SCSI sense data in binary or as a sequence of ASCII hexadecimal bytes and decodes it. The primary reference for the decoding is SPC-3 ANSI INCITS 408-2005 and the most recent draft SPC-4 revision 29 which can be found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> and other locations on the internet. </p>
<p> SCSI sense data is often found in kernel log files as a result of something going wrong but may just be informative. It is often shown as a sequence of hexadecimal bytes, starting with 70, 71, 72, 73, f0 or f1. Sense data could be up to 252 bytes long but typically is much shorter than that, 18 bytes long is often seen and is usually associated with the older &quot;fixed&quot; format sense data. </p>
<p> The sense data can be provided on the command line or in a file. If given on the command line the sense data should be a sequence of hexadecimal bytes separated by space. Alternatively a file can be given with the contents in binary or ASCII hexadecimal bytes. The latter form can contain several lines each with none, one or more ASCII hexadecimal bytes separated by space (comma or tab). The hash symbol may appear and it and the rest of the line is ignored making it useful for comments.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;binary</code>=<i>FN</i></p>
<dd>the sense data is read in binary from a file called <i>FN</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>this option is used in conjunction with <i>&#8211;write=WFN</i> in order to change the output written to <i>WFN</i> to lines of ASCII hex bytes suitable for a C language compiler. Each line contains up to 16 bytes (e.g. a line starting with &quot;0x3b,0x07,0x00,0xff&quot;).</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FN</i></p>
<dd>the sense data is read in ASCII hexadecimal from a file called <i>FN</i>. The sense data should appear as a sequence of bytes separated by space, comma, tab or newline. Everything from and including a hash symbol to the end of that line is ignored. If <i>&#8211;nospace</i> is set then no separator is required between the ASCII hexadecimal digits in <i>FN</i> with bytes decoded from pairs of ASCII hexadecimal digits.</p>
<dt><code>-n</code>, <code>&#8211;nospace</code></p>
<dd>expect ASCII hexadecimal to be a string of hexadecimal digits with no spaces between them. Bytes are decoded by taking two hexadecimal digits at a time, so an even number of digits is expected. The string of hexadecimal digits may be on the command line (replacing &quot;H1 H2 H3&quot;) or spread across multiple lines the <i>FN</i> given to <i>&#8211;file=</i>.</p>
<dt><code>-s</code>, <code>&#8211;status</code>=<i>SS</i></p>
<dd>where <i>SS</i> is a SCSI status byte value, given in hexadecimal. The SCSI status byte is related to but distinct from sense data.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the degree of verbosity (debug messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>output version string then exit.</p>
<dt><code>-w</code>, <code>&#8211;write</code>=<i>WFN</i></p>
<dd>writes the sense data out to a file called <i>WFN</i>. If necessary <i>WFN</i> is created. If <i>WFN</i> exists then it is truncated prior to writing the sense data to it. If the <i>&#8211;hex</i> option is also given then ASCII hex is written to <i>WFN</i> (see the <i>&#8211;hex</i> option description); otherwise binary is written to <i>WFN</i>. This option is a convenience and may be helpful in converting the ASCII hexadecimal representation of sense data (or anything else) into the equivalent binary or a compilable ASCII hex form.</dl>
<h2>Notes</h2>
<p>Unlike most utilities in this package, this utility does not access a SCSI device (logical unit). This utility accesses a library associated with this package. Amongst other things the library decodes SCSI sense data.</p>
<h2>Examples</h2>
<p>Sense data is often printed out in kernel logs and sometimes on the command line when verbose or debug flags are given. It will be at least 8 bytes long, often 18 bytes long but may be longer. A sense data string might look like this: f0 00 03 00 00 12 34 0a 00 00 00 00 11 00 00 00<br />
 00 00 Cut and paste it after the sg_decode_sense command:<br />
&nbsp;<wbr>&nbsp;<wbr>sg_decode_sense f0 00 03 00 00 12 34 0a 00 00 00 00 11 00 00 00 00 00 and for this sense data the output should look like this: </p>
<pre><code>Fixed format, current;  Sense key: Medium Error


Additional sense: Unrecovered read error

Info fld=0x1234 [4660]</code></pre>
<p> For a medium error the Info field is the logical block address (LBA) of the lowest numbered block that the associated SCSI command was not able to read (verify or write).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_decode_sense is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2010-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_requests(sg3_utils)</code> </p>
