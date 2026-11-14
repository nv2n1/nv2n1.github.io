---
title: "mcd(1)"
name: "mcd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcd/"
description: "mcd – change MSDOS directory"
---

<h2>Name</h2>
<p> mcd &#8211; change MSDOS directory </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mcd</tt> command is used to change the mtools working directory on the MS-DOS disk. It uses the following syntax: </p>
<p>&nbsp; </p>
<pre>
<tt>mcd [</tt><i>msdosdirectory</i><tt>]
</tt></pre>
<p>&nbsp; </p>
<p> Without arguments, <tt>mcd</tt> reports the current device and working directory. Otherwise, <tt>mcd</tt> changes the current device and current working directory relative to an MS-DOS file system. </p>
<p> The environmental variable <tt>MCWD</tt> may be used to locate the file where the device and current working directory information is stored. The default is <tt>&infin;$HOME/.mcwdIntegral</tt>. Information in this file is ignored if the file is more than 6 hours old. </p>
<p> <tt>Mcd</tt> returns 0 on success or 1 on failure. </p>
<p> Unlike MS-DOS versions of <tt>CD</tt>, <tt>mcd</tt> can be used to change to another device. It may be wise to remove old <tt>&infin;.mcwdIntegral</tt> files at logout. </p>
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
