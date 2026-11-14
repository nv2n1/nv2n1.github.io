---
title: "sethead(1)"
name: "sethead"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sethead/"
description: "sethead – Set FITS or IRAF header keyword values"
---

<h2>Name</h2>
<p> sethead &#8211; Set FITS or IRAF header keyword values</p>
<h2>Synopsis</h2>
<p> sethead [-dknv][r letter] &lt;FITS or IRAF file&gt; kw1=val1 kw2=val2 &#8230; kwn=valuen</p>
<h2>Description</h2>
<p> Set parameters in the header of a FITS or IRAF image. If the keywords do not already exist, they are added at the end of the header. Values are assumed to be numeric if they contain no alphabetic characters and right-aligned. Otherwise they are left-aligned after the equals sign, and padded by spaces to a minimum of 8 characters. To set keywords in a list of files, substitute @&lt;listfile&gt; for the file names on the command line. To set a lot of keywords, put them, one per line, in a file and substitute @&lt;keylistfile&gt; on the command line. If two @ commands are present, the program will figure out which contains file names and which contains keywords. Lines in a keyword list file which do not contain an = are ignored. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd> Write HISTORY line into output header with <code>sethead</code> version, current date and time, and names of keywords set.</p>
<dt><code>-k</code></p>
<dd> Write SETHEAD keyword into output header with <code>sethead</code> version, current date and time, and names of keywords set. If a SETHEAD keyword already exists, move the old value to a HISTORY line before writing the new value</p>
<dt><code>-n</code></p>
<dd> Write a new file with an added &quot;e&quot; before the extension.</p>
<dt><code>-r letter</code></p>
<dd> Rename existing keywords whose values are being reset by prepending the character &quot;letter&quot;. Drop the last character if the changed keyword is already 8 characters long.</p>
<dt><code>-v</code></p>
<dd> Print confirmations of each parameter setting</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/sethead.html">http://tdc-www.harvard.edu/software/wcstools/sethead.html</a></p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
