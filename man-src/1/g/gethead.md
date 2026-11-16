---
title: "gethead(1)"
name: "gethead"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gethead/"
description: "gethead – Print FITS or IRAF header keyword values"
---

<h2>Name</h2>
<p> gethead &#8211; Print FITS or IRAF header keyword values</p>
<h2>Synopsis</h2>
<p> gethead [-hptv] [-d pathname] [-n num] &lt;FITS or IRAF file&gt; kw1 kw2 &#8230; kwn</p>
<h2>Description</h2>
<p> Print values of the specified keywords from the given image header. By default they are all listed on one line, separated by spaces. The <i>-v</i> flag causes the keyword names and values to be printed, one keyword per line. To read keywords from a list of files, substitute @&lt;listfile&gt; for the file names on the command line. To read a lot of keywords, put them, one per line, in a file and substitute @&lt;keylistfile&gt; on the command line. If two @ commands are present, the program will figure out which contains file names and which contains keywords. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd> List file name even if keywords are not found</dd>
<dt><code>-d</code></dt>
<dd> Root directory for input files (default is cwd)</dd>
<dt><code>-e</code></dt>
<dd> Output keyword=value&#8217;s on one line per file</dd>
<dt><code>-f</code></dt>
<dd> Never print filenames (default is to print them if more than one)</dd>
<dt><code>-g</code></dt>
<dd> Output keyword=value&#8217;s on one line per keyword</dd>
<dt><code>-h</code></dt>
<dd> flag causes the keyword names to be printed at top of columns.</dd>
<dt><code>-n</code></dt>
<dd> Number of decimal places in numeric output</dd>
<dt><code>-o</code></dt>
<dd> OR conditions instead of ANDing them</dd>
<dt><code>-p</code></dt>
<dd> Print full pathnames of files</dd>
<dt><code>-t</code></dt>
<dd> flag causes the output to be in tab-separated tables with keyword column headings.</dd>
<dt><code>-u</code></dt>
<dd> Always print ___ if keyword not found, event if only one keyword in search</dd>
<dt><code>-v</code></dt>
<dd> Print output as &lt;keyword&gt;=&lt;value&gt;, one per line </dd>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/gethead.html">http://tdc-www.harvard.edu/software/wcstools/gethead.html</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
