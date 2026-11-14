---
title: "mlabel(1)"
name: "mlabel"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlabel/"
description: "mlabel – make an MSDOS volume label"
---

<h2>Name</h2>
<p> mlabel &#8211; make an MSDOS volume label </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mlabel</tt> command adds a volume label to a disk. Its syntax is: <i> </i></p>
<pre><code>
mlabel[-vcsn][-N serial] drive : [new_label]
</code></pre>
<p>&nbsp; </p>
<p> <tt>Mlabel</tt> displays the current volume label, if present. If <i>new_label</i> is not given, and if neither the <tt>c</tt> nor the <tt>s</tt> options are set, it prompts the user for a new volume label. To delete an existing volume label, press return at the prompt. </p>
<p> The label is limited to 11 single-byte characters, e.g. <tt>Name1234567</tt>. </p>
<p> Reasonable care is taken to create a valid MS-DOS volume label. If an invalid label is specified, <tt>mlabel</tt> changes the label (and displays the new label if the verbose mode is set). <tt>Mlabel</tt> returns 0 on success or 1 on failure. </p>
<p> Mlabel supports the following options:</p>
<dl>
<dt><tt>c</tt>&nbsp;</p>
<dd> Clears an existing label, without prompting the user</p>
<dt><tt>s</tt>&nbsp;</p>
<dd> Shows the existing label, without prompting the user.</p>
<dt><tt>n&nbsp;</tt>&nbsp;</p>
<dd> Assigns a new (random) serial number to the disk</p>
<dt><tt>N&nbsp;</tt><i>serial</i><tt></tt>&nbsp;</p>
<dd> Sets the supplied serial number. The serial number should be supplied as an 8 digit hexadecimal number, without spaces</dl>
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
