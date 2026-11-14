---
title: "sg_senddiag(8)"
name: "sg_senddiag"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_senddiag/"
description: "sg_senddiag – performs a SCSI SEND DIAGNOSTIC command"
---

<p>sg_senddiag &#8211; performs a SCSI SEND DIAGNOSTIC command</p>
<h2>Synopsis</h2>
<p><code>sg_senddiag</code> [<i>&#8211;doff</i>] [<i>&#8211;extdur</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;list</i>] [<i>&#8211;pf</i>] [<i>&#8211;raw=H,H&#8230;</i>] [<i>&#8211;raw=-</i>] [<i>&#8211;selftest=ST</i>] [<i>&#8211;test</i>] [<i>&#8211;uoff</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_senddiag</code> [<i>-doff</i>] [<i>-e</i>] [<i>-h</i>] [<i>-H</i>] [<i>-l</i>] [<i>-pf</i>] [<i>-raw=H,H&#8230;</i>] [<i>-raw=-</i>] [<i>-s=ST</i>] [<i>-t</i>] [<i>-uoff</i>] [<i>-v</i>] [<i>-V</i>] [<i>-?</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends a SCSI SEND DIAGNOSTIC command to the <i>DEVICE</i>. It can issue self-tests, find supported diagnostic pages or send arbitrary diagnostic pages. </p>
<p> When the <i>&#8211;list</i> option and a <i>DEVICE</i> are given then the utility sends a SCSI RECEIVE DIAGNOSTIC RESULTS command to fetch the response (i.e. the page numbers of supported diagnostic pages). </p>
<p> When the <i>&#8211;list</i> option is given without a <i>DEVICE</i> then a list of diagnostic page names and their numbers, known by this utility, are listed. </p>
<p> This utility supports two command line syntax-es, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;doff</code></p>
<dd>set the Device Offline (DevOffL) bit (default is clear). Only significant when <i>&#8211;test</i> option is set for the default self-test. When set other operations on any logical units controlled by the this device server (target) may be affected (delayed) while a default self-test is underway.</p>
<dt><code>-e</code>, <code>&#8211;extdur</code></p>
<dd>outputs the expected extended self-test duration. The duration is given in seconds (and minutes in parentheses). This figure is obtained from mode page 0xa (i.e. the control mode page).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>outputs response from RECEIVE DIAGNOSTIC RESULTS in hex rather than decode it.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>when a <i>DEVICE</i> is also given lists the names of all diagnostic pages supported by this device. The request is sent via a SEND DIAGNOSTIC command (with the &quot;pF&quot; bit set) and the response is fetched by a RECEIVE DIAGNOSTIC RESULTS command. When used in the absence of a <i>&#8211;list</i> argument then a list of diagnostic page names and their numbers, known by this utility, are listed.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;pf</code></p>
<dd>set Page Format (PF) bit. By default it is clear (i.e. 0) unless the list <i>&#8211;list</i> option is given in which case the Page Format bit is set (as required by SPC-3).</p>
<dt><code>-r</code>, <code>&#8211;raw</code>=<i>H,H&#8230;</i></p>
<dd>string of comma separated hex numbers each of which should resolve to a byte value (i.e. 0 to ff inclusive). A (single) space separated string of hex bytes is also allowed but the list needs to be in quotes. This sequence forms a diagnostic page to be sent with the SCSI SEND DIAGNOSTIC command. Mostly likely the <i>&#8211;pf</i> option should also be given.</p>
<dt><code>-r</code>, <code>&#8211;raw=-</code></p>
<dd>reads sequence of bytes from stdin. The sequence may be comma, space, tab or linefeed (newline) separated. If a line contains &quot;#&quot; then the remaining characters on that line are ignored. Otherwise each non separator character should resolve to a byte value (i.e. 0 to ff inclusive). This sequence forms a diagnostic page to be sent with the SCSI SEND DIAGNOSTIC command. Mostly likely the <i>&#8211;pf</i> option should also be given.</p>
<dt><code>-s</code>, <code>&#8211;selftest</code>=<i>ST</i></p>
<dd>where <i>ST</i> is the self-test code. The default value is 0 which is inactive. Some other values: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>1</code>&nbsp;<wbr>: background short self-test </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>2</code>&nbsp;<wbr>: background extended self-test </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>4</code>&nbsp;<wbr>: aborts a&nbsp;<wbr>(background)&nbsp;<wbr>self-test that is in progress </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>5</code>&nbsp;<wbr>: foreground short self-test </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>6</code>&nbsp;<wbr>: foreground extended self-test<br />
 This option is mutually exclusive with default self-test (i.e. can&#8217;t have (<i>ST</i> &gt; 0) and <i>&#8211;test</i>).</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>sets the _default_ Self Test (SelfTest) bit. By default this is clear (0). The <i>&#8211;selftest=ST</i> option should not be active together with this option. Both the <i>&#8211;doff</i> and/or <i>&#8211;uoff</i> options can be used with this option.</p>
<dt><code>-u</code>, <code>&#8211;uoff</code></p>
<dd>set the Unit Offline (UnitOffL) bit (default is clear). Only significant when <i>&#8211;test</i> option is set for the default self-test. When set other operations on this logical unit may be affected (delayed) while a default self-test is underway. Some devices (e.g. Fujitsu disks) do more tests when this bit is set.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>All devices should support the default self-test. The &#8216;short&#8217; self-test codes should complete in 2 minutes or less. The &#8216;extended&#8217; self-test codes&#8217; maximum duration is vendor specific (e.g. a little over 10 minutes with the author&#8217;s disks). The foreground self-test codes wait until they are completed while the background self-test codes return immediately. The results of both foreground and background self-test codes are placed in the &#8216;self-test results&#8217; log page (see <a href="/docs/linux/man/8-sg_logs/">sg_logs</a>(8)). The SCSI command timeout for this utility is set to 60 minutes to allow for slow foreground extended self-tests. </p>
<p> If the <i>DEVICE</i> is a disk then no file systems residing on that disk should be mounted during a foreground self-test. The reason is that other SCSI commands may become queued behind the foreground self-test and timeout. </p>
<p> When the <i>&#8211;raw=H,H&#8230;</i> option is given then self-tests should not be selected. However the <code>&#8211;pf</code> (i.e. &quot;page format&quot;) option should be given. The length of the diagnostic page to be sent is derived from the number of bytes given to the <i>&#8211;raw=H,H&#8230;</i> option. The diagnostic page code (number) should be the first byte of the sequence (i.e. as dictated by SPC-3 diagnostic page format). See the EXAMPLES section below. </p>
<p> Arbitrary diagnostic pages can be read (in hex) with the <a href="/docs/linux/man/8-sg_ses/">sg_ses</a>(8) utility (not only those defined in SES-2). </p>
<p> If the utility is used with no options (e.g. &quot;sg_senddiag /dev/sg1&quot;) Then a degenerate SCSI SEND DIAGNOSTIC command is sent with zero in all its fields apart from the opcode. Some devices report this as an error while others ignore it. It is not entirely clear from SPC-3 if it is invalid to send such a command. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. </p>
<p> To access SCSI enclosures see the <a href="/docs/linux/man/8-sg_ses/">sg_ses</a>(8) utility. sg_ses uses the SCSI SEND DIAGNOSTIC and RECEIVE DIAGNOSTIC RESULTS commands as outlined in the SES-2 (draft) standard.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_senddiag is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option.</p>
<dl>
<dt><code>-doff</code></p>
<dd>set the Device Offline (DevOffL) bit (default is clear). Only significant when <i>-t</i> option is set for the default self-test. Equivalent to <i>&#8211;doff</i> in the main description.</p>
<dt><code>-e</code></p>
<dd>outputs the expected extended self-test duration. Equivalent to <i>&#8211;extdur</i> in the main description.</p>
<dt><code>-h</code></p>
<dd>outputs response from RECEIVE DIAGNOSTIC RESULTS in hex rather than decode it.</p>
<dt><code>-H</code></p>
<dd>outputs response from RECEIVE DIAGNOSTIC RESULTS in hex rather than decode it.</p>
<dt><code>-l</code></p>
<dd>when a <i>DEVICE</i> is also given lists the names of all diagnostic pages supported by this device. The request is sent via a SEND DIAGNOSTIC command (with the &quot;pf&quot; bit set) and the response is fetched by a RECEIVE DIAGNOSTIC RESULTS command. When used in the absence of a <i>DEVICE</i> argument then a list of diagnostic page names and their numbers, known by this utility, are listed.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-pf</code></p>
<dd>set Page Format (PF) bit. By default it is clear (i.e. 0) unless the <i>-l</i> option is given in which case the Page Format bit is set (as required by SPC-3).</p>
<dt><code>-raw</code>=<i>H,H&#8230;</i></p>
<dd>string of comma separated hex numbers each of which should resolve to a byte value (i.e. 0 to ff inclusive). This sequence forms a diagnostic page to be sent with the SCSI SEND DIAGNOSTIC command. Mostly likely the <i>-pf</i> option should also be given.</p>
<dt><code>-raw=-</code></p>
<dd>reads sequence of bytes from stdin. The sequence may be comma, space, tab or linefeed (newline) separated. If a line contains &quot;#&quot; then the remaining characters on that line are ignored. Otherwise each non separator character should resolve to a byte value (i.e. 0 to ff inclusive). This sequence forms a diagnostic page to be sent with the SCSI SEND DIAGNOSTIC command. Mostly likely the <i>-pf</i> option should also be given.</p>
<dt><code>-s</code>=<i>ST</i></p>
<dd>where <i>ST</i> is the self-test code. The default value is 0 which is inactive. A value of 1 selects a background short self-test; 2 selects a background extended self-test; 5 selects a foreground short self-test; 6 selects a foreground extended test. A value of 4 will abort a (background) self-test that is in progress. This option is mutually exclusive with default self-test (i.e. <i>-t</i>).</p>
<dt><code>-t</code></p>
<dd>sets the _default_ Self Test (SelfTest) bit. By default this is clear (0). The <i>-s=ST</i> option should not be active together with this option. Both the <i>-doff</i> and/or <i>-uoff</i> options can be used with this option.</p>
<dt><code>-uoff</code></p>
<dd>set the Unit Offline (UnitOffL) bit (default is clear). Equivalent to <i>&#8211;uoff</i> in the main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</p>
<dt><code>-?</code></p>
<dd>output usage message. Ignore all other parameters.</dl>
<h2>Examples</h2>
<p>The examples sub-directory in the sg3_utils packages contains two example scripts that turn on the CJTPAT (jitter pattern) on some SAS disks (one script for each phy). One possible invocation for phy 1 is: </p>
<pre><code>sg_senddiag --pf --raw=- /dev/sg2 &lt; sdiag_sas_p1_cjtpat.txt</code></pre>
<p> There is also an example script that turns on the IDLE pattern. Once a test pattern has been started it can be turned off by resetting the phy or with the STOP phy pattern function: </p>
<pre><code>sg_senddiag --pf --raw=- /dev/sg2 &lt; sdiag_sas_p1_stop.txt</code></pre>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2011 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_ses/">sg_ses</a>(8), <a href="/docs/linux/man/8-sg_logs/">sg_logs</a>(8), smartmontools(see net)</code> </p>
