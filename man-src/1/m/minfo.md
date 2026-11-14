---
title: "minfo(1)"
name: "minfo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-minfo/"
description: "minfo – print the parameters of a MSDOS filesystem"
---

<h2>Name</h2>
<p> minfo &#8211; print the parameters of a MSDOS filesystem </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>minfo</tt> command prints the parameters of a MS-DOS file system, such as number of sectors, heads and cylinders. It also prints an mformat command line which can be used to create a similar MS-DOS file system on another media. However, this doesn&#8217;t work with 2m or XDF media, and with MS-DOS 1.0 file systems <i> </i></p>
<pre>
<tt>minfo</tt> <i>drive</i>:
</pre>
<p>&nbsp; </p>
<p> Minfo supports the following option:</p>
<dl>
<dt><tt>v</tt>&nbsp;</p>
<dd> Prints a hexdump of the boot sector, in addition to the other information</dl>
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
