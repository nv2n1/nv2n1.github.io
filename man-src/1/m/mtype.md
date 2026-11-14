---
title: "mtype(1)"
name: "mtype"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtype/"
description: "mtype – display contents of an MSDOS file"
---

<h2>Name</h2>
<p> mtype &#8211; display contents of an MSDOS file </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mtype</tt> command is used to display contents of an MS-DOS file. Its syntax is: </p>
<p> <i> </i></p>
<pre><code>
mtype[-ts] msdosfile[msdosfiles...]
</code></pre>
<p>&nbsp; </p>
<p> <tt>Mtype</tt> displays the specified MS-DOS file on the screen. </p>
<p> In addition to the standard options, <tt>Mtype</tt> allows the following command line options:</p>
<dl>
<dt><tt>t</tt>&nbsp;</p>
<dd> Text file viewing. <tt>Mtype</tt> translates incoming carriage return/line feeds to line feeds.</p>
<dt><tt>s</tt>&nbsp;</p>
<dd> <tt>Mtype</tt> strips the high bit from the data.</dl>
<p> The <tt>mcd</tt> command may be used to establish the device and the current working directory (relative to MS-DOS), otherwise the default is <tt>A:/</tt>. </p>
<p> <tt>Mtype</tt> returns 0 on success, 1 on utter failure, or 2 on partial failure. </p>
<p> Unlike the MS-DOS version of <tt>TYPE</tt>, <tt>mtype</tt> allows multiple arguments. </p>
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
