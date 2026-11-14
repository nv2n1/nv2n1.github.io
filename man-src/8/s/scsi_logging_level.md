---
title: "scsi_logging_level(8)"
name: "scsi_logging_level"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_logging_level/"
description: "scsi_logging_level – access Linux SCSI logging level information"
---

<p>scsi_logging_level &#8211; access Linux SCSI logging level information</p>
<h2>Synopsis</h2>
<p><code>scsi_logging_level</code> [<i>&#8211;all=LEV</i>] [<i>&#8211;create</i>] [<i>&#8211;error=LEV</i>] [<i>&#8211;get</i>] [<i>&#8211;help</i>] [<i>&#8211;highlevel=LEV</i>] [<i>&#8211;hlcomplete=LEV</i>] [<i>&#8211;hlqueue=LEV</i>] [<i>&#8211;ioctl=LEV</i>] [<i>&#8211;llcomplete=LEV</i>] [<i>&#8211;llqueue=LEV</i>] [<i>&#8211;lowlevel=LEV</i>] [<i>&#8211;midlevel=LEV</i>] [<i>&#8211;mlcomplete=LEV</i>] [<i>&#8211;mlqueue=LEV</i>] [<i>&#8211;scan=LEV</i>] [<i>&#8211;set</i>] [<i>&#8211;timeout=LEV</i>] [<i>&#8211;version</i>]</p>
<h2>Description</h2>
<p>This bash shell script accesses the Linux SCSI subsystem logging level. The current values can be shown (e.g. with <i>&#8211;get</i>) or changed (e.g. with <i>&#8211;set</i>). Superuser permissions will typically be required to set the logging level. </p>
<p> One of these options: <i>&#8211;create</i>, <i>&#8211;get</i> or <i>&#8211;set</i> is required. Only one can be given.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code>=<i>LEV</i></p>
<dd><i>LEV</i> is used for all SCSI_LOG fields.</p>
<dt><code>-c</code>, <code>&#8211;create</code></p>
<dd>Options are parsed and placed in internal fields that are displayed but no logging levels are changed within the Linux kernel.</p>
<dt><code>-E</code>, <code>&#8211;error</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_ERROR field.</p>
<dt><code>-g</code>, <code>&#8211;get</code></p>
<dd>Fetches the current SCSI logging levels from the Linux kernel and displays them.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;highlevel</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_HLQUEUE and SCSI_LOG_HLCOMPLETE fields.</p>
<dt><code>&#8211;hlcomplete</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_HLCOMPLETE field.</p>
<dt><code>&#8211;hlqueue</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_HLQUEUE field.</p>
<dt><code>-I</code>, <code>&#8211;ioctl</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_IOCTL field.</p>
<dt><code>&#8211;llcomplete</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_LLCOMPLETE field.</p>
<dt><code>&#8211;llqueue</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_LLQUEUE field.</p>
<dt><code>-L</code>, <code>&#8211;lowlevel</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_LLQUEUE and SCSI_LOG_LLCOMPLETE fields.</p>
<dt><code>-M</code>, <code>&#8211;midlevel</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_MLQUEUE and SCSI_LOG_MLCOMPLETE fields.</p>
<dt><code>&#8211;mlcomplete</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_MLCOMPLETE field.</p>
<dt><code>&#8211;mlqueue</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_MLQUEUE field.</p>
<dt><code>-S</code>, <code>&#8211;scan</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_SCAN field.</p>
<dt><code>-s</code>, <code>&#8211;set</code></p>
<dd>Uses the fields specified in this command&#8217;s options and attempts to apply them to the Linux SCSI subsystem logging levels. Typically superuser permissions will be required to do this.</p>
<dt><code>-T</code>, <code>&#8211;timeout</code>=<i>LEV</i></p>
<dd><i>LEV</i> is placed in the SCSI_LOG_TIMEOUT field.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Outputs the version information and then exits.</dl>
<h2>Notes</h2>
<p>The <i>&#8211;get</i> and <i>&#8211;set</i> options access the /proc/sys/dev/scsi/logging_level pseudo file.</p>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Any other exit status indicates that an error has occurred.</p>
<h2>Authors</h2>
<p>Written by IBM. Small alterations by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; IBM Corp. 2006<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<p> The software was obtained from an IBM package called s390-tools-1.6.2 found on that company&#8217;s &quot;developerworks&quot; site. The most recent version of that package at this time is 1.8.3 .</p>
