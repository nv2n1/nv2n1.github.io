---
title: "keyhead(1)"
name: "keyhead"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keyhead/"
description: "keyhead – Change FITS or IRAF header keyword names"
---

<h2>Name</h2>
<p> keyhead &#8211; Change FITS or IRAF header keyword names</p>
<h2>Synopsis</h2>
<p> sethead [-hknv] &lt;FITS or IRAF file&gt; kw1=kw1a kw2=kwd2a &#8230; kwn=kwdna</p>
<h2>Description</h2>
<p> Change the names of keywords in FITS or IRAF image headers. Each current image keyword whose entry is to be modified should be followed by an equal sign and a second keyword, with no intervening spaces. If the -r option is used, the value of the second keyword is transfered to that of the first. Otherwise, the name of the first keyword is changed to the second keyword. To change keywords in a list of files, substitute @&lt;listfile&gt; for the file names on the command line. To change a lot of keywords, put them, one pair separated by an = sign with no spaces per line, in a file and substitute @&lt;keylistfile&gt; on the command line. If two @ commands are present, the program will figure out which contains file names and which contains keywords. Lines in a keyword list file which do not contain an = are ignored. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd> Write HISTORY line into output header with <code>sethead</code> version, current date and time, and names of keywords set.</p>
<dt><code>-k</code></p>
<dd> Write KEYHEAD keyword into output header with the <code>keyhead</code> version, current date and time, and names of keywords whose names are changed. If a KEYHEAD keyword already exists, move the old value to a HISTORY line before writing the new value</p>
<dt><code>-n</code></p>
<dd> Write a new file with an added &quot;e&quot; before the extension.</p>
<dt><code>-r letter</code></p>
<dd> Replace value of 1st keyword with value of 2nd keyword instead of changing the name of the 1st keyword to the 2nd keyword. The 2nd keyword remains in the header. If the 1st keyword does not exist in the header, it is created.</p>
<dt><code>-v</code></p>
<dd> Print confirmations of each keyword change. </p>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/keyhead.html">http://tdc-www.harvard.edu/software/wcstools/keyhead.html</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
