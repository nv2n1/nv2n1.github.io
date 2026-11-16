---
title: "cfetoolcreate(8)"
name: "cfetoolcreate"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolcreate/"
description: "cfetool create – Set up a new Database"
---

<p>cfetool create &#8211; Set up a new Database</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>create</code> <i>name</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;step</code>|<code>-s</code>&nbsp;<wbr><i>step</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;cfenvd</code>|<code>-c</code>] [<code>&#8211;histograms</code>|<code>-H</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;file</code>|<code>-f</code>&nbsp;<wbr><i>filename</i>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Creates a new database and, optionally, histogram file in a new directory with the name given. If the <code>-p</code> option is specified, it will be created as a subdirectory of the path given. Otherwise, it will be a subdirectory of the current working directory. </p>
<p> The <code>-d</code>, <code>-w</code>, and <code>-y</code> options specify the period over which the data will span, and may be combined to create multiple databases. If they are all ommitted, the default is weekly.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;path</code>|<code>-p</code></dt>
<dd>The directory in which to create the new database folder. If this argument is not provided, the current working directory will be used.</dd>
<dt><code>&#8211;step</code>|<code>-s</code></dt>
<dd>The interval, in minutes, with which the database will be updated. If this argument is not provided, cfetool assumes a default of 5 minutes.</dd>
<dt><code>&#8211;daily</code>|<code>-d</code></dt>
<dd>Create a database for recording daily patterns.</dd>
<dt><code>&#8211;weekly</code>|<code>-w</code></dt>
<dd>Create a database for recording weekly patterns.</dd>
<dt><code>&#8211;yearly</code>|<code>-y</code></dt>
<dd>Create a database for recording yearly patterns.</dd>
<dt><code>&#8211;cfenvd</code>|<code>-c</code></dt>
<dd>Communicate with cfengine. If this option is specified, cfetool will set classes understandable by cfagent. For more information, see the <code>cfenvd</code> documentation.</dd>
<dt><code>&#8211;histograms</code>|<code>-H</code></dt>
<dd>Create a histogram file, to store information about the probability distribiution of fluctuations about the mean value over all times of day. Cfetool won&#8217;t write anything to this file for the first four weeks, as it has to have reliable mean values in order to accurately calculate it.</dd>
<dt><code>&#8211;verbose</code>|<code>-v</code></dt>
<dd>Print details of the command&#8217;s execution to the standard output stream.</dd>
<dt><code>&#8211;file</code>|<code>-f</code></dt>
<dd>Specifies a file which contains measurements to feed into the database in batch mode. Used for testing purposes. Each line in the file should be in either of these formats: </dd>
<p> <i>month</i>/<i>day</i>/<i>year</i> <i>hour</i>:<i>min</i>:<i>sec</i> <i>value</i> </p>
<p> or </p>
<p> <i>epoch</i> <i>value</i></p>
<dt><code>&#8211;help</code>|<code>-h</code></dt>
<dd>Prints a short help message and then exits.</dd></dl>
<h2>Example</h2>
<pre> % cfetool create temperature --path /my/path --histograms --step 10</pre>
<p>Creates an empty database and histogram file in <code>/my/path/temperature/</code>, ready to store values over ten minute intervals spanning a one-week period.</p>
<h2>Authors</h2>
<p>The code and documentation were contributed by Stanford Linear Accelerator Center, a department of Stanford University. This documentation was written by</p>
<dl>
<dt>Elizabeth Cassell &lt;e_a_c [at] mailsnare.net&gt; and</dt>
<dd>
</dd><dt>Alf Wachsmann &lt;alfw [at] slac.stanford.edu&gt;</dt>
<dd></dd></dl>
<h2>Copyright And Disclaimer</h2>
<pre> Copyright 2004 Alf Wachsmann &lt;alfw [at] slac.stanford.edu&gt; and
 Elizabeth Cassell &lt;e_a_c [at] mailsnare.net&gt;
 All rights reserved.</pre>
