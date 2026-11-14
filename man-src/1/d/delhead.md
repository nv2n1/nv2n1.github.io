---
title: "delhead(1)"
name: "delhead"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delhead/"
description: "delhead – Set FITS or IRAF header keyword values"
---

<h2>Name</h2>
<p> delhead &#8211; Set FITS or IRAF header keyword values</p>
<h2>Synopsis</h2>
<p> delhead [-nv] &lt;FITS or IRAF file[s]&gt; kw1 kw2 &#8230; kwn</p>
<h2>Description</h2>
<p> Delete keyword entries from the header of FITS or IRAF image[s]. If a keyword does not already exist, ignore it. To delete keywords in a list of files, substitute @&lt;listfile&gt; for the file names on the command line. To delete a lot of keywords, put them, one per line, in a file and substitute @&lt;keylistfile&gt; on the command line. If two @ commands are present, the program will figure out which contains file names and which contains keywords.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd> Write a new file with an added &quot;e&quot; before the extension. The default is to overwrite the input file.</p>
<dt><code>-v</code></p>
<dd> Print confirmations of each parameter setting</dl>
<h2>Web page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/delhead.html">http://tdc-www.harvard.edu/software/wcstools/delhead.html</a></p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
