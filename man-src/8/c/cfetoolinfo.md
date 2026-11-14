---
title: "cfetoolinfo(8)"
name: "cfetoolinfo"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolinfo/"
description: "cfetool info – Get information about a database"
---

<p>cfetool info &#8211; Get information about a database</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>info</code> <i>name</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Prints out some basic information about the specified database, including: the location of the database, the location of the histogram file (if there is one), the step interval, the database age, the time it was last updated, and the current overall average and variation.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;path</code>|<code>-p</code> <i>directory name</i></p>
<dd>The directory in which to find the database folder. If this argument is not provided, the current working directory will be assumed.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Provide information about the daily averages database.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Provide information about the weekly averages database.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Provide information about the yearly averages database.</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd>Print details of the command&#8217;s execution to the standard output stream.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Prints a short help message and then exits.</dl>
<h2>Example</h2>
<pre> % cfetool info temperature --path /my/path</pre>
<pre> Weekly average database:
 Database Location: /my/path/temperature/weekly.db
 Histogram file: /my/path/temperature/weekly.hist
 Step: 10 minutes
 Database Age: 0.000992 weeks (1 steps)
 Last update: Mon Sep 13 16:20:40 2004 (1095117640)
 Current average: 7.105000, Var: 38.280217</pre>
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
