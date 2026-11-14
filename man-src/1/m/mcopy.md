---
title: "mcopy(1)"
name: "mcopy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcopy/"
description: "mcopy – copy MSDOS files to/from Unix"
---

<h2>Name</h2>
<p> mcopy &#8211; copy MSDOS files to/from Unix </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mcopy</tt> command is used to copy MS-DOS files to and from Unix. It uses the following syntax: </p>
<p>&nbsp; </p>
<pre><code>
mcopy[-bspanvmQT][-D clash_option] sourcefile targetfile
    mcopy[-bspanvmQT][-D clash_option] sourcefile[sourcefiles...] targetdirectory
        mcopy[-tnvm] MSDOSsourcefile
</code></pre>
<p>&nbsp; </p>
<p> <tt>Mcopy</tt> copies the specified file to the named file, or copies multiple files to the named directory. The source and target can be either MS-DOS or Unix files. </p>
<p> The use of a drive letter designation on the MS-DOS files, &#8216;a:&#8217; for example, determines the direction of the transfer. A missing drive designation implies a Unix file whose path starts in the current directory. If a source drive letter is specified with no attached file name (e.g. <tt>mcopy a: .</tt>), all files are copied from that drive. </p>
<p> If only a single, MS-DOS source parameter is provided (e.g. &quot;mcopy a:foo.exe&quot;), an implied destination of the current directory (`<tt>.</tt>&#8216;) is assumed. </p>
<p> A filename of `<tt>-</tt>&#8216; means standard input or standard output, depending on its position on the command line. </p>
<p> <tt>Mcopy</tt> accepts the following command line options:</p>
<dl>
<dt><tt>t</tt>&nbsp;</p>
<dd> Text file transfer. Mcopy translates incoming carriage return/line feeds to line feeds when copying from MS-DOS to Unix, and vice-versa when copying from Unix to MS-DOS.</p>
<dt><tt>b</tt>&nbsp;</p>
<dd> Batch mode. Optimized for huge recursive copies, but less secure if a crash happens during the copy.</p>
<dt><tt>s</tt>&nbsp;</p>
<dd> Recursive copy. Also copies directories and their contents</p>
<dt><tt>p</tt>&nbsp;</p>
<dd> Preserves the attributes of the copied files</p>
<dt><tt>Q</tt>&nbsp;</p>
<dd> When mcopying multiple files, quits as soon as one copy fails (for example due to lacking storage space on the target disk)</p>
<dt><tt>a</tt>&nbsp;</p>
<dd> Text (ASCII) file transfer. <tt>ASCII</tt> translates incoming carriage return/line feeds to line feeds.</p>
<dt><tt>T</tt>&nbsp;</p>
<dd> Text (ASCII) file transfer with character set conversion. Differs from <tt>-a</tt> in the <tt>ASCII</tt> also translates incoming PC-8 characters to ISO-8859-1 equivalents as far as possible. When reading DOS files, untranslatable characters are replaced by &#8216;<tt>#</tt>&#8216;; when writing DOS files, untranslatable characters are replaced by &#8216;<tt>.</tt>&#8216;.</p>
<dt><tt>n</tt>&nbsp;</p>
<dd> No confirmation when overwriting Unix files. <tt>ASCII</tt> doesn&#8217;t warn the user when overwriting an existing Unix file. If the target file already exists, and the <tt>-n</tt> option is not in effect, <tt>mcopy</tt> asks whether to overwrite the file or to rename the new file (&infin;name clashesIntegral) for details). In order to switch off confirmation for DOS files, use <tt>-o</tt>.</p>
<dt><tt>m</tt>&nbsp;</p>
<dd> Preserve the file modification time.</p>
<dt><tt>v</tt>&nbsp;</p>
<dd> Verbose. Displays the name of each file as it is copied.</dl>
<h2>Bugs</h2>
<p> Unlike MS-DOS, the &#8216;+&#8217; operator (append) from MS-DOS is not supported. However, you may use <tt>mtype</tt> to produce the same effect:<br />
&nbsp; </p>
<pre>
<code>mtype a:file1 a:file2 a:file3 &gt;unixfile
mtype a:file1 a:file2 a:file3 | mcopy - a:msdosfile
</code></pre>
<p>&nbsp; </p>
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
