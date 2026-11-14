---
title: "sg_requests(8)"
name: "sg_requests"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_requests/"
description: "sg_requests – send one or more SCSI REQUEST SENSE commands"
---

<p>sg_requests &#8211; send one or more SCSI REQUEST SENSE commands</p>
<h2>Synopsis</h2>
<p><code>sg_requests</code> [<i>&#8211;desc</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;progress</i>] [<i>&#8211;raw</i>] [<i>&#8211;status</i>] [<i>&#8211;time</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send SCSI REQUEST SENSE command to <i>DEVICE</i> and output the parameter data response which is expected to be in sense data format. Both fixed and descriptor sense data formats are supported. </p>
<p> Multiple REQUEST SENSE commands can be sent with the <i>&#8211;num=NUM</i> option. This can be used for timing purposes or monitoring the progress indication.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;desc</code></p>
<dd>sets the DESC bit in the REQUEST SENSE SCSI cdb. The <i>DEVICE</i> should return sense data in descriptor (rather than fixed) format. This will only occur if the <i>DEVICE</i> recognizes descriptor format (SPC-3 and later). If the device is pre SPC-3 then setting a bit in a reserved field may cause a check condition status with an illegal request sense key, but will most likely be ignored.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output response in ASCII hexadecimal.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the (maximum) response length in bytes. It is placed in the cdb&#8217;s &quot;allocation length&quot; field. If not given (or <i>LEN</i> is zero) then 252 is used. The maximum value of <i>LEN</i> is 255 (but SPC-4 recommends 252).</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>perform <i>NUM</i> SCSI REQUEST SENSE commands, stopping when either <i>NUM</i> is reached or an error occurs. The default value for <i>NUM</i> is 1 .</p>
<dt><code>-p</code>, <code>&#8211;progress</code></p>
<dd>show progress indication (a percentage) if available. If <i>&#8211;number=NUM</i> is given, <i>NUM</i> is greater than 1 and an initial progress indication was detected then this utility waits 30 seconds before subsequent checks. Exits when <i>NUM</i> is reached or there are no more progress indications. Ignores <i>&#8211;hex</i>, <i>&#8211;raw</i> and <i>&#8211;time</i> options. See NOTES section below.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output response in binary (to stdout).</p>
<dt><code>-s</code>, <code>&#8211;status</code></p>
<dd>if the REQUEST SENSE command finished without error (as indicated by its SCSI status) then the contents of the parameter data are analysed as sense data and the exit status is set accordingly. The default action (i.e. when this option is not given) is to ignore the contents of the parameter data for the purposes of setting the exit status. Some types of error set a sense key of &quot;NO SENSE&quot; with non-zero information in the additional sense code (e.g. the FAILURE PREDICTION THRESHOLD EXCEEDED group of codes); this results in an exit status value of 10. If the sense key is &quot;NO SENSE&quot; and both asc and ascq are zero then the exit status is set to 0 . See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page for exit status values.</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd>time the SCSI REQUEST SENSE command(s) and calculate the average number of operations per second.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output). Additionally the response (if received) is output in ASCII-HEX. Use this option multiple times for greater verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>In SCSI 1 and 2 the REQUEST SENSE command was very important for error and warning processing in SCSI. The autosense capability rendered this command almost superfluous. </p>
<p> However recent SCSI drafts (e.g. SPC-4 rev 14 and SBC-3 rev 14) increase the utility of the REQUEST SENSE command. Idle and standby (low) power conditions can be detected with this command. </p>
<p> The REQUEST SENSE command is not marked as mandatory in SPC-3 (i.e. for all SCSI devices) but is marked as mandatory in SBC-2 (i.e. for disks), SSC-3 (i.e. for tapes) and MMC-4 (i.e. for CD/DVD/HD-DVD/BD drives). </p>
<p> The progress indication is optionally part of the sense data. When a prior command that takes a long time to complete (and typically precludes other media access commands) is still underway, the progress indication can be used to determine how long before the device returns to its normal state. </p>
<p> The SCSI FORMAT command for disks used with the IMMED bit set is an example of an operation that takes a significant amount of time and precludes other media access during that time. The IMMED bit set instructs the FORMAT command to return control to the application client once the format has commenced (see SBC-3). Several long duration SCSI commands associated with tape drives also use the progress indication (see SSC-3). </p>
<p> Early standards suggested that the SCSI TEST UNIT READY command be used for polling the progress indication. More recent standards seem to suggest the SCSI REQUEST SENSE command should be used instead.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_requests is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg3_utils</code> </p>
