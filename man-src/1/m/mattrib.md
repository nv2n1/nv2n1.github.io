---
title: "mattrib(1)"
name: "mattrib"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mattrib/"
description: "mattrib – change MSDOS file attribute flags"
---

<h2>Name</h2>
<p> mattrib &#8211; change MSDOS file attribute flags </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> <tt>Mattrib</tt> is used to change MS-DOS file attribute flags. It has the following syntax: </p>
<p> <tt>mattrib</tt> [<tt>-a|+a</tt>] [<tt>-h|+h</tt>] [<tt>-r|+r</tt>] [<tt>-s|+s</tt>] [<tt>-/</tt>] [<tt>-p</tt>] [<tt>-X</tt>] <i>msdosfile</i> [ <i>msdosfiles</i> &#8230; ] </p>
<p> <tt>Mattrib</tt> adds attribute flags to an MS-DOS file (with the `<tt>+</tt>&#8216; operator) or remove attribute flags (with the `<tt>-</tt>&#8216; operator). </p>
<p> <tt>Mattrib</tt> supports the following attribute bits:</p>
<dl>
<dt><tt>a</tt>&nbsp;</p>
<dd> Archive bit. Used by some backup programs to indicate a new file.</p>
<dt><tt>r</tt>&nbsp;</p>
<dd> Read-only bit. Used to indicate a read-only file. Files with this bit set cannot be erased by <tt>DEL</tt> nor modified.</p>
<dt><tt>s</tt>&nbsp;</p>
<dd> System bit. Used by MS-DOS to indicate a operating system file.</p>
<dt><tt>h</tt>&nbsp;</p>
<dd> Hidden bit. Used to make files hidden from <tt>DIR</tt>.</dl>
<p> <tt>Mattrib</tt> supports the following command line flags:</p>
<dl>
<dt><tt>/</tt>&nbsp;</p>
<dd> Recursive. Recursively list the attributes of the files in the subdirectories.</p>
<dt><tt>X</tt>&nbsp;</p>
<dd> Concise. Prints the attributes without any whitespace padding. If neither the &quot;/&quot; option is given, nor the <i>msdosfile</i> contains a wildcard, and there is only one MS-DOS file parameter on the command line, only the attribute is printed, and not the filename. This option is convenient for scripts</p>
<dt><tt>p</tt>&nbsp;</p>
<dd> Replay mode. Outputs a series of mformat commands that will reproduce the current situation, starting from a situation as left by untarring the MS-DOS file system. Commands are only output for attribute settings that differ from the default (archive bit set for files, unset for directories). This option is intended to be used in addition to tar. The <tt>readonly</tt> attribute is not taken into account, as tar can set that one itself.</dl>
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
