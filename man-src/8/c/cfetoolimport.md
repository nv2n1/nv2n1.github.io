---
title: "cfetoolimport(8)"
name: "cfetoolimport"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfetoolimport/"
description: "cfetool import – import the contents of a database from XML format"
---

<p>cfetool import &#8211; import the contents of a database from XML format</p>
<h2>Synopsis</h2>
<p><code>cfetool</code> <code>import</code> <i>name</i> <code>&#8211;file</code>|<code>-f</code>&nbsp;<wbr><i>filename</i> [<code>&#8211;path</code>|<code>-p</code>&nbsp;<wbr><i>directory name</i>] [<code>&#8211;daily</code>|<code>-d</code>] [<code>&#8211;weekly</code>|<code>-w</code>] [<code>&#8211;yearly</code>|<code>-y</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;help</code>|<code>-h</code>]</p>
<h2>Description</h2>
<p>Creates a new database from it&#8217;s <font SIZE="-1">XML</font> representation, in the format created by <code>rrdtool dump</code>. </p>
<p> The <code>-d</code>, <code>-w</code>, and <code>-y</code> options specify which databases to create and look for in the dump, and may be combined. If they are all ommitted, the default is to only import the weekly database.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;file</code>|<code>-f</code> <i>filename</i></p>
<dd>Specifies the <font SIZE="-1">XML</font> file to restore.</p>
<dt><code>&#8211;path</code>|<code>-p</code></p>
<dd>The directory in which to create the new database folder. If this argument is not provided, the current working directory will be used.</p>
<dt><code>&#8211;daily</code>|<code>-d</code></p>
<dd>Create a database for recording daily patterns.</p>
<dt><code>&#8211;weekly</code>|<code>-w</code></p>
<dd>Create a database for recording weekly patterns.</p>
<dt><code>&#8211;yearly</code>|<code>-y</code></p>
<dd>Create a database for recording yearly patterns.</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd>Print details of the command&#8217;s execution to the standard output stream.</p>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Print a short help message and then exit.</dl>
<h2>Example</h2>
<pre> % cfetool import temperature_copy --path /my/path --file ./temperature.xml</pre>
<p>Create a new weekly database, <tt>&quot;temperature_copy&quot;</tt>, in the <tt>&quot;/my/path&quot;</tt> directory, and import it&#8217;s contents from the file <tt>&quot;temperature.xml&quot;</tt> in the current working directory.</p>
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
