---
title: "mcat(1)"
name: "mcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcat/"
description: "mcat – dump raw disk image"
---

<h2>Name</h2>
<p> mcat &#8211; dump raw disk image </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mcat</tt> command is used to copy an entire disk image from or to the floppy device. It uses the following syntax: </p>
<p> <tt>mcat</tt> [<tt>-w</tt>] <i>drive</i><tt>:</tt> </p>
<p> <tt>Mcat</tt> performs the same task as the Unix <tt>cat</tt> command. It is included into the mtools package, since <tt>cat</tt> cannot access remote floppy devices offered by the mtools floppy daemon. Now it is possible to create boot floppies remotely. </p>
<p> The default operation is reading. The output is written to stdout. </p>
<p> If the <tt>-w</tt> option is specified, mcat reads a disk-image from stdin and writes it to the given device. <code>Use this carefully!</code> Because of the low-level nature of this command, it will happily destroy any data written before on the disk without warning! </p>
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
