---
title: "mzip(1)"
name: "mzip"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mzip/"
description: "mzip – change protection mode and eject disk on Zip/Jaz drive"
---

<h2>Name</h2>
<p> mzip &#8211; change protection mode and eject disk on Zip/Jaz drive </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mzip</tt> command is used to issue ZIP disk specific commands on Linux, Solaris or HP-UX. Its syntax is: </p>
<p> <i> </i></p>
<pre>
<tt>mzip</tt> [<tt>-epqrwx</tt>]
</pre>
<p>&nbsp; </p>
<p> <tt>Mzip</tt> allows the following command line options:</p>
<dl>
<dt><tt>e</tt>&nbsp;</p>
<dd> Ejects the disk.</p>
<dt><tt>f</tt>&nbsp;</p>
<dd> Force eject even if the disk is mounted (must be given in addition to <tt>-e</tt>).</p>
<dt><tt>r</tt>&nbsp;</p>
<dd> Write protect the disk.</p>
<dt><tt>w</tt>&nbsp;</p>
<dd> Remove write protection.</p>
<dt><tt>p</tt>&nbsp;</p>
<dd> Password write protect.</p>
<dt><tt>x</tt>&nbsp;</p>
<dd> Password protect</p>
<dt><tt>u</tt>&nbsp;</p>
<dd> Temporarily unprotect the disk until it is ejected. The disk becomes writable, and reverts back to its old state when ejected.</p>
<dt><tt>q</tt>&nbsp;</p>
<dd> Queries the status</dl>
<p> To remove the password, set it to one of the password-less modes <tt>-r</tt> or <tt>-w</tt>: mzip will then ask you for the password, and unlock the disk. If you have forgotten the password, you can get rid of it by low-level formatting the disk (using your SCSI adapter&#8217;s BIOS setup). </p>
<p> The ZipTools disk shipped with the drive is also password protected. On MS-DOS or on a Mac, this password is automatically removed once the ZipTools have been installed. From various articles posted to Usenet, I learned that the password for the tools disk is <tt>APlaceForYourStuff</tt>. Mzip knows about this password, and tries it first, before prompting you for a password. Thus <tt>mzip -w z:</tt> unlocks the tools disk. The tools disk is formatted in a special way so as to be usable both in a PC and in a Mac. On a PC, the Mac file system appears as a hidden file named <tt>&infin;partishn.macIntegral</tt>. You may erase it to reclaim the 50 Megs of space taken up by the Mac file system. </p>
<h2>Bugs</h2>
<p> This command is a big kludge. A proper implementation would take a rework of significant parts of mtools, but unfortunately I don&#8217;t have the time for this right now. The main downside of this implementation is that it is inefficient on some architectures (several successive calls to mtools, which defeats mtools&#8217; caching). </p>
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
