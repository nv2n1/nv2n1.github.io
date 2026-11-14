---
title: "mbadblocks(1)"
name: "mbadblocks"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbadblocks/"
description: "mbadblocks – tests a floppy disk, and marks the bad blocks in the FAT"
---

<h2>Name</h2>
<p> mbadblocks &#8211; tests a floppy disk, and marks the bad blocks in the FAT </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mbadblocks</tt> command is used to mark some clusters on an MS-DOS filesystem bad. It has the following syntax: </p>
<p> <tt>mbadblocks</tt> [<tt>-s</tt> <i>sectorlist</i>|<tt>-c</tt> <i>clusterlist</i>|-w] <i>drive</i><tt>:</tt> </p>
<p> If no command line flags are supplied, <tt>Mbadblocks</tt> scans an MS-DOS filesystem for bad blocks by simply trying to read them and flag them if read fails. All blocks that are unused are scanned, and if detected bad are marked as such in the FAT. </p>
<p> This command is intended to be used right after <tt>mformat</tt>. It is not intended to salvage data from bad disks. </p>
<h2>Command line options</h2>
<dl>
<dt><tt>c&nbsp;</tt><i>file</i><tt></tt>&nbsp;</p>
<dd> Use a list of bad clusters, rather than scanning for bad clusters itself.</p>
<dt><tt>s&nbsp;</tt><i>file</i><tt></tt>&nbsp;</p>
<dd> Use a list of bad sectors (counted from beginning of filesystem), rather than trying for bad clusters itself.</p>
<dt><tt>w</tt>&nbsp;</p>
<dd> Write a random pattern to each cluster, then read it back and flag cluster as bad if mismatch. Only free clusters are tested in such a way, so any file data is preserved.</dl>
<h2>Bugs</h2>
<p> <tt>Mbadblocks</tt> should (but doesn&#8217;t yet :-( ) also try to salvage bad blocks which are in use by reading them repeatedly, and then mark them bad. </p>
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
