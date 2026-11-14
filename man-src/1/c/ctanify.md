---
title: "ctanify(1)"
name: "ctanify"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctanify/"
description: "ctanify – Prepare a package for upload to CTAN"
---

<h2 class="name">NAME</h2>
<p> ctanify &#8211; Prepare a package for upload to CTAN </p>
<h2>SYNOPSIS</h2>
<p> ctanify [<code>&#8211;pkgname</code>=<i>string</i>] [<code>&#8212;</code>[<code>no</code>]<code>auto</code>] [<code>&#8211;tdsonly</code>=<i>filespec</i> &#8230;] [<code>&#8212;</code>[<code>no</code>]<code>unixify</code>] [<code>&#8212;</code>[<code>no</code>]<code>skip</code>] [<code>&#8211;tdsdir</code>=<i>dirname</i> &#8230;] [<code>&#8211;tex</code>=<i>macro_pkg</i>] [<code>&#8212;</code>[<code>no</code>]<code>miscify</code>] [<code>&#8212;</code>[<code>no</code>]<code>tds</code>] <i>filespec</i>[=<i>dirname</i>] &#8230; </p>
<p> ctanify [<code>&#8211;help</code>] </p>
<p> ctanify [<code>&#8211;version</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ctanify</code> is intended for developers who have a LaTeX package that they want to distribute via the Comprehensive TeX Archive Network (<font SIZE="-1">CTAN</font>). Given a list of filenames, <code>ctanify</code> creates a tarball (a <i>.tar.gz</i> file) with the files laid out in <font SIZE="-1">CTAN</font>&#8216;s preferred structure. The tarball additionally contains a <font SIZE="-1">ZIP </font>(<i>.zip</i>) file with copies of all files laid out in the standard TeX Directory Structure (<font SIZE="-1">TDS</font>), which facilitates inclusion of the package in the TeX Live distribution.</p>
<h2>OPTIONS</h2>
<p> <code>ctanify</code> accepts the following command-line options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Output basic usage information and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Output <code>ctanify</code>&#8216;s version number and exit.</p>
<dt><code>-p</code> <i>string</i>, <code>&#8211;pkgname</code>=<i>string</i></p>
<dd> Specify explicitly a package name. Normally, <code>ctanify</code> uses the base name of the first <i>.ins</i> or <i>.sty</i> file listed as the package name. The package name forms the base name of the tarball that <code>ctanify</code> produces.</p>
<dt><code>&#8211;noauto</code></p>
<dd> Do not automatically add files to the tarball. Normally, <code>ctanify</code> automatically includes all files mentioned in a <i>.ins</i> file.</p>
<dt><code>-t</code> <i>filespec</i>, <code>&#8211;tdsonly</code>=<i>filespec</i></p>
<dd> Specify a subset of the files named on the command line to include only in the <font SIZE="-1">TDS ZIP</font> file, not in the <font SIZE="-1">CTAN</font> package directory. Wildcards are allowed (quoted if necessary), and <code>&#8211;tdsonly</code> can be used multiple times on the same command line.</dl>
<p> At least one filename must be specified on the command line. <code>ctanify</code> automatically places files in the <font SIZE="-1">TDS</font> tree based on their extension, but this can be overridden by specifying explicitly a target <font SIZE="-1">TDS</font> directory using the form <i>filespec</i>=<i>dirname</i>. Wildcards are allowed for the filespec (quoted if necessary).</p>
<h2>ADDITIONAL OPTIONS</h2>
<p> The following options are unlikely to be necessary in ordinary usage. They are provided for special circumstances that may arise.</p>
<dl>
<dt><code>-d</code> <i>dirname</i>, <code>&#8211;tdsdir</code>=<i>dirname</i></p>
<dd> Instead of creating a tarball for <font SIZE="-1">CTAN,</font> merely create the package <font SIZE="-1">TDS</font> tree rooted in directory <i>dirname</i>.</p>
<dt><code>-T</code> <i>macro_pkg</i>, <code>&#8211;tex</code>=<i>macro_pkg</i></p>
<dd> Assert that the files being packaged for <font SIZE="-1">CTAN</font> target a TeX macro package other than LaTeX. Some common examples of <i>macro_pkg</i> are <tt>&quot;generic&quot;</tt>, <tt>&quot;plain&quot;</tt>, and <tt>&quot;context&quot;</tt>.</p>
<dt><code>-nou</code>, <code>&#8211;no-unixify</code></p>
<dd> Store text files unmodified instead of converting their end-of-line character to Unix format (a single linefeed character with no carriage-return character), even though <font SIZE="-1">CTAN</font> prefers receiving all files with Unix-format end-of-line characters.</p>
<dt><code>-nok</code>, <code>&#8211;no-skip</code></p>
<dd> Force <code>ctanify</code> to include files such as Unix hidden files, Emacs backup files, and version-control metadata files, all of which <font SIZE="-1">CTAN</font> dislikes receiving.</p>
<dt><code>-m</code>, <code>&#8211;miscify</code></p>
<dd> Rename directories containing a single file to <tt>&quot;misc&quot;</tt>. (For example, rename <tt>&quot;tex/latex/mypackage/mypackage.sty&quot;</tt> to <tt>&quot;tex/latex/misc/mypackage.sty&quot;</tt>.) This was common practice in the past but is now strongly discouraged.</p>
<dt><code>-nos</code>, <code>&#8211;no-tds</code></p>
<dd> Do not embed a .tds.zip file in the generated tarball.</dl>
<h2>DIAGNOSTICS</h2>
<dl>
<dt>&quot;Failed to copy filename<tt> (No such file or directory)&quot;</p>
<dd> This message is typically caused by a </tt><i>.ins</i> file that generates <i>filename</i> but that has not already been run through <i>tex</i> or <i>latex</i> to actually produce <i>filename</i>. <code>ctanify</code> does not automatically run <i>tex</i> or <i>latex</i>; this needs to be done manually by the user. See &#8220;<font SIZE="-1">CAVEATS&#8221;</font> for more information.</p>
<dt>&quot;Modified filename<tt> to use Unix line endings (use --no-unixify to prevent this)&quot;</p>
<dd> For consistency, </tt><font SIZE="-1"><tt>CTAN</tt></font><tt> stores all text files with Unix-style line endings (a single linefeed character with no carriage-return character). To help in this effort, </tt><code>ctanify</code> automatically replaces non-Unix-style line endings. The preceding merely message notifies the user that he should not be alarmed to see a different size for <i>filename</i> in the tarball versus the original <i>filename</i> on disk (which <code>ctanify</code> never modifies). If there&#8217;s a good reason to preserve the original line endings (and there rarely is), the <code>&#8211;no-unixify</code> option can be used to prevent <code>ctanify</code> from altering any files when storing them in the tarball.</p>
<dt>&quot;Excluding filename<tt> (use --no-skip to force inclusion)&quot;</p>
<dd> </tt><code>ctanify</code> normally ignores files&#8212;even when specified explicitly on the command line&#8212;that <font SIZE="-1">CTAN</font> prefers not receiving. These include files whose names start with &quot;<i>.</i>&#8220; (Unix hidden files), end in &#8221;<i>~</i>&quot; (Emacs automatic backups), or that come from a <i></i><font SIZE="-1"><i>CVS</i></font><i></i> or <i>.svn</i> directory (version-control metadata files). If there&#8217;s a good reason to submit such files to <font SIZE="-1">CTAN </font>(and there rarely is), the <code>&#8211;no-skip</code> option can be used to prevent <code>ctanify</code> from ignoring them.</p>
<dt>&quot;CTAN prefers having only PDF documentation (re: filename<tt>)&quot;</p>
<dd> Because of the popularity of the </tt><font SIZE="-1"><tt>PDF</tt></font><tt> format, </tt><font SIZE="-1"><tt>CTAN</tt></font><tt> wants to have as much documentation as possible distributed in </tt><font SIZE="-1"><tt>PDF. </tt></font><tt> The preceding message asks the user to replace any PostScript or </tt><font SIZE="-1"><tt>DVI</tt></font><tt> documentation with </tt><font SIZE="-1"><tt>PDF</tt></font><tt> if possible. (</tt><code>ctanify</code> will still include PostScript and <font SIZE="-1">DVI</font> documentation in the tarball; the preceding message is merely a polite request.)</p>
<dt>&quot;Not including filename<tt> in the TDS tree (unknown extension)&quot;</p>
<dd> </tt><code>ctanify</code> places files in the <font SIZE="-1">TDS</font> tree based on a table of file extensions. For example, all <i>.sty</i> files are placed in <i>tex/latex/package-name</i>. If <code>ctanify</code> does not know where to put a file it does not put it anywhere. See the last paragraph of &#8220;<font SIZE="-1">OPTIONS&#8221;</font> for an explanation of how to specify explicitly a file&#8217;s target location in the <font SIZE="-1">TDS</font> tree. For common file extensions that happen to be absent from <code>ctanify</code>&#8216;s table, consider also notifying <code>ctanify</code>&#8216;s author at the address shown below under &#8220;<font SIZE="-1">AUTHOR&#8221;</font>.</dl>
<h2>EXAMPLES</h2>
<h3>The Common Case</h3>
<p> Normally, all that&#8217;s needed is to tell <code>ctanify</code> the name of the <i>.ins</i> file (or <i>.sty</i> if the package does not use DocStrip) and the prebuilt documentation, if any: </p>
<pre>
    $ ctanify mypackage.ins mypackage.pdf README
      490347  mypackage.tar.gz
                  1771  mypackage/README
                 15453  mypackage/mypackage.dtx
                  1957  mypackage/mypackage.ins
                277683  mypackage/mypackage.pdf
                246935  mypackage.tds.zip
                            1771  doc/latex/mypackage/README
                          277683  doc/latex/mypackage/mypackage.pdf
                           15453  source/latex/mypackage/mypackage.dtx
                            1957  source/latex/mypackage/mypackage.ins
                            1725  tex/latex/mypackage/mypackage.sty
</pre>
<p> <code>ctanify</code> outputs the size in bytes of the resulting tarball, each file within it, and each file within the contained <font SIZE="-1">ZIP</font> file. In the preceding example, notice how <code>ctanify</code> automatically performed all of the following operations:</p>
<dl>
<dt>&bull;</p>
<dd> including <i>mypackage.dtx</i> (found by parsing <i>mypackage.ins</i>) in both the <i>mypackage</i> directory and the <font SIZE="-1">ZIP</font> file,</p>
<dt>&bull;</p>
<dd> including <i>mypackage.sty</i> (found by parsing <i>mypackage.ins</i>) in the <font SIZE="-1">ZIP</font> file but, because it&#8217;s a generated file, not in the <i>mypackage</i> directory, and</p>
<dt>&bull;</p>
<dd> placing all files into appropriate <font SIZE="-1">TDS</font> directories (documentation, source, main package) within the <font SIZE="-1">ZIP</font> file.</dl>
<p> Consider what it would take to manually produce an equivalent <i>mypackage.tar.gz</i> file. <code>ctanify</code> is definitely a simpler, quicker alternative.</p>
<h3>Advanced Usage</h3>
<p> <code>ctanify</code> assumes that PostScript files are documentation and therefore stores them under <i>doc/latex/package-name/</i> in the <font SIZE="-1">TDS</font> tree within the <font SIZE="-1">ZIP</font> File. Suppose, however, that a LaTeX package uses a set of PostScript files to control <code>dvips</code>&#8216;s output. In this case, <code>ctanify</code> must be told to include those PostScript files in the package directory, not the documentation directory. </p>
<pre>
    $ ctanify mypackage.ins &quot;mypackage*.ps=tex/latex/mypackage&quot;
</pre>
<h2>FILES</h2>
<dl>
<dt><i>perl</i></p>
<dd> <code>ctanify</code> is written in Perl and needs a Perl installation to run.</p>
<dt><i>tar</i>, <i>gzip</i></p>
<dd> <code>ctanify</code> requires the <font SIZE="-1">GNU </font><i>tar</i> and <i>gzip</i> programs to create a compressed tarball (<i>.tar.gz</i>).</p>
<dt><i>zip</i></p>
<dd> <code>ctanify</code> uses a <i>zip</i> program to archive the <font SIZE="-1">TDS</font> tree within the main tarball.</dl>
<h2>CAVEATS</h2>
<p> <code>ctanify</code> does not invoke <i>tex</i> or <i>latex</i> on its own, e.g., to process a <i>.ins</i> file. The reason is that <code>ctanify</code> does not know in the general case how to produce all of a package&#8217;s generated files. It was deemed better to do nothing than to risk overwriting existing <i>.sty</i> (or other) files or to include outdated generated files in the tarball. In short, before running <code>ctanify</code> you should manually process any <i>.ins</i> files and otherwise generate any files that should be sent to <font SIZE="-1">CTAN.</font> </p>
<p> <code>ctanify</code> has been tested only on Linux. It may work on <font SIZE="-1">OS</font>&nbsp;X. I&#8217;ve been told that it works on Windows when run using Cygwin. Volunteers willing to help port <code>ctanify</code> to other platforms are extremely welcome.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-latex/">latex</a></i>(1), Guidelines for uploading TDS-Packaged materials to <font SIZE="-1">CTAN </font>(&lt;<a rel="nofollow" href="http://www.ctan.org/TDS-guidelines">http://www.ctan.org/TDS-guidelines</a>&gt;), A Directory Structure for TeX Files (&lt;<a rel="nofollow" href="http://tug.org/tds/">http://tug.org/tds/</a>&gt;),</p>
<h2>AUTHOR</h2>
<p> Scott Pakin, <i>scott+ctify [at] pakin.org</i></p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2017 Scott Pakin </p>
<p> This work may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1.3c of this license or (at your option) any later version. The latest version of this license is in </p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="http://www.latex-project.org/lppl.txt">http://www.latex-project.org/lppl.txt</a>&gt;</dl>
<p> and version 1.3c or later is part of all distributions of LaTeX version 2008/05/04 or later. </p>
<h2>Index</h2>
