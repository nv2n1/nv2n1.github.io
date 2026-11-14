---
title: "cfetoolcheck(8)"
name: "cfetoolcheck"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolcheck/"
description: "cfetool check – Check a new value against the averages currently in the database"
---

<p>cfetool check &#8211; Check a new value against the averages currently in the database</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>check</code> <i>name</i> <code>&#8211;value</code>|<code>-V</code>&nbsp;<wbr><i>value</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;time</code>|<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;histograms</code>|<code>-H</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Takes a new value and checks it against the averages currently in the database specified by <i>name</i>, located at the path specified by the <code>-p</code> argument, or the current working directory if the <code>-p</code> argument is ommitted. The value will be associated with the current time, unless the <code>-t</code> option is given. The output indicates how much higher or lower the new value is compared to the averages in the database, in terms of the number of standard deviations. </p>
<p> The <code>-d</code>, <code>-w</code> and <code>-y</code> options specify the databases to check the new value against. If all three options are omitted, only the weekly database will be accessed.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;value</code>|<code>-v</code> <i>value</i></p>
<dd>Specifies the new value to check against the database averages.</p>
<dt><code>&#8211;path</code>|<code>-p</code> <i>directory name</i></p>
<dd>The directory in which the database specified by <i>name</i> can be found.</p>
<dt><code>&#8211;time</code>|<code>-t</code></p>
<dd>The time the value was collected, in seconds since epoch (January 1st, 1970). If this argument is omitted, the current time will be used.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Check the new value against the daily averages database.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Check the new value against the weekly averages database.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Check the new value against the yearly averages database.</p>
<dt><code>&#8211;histograms</code>|<code>-H</code></p>
<dd>Check which histogram bucket the new value would fall into. The histogram is divided into 64 buckets, which represent distances from the mean value. Bucket 64 represents two standard deviations above the expected value, and bucket 0 represents two standard deviations below the expected value.</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd>Print details of the command&#8217;s execution to the standard output stream.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Print a short help message and then exit.</dl>
<h2>Output</h2>
<p>Before exiting, <tt>&quot;cfetool check&quot;</tt> will print one line to the standard output stream, in the following format: </p>
<p> yrly=<i>ynum</i>,bkt=<i>ybkt</i>;wkly=<i>wnum</i>,bkt=<i>wbkt</i>;dly=<i>dnum</i>,bkt=<i>dbkt</i> </p>
<p> <i>ybkt</i>, <i>wbkt</i> and <i>dbkt</i> represent the histogram bucket the given value falls into, and will be 0 for databases that are not being checked against, and if there is no histogram file or the <code>-H</code> option was not specified. </p>
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
<p> <tt>&quot;cfetool check&quot;</tt> also exits with a code corresponding to the above table. If more than one database is being checked against, the most negative result from all checks is returned, and the individual results must be obtained from the standard output stream, as described above.</p>
<h2>Example</h2>
<pre> % cfetool check temperature --path /my/path --value 20 --histograms
 yrly=0,bkt=0;wkly=-6,bkt=51;dly=0,bkt=0</pre>
<p>Checks the value 20 against the weekly temperature database and histogram files located in <code>/my/path/</code> using the current time. The output indicates that the new value given was within cfetool&#8217;s noise threshold, and also within 2 standard deviations of the previous average stored in the weekly database.</p>
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
