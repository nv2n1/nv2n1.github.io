---
title: "mren(1)"
name: "mren"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mren/"
description: "mren – rename an existing MSDOS file"
---

<h2>Name</h2>
<p> mren &#8211; rename an existing MSDOS file </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mren</tt> command is used to rename or move an existing MS-DOS file or subdirectory. Its syntax is: </p>
<p> <i> </i></p>
<pre>
<tt>mren</tt> [<tt>-voOsSrRA</tt>] <i>sourcefile</i> <i>targetfile</i>
</pre>
<p>&nbsp; </p>
<p> <tt>Mren</tt> renames an existing file on an MS-DOS file system. </p>
<p> In verbose mode, <tt>Mren</tt> displays the new filename if the name supplied is invalid. </p>
<p> If the first syntax is used (only one source file), and if the target name doesn&#8217;t contain any slashes or colons, the file (or subdirectory) is renamed in the same directory, instead of being moved to the current <tt>mcd</tt> directory as would be the case with <tt>mmove</tt>. Unlike the MS-DOS version of <tt>REN</tt>, <tt>mren</tt> can be used to rename directories. </p>
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
