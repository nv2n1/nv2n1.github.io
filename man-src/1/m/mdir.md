---
title: "mdir(1)"
name: "mdir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdir/"
description: "mdir – display an MSDOS directory"
---

<h2>Name</h2>
<p> mdir &#8211; display an MSDOS directory </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mdir</tt> command is used to display an MS-DOS directory. Its syntax is: </p>
<p> <tt>mdir</tt> [<tt>-/</tt>] [<tt>-f</tt>] [<tt>-w</tt>] [<tt>-a</tt>] [<tt>-b</tt>] <i>msdosfile</i> [ <i>msdosfiles</i>&#8230;] </p>
<p> <tt>Mdir</tt> displays the contents of MS-DOS directories, or the entries for some MS-DOS files. </p>
<p> <tt>Mdir</tt> supports the following command line options:</p>
<dl>
<dt><tt>/</tt>&nbsp;</p>
<dd> Recursive output, just like MS-DOS&#8217; <tt>-s</tt> option</p>
<dt><tt>w</tt>&nbsp;</p>
<dd> Wide output. With this option, <tt>mdir</tt> prints the filenames across the page without displaying the file size or creation date.</p>
<dt><tt>a</tt>&nbsp;</p>
<dd> Also list hidden files.</p>
<dt><tt>f</tt>&nbsp;</p>
<dd> Fast. Do not try to find out free space. On larger disks, finding out the amount of free space takes up some non trivial amount of time, as the whole FAT must be read in and scanned. The <tt>-f</tt> flag bypasses this step. This flag is not needed on FAT32 file systems, which store the size explicitly.</p>
<dt><tt>b</tt>&nbsp;</p>
<dd> Concise listing. Lists each directory name or filename, one per line (including the filename extension). This switch displays no heading information and no summary. Only a newline separated list of pathnames is displayed.</dl>
<p> An error occurs if a component of the path is not a directory. </p>
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
