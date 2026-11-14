---
title: "mclasserase(1)"
name: "mclasserase"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mclasserase/"
description: "mclasserase – erase memory cards"
---

<h2>Name</h2>
<p> mclasserase &#8211; erase memory cards </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mclasserase</tt> command is used to wipe memory cards by overwriting it three times: first with <tt>0xff</tt>, then with <tt>0x00</tt>, then with <tt>0xff</tt> again. The command uses the following syntax: </p>
<p>&nbsp; </p>
<pre>
<tt>mclasserase [</tt><tt>-d] </tt><i>msdosdrive</i><tt>
</tt></pre>
<p>&nbsp; </p>
<p> MS-DOS drive is optional, if none is specified, use <tt>A:</tt>. If more than one drive are specified, all but the last are ignored. </p>
<p> <tt>Mclasserase</tt> accepts the following command line options:</p>
<dl>
<dt><tt>d</tt>&nbsp;</p>
<dd> Stop after each erase cycle, for testing purposes</p>
<dt><tt>p</tt>&nbsp;</p>
<dd> Not yet implemented</dl>
<p> <tt>Mclasserase</tt> returns 0 on success or -1 on failure. </p>
<h2>See Also</h2>
<p> Mtools&#8217; texinfo doc</p>
<h2>Viewing the texi doc</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation. However, this process is only approximative, and some items, such as crossreferences, footnotes and indices are lost in this translation process. Indeed, these items have no appropriate representation in the manpage format. Moreover, not all information has been translated into the manpage version. Thus I strongly advise you to use the original texinfo doc. See the end of this manpage for instructions how to view the texinfo doc.</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate a printable copy from the texinfo doc, run the following commands:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make dvi; dvips mtools.dvi
</code></pre>
</dl>
<p>&nbsp;</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate a html copy, run:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make html
</code></pre>
</dl>
<p>&nbsp; A premade html can be found at <tt>&infin;<a rel="nofollow" href="http://www.gnu.org/software/mtools/manual/mtools.htmlIntegral">http://www.gnu.org/software/mtools/manual/mtools.htmlIntegral</a></tt></p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate an info copy (browsable using emacs&#8217; info mode), run:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make info
</code></pre>
</dl>
<p>&nbsp; </p>
<p> The texinfo doc looks most pretty when printed or as html. Indeed, in the info version certain examples are difficult to read due to the quoting conventions used in info. </p>
<h2>Index</h2>
