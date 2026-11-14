---
title: "cfetoolgraph(8)"
name: "cfetoolgraph"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolgraph/"
description: "cfetoolgraph – create graphs from a cfetool database"
---

<p>cfetoolgraph &#8211; create graphs from a cfetool database</p>
<h2>Synopsis</h2>
<p><code>cfetoolgraph</code> <i>name</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;timestamps</code>|<code>-T</code>] [<code>&#8211;resolution</code>|<code>-r</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>The cfetoolgraph command dumps graphs of averages for visual inspection of the normal state database. The files are in a format viewable by <tt>&quot;gnuplot&quot;</tt> or <tt>&quot;xgmr&quot;</tt> or other graphical plotting program. </p>
<p> The command generates three or four files in a subdirectory of the database directory with a name beginning with either <tt>&quot;daily&quot;</tt>, <tt>&quot;weekly&quot;</tt> or <tt>&quot;yearly&quot;</tt>, then <tt>&quot;-&quot;</tt>, then either <tt>&quot;snapshot&quot;</tt> or the current time, if the <code>-T</code> option is used. The files are named <tt>&quot;average&quot;</tt>, <tt>&quot;stddev&quot;</tt>, and <tt>&quot;graph&quot;</tt>. The <tt>&quot;graph&quot;</tt> file contains both the averages and standard deviations, useful for plotting with error bars. </p>
<p> If a histogram file is present, a fourth file named <tt>&quot;distr&quot;</tt> will also be created, plotting the distribution of fluctuations about the mean value. </p>
<p> If the <code>-d</code>, <code>-w</code> and <code>-y</code> options are all omitted, the default is to only graph the weekly database.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;path</code>|<code>-p</code> <i>directory name</i></p>
<dd>The directory in which the database specified by <i>name</i> can be found.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Graph the daily averages database.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Graph the weekly averages database.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Graph the yearly averages database.</p>
<dt><code>&#8211;timestamps</code>|<code>-T</code></p>
<dd>Time-stamp the output filenames with the current time, in order to give a unique name.</p>
<dt><code>&#8211;resolution</code>|<code>-r</code></p>
<dd>Generate high resolution data (), instead of averaging data over periods of one hour to generate simpler and smoother graphs.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Prints a short help message and then exits.</dl>
<h2>Example</h2>
<pre> % cfetoolgraph temperature --path /my/path --resolution</pre>
<p>Create graph files of the weekly database in high resolution in the <tt>&quot;/my/path/temperature/weekly-snapshot&quot;</tt> directory.</p>
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
