---
title: "sg_turs(8)"
name: "sg_turs"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_turs/"
description: "sg_turs – send one or more SCSI TEST UNIT READY commands"
---

<p>sg_turs &#8211; send one or more SCSI TEST UNIT READY commands</p>
<h2>Synopsis</h2>
<p><code>sg_turs</code> [<i>&#8211;help</i>] [<i>&#8211;number=NUM</i>] [<i>&#8211;progress</i>] [<i>&#8211;time</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_turs</code> [<i>-n=NUM</i>] [<i>-p</i>] [<i>-t</i>] [<i>-v</i>] [<i>-V</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends one or more SCSI TEST UNIT READY commands to the <i>DEVICE</i>. This may be useful for timing the per command overhead. Note that TEST UNIT READY has no associated data, just a 6 byte command and a returned SCSI status value. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-n</code>, <code>&#8211;number</code>=<i>NUM</i></p>
<dd>performs TEST UNIT READY <i>NUM</i> times. If not given defaults to 1. These suffix multipliers are permitted: c C *1; w W *2; b B *512; k K KiB *1,024; KB *1,000; m M MiB *1,048,576; MB *1,000,000; g G GiB *1,073,741,824; and GB *1,000,000,000 . Also a suffix of the form &quot;x&lt;n&gt;&quot; multiplies the leading number by &lt;n&gt;. Alternatively a hex number may be given, prefixed by either &#8216;0x&#8217; or has a trailing &#8216;h&#8217;.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;progress</code></p>
<dd>show progress indication (a percentage) if available. If <i>&#8211;number=NUM</i> is given, <i>NUM</i> is greater than 1 and an initial progress indication was detected then this utility waits 30 seconds before subsequent checks. Exits when <i>NUM</i> is reached or there are no more progress indications. Ignores <i>&#8211;time</i> option. See NOTES section below.</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd>after completing the requested number of TEST UNIT READY commands, outputs the total duration and the average number of commands executed per second.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print version string then exit.</dl>
<h2>Notes</h2>
<p>The progress indication is optionally part of the sense data. When a prior command that takes a long time to complete (and typically precludes other media access commands) is still underway, the progress indication can be used to determine how long before the device returns to its normal state. </p>
<p> The SCSI FORMAT command for disks used with the IMMED bit set is an example of an operation that takes a significant amount of time and precludes other media access during that time. The IMMED bit set instructs the FORMAT command to return control to the application client once the format has commenced (see SBC-3). Several long duration SCSI commands associated with tape drives also use the progress indication (see SSC-3). </p>
<p> Early standards suggested that the SCSI TEST UNIT READY command be used for polling the progress indication. More recent standards seem to suggest the SCSI REQUEST SENSE command should be used instead.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_turs is 0 when it is successful (e.g. in the case of a mechanical disk, it is spun up and ready to accept commands). For this utility the other exit status of interest is 2 corresponding to the &quot;not ready&quot; sense key. For other exit status values see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option.</p>
<dl>
<dt><code>-n</code>=<i>NUM</i></p>
<dd>performs TEST UNIT READY <i>NUM</i> times. If not given defaults to 1. Equivalent to <i>&#8211;number=NUM</i> in the main description.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-p</code></p>
<dd>show progress indication (a percentage) if available. Equivalent to <i>&#8211;progress</i> in the main description.</p>
<dt><code>-t</code></p>
<dd>after completing the requested number of TEST UNIT READY commands, outputs the total duration and the average number of commands executed per second. Equivalent to <i>&#8211;time</i> in the main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</dl>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2012 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq, sg_request (sg3_utils)</code> </p>
