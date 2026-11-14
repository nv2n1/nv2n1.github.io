---
title: "powertop(8)"
name: "powertop"
section: "8"
letter: "p"
url: "/docs/linux/man/8-powertop/"
description: "powertop – a power consumption and power management diagnosis tool."
---

<p>powertop &#8211; a power consumption and power management diagnosis tool.</p>
<h2>Synopsis</h2>
<p><code>powertop</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p><code>powertop</code> is a program that helps to diagnose various issues with power consumption and power management. It also has an interactive mode allowing one to experiment with various power management settings. When invoking powertop without arguments powertop starts in interactive mode.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;auto-tune</code></p>
<dd>Set all tunable options to their good setting without interaction.</p>
<dt><code>-c</code>, <code>&#8211;calibrate</code></p>
<dd>runs powertop in calibration mode. When running on battery, powertop can track power consumption as well as system activity. When there are enough measurements, powertop can start to report power estimates. One can get more accurate estimates by using this option to enable a calibration cycle. This will cycle through various display levels and USB device activities and workloads.</p>
<dt><code>-C</code>[<i>FILENAME</i>], <code>&#8211;csv</code>[<code>=</code><i>FILENAME</i>]</p>
<dd>generate a CSV report. If a filename is not specified then the default name &quot;powertop.csv&quot; is used. If filename is &quot;<code>&#8211;</code>&quot; then STDOUT is used. The CSV report can be used for reporting and data analysis.</p>
<dt><code>-d</code>[<i>FILENAME</i>], <code>&#8211;dump</code>[<code>=</code><i>FILENAME</i>]</p>
<dd>generate a plain text report. If a filename is not specified or it is &quot;<code>&#8211;</code>&quot; then STDOUT is used.</p>
<dt><code>&#8211;debug</code></p>
<dd>&nbsp;<wbr>run in&nbsp;<wbr>&quot;debug&quot;&nbsp;<wbr>mode.</p>
<dt><code>&#8211;extech=</code><i>devnode</i></p>
<dd>use the Extech Power Analyzer for measurements. This allows one to specify the serial device node of the serial to USB adaptor connecting to the Extech Power Analyzer, for example /dev/ttyUSB0.</p>
<dt><code>&#8211;help</code></p>
<dd>&nbsp;<wbr>show the help message.</p>
<dt><code>-r</code>[<i>FILENAME</i>], <code>&#8211;html</code>[<code>=</code><i>FILENAME</i>]</p>
<dd>generate an HTML report. If a filename is not specified then the default name &quot;powertop.html&quot; is used. If filename is &quot;<code>&#8211;</code>&quot; then STDOUT is used. The HTML report can be sent to others to help diagnose power issues.</p>
<dt><code>&#8211;iteration</code>[<code>=</code><i>iterations</i>]</p>
<dd>number of times to run each test.</p>
<dt><code>&#8211;workload</code>[<code>=</code><i>workload</i>]</p>
<dd>file to execute for workload.</p>
<dt><code>&#8211;quiet</code></p>
<dd>&nbsp;<wbr>supress stderr output.</p>
<dt><code>&#8211;time</code>[<code>=</code><i>seconds</i>]</p>
<dd>generate a report for a specified number of seconds.</p>
<dt><code>&#8211;version</code></p>
<dd>print version information and exit.</dl>
<h2>Bugs</h2>
<p>Send bug reports to &lt;powertop [at] lists.01.org&gt;</p>
<h2>See Also</h2>
<p>The program is more fully described at <a rel="nofollow" href="https://01.org/powertop">https://01.org/powertop</a></p>
<h2>Author</h2>
<p>powertop was written by Arjan van de Ven &lt;arjan [at] linux.intel.com&gt;, and is currently maintained by Chris E Ferron &lt;chris.e.ferron [at] linux.intel.com&gt;.</p>
