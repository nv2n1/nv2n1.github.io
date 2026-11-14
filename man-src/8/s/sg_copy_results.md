---
title: "sg_copy_results(8)"
name: "sg_copy_results"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_copy_results/"
description: "sg_copy_results – send SCSI RECEIVE COPY RESULTS command (XCOPY related)"
---

<p>sg_copy_results &#8211; send SCSI RECEIVE COPY RESULTS command (XCOPY related)</p>
<h2>Synopsis</h2>
<p><code>sg_copy_results</code> [<i>&#8211;failed</i>|<i>&#8211;params</i>|<i>&#8211;receive</i>|<i>&#8211;status</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;list_id=ID</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;xfer_len=BTL</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility is designed to query the status of the SCSI Extended Copy (XCOPY) facility (see SPC-3 revision 23 sections 6.3 and 6.17), present in some modern storage arrays. This utility sends a SCSI RECEIVE COPY RESULTS command to the given <i>DEVICE</i> and displays the response. During the draft stages of SPC-4 the T10 committee has expanded the XCOPY command so that it now has two variants: &quot;LID1&quot; (for a List Identifier length of 1 byte) and &quot;LID4&quot; (for a List Identifier length of 4 bytes). This utility supports the older, LID1 variant which is also found in SPC-3 and earlier. While the LID1 variant in SPC-4 is command level (binary) compatible with XCOPY as defined in SPC-3, some of the command naming has changed. This utility uses the older, SPC-3 XCOPY names. The command has four distinct modes of operation, distinguished by the service action field:</p>
<dl>
<dt><code>COPY STATUS</code></p>
<dd>Displays the current status of the EXTENDED COPY command identified by the list id field.</p>
<dt><code>RECEIVE DATA</code></p>
<dd>Return the held data read by the EXTENDED COPY command identified by the list id field. This option is only meaningful if the respective segment descriptor are supported.</p>
<dt><code>OPERATING PARAMETERS</code></p>
<dd>Return copy manager operating parameters. This option is also useful to determine if the SCSI Extended Copy facility is supported.</p>
<dt><code>FAILED SEGMENT DETAILS</code></p>
<dd>Return copy target device sense data and other information about any failed segments. </p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;failed</code></p>
<dd>sets the service action field to FAILED SEGMENT DETAILS [4].</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>prints out the response buffer in hex.</p>
<dt><code>-l</code>, <code>&#8211;list_id</code>=<i>ID</i></p>
<dd>sets the list identifier field to <i>ID</i> (default: 0).</p>
<dt><code>-p</code>, <code>&#8211;params</code></p>
<dd>sets the service action field to OPERATING PARAMETERS [3]. This is the default.</p>
<dt><code>-r</code>, <code>&#8211;receive</code></p>
<dd>sets the service action field to RECEIVE DATA [1].</p>
<dt><code>-s</code>, <code>&#8211;status</code></p>
<dd>sets the service action field to COPY STATUS [0].</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-x</code>, <code>&#8211;xfer_len</code>=<i>BTL</i></p>
<dd>sets the allocation length field to <i>BTL</i>. It is the byte transfer length and is the maximum (byte) size of the response. <i>BTL</i> must be less than 10000 and defaults to 520.</dl>
<h2>Notes</h2>
<p>Decoding of <i>RECEIVE DATA</i> service action is not implemented.</p>
<h2>Examples</h2>
<p>Query the operating parameters for a device: # sg_copy_results -p /dev/sdo<br />
 Receive copy results (report operating parameters):<br />
&nbsp;<wbr>Supports no list identifier: no<br />
&nbsp;<wbr>Maximum target descriptor count: 2<br />
&nbsp;<wbr>Maximum segment descriptor count: 1<br />
&nbsp;<wbr>Maximum descriptor list length: 92 bytes<br />
&nbsp;<wbr>Maximum segment length: 33553920 bytes<br />
&nbsp;<wbr>Inline data not supported<br />
&nbsp;<wbr>Held data limit: 0 bytes<br />
&nbsp;<wbr>Maximum stream device transfer size: 0 bytes<br />
&nbsp;<wbr>Total concurrent copies: 0<br />
&nbsp;<wbr>Maximum concurrent copies: 255<br />
&nbsp;<wbr>Data segment granularity: 512 bytes<br />
&nbsp;<wbr>Inline data granularity: 1 bytes<br />
&nbsp;<wbr>Held data granularity: 1 bytes<br />
&nbsp;<wbr>Implemented descriptor list:<br />
&nbsp;<wbr>&nbsp;<wbr>Segment descriptor 0x02: Copy from block device to block device<br />
&nbsp;<wbr>&nbsp;<wbr>Target descriptor 0xe4: Identification descriptor </p>
<h2>Exit Status</h2>
<p>The exit status of sg_copy_results is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012-2013 Hannes Reinecke and Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_xcopy(sg3_utils)</code> </p>
