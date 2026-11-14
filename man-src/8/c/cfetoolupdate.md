---
title: "cfetoolupdate(8)"
name: "cfetoolupdate"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolupdate/"
description: "cfetool update – Update the database with a new value"
---

<p>cfetool update &#8211; Update the database with a new value</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>update</code> <i>name</i> <code>&#8211;value</code>|<code>-V</code>&nbsp;<wbr><i>value</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;time</code>|<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;cfenvd</code>|<code>-c</code>] [<code>&#8211;histograms</code>|<code>-H</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Takes a new value and uses it to update the database specified by <i>name</i>, located at the path specified by the <code>-p</code> argument, or the current working directory if the <code>-p</code> argument is ommitted. The value will be associated with the current time, unless the <code>-t</code> option is given. In order for cfetool to function properly, this command should be issued at least once during each interval specified by the <code>&#8211;step</code> option of <tt>&quot;cfetool create&quot;</tt>. </p>
<p> The <code>-d</code>, <code>-w</code> and <code>-y</code> options specify the databases to update. If all three options are omitted, only the weekly database will be updated.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;value</code>|<code>-v</code> <i>value</i></p>
<dd>Specifies a new value to update the database with.</p>
<dt><code>&#8211;path</code>|<code>-p</code> <i>directory name</i></p>
<dd>The directory in which the database specified by <i>name</i> can be found.</p>
<dt><code>&#8211;time</code>|<code>-t</code></p>
<dd>The time the value was collected, in seconds since epoch (January 1st, 1970). If this argument is omitted, the current time will be used.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Update the daily averages database.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Update the weekly averages database.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Update the yearly averages database.</p>
<dt><code>&#8211;cfenvd</code>|<code>-c</code></p>
<dd>Communicate with cfengine. If this option is specified, cfetool will define classes understandable by cfagent. For more information, refer to the documentation for <code>cfenvd</code>.</p>
<dt><code>&#8211;histograms</code>|<code>-H</code></p>
<dd>Collect histogram information about the probability distribiution of fluctuations about the mean value over all times of day. Cfetool won&#8217;t write anything to this file for the first four weeks, as it has to have reliable mean values in order to accurately calculate it.</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd>Print details of the command&#8217;s execution to the standard output stream.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Print a short help message and then exit.</dl>
<h2>Output</h2>
<p>Before exiting, <tt>&quot;cfetool update&quot;</tt> will print one line to the standard output stream in the following format: </p>
<p> yrly=<i>ynum</i>,wkly=<i>wnum</i>,dly=<i>dnum</i> </p>
<p> <i>ynum</i>, <i>wnum</i> and <i>dnum</i> will be either the number 0 if the corresponding database was not updated, or a code indicating the state of the given statistic, as compared to an average of equivalent earlier times, as specified below: </p>
<pre> code high|low|normal meaning
 -------------------------------------------------------------
 -2 - no sigma variation
 -------------------------------------------------------------
 -4 low within noise threshold, and within
 -5 normal 2 standard deviations from
 -6 high expected value
 -------------------------------------------------------------
 -14 low microanomaly: within noise
 -15 normal threshold, but 2 or more standard
 -16 high deviations from expected value
 -------------------------------------------------------------
 -24 low normal; within 1 standard deviation
 -25 normal from the expected value
 -26 high 
 -------------------------------------------------------------
 -34 low dev1; more than 1 standard 
 -35 normal deviation from the expected
 -36 high value
 ------------------------------------------------------------
 -44 low dev2; more than 2 standard
 -45 normal deviations from the expected
 -46 high value
 -------------------------------------------------------------
 -54 low anomaly; more than 3 standard
 -55 normal deviations from the expected
 -56 high value</pre>
<p>Where &#8220;low&#8221; indicates that the current value is below both the expected value for the current time position, and the global average value. &#8220;high&#8221; indicates that the current value is above those values. &#8220;normal&#8221; indicates that the current value is within the range of expected values. </p>
<p> <tt>&quot;cfetool update&quot;</tt> also exits with a code corresponding to the above table. If more than one database is being updated, the most negative result from the updates is returned, and the individual results must be obtained from the standard output stream, as described above.</p>
<h2>Example</h2>
<pre> % cfetool update temperature --path /my/path --value 14.5 --histograms
 yrly=0,wkly=-6,dly=0</pre>
<p>Updates the weekly temperature database and histogram files located in <code>/my/path/</code> with the value 14.5 using the current time as the update time. The output indicates that only a weekly database was updated, and the new value given was within cfetool&#8217;s noise threshold, and also within 2 standard deviations of the previous average stored in the database.</p>
<h2>Authors</h2>
<p>The code and documentation were contributed by Stanford Linear Accelerator Center, a department of Stanford University. This documentation was written by</p>
<dl>
<dt>Elizabeth Cassell &lt;e_a_c [at] mailsnare.net&gt; and</p>
<dd>
<dt>Alf Wachsmann &lt;alfw [at] slac.stanford.edu&gt;</p>
<dd></dl>
<h2>Copyright And Disclaimer</h2>
<pre> Copyright 2004 Alf Wachsmann &lt;alfw [at] slac.stanford.edu&gt; and
 Elizabeth Cassell &lt;e_a_c [at] mailsnare.net&gt;
 All rights reserved.</pre>
