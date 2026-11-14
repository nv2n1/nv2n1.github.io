---
title: "cfetooldump(8)"
name: "cfetooldump"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetooldump/"
description: "cfetool dump – dump the contents of a database in XML format"
---

<p>cfetool dump &#8211; dump the contents of a database in XML format</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>dump</code> <i>name</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;file</code>|<code>-f</code>&nbsp;<wbr><i>filename</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Prints the contents of the specified database in <font SIZE="-1">XML</font> format, with comments for human readability. This format can be read by <code>cfetool import</code>. </p>
<p> The <code>-d</code>, <code>-w</code>, and <code>-y</code> options specify which databases to include in the dump, and may be combined. If they are all ommitted, the default is to only dump the weekly database.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;path</code>|<code>-p</code> <i>directory name</i></p>
<dd>Names the directory in which the database specified by <i>name</i> can be found.</p>
<dt><code>&#8211;file</code>|<code>-f</code> <i>filename</i></p>
<dd>Names a file to print the <font SIZE="-1">XML</font> to. If this option is omitted, the <font SIZE="-1">XML</font> will be printed to the standard output stream.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Include the daily pattern database in the dump.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Include the weekly pattern database in the dump.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Include the yearly pattern database in the dump.</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd>Print details of the command&#8217;s execution to the standard output stream. When using this argument, it is recommended that you also provide the <code>-f</code> argument, to avoid sharing the standard output stream.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Print a short help message and then exit.</dl>
<h2>Example</h2>
<pre> % cfetool dump temperature --path /my/path -f temperature.xml</pre>
<p>Prints the following to the file <code>temperature.xml</code>: </p>
<pre> &lt;!-- cfetool Database Dump --&gt;
 &lt;dump&gt;</pre>
<pre> &lt;name&gt; temperature &lt;/name&gt;</pre>
<pre> &lt;age&gt; 1 &lt;/age&gt; &lt;!-- steps (0.001 weeks) --&gt;</pre>
<pre> &lt;step&gt; 10 &lt;/step&gt; &lt;!-- minutes --&gt;</pre>
<pre> &lt;!-- consecutive updates --&gt;
 &lt;iterations&gt; 1 &lt;/iterations&gt;</pre>
<pre> &lt;!-- last update at Tue Aug 31 10:32:05 2004 --&gt;
 &lt;timestamp&gt; 1093973525 &lt;/timestamp&gt;</pre>
<pre> &lt;!-- current weighted average --&gt;
 &lt;expect&gt; 7.105000 &lt;/expect&gt;</pre>
<pre> &lt;!-- current variance --&gt;
 &lt;var&gt; 38.280217 &lt;/var&gt;</pre>
<pre> &lt;!-- data entries --&gt;
 &lt;entry&gt; &lt;timekey&gt; Tue:Hr10:Min30_40 &lt;/timekey&gt;
 &lt;expect&gt; 10.150000 &lt;/expect&gt;
 &lt;var&gt; 13.245750 &lt;/var&gt;
 &lt;/entry&gt;</pre>
<pre><code>&lt;/dump&gt;</code></pre>
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
